''' -------------------Begining------------------- '''
class Car:
    def __init__(self, plate_number:int, model:str, battery_level:int, mileage:int, status:str):
        self.plate_number = plate_number
        self.model = model
        self.battery_level = battery_level
        self.mileage = mileage
        self.status = status
    
    def drive(self,km):
        self.mileage = km
        return self.mileage

    def charge(self,amount):
        self.battery_level = amount
        return self.battery_level

    def __str__(self):
        header = "Car Info".center(50,"-")
        info = f"Model--> {self.model}\nPlate Number--> {self.plate_number}\nBattery Level--> {self.battery_level}%\nMileage--> {self.mileage} K.M\nStatus--> {self.status}"
        return f"{header}\n{info}"
    
    def __eq__(self, other):
        return self.plate_number == other.plate_number

    def __lt__(self,other):
        return self.mileage < other.mileage
    
class Driver:
    def __init__(self, name:str,experince_level:int, assigned_car=None):
        self.name = name
        self.experince_level = experince_level
        self.assigned_car = assigned_car
    
    def assign_car(self):
        self.assigned_car =Car

'''-----------------------End------------------------------'''
        

        
'''---------------------Test Env---------------------------'''
car1 = Car(
    plate_number=1,
    model="Peykan",
    battery_level=10,
    mileage=100,
    status="available"
    )
car2 = Car(
    plate_number=2,
    model="Pride",
    battery_level=5,
    mileage=180,
    status="available"
    )
car3 = Car(
    plate_number=3,
    model="Samand",
    battery_level=5,
    mileage=90,
    status="available"
    )

driver1 = Driver(name="Ali",experince_level=1,assigned_car=None)
driver1.assign_car=car3
print(driver1.assigned_car)

