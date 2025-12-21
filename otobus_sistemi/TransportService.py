import json
import os
from datetime import datetime

from Repository import TransportRepository

try:
    from payment_system import BankaServisi, PaymentService
except ImportError:
    print("Hata: payment_system.py dosyası aynı dizinde bulunamadı!")

try:
    from Bus import Bus
    from Tramvay import Tramvay
    from Metro import Metro
    from Scooter import Scooter
    from Vapur import Vapur
    from Shuttle import Shuttle
    from Havaray import Havaray
    from Bicycle import Bicycle
    from Metrobus import Metrobus 
    from Teleferik import Teleferik
    from DenizTaksi import DenizTaksi
except ImportError as e:
    print(f"Arac dosyalari eksik! ({e})")

class TransportService:
    def __init__(self, arac_dosyasi="araclar.json", sefer_dosyasi="seferler.json"):
        self.arac_dosyasi = arac_dosyasi
        self.sefer_dosyasi = sefer_dosyasi
        
        # Listeyi artik Repository tutuyor
        self.repository = TransportRepository()
        
        # Verileri yukleyip repoya atiyoruz
        self.__araclari_yukle()
        self.__sefer_kayitlari = self.__dosya_oku(self.sefer_dosyasi)

    def __dosya_oku(self, dosya_yolu):
        if not os.path.exists(dosya_yolu): return []
        with open(dosya_yolu, 'r', encoding='utf-8') as f:
            try: return json.load(f)
            except: return []

    def __dosya_yaz(self, dosya_yolu, veri):
        with open(dosya_yolu, 'w', encoding='utf-8') as f:
            json.dump(veri, f, ensure_ascii=False, indent=4)

    def __araclari_yukle(self):
        ham_veriler = self.__dosya_oku(self.arac_dosyasi)
        
        if isinstance(ham_veriler, dict) and "filo" in ham_veriler:
            ham_veriler = ham_veriler["filo"]
            
        print("Sistem verileri isleniyor...")
        
        for veri in ham_veriler:
            try:
                arac = None
                tip = veri.get('arac') or veri.get('tip')
                
                if tip == 'Bus':
                    arac = Bus(veri['id'], veri['durum'], 100, veri.get('otobus_tipi'), veri.get('plaka'), veri['mevcut_lokasyon'])
                elif tip == 'Shuttle':
                    arac = Shuttle(veri['id'], veri['kapasite'], veri['durum'], veri.get('batarya_yuzdesi', 100), veri['mevcut_lokasyon'])
                elif tip == 'Metro':
                    arac = Metro(veri['id'], veri['durum'], 100, 500, veri['kapasite'], 2.0, 5.0, veri.get('hat_ismi', 'M1'), veri['mevcut_lokasyon'])
                elif tip == 'Havaray':
                    arac = Havaray(veri['id'], veri['kapasite'], veri['durum'], 100, 100, 0.7, 3.46, veri['mevcut_lokasyon'])
                elif tip == 'Scooter':
                    arac = Scooter(veri['id'], veri['durum'], veri.get('batarya_yuzdesi', 100), 0.5, 2.5, 5.0, veri['mevcut_lokasyon'])
                elif tip == 'Bicycle':
                    arac = Bicycle(veri['id'], veri['durum'], 3.0, 1.0, veri['mevcut_lokasyon'])
                elif tip == 'Vapur':
                    arac = Vapur(veri['id'], veri['durum'], 500, 1000, veri.get('kapasite', 500), veri.get('gemi_ismi', 'Vapur'))
                elif tip == 'Metrobus':
                     arac = Metrobus(veri['id'], veri['durum'], "34 BRT 01", 180, 250, 100, veri['mevcut_lokasyon'])
                elif tip == 'Teleferik':
                     # Varsayilan degerler ile olusturma
                     arac = Teleferik(veri['id'], veri['durum'], 20, 1500, 50.0, veri['mevcut_lokasyon'])
                elif tip == 'DenizTaksi':
                     arac = DenizTaksi(veri['id'], veri['durum'], 10, 100.0, 50.0, 100, veri['mevcut_lokasyon'])
                
                if arac:
                    # Listeye degil Repository'e ekliyoruz
                    self.repository.add(arac)
            except Exception as e:
                print(f"{veri.get('id')} yuklenemedi: {e}")

    def arac_kayit(self, arac):
        # Repository uzerinden ekleme
        self.repository.add(arac)
        print(f"Arac sisteme manuel eklendi: {type(arac).__name__} ({arac.get_id()})")

    # Yeni eklenen metod: Hoca beklentisi silme testi icin
    def arac_sil(self, arac_id):
        sonuc = self.repository.remove(arac_id)
        if sonuc:
            print(f"Arac silindi: {arac_id}")
        else:
            print(f"Silinecek arac bulunamadi: {arac_id}")
        return sonuc
        
    def arac_bul(self, arac_id):
        return self.repository.find_by_id(arac_id)

    def turnike_odeme_yap(self, arac_id, binis, inis, yolcu_adi):
        print(f"\nTURNIKE ISLEMI ({yolcu_adi}) ---")
        arac = self.repository.find_by_id(arac_id)
        
        if not arac:
            print("Turnike araci taniyamadi!")
            return

        try:
            # 1. ADIM: Once ucreti hesapla (Sıralama buraya çekildi)
            if isinstance(arac, (Scooter, Bicycle)):
                 ucret, mesafe = arac.ucret_hesapla(binis, inis, sure_dk=15)
            else:
                 ucret, mesafe = arac.ucret_hesapla(binis, inis)
            
            # 2. ADIM: Hesaplanan ucreti bankaya gonder
            if ucret > 0:
                print(f"Hesaplanan Tutar: {ucret:.2f} TL")
                banka = BankaServisi()
                basarili = banka.odeme_al(yolcu_adi, ucret, f"Ulasim: {type(arac).__name__}")
                
                if basarili:
                    print(f"Turnike acildi... Iyi yolculuklar! Guzergah: {binis} -> {inis}")
                else:
                    print("Odeme Banka tarafindan reddedildi! Gecis basarisiz.")
            else:
                print("Ucretsiz gecis veya hatali durak bilgisi.")
                
        except Exception as e:
            print(f"Islem sirasinda bir hata olustu: {e}")
            
    def uygun_arac_bul(self, gerekli_kapasite):
        print(f"\n{gerekli_kapasite} kisilik yer olan araclar araniyor...")
        
        bulunanlar = self.repository.filter_by_capacity(gerekli_kapasite)
                
        if bulunanlar:
            print(f"Toplam {len(bulunanlar)} uygun arac bulundu:")
            for a in bulunanlar:
                durum = "Bilinmiyor"
                try:
                    durum = a.get_durum()
                except:
                    pass
                
                if durum == "Müsait":
                    print(f"   - {type(a).__name__} (ID: {a.get_id()}) | Konum: {a.get_mevcut_lokasyon()}")
        else:
            print("Maalesef uygun kapasiteli musait arac yok.")
        
        return bulunanlar

    def sefer_baslat(self, arac_id, hedef):
        print(f"\nSEFER EMRI: Arac {arac_id} -> {hedef}")
        
        # Repository'den bulma
        arac = self.repository.find_by_id(arac_id)
        
        if arac:
            arac.motoru_calistir()
            # Durum guncelleme
            try:
                arac.set_durum("Seferde")
            except:
                pass
            print(f"Sistem: {arac_id} numarali arac {hedef} konumuna yonlendirildi.")
        else:
            print("Arac bulunamadi.")

    def aktif_seferleri_listele(self):
        print("\nAKTIF SEFER LISTESI")
        sayac = 0
        # Tum araclari Repository'den cek
        tum_araclar = self.repository.get_all()
        
        for arac in tum_araclar:
            try:
                if arac.get_durum() != "Müsait" and arac.get_durum() != "Garajda":
                    print(f"- {type(arac).__name__} ({arac.get_id()}) su an gorevde.")
                    sayac += 1
            except:
                continue
                
        if sayac == 0:
            print("Su an aktif seferde arac yok.")

    def gun_sonu_raporu_olustur(self):
        zaman = datetime.now()
        dosya_adi = "gun_sonu_raporu.txt"
        
        # Tum veriyi Repo'dan al
        tum_filo = self.repository.get_all()
        
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            dosya.write("GUN SONU FILO RAPORU\n")
            dosya.write("==============================\n")
            dosya.write(f"Rapor Tarihi: {zaman}\n\n")
            for arac in tum_filo:
                # __str__ metodu yoksa manuel bilgi yazdirma
                try:
                    info = f"ID: {arac.get_id()} | Tip: {type(arac).__name__}"
                    try:
                        info += f" | Durum: {arac.get_durum()}"
                    except: pass
                    dosya.write(info + "\n")
                except:
                    dosya.write(f"Arac ID: {arac.get_id()}\n")
                
        print(f"Rapor basariyla '{dosya_adi}' olarak kaydedildi.")