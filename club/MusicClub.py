from base import Club
from datetime import datetime
import uuid
from typing import List, Dict, Any, Optional


class MusicClub(Club):
    def __init__(self, name, description, muzik_turu):
        super().__init__(name, 0, description, datetime.now())
        self.muzik_turu = muzik_turu

    def uye_kabul_sartlari(self) -> list:
        return ["Müzik kulağı testi", "Enstrüman yeteneği"]

    def etkinlik_tipi_belirle(self) -> str:
        return "Konser ve Dinleti"
