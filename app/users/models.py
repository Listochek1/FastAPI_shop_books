from app.models import Base
from sqlalchemy import DateTime, ForeignKey, String
from app.models import Base
from sqlalchemy.orm import Mapped,mapped_column
from datetime import date
import datetime

class UsersModel(Base):
    __tablename__ = "users"
    login : Mapped[str]  = mapped_column(String(length=40),nullable=False)
    password : Mapped[str] = mapped_column(String,nullable=False)
    date_reg : Mapped[datetime.datetime] = mapped_column(DateTime,nullable=False,default=datetime.datetime.utcnow)