from repository import TransportRepository

class TransportService:
    def __init__(self):
        self.repo = TransportRepository()

    def arac_kayit(self, arac):
        self.repo.arac_ekle(arac)

    def arac_silme(self, arac_id):
        self.repo.arac_sil(arac_id)

    def sefer_baslat(self, arac_id, hedef_yer):
        arac = self.repo.id_ile_bul(arac_id)
        if arac:
            arac.seferde_mi = True
            arac.mevcut_lokasyon = f"Yolda: {hedef_yer}"
            print(f"Sefer başlatıldı. Araç ID: {arac_id} Hedef: {hedef_yer}")
        else:
            print("Hata: Araç bulunamadı, sefer başlatılamadı.")

    def sefer_bitir(self, arac_id):
        arac = self.repo.id_ile_bul(arac_id)
        if arac:
            arac.seferde_mi = False
            arac.dolu_koltuk = 0 
            arac.mevcut_lokasyon = "Garaj"
            print(f"Sefer bitti. Araç garaja döndü: {arac_id}")

    def bilet_satis(self, arac_id, kisi_sayisi):
        arac = self.repo.id_ile_bul(arac_id)
        if arac:
            bos_yer = arac.kapasite - arac.dolu_koltuk
            if bos_yer >= kisi_sayisi:
                arac.dolu_koltuk += kisi_sayisi
                print(f"Bilet satışı onaylandı. Kalan boş yer: {bos_yer - kisi_sayisi}")
            else:
                print("Kapasite yetersiz! Satış yapılmadı.")
        else:
            print("Araç sistemde yok.")

    def tum_araclari_yazdir(self):
        print("--- TÜM ARAÇ LİSTESİ ---")
        liste = self.repo.araclari_listele()
        for arac in liste:
            arac.bilgi_ver()
            print("-----------------------")