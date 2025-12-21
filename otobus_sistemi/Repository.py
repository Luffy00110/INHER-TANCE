class TransportRepository:
    def __init__(self):
        self.__database = []

    def add(self, arac):
        self.__database.append(arac)

    def remove(self, arac_id):
        arac = self.find_by_id(arac_id)
        if arac:
            self.__database.remove(arac)
            return True
        return False

    def get_all(self):
        return self.__database

    def find_by_id(self, arac_id):
        for arac in self.__database:
            if arac.get_id() == arac_id:
                return arac
        return None

    def filter_by_capacity(self, min_kapasite):
        uygun_araclar = []
        for arac in self.__database:
            # Kapasite kontrolu
            try:
                kap = arac.get_kapasite()
                if kap >= min_kapasite:
                    uygun_araclar.append(arac)
            except:
                continue
        return uygun_araclar