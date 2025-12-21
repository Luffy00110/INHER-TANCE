from CreditCardPayment import CreditCardPayment
from datetime import date

#Ödeme işlemi sırasında yetkilendirme başarısız olduğunda fırlatılır.
class AuthorizationError(Exception):
    pass

#Bir ödeme işlemine ait detayları saklar.
class Transaction:
    def __init__(self, owner, amount, payment_type, id=None, tarih=None, komisyon=0):
        self._owner = owner
        self._amount = amount
        self._payment_type = payment_type
        self.komisyon = komisyon
        self._id = id
        self._tarih = tarih or date.today()

    #Özellikler
    @property
    def owner(self):
        return self._owner

    @property
    def amount(self):
        return self._amount

    @property
    def payment_type(self):
        return self._payment_type

    @property
    def id(self):
        return self._id

    @property
    def tarih(self):
        return self._tarih

#Ödeme ve menü işlemlerini yönetir.
class PaymentService:
   
      #Yemekhane menüsünü döndürür. (kategorilere ayrılmış)
      @classmethod
      def _init_yemekhane_menu(cls):
          return {
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

     #Günün menüsünü döndürür.
      @classmethod
      def _init_gunun_menusu(cls):
          return {       
                 "corba": ["Mercimek Çorbası"],
                 "yemek": ["Kayseri Mantısı"],
                 "garnitur": ["Çoban Salata"],
                 "tatli": ["Sütlaç"],
                 "icecek": ["Ayran"],
                 "promosyon": ["Çeyrek ekmek", "500 ml su"]
          } 
        
     #Ayın her haftası için popüler olarak belirlenen yemekhane menülerini listelenmektedir.
      @classmethod
      def _init_ayin_menusu(cls):
           return {
            "1.hafta": ["Mercimek Çorbası", "Tavuk Döner", "Ayran", "Triliçe"],
            "2.hafta": ["Şehriye Çorbası", "Kayseri Yağlaması", "Kola", "Sütlaç"],
            "3.hafta": ["Ezogelin Çorbası", "Et Döner", "Limonata", "Kazandibi" ],
            "4.hafta": ["Domates Çorbası", "İzmir Köfte", "Gazoz", "Baklava"]
        }

     #Kafeterya menüsünü döndürür.
      @classmethod
      def _init_kafeterya_menu(cls):
           return {
              "yiyecek": {
                 "Salamlı Tost": 45,
                 "Kaşarlı Tost": 40,
                 "Karışık Tost": 60,
                 "Hamburger" : 90,
                 "Sandviç": 50,
                 "Açma" : 30,
                 "Kete" : 30,
                 "Simit" : 25,
                 "Poğaça": 20,
            },
              "icecek": {
                 "Ayran": 10,
                 "Maden Suyu" : 30,
                 "Kola" : 60,
            },
              "atistirmalik": {
                 "Cips": 25,
                 "Çikolata": 40,
                 "Bisküvi": 45
            }
        }

     #Kafe menüsünü döndürür.
      @classmethod
      def _init_kafe_menu(cls):
           return {              
              "sicak_icecek": {
                 "Türk Kahvesi": 60,
                 "Latte": 35,
                 "Americano": 45,
                 "Cappuccino": 55,
                 "Salep": 40
            },
              "soguk_icecek": {
                 "Cold Brew": 60,
                 "Frappe": 35,
                 "Iced Latte": 55,
                 "Iced Mocha": 45,
                 "Iced Americano": 50,
                 "Milkshake": 40
            }
       }
        
    #Otomat ürünlerini döndürür.
      @classmethod
      def _init_otomat(cls):
           return {
              "1": {"ad": "Su", "fiyat": 20, "stok": 8},
              "2": {"ad": "Bisküvi", "fiyat": 45, "stok": 8},
              "3": {"ad": "Çikolata", "fiyat": 30, "stok": 8},
              "4": {"ad": "Meyve Suyu", "fiyat": 20, "stok": 8},
              "5": {"ad": "Sakız", "fiyat": 35, "stok": 8},
              "6": {"ad": "Lolipop", "fiyat": 45, "stok": 8}      
        }

      def __init__(self, payment_repo, transaction_repo):
            self.payment_repo = payment_repo
            self.transaction_repo = transaction_repo
            self._yemekhane_menu = type(self)._init_yemekhane_menu()
            self._gunun_menusu = type(self)._init_gunun_menusu()
            self._ayin_menusu = type(self)._init_ayin_menusu()
            self._kafeterya_menu = type(self)._init_kafeterya_menu()
            self._kafe_menu = type(self)._init_kafe_menu()
            self._otomat = type(self)._init_otomat()
    
    #Menü ve sipariş fonksiyonları
      def gunun_menusunden_siparis(self):
          secilenler = []
          for kategori in self._gunun_menusu:
              for ad in self._gunun_menusu[kategori]:
                  for urun in self._yemekhane_menu[kategori]:
                      if urun["ad"] == ad:
                          secilenler.append(urun)
          return secilenler
    
    #Kafeteryadan ürün seçimi yapar.
      def kafeterya_siparis(self, kategori, urun_adi):
          if kategori not in self._kafeterya_menu:
              raise Exception("Geçersiz kategori")
          urun = self._kafeterya_menu[kategori].get(urun_adi)
          if urun is None:
              raise Exception("Ürün bulunamadı")
          if urun.get("stok", 1) <= 0:
              raise Exception("Ürün stokta yok")
          urun["stok"] -= 1
          return {"ad": urun_adi, "fiyat": urun["fiyat"]}
    
    #Kafe ürününün ekleri
      _bardak_boyut = { "tall": 0, "grande": 20,  "venti": 35 }

      _ekstra_shot_ucreti = 15

    #Kafe ürününü boyut ve shot ekleyerek fiyatlandırır.
      def kafe_siparis(self, kategori, kahve_adi, boyut, shot=0):
        if kategori not in self._kafe_menu:
            raise Exception("Geçersiz içecek kategorisi!")
        if kahve_adi not in self._kafe_menu[kategori]:
            raise Exception("Kahve bulunamadı!")
        if boyut not in type(self)._bardak_boyut:
            raise Exception("Geçersiz bardak boyutu!")
        
        fiyat = self._kafe_menu[kategori][kahve_adi]
        fiyat += type(self)._bardak_boyut[boyut]
        fiyat += shot * type(self)._ekstra_shot_ucreti
        return fiyat
      
    #Otomat ürününü stok kontrolü ile döndürür.
      def otomat_siparis(self, kod):
        if kod not in self._otomat:
            raise Exception("Geçersiz ürün kodu")
        urun = self._otomat[kod]
        if urun["stok"] <= 0:
            raise Exception("Otomatta ürün kalmadı")
        urun["stok"] -= 1
        return {"ad": urun["ad"],"fiyat": urun["fiyat"]} 

    # Menüdeki tüm kategorileri ve ürünleri döndürmeyi sağlar.
      def yemekhane_menu_listele(self):
          return self._yemekhane_menu
    
      def kafeterya_menu_listele(self):
          return self._kafeterya_menu
    
      def kafe_menu_listele(self):
          return self._kafe_menu
    
      def otomat_menu_listele(self):
          return self._otomat
    
    # Kullanıcının seçtiği ürünlere göre sipariş oluşturur.
      def siparis_olustur(self, secilen_urunler):
          siparis = []
          for kategori in self._yemekhane_menu:
              for urun in self._yemekhane_menu[kategori]:
                  if urun["ad"] in secilen_urunler and urun not in siparis:
                      siparis.append(urun)
          return siparis
    
    #Toplam tutarı hesaplama
      @staticmethod
      def toplam_tutar_hesapla(siparis):
          return sum([urun["fiyat"] for urun in siparis])
    
    #Kullanıcının bakiyesine göre otomatik ödeme yöntemi seçilir.
      def uygun_odeme_yontemi_sec(self, owner, toplam_tutar):
          yontemler = self.payment_repo.kullanici_secimi(owner) or []
          for method in yontemler:
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
        try:
            success = payment_method.odeme(toplam_tutar)
            if success:
                # Ödeme sonrası Transaction kaydı oluşturma
                if isinstance(payment_method, CreditCardPayment):
                   komisyon = payment_method.komisyon_tutari(toplam_tutar)
                else:
                   komisyon = 0
                self.transaction_repo.ekle(Transaction(owner, toplam_tutar, type(payment_method).__name__, komisyon))
                return True
            return False
        except AuthorizationError as e:
            print(e)
            return False
        
    #Ödeme iade metodu
      def odeme_iade(self, transaction_id):
        islem = self.transaction_repo.id_ile_getir(transaction_id)
        if islem:
            self.transaction_repo._transactions.remove(islem)
            print(f"{islem.amount} TL iade edildi: {islem.owner}")
            return True
        return False
        
    #İşlem geçmişini listeleme
      def islem_gecmisi(self, owner=None):
          if owner:
              return self.transaction_repo.kullanici_secimi(owner)
          return self.transaction_repo.listele()
    
      def tarih_araligi_raporu(self, baslangic, bitis):     
          return self.transaction_repo.tarih_araligi_getir(baslangic, bitis)