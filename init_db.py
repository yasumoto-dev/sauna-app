from models import Base, engine, SessionLocal, Facility

Base.metadata.create_all(bind=engine)

session = SessionLocal()

facilities = [
    Facility(name="おふろの王様 和光店", prefecture="埼玉県", sauna_temp=90, water_temp=16),
    Facility(name="かるまる池袋", prefecture="東京都", sauna_temp=95, water_temp=14),
    Facility(name="スパジアムジャポン", prefecture="埼玉県", sauna_temp=92, water_temp=15)

]

session.add_all(facilities)
session.commit()
session.close()

print("データベースを初期化しました。")