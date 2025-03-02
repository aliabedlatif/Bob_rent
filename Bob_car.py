class Vehicles:
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day

    def displayinfo(self):
        return f"Car:{self.brand},{self.model},Year:{self.year},Rent price: ${self.rental_price_per_day}/day"
    
    def Calculate_rental_cost(self,days):
        rent_cost = days * self.rental_price_per_day
        return rent_cost
    
class Car(Vehicles):
    def __init__(self, brand, model, year, rental_price_per_day):
        super().__init__(brand, model, year, rental_price_per_day)
        