# "(And
# .Mileage.range(..30000).
# _
# .Year.range(..202506).
# _
# .Hidden.N.
# _
# .(C.CarType.N._.Manufacturer.BMW.)
# _
# .ServiceMark.EncarDiagnosisP0.
# _
# .BuyType.Delivery.
# _
# .OfficeCityState.경기.
# )",
# type
# brand
# model
# year
# mileage
# price
# encar_diagnosis
# https://api.encar.com/search/car/list/premium?count=true&q=(And.(C.CarType.N._.Manufacturer.%EB%9E%9C%EB%93%9C%EB%A1%9C%EB%B2%84.))&sr=%7CModifiedDate%7C0%7C5

class Query:
    car_filter: str = None
    year_filter: str = None
    month_filter: str = None

    @staticmethod
    def build(self):
        pass

    def add_car_filter(self, type="N", brand: str = None, model: str = None):
        if not type and not brand:
            raise ValueError("At least type or brand must be specified")

    def add_year_filter(self, start: int = None, end: int = None):
        if not start and not end:
            raise ValueError("At least start or end year must be specified")

    def add_month_filter(self):
        pass

    def add_mileage_filter(self):
        pass

    def add_price_filter(self):
        pass

    def add_diagnosis_filter(self):
        pass
