from dapodik_webservice import DapodikWebservice
from dataclasses import asdict
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from typing import Optional

from bopku.db import Base


class Sekolah(Base):
    __tablename__ = "sekolah"
    id: int = Column(Integer, primary_key=True)
    # Cred
    server_dapodik: str = Column(String, nullable=True)
    email_dapodik: str = Column(String, nullable=True)
    password_dapodik: str = Column(String, nullable=True)
    email_simdak: str = Column(String, nullable=True)
    password_simdak: str = Column(String, nullable=True)
    token: str = Column(String, nullable=True)
    # Debug time
    created_at: datetime = Column(DateTime, server_default=func.now())
    updated_at: datetime = Column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
    # Data
    sekolah_id: str = Column(String, nullable=True)
    nama: str = Column(String, nullable=True)
    nss: str = Column(String, nullable=True)
    npsn: str = Column(String, nullable=True)
    bentuk_pendidikan_id: int = Column(Integer, nullable=True)
    bentuk_pendidikan_id_str: str = Column(String, nullable=True)
    status_sekolah: str = Column(String, nullable=True)
    status_sekolah_str: str = Column(String, nullable=True)
    alamat_jalan: str = Column(String, nullable=True)
    rt: str = Column(String, nullable=True)
    rw: str = Column(String, nullable=True)
    kode_wilayah: str = Column(String, nullable=True)
    kode_pos: str = Column(String, nullable=True)
    nomor_telepon: str = Column(String, nullable=True)
    nomor_fax: str = Column(String, nullable=True)
    email: str = Column(String, nullable=True)
    website: str = Column(String, nullable=True)
    is_sks: bool = Column(Boolean, nullable=True)
    lintang: str = Column(String, nullable=True)
    bujur: str = Column(String, nullable=True)
    dusun: str = Column(String, nullable=True)
    desa_kelurahan: str = Column(String, nullable=True)
    kecamatan: str = Column(String, nullable=True)
    kabupaten_kota: str = Column(String, nullable=True)
    provinsi: str = Column(String, nullable=True)

    def __init__(
        self,
        token: str,
        npsn: str,
        email_simdak: str,
        password_simdak: str,
        server_dapodik: str = "http://localhost:5774",
    ):
        self.token = token
        self.npsn = npsn
        self.email_simdak = email_simdak
        self.password_simdak = password_simdak
        self.server_dapodik = server_dapodik
        self.__ws__: Optional[DapodikWebservice] = None
        try:
            sekolah: dict = asdict(self.ws.sekolah)
            for key, value in sekolah.items():
                setattr(self, key, value)
        except Exception:
            pass

    def __str__(self) -> str:
        return self.nama

    @property
    def ws(self) -> DapodikWebservice:
        if self.__ws__:
            return self.__ws__
        self.__ws__ = DapodikWebservice(
            self.token,
            self.npsn,
            self.server_dapodik,
        )
        return self.__ws__
