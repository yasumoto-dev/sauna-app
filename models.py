#sqalchemyを使ったDB設計
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import declarative_base,relationship,sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///sauna.db"

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

