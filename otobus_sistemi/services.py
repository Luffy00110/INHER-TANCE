from repository import TransportRepository

class Bilet:
    def __init__(self, yolcu_adi, binis, inis, tutar):
        self.yolcu_adi = yolcu_adi
        self.binis = binis
        self.inis = inis
        self.tutar = tutar

    def bilet_ozeti(self):
        return f"🎫 {self.yolcu_adi}: {self.nereden} -> {self.inis} ({self.tutar} TL)"

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
    
    def aktif_seferleri_listele(self):
        print("--- Seferde Bulunan Araçlar ---")
        tum_araclar = self.repo.araclari_listele()
        bulundu = False
        for arac in tum_araclar:
            if arac.seferde_mi:
                print(f"Araç ID: {arac.id} - Konum: {arac.mevcut_lokasyon}")
                bulundu = True
        
        if not bulundu:
            print("Şu an seferde olan araç yok.")

    def uygun_arac_bul(self, gerekli_koltuk_sayisi):
        print(f"--- {gerekli_koltuk_sayisi} kişilik bilet için uygun sefer aranıyor.")
        uygunlar = self.repo.bos_koltuga_gore_filtrele(gerekli_koltuk_sayisi)
        
        if uygunlar:
            for arac in uygunlar:
                bos = arac.kapasite - arac.dolu_koltuk
                print(f"Bulundu -> Araç ID: {arac.id} (Boş Yer: {bos})")
        else:
            print("Maalesef uygun kapasiteli araç bulunamadı.")