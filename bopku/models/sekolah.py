from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, func

from bopku.db import Base


class Sekolah(Base):
    __tablename__ = "sekolah"
    id: int = Column(Integer, primary_key=True)
    nama: str = Column(String)
    # Cred
    email: str = Column(String)
    password: str = Column(String, nullable=True)
    token: str = Column(String, nullable=True)
    # Debug time
    created_at: datetime = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at: datetime = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def __str__(self) -> str:
        return self.nama
