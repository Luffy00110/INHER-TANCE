from app.modules.club.base import Club
from datetime import datetime, timedelta
import random
# Etkinlik verileri:
class ClubEvent:
    #Kulüplerin düzenlediği etkinlikleri temsil eden sınıf.
    
    def __init__(self, title: str, club_name: str, location: str, quota: int, date_time: datetime):
        self.event_id = random.randint(1000, 9999)
        self.title = title
        self.club_name = club_name
        self.location = location
        self.quota = quota
        self.date_time = date_time
        self.attendees = []  # Katılımcı listesi
        self.is_active = True

    def katilimci_ekle(self, ogrenci_adi: str) -> bool:
        if len(self.attendees) >= self.quota:
            print(f"[DOLU] '{self.title}' için yer yok.")
            return False
        self.attendees.append(ogrenci_adi)
        print(f"[KAYIT] {ogrenci_adi} -> {self.title} etkinliğine eklendi.")
        return True

