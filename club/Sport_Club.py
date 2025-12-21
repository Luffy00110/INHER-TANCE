from base import Club
from datetime import datetime
import uuid
from typing import List, Dict, Any, Optional

class SportClub(Club):
    def __init__(self, name, description, brans, saha):
        # Base class'a varsayılan değerleri gönderiyoruz (0 üye, şu anki tarih)
        super().__init__(name, 0, description, datetime.now())
        self.brans = brans
        self.antrenman_sahasi = saha

    # Abstract Metot 1 
    def uye_kabul_sartlari(self) -> list:
        return ["Sağlık raporu", "Spor kıyafeti", "Antrenman disiplini"]

    # Abstract Metot 2 
    def etkinlik_tipi_belirle(self) -> str:
        return "Turnuva ve Maç"

    # Ekstra Metot
    def antrenman_planla(self, saat):
        print(f"SPOR {self.name}, {self.antrenman_sahasi} sahasında {saat} antrenmanı yapacak.")