#sqalchemyを使ったDB設計
import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

#Neon(PostgreSQL)に接続
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///sauna.db")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL,echo=True)
SessionLocal = sessionmaker(bind=engine)

#モデルクラスの親クラス
Base = declarative_base()

#親クラスを継承
class Facility(Base):
    __tablename__ = "facilities"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    prefecture = Column(String, nullable=False)
    sauna_temp = Column(Integer, nullable=False)
    water_temp = Column(Integer, nullable=False)

    reviews = relationship("Review", back_populates="facility", cascade="all,delete-orphan")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer,primary_key=True)
    facility_id = Column(Integer, ForeignKey("facilities.id"), nullable=False)
    user_name = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    created_at =Column(DateTime, default=datetime.utcnow)

    facility = relationship("Facility", back_populates="reviews")


#テーブルの作成処理
Base.metadata.create_all(bind=engine)

session = SessionLocal()

#施設データの初期リスト
facilities = [
    Facility(name="おふろの王様 和光店", prefecture="埼玉県", sauna_temp=90, water_temp=16),
    Facility(name="かるまる池袋", prefecture="東京都", sauna_temp=95, water_temp=14),
    Facility(name="スパジアムジャポン", prefecture="埼玉県", sauna_temp=92, water_temp=15)

]

#同施設の登録防止
for data in facilities:
    existing = session.query(Facility).filter_by(name=data.name).first()
    if existing is None:
        session.add(data)

session.commit()
session.close()