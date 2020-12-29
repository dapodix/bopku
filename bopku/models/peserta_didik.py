from dapodik_webservice import PesertaDidik as WsPesertaDidik
from dataclasses import asdict
from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from typing import Optional

from bopku.db import Base
from . import Sekolah


class PesertaDidik(Base):
    __tablename__ = "peserta_didik"
    id: int = Column(Integer, primary_key=True)
    sekolah_id: int = Column(
        Integer, ForeignKey("sekolah.id", ondelete="CASCADE", name="sekolah")
    )
    sekolah: Sekolah = relationship(
        "Sekolah",
        uselist=False,
        foreign_keys="PesertaDidik.sekolah_id",
        post_update=True,
    )
    # Data
    registrasi_id: str = Column(String, nullable=False)
    jenis_pendaftaran_id: str = Column(String, nullable=False)
    jenis_pendaftaran_id_str: str = Column(String, nullable=False)
    nipd: str = Column(String, nullable=False)
    tanggal_masuk_sekolah: str = Column(String, nullable=False)
    sekolah_asal: Optional[str] = Column(String, nullable=True)
    peserta_didik_id: str = Column(String, nullable=False)
    nama: str = Column(String, nullable=False)
    nisn: str = Column(String, nullable=False)
    jenis_kelamin: str = Column(String, nullable=False)
    nik: str = Column(String, nullable=False)
    tempat_lahir: str = Column(String, nullable=False)
    tanggal_lahir: str = Column(String, nullable=False)
    agama_id: int
    agama_id_str: str = Column(String, nullable=False)
    alamat_jalan: Optional[str] = Column(String, nullable=True)
    nomor_telepon_rumah: Optional[str] = Column(String, nullable=True)
    nomor_telepon_seluler: Optional[str] = Column(String, nullable=True)
    nama_ayah: str = Column(String, nullable=False)
    pekerjaan_ayah_id: int
    pekerjaan_ayah_id_str: str = Column(String, nullable=False)
    nama_ibu: str = Column(String, nullable=False)
    pekerjaan_ibu_id: int
    pekerjaan_ibu_id_str: str = Column(String, nullable=False)
    nama_wali: Optional[str] = Column(String, nullable=True)
    pekerjaan_wali_id: int
    pekerjaan_wali_id_str: str = Column(String, nullable=False)
    tinggi_badan: str = Column(String, nullable=False)
    berat_badan: str = Column(String, nullable=False)
    semester_id: str = Column(String, nullable=False)
    anggota_rombel_id: str = Column(String, nullable=False)
    rombongan_belajar_id: str = Column(String, nullable=False)
    tingkat_pendidikan_id: str = Column(String, nullable=False)
    nama_rombel: str = Column(String, nullable=False)
    kurikulum_id: str = Column(String, nullable=False)
    kurikulum_id_str: str = Column(String, nullable=False)
    # Debug time
    created_at: datetime = Column(DateTime, server_default=func.now())
    updated_at: datetime = Column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    def __init__(self, peserta_didik: WsPesertaDidik):
        pd_data: dict = asdict(peserta_didik)
        for key, value in pd_data.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return self.nama
