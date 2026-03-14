from flask import Flask, render_template, request, redirect, url_for
from models import SessionLocal, Facility, Review

app = Flask(__name__)


@app.route("/")
def index():
    session = SessionLocal()
    facilities = session.query(Facility).all()
    session.close()
    return render_template("index.html", facilities=facilities)


@app.route("/facility/<int:facility_id>")
def facility_detail(facility_id):
    session = SessionLocal()
    facility = session.query(Facility).filter(Facility.id == facility_id).first()
    reviews = session.query(Review).filter(Review.facility_id == facility_id).order_by(Review.created_at.desc()).all()
    session.close()

    return render_template("facility_detail.html", facility=facility, reviews=reviews)


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
    session.add(new_review)
    session.commit()
    session.close()

    return redirect(url_for("facility_detail", facility_id=facility_id))


if __name__ == "__main__":
    app.run(debug=True)