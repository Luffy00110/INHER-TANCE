import random
from datetime import datetime
from payment_system import CreditCardPayment
from repository import PaymentMethodRepository, TransactionRepository

# Ödeme sistemi hatalarını yönetmek için özel hata sınıfı.
class PaymentSystemError(Exception):
    pass

# Kampüs içindeki tüm finansal işlemleri ve banka entegrasyonunu yönetir.
class BankaServisi:
    def __init__(self):
        self.__kasa = 0
        self.__gecmis = []
        self.__basarisiz_denemeler = 0
        self.__sistem_durumu = "AKTİF"

    def odeme_al(self, kullanici, miktar, aciklama="Genel Ödeme"):
        print(f"\n İşlem Sahibi: {kullanici} | Tutar: {miktar} TL | Tip: {aciklama}")
        
        if self.__sistem_durumu != "AKTİF":
            raise PaymentSystemError("Banka sistemi şu an bakımda!")

        if random.random() < 0.15 or miktar < 0:
            self.__basarisiz_denemeler += 1
            self._kaydet(kullanici, miktar, "BAŞARISIZ", aciklama)
            return False

        self.__kasa += miktar
        self._kaydet(kullanici, miktar, "BAŞARILI", aciklama)
        return True

    def _kaydet(self, kullanici, miktar, durum, aciklama):
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        kayit = {
            "zaman": zaman,
            "kullanici": kullanici,
            "miktar": miktar,
            "durum": durum,
            "aciklama": aciklama
        }
        self.__gecmis.append(kayit)

    def gun_sonu_raporu(self):
        print("\n" + "="*40)
        print(f" GÜNLÜK FİNANSAL RAPOR - {datetime.now().date()}")
        print(f" Toplam Ciro: {self.__kasa} TL")
        print(f" Başarısız İşlem Sayısı: {self.__basarisiz_denemeler}")
        print("-" * 40)
        for i in self.__gecmis:
            print(f"[{i['zaman']}] {i['kullanici']}: {i['miktar']} TL ({i['durum']})")
        print("="*40 + "\n")

    def kulup_aidat_onayi(self, kullanici, kulup_adi):
        aidat_tutari = 150.0
        return self.odeme_al(kullanici, aidat_tutari, f"{kulup_adi} Aidat")

    def tarihe_gore_sorgula(self, hedef_tarih):
        toplam = 0
        for islem in self.__gecmis:
            if hedef_tarih in islem["zaman"]:
                toplam += islem["miktar"]
        return toplam

    @classmethod
    def servis_versiyonu(cls):
        return "v2.4.0 - Güvenli Kampüs Ödeme Motoru"

    @staticmethod
    def kur_donustur(miktar, kur=34.5):
        return miktar / kur

    @property
    def kasa_miktari(self):
        return self.__kasa

# ---------------- PaymentService (Ortak Modül) ----------------

class PaymentService:
    def __init__(self, payment_repo, transaction_repo, banka_servisi=None):
        self.payment_repo = payment_repo
        self.transaction_repo = transaction_repo
        self.banka = banka_servisi or BankaServisi()

    def uygun_odeme_yontemi_sec(self, owner, toplam_tutar):
        yontemler = self.payment_repo.kullanici_secimi(owner) or []
        for method in yontemler:
            if method.kontrol(toplam_tutar):
                return method
        return None

    def odeme_yap(self, owner, payment_method, siparis):
        toplam_tutar = sum([urun["fiyat"] for urun in siparis])
        if not payment_method.kontrol(toplam_tutar):
            raise PaymentSystemError("Yetkilendirme başarısız: Yetersiz bakiye/limit")
        success = payment_method.odeme(toplam_tutar)
        if success:
            self.transaction_repo.islem_ekle({
                "owner": owner,
                "tutar": toplam_tutar,
                "siparis": siparis
            })
        return success

    # Demo veya ulaşım / kulüp ödemeleri için helper
    def odeme_uygula(self, owner, siparis, odeme_tipi="Banka"):
        if odeme_tipi == "Banka":
            toplam = sum([u["fiyat"] for u in siparis])
            return self.banka.odeme_al(owner, toplam, "Uygulama Ödemesi")
        else:
            # Diğer ödeme tipleri (Cüzdan, Kredi Kartı) entegre edilebilir
            odeme_yontemi = self.uygun_odeme_yontemi_sec(owner, sum([u["fiyat"] for u in siparis]))
            if odeme_yontemi:
                return self.odeme_yap(owner, odeme_yontemi, siparis)
            return False
