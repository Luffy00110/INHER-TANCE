from abc import ABC, abstractmethod
from datetime import datetime
import uuid
from typing import List, Dict, Any, Optional

class Club(ABC):
    # Club ana sınıf 
    def __init__(self,name, member_count, description, created_at):
        self.name = name
        self.member_count = member_count
        self.description = description
        self.created_at = created_at
    
    @abstractmethod
    def uye_kabul_sartlari(self) -> list:
        # Üye olmak için gereken şartları listeler.
        pass

    @abstractmethod
    def etkinlik_tipi_belirle(self) -> str:
        # Kulubün etkinlik türünü verir.
        pass

    def get_summary(self):
        """Kulübün özet bilgisini döndürür."""
        return f"{self.name} ({self.member_count} Üye) - {self.description}"

    def uye_sayisi_guncelle(self, yeni_sayi):
        # Üye sayısını günceller.
        if yeni_sayi >= 0:
            self.member_count = yeni_sayi
            print(f"[{self.name}] Üye sayısı güncellendi: {self.member_count}")
        else:
            print("Hata: Üye sayısı negatif olamaz.")


    @staticmethod
    def isim_kontrol(isim: str) -> bool:
        """
        Kulüp isminin kurallara uygun olup olmadığını kontrol eder.
        Self almaz!
        """
        if len(isim) < 3:
            print("Hata: İsim çok kısa.")
            return False
        return True

    @classmethod
    def genel_kurallar(cls):
        """
        Tüm kulüpler için geçerli genel kuralları basar.
        """
        print(f"\n--- {cls.__name__} SİSTEM KURALLARI ---")
        print("1. Her kulüp bir danışman hocaya sahip olmalıdır.")
        print("2. Etkinlikler 1 hafta önceden bildirilmelidir.")
