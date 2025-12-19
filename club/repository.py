class ClubRepository:
    def __init__(self):
        self.kulupler_listesi = []
        self.etkinlikler_listesi = []
        # Kulüpleri ve etkinlikleri burada saklar

    # Külup işlemleri burda saklanır
    def save_club(self,kulup):
        #Kulübü listeye ekler
        self.kulupler_listesi.append(kulup)

    def list_all_clubs(self):
        # kulüpleri döndürür
        return self.kulupler_listesi
    def find_club_by_name(self,isim):
        for kulup in self.kulupler_listesi:
            if kulup.name.lower() == isim.lower():
                return kulup
            return None
    # Etkinlik işlemleri

    def save_event(self, etkinlik):
        # Etkinliği listeye kaydeder
        self.etkinlikler_listesi.append(etkinlik)

    def get_events_by_club(self, kulup_adi):
        # Bir kulübün etkinliklerini bulur
        sonuclar = []
        for etkinlik in self.etkinlikler_listesi:
            if etkinlik.club_name == kulup_adi:
                sonuclar.append(etkinlik)
        return sonuclar
        
    
