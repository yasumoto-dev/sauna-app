#webアプリ本体の作成
from flask import Flask, render_template, request, redirect, url_for, abort
from models import SessionLocal, Facility, Review

#Flaskアプリ作成
app = Flask(__name__)


#施設一覧表示
@app.route("/")
def index():
    session = SessionLocal()
    facilities = session.query(Facility).all()
    session.close()
    return render_template("index.html", facilities=facilities)


#施設登録ページ表示
@app.route("/facility/new")
def new_facility():
    return render_template("facility_form.html")


#施設登録処理
@app.route("/facility/create", methods=["POST"])
def create_facility():
    name = request.form["name"]
    prefecture = request.form["prefecture"]
    sauna_temp = request.form["sauna_temp"]
    water_temp = request.form["water_temp"]

    session = SessionLocal()

    #同施設の登録防止処理
    existing_facility = session.query(Facility).filter_by(name=name).first()
    if existing_facility:
        session.close()
        return render_template(
            "facility_form.html",
            error="同じ名前の施設はすでに登録されています"
        )

    new_facility = Facility(
        name = name,
        prefecture = prefecture,
        sauna_temp = int(sauna_temp),
        water_temp = int(water_temp)
    )

    session.add(new_facility)
    session.commit()
    session.close()

    return redirect(url_for("index"))


#施設情報表示
@app.route("/facility/<int:facility_id>")
def facility_detail(facility_id):
    session = SessionLocal()
    facility = session.query(Facility).filter(Facility.id == facility_id).first()
    reviews = session.query(Review).filter(Review.facility_id == facility_id).order_by(Review.created_at.desc()).all()
    session.close()

    return render_template("facility_detail.html", facility=facility, reviews=reviews)


#コメント投稿
@app.route("/facility/<int:facility_id>/review", methods=["POST"])
def add_review(facility_id):
    user_name = request.form["user_name"]
    comment = request.form["comment"]

    session = SessionLocal()
    new_review = Review(
        facility_id=facility_id,
        user_name=user_name,
        comment=comment
    )
    #DBへ追加
    session.add(new_review)
    session.commit()

    session.close()

    return redirect(url_for("facility_detail", facility_id=facility_id))


#コメント削除
@app.route("/review/<int:review_id>/delete", methods=["POST"])
def delete_comment(review_id):
    session = SessionLocal()

    review = session.query(Review).filter(Review.id == review_id).first()

    if not review:
        session.close()
        abort(404)

    facility_id = review.facility_id
    
    session.delete(review)
    session.commit()
    session.close()    

    return redirect(url_for("facility_detail", facility_id=facility_id))


if __name__ == "__main__":
    app.run(debug=True)