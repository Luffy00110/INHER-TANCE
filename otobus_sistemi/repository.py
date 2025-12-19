class TransportRepository:
    def __init__(self):
        self.arac_listesi = []

    def arac_ekle(self, arac):
        self.arac_listesi.append(arac)
        print(f"Repository: {arac.id} sisteme kaydedildi.")

    def arac_sil(self, arac_id):
        for arac in self.arac_listesi:
            if arac.id == arac_id:
                self.arac_listesi.remove(arac)
                print(f"Repository: {arac_id} silindi.")
                return True
        return False

    def id_ile_bul(self, arac_id):
        for arac in self.arac_listesi:
            if arac.id == arac_id:
                return arac
        return None

    def araclari_listele(self):
        return self.arac_listesi

    def bos_koltuga_gore_filtrele(self, min_bos_koltuk):
        uygun_araclar = []
        for arac in self.arac_listesi:
            bos_yer = arac.kapasite - arac.dolu_koltuk
            if bos_yer >= min_bos_koltuk:
                uygun_araclar.append(arac)
        return uygun_araclar