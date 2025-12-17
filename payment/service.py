from datetime import date

class AuthorizationError(Exception):
    pass

class Transaction:
    def __init__(self, owner, amount, payment_type, id=None, tarih=None):
        self.owner = owner
        self.amount = amount
        self.payment_type = payment_type
        self.id = id
        self.tarih = tarih or date.today()


class PaymentService:
    def __init__(self, payment_repo, transaction_repo):
        self.payment_repo = payment_repo
        self.transaction_repo = transaction_repo

        # Yemekhane menüsü (kategorilere ayrılmış)
        self.menu = {
            "corba": [
                {"ad": "Mercimek Çorbası", "fiyat": 40},
                {"ad": "Ezogelin Çorbası", "fiyat": 30},
                {"ad": "Domates Çorbası", "fiyat": 30},
                {"ad": "Yayla Çorbası", "fiyat": 20},
                {"ad": "Şehriye Çorbası", "fiyat": 20},
                {"ad": "Tutmaç Çorbası", "fiyat": 30},
                {"ad": "Sebze Çorbası", "fiyat": 20},
            ],
            "yemek": [
                {"ad": "Kayseri Mantısı", "fiyat": 70},
                {"ad": "Kayseri Yağlaması", "fiyat": 80},
                {"ad": "Et Döner", "fiyat": 90},
                {"ad": "Kıymalı Pide", "fiyat": 50},
                {"ad": "Tavuk Döner", "fiyat": 60},
                {"ad": "Somon Balık", "fiyat": 60},
                {"ad": "İzmir Köfte", "fiyat": 70},              
                {"ad": "Karnıyarık", "fiyat": 40},
                {"ad": "Spagetti Makarna", "fiyat": 30},
                {"ad": "Tavuk Şiş", "fiyat": 80},
                {"ad": "Hünkar Beğendi", "fiyat": 60},
                {"ad": "Tavuk Sote", "fiyat": 75},
                {"ad": "Kuru Fasulye", "fiyat": 40}
            ],
            "garnitur": [
                {"ad": "Çoban Salata", "fiyat": 30},
                {"ad": "Rus Salata", "fiyat": 40},
                {"ad": "Pirinç Pilavı", "fiyat": 30},
                {"ad": "Bulgur Pilavı", "fiyat": 25},
                {"ad": "Makarna", "fiyat": 30},
                {"ad": "Patates Kızartması", "fiyat": 25},
                {"ad": "Yoğurt", "fiyat": 30}
            ],

            "tatli": [
                {"ad": "Baklava", "fiyat": 50},
                {"ad": "Kemalpaşa Tatlısı", "fiyat":40},
                {"ad": "Triliçe", "fiyat": 35},
                {"ad": "Sütlaç", "fiyat": 35},
                {"ad": "Kadayıf", "fiyat": 30},
                {"ad": "Kazandibi", "fiyat": 30},
                {"ad": "Şekerpare", "fiyat": 25},
                {"ad": "İrmik Helvası", "fiyat": 30}
            ],
            "icecek": [
                {"ad": "Ayran", "fiyat": 10},
                {"ad": "Kola", "fiyat": 30},
                {"ad": "Meyve Suyu", "fiyat": 15},
                {"ad": "Çay", "fiyat": 10},
                {"ad": "Gazoz", "fiyat": 25},
                {"ad": "Limonata", "fiyat": 25}
            ],
            "promosyon": [
                {"ad": "Çeyrek ekmek", "fiyat": 0},
                {"ad": "500 ml su", "fiyat": 0}
            ]
        }

        self.gunun_menusu = {
            "corba": ["Mercimek Çorbası"],
            "yemek": ["Kayseri Mantısı"],
            "garnitur": ["Çoban Salata"],
            "tatli": ["Sütlaç"],
            "icecek": ["Ayran"],
            "promosyon": ["Çeyrek ekmek", "500 ml su"]
        } 

        self.ayin_menusu = {
            "1.hafta": ["Mercimek Çorbası", "Tavuk Döner", "Ayran", "Triliçe"],
            "2.hafta": ["Şehriye Çorbası", "Kayseri Yağlaması", "Kola", "Sütlaç"],
            "3.hafta": ["Ezogelin Çorbası", "Et Döner", "Limonata", "Kazandibi" ],
            "4.hafta": ["Domates Çorbası", "İzmir Köfte", "Gazoz", "Baklava"]
        }
    def gunun_menusunden_siparis(self):
        secilenler = []

        for kategori in self.gunun_menusu:
            for ad in self.gunun_menusu[kategori]:
                for urun in self.menu[kategori]:
                    if urun["ad"] == ad:
                        secilenler.append(urun)
        return secilenler
    
    
    def ayin_menusunu_getir(self):
        return self.ayin_menusu


    # Menüdeki tüm kategorileri ve ürünleri döndürmeyi sağlar.
    def menu_listele(self):
        return self.menu

    # Kullanıcının seçtiği ürünlere göre sipariş oluşturur.
    def siparis_olustur(self, secilen_urunler):
        siparis = []

        for kategori in self.menu:
            for urun in self.menu[kategori]:
                if urun["ad"] in secilen_urunler:
                    siparis.append(urun)

        return siparis
    
    #Toplam tutarı hesaplama
    def toplam_tutar_hesapla(self, siparis):
        toplam = 0
        for urun in siparis:
            toplam += urun["fiyat"]
        return toplam
    
    #Kullanıcının bakiyesine göre otomatik ödeme yöntemi seçilir.
    def uygun_odeme_yontemi_sec(self, owner, toplam_tutar):
        for method in self.payment_repo.kullanici_secimi(owner):
          if method.kontrol(toplam_tutar):
            return method
        return None

    #Ödeme gerçekleştirme
    def odeme_yap(self, owner, payment_method, siparis):
        if payment_method is None:
            raise AuthorizationError("Uygun ödeme yöntemi bulunamadı")
        toplam_tutar = self.toplam_tutar_hesapla(siparis)
        if not payment_method.kontrol(toplam_tutar):
           raise AuthorizationError("Yetkilendirme başarısız: Yetersiz bakiye/limit")
        if payment_method.odeme(toplam_tutar):
            self.transaction_repo.islem_ekle(Transaction(owner, toplam_tutar, type(payment_method).__name__))
            return True
        return False

    #İşlem geçmişini listeleme
    def islem_gecmisi(self, owner=None):
        if owner:
            return self.transaction_repo.kullanici_secimi(owner)
        return self.transaction_repo.listele()
    
    def tarih_araligi_raporu(self, baslangic, bitis):     
        return self.transaction_repo.tarih_araligi_getir(baslangic, bitis)
