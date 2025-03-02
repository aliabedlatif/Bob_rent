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
    def __init__(self, brand, model, year,seating_capacity ,rental_price_per_day):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def displayinfo(self):
        return f"car:{self.brand} {self.model}, Year:{self.year}, Seats:{self.seating_capacity}, Rent Price: ${self.rental_price_per_day}/day"
        
class Bike(Vehicles):
    def __init__(self, brand, model, year,engine_capacity, rental_price_per_day):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity
    
    def diplayinfo(self):
        return f"Bike:{self.brand} {self.model}, Year:{self.year}, Engine:{self.engine_capacity}cc, Rent Price: ${self.rental_price_per_day}/day"

car = Car("Toyota","Corolla",2020,5,50)

bike = Bike("Yamaha","R1",2019,998,30)

print(car.displayinfo())

print(bike.displayinfo(),"\n")

rentcost = car.calculate_rental_cost(3)

print(f"Rental cost for Toyota corolla for 3 days: ${rentcost}")

rentcost = bike.calculate_rental_cost(5)

print(f"Rental cost for Yamaha R1 for 5 days: ${rentcost}\n")