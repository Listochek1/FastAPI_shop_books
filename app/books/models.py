from sqlalchemy import Date, ForeignKey, String
from app.models import Base
from sqlalchemy.orm import Mapped,mapped_column


class AuthorsModel(Base):
    __tablename__ = "authors"
    first_name  : Mapped[str]  = mapped_column(String(length=40),nullable=True)
    last_name : Mapped[str] = mapped_column(String(length=40),nullable=True)


class BooksModel(Base):
    __tablename__ = "books"
    title  : Mapped[str]  = mapped_column(String(length=50),nullable=True)
    author : Mapped[int] = mapped_column(ForeignKey("authors.id"))
    genre  : Mapped[str]  = mapped_column(ForeignKey("genres.id"))
    date_publication : Mapped[Date] = mapped_column(
        Date, nullable=True
    )

class GenreModel(Base):
    __tablename__ = "genres"
    title : Mapped[str] = mapped_column(String(length=30),nullable=True)
    description : Mapped[str] = mapped_column(String(length=30),nullable=True)
