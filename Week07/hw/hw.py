from argon2 import PasswordHasher
import time
import json
from tabulate import tabulate


class User:
    user_id = 1
    user_auth = False
    
    def __init__(self, account_create_date=time.ctime()):
        self.user_name = input("User Name: ")
        self.password = PasswordHasher().hash(input("Password: "))
        self.first_name = input("First Name: ")
        self.last_name = input("Last Name: ")
        self.phone = input("Phone Number: ")
        self.birth_date = input("Birth date: ")
        self.account_create_date = account_create_date
        self.role = "passenger"
        

    def user_dict(self):
        return {
            "user ID": User.user_id,
            "user name": self.user_name,
            "password": self.password,
            "first name": self.first_name,
            "last name": self.last_name,
            "phone": self.phone,
            "birth date": self.birth_date,
            "account create date": self.account_create_date,
            "role": self.role,
        }

    def user_role(self):
        if self.role == "admin":
            return True
        else:
            return False
    
    def user(self):
       return f"{self.user_name}"
    
    def id_counter(self,data):
        last_id =1
        if data:
            last_id = max(item.get("user ID",0) for item in data)
        User.user_id = last_id + 1

    def add_user(self):
        try:
            with open("Users.json", "r") as users_file:
                try:
                    data = json.load(users_file)
                    if self.user_name in [d['user name'] for d in data]:
                        print("User Name Exist")
                    else:
                        User.id_counter(self,data)
                        print("User Created")
                        data.append(User.user_dict(self))
                        with open("Users.json", "w") as users_file:
                            json.dump(data, users_file, indent=2)
                except json.JSONDecodeError:
                    data = []
        except FileNotFoundError:
                with open("Users.json", "w") as users_file:
                    print("User Created")
                    data = ([User.user_dict(self)])
                    User.id_counter(self,data)
                    json.dump(data, users_file, indent=2)
        
    def add_admin(self):
        with open("Users.json", "r") as users_file:
            data = json.load(users_file)
            user_input = input("User ID: ")
            if int(user_input) in [d['user ID'] for d in data]:
                user_info = [d for d in data if d["user ID"] == int(user_input)][0]
                user_info["role"]="admin"
        with open("Users.json", "w") as users_file:
            json.dump(data, users_file, indent=2)
        print(f"{user_info["user name"]} {user_info["last name"]} change to Admin")
 
    def login(self):
        print("Site Login".center(50, "*"))
        try:
            with open("Users.json", "r") as users_file:
                    data = json.load(users_file)
                    user_input = input("User name: ")
                    if user_input in [d["user name"] for d in data]:
                        user_info = [d for d in data if d["user name"]==user_input][0]
                        try:
                            PasswordHasher().verify(user_info.get("password"), input("Password: "))
                            User.user_auth = True
                            print("Login Sucessfully") 
                        except Exception:
                            print("Login Failed")               
        except FileNotFoundError:
            print("First Create Account")
        
    def search(self):
        if User.user_auth == True:
            self.user_travel_origin = input("Origin: ")
            self.user_travel_destination = input("Destination: ")
            self.user_travel_date = input("Date: ")

    def show_user_lst(self):
        with open("Users.json", "r") as user_file:
            data = json.load(user_file)
            final = []
            for item in data:
                filter_data = {k:v for k,v in item.items() if k not in {"password"}}
                final.append(filter_data)
            print(tabulate(final,headers="keys"))


class Travel:
    travel_id = 0

    def __init__(self):
        self.travel_origin = input("Origin: ")
        self.travel_destination = input("Destination: ")
        self.travel_time = input("Travel Time: ")
        self.travel_duration = input("Travel Duration: ")
        self.travel_capacity = input("Travel Capacity: ")
        self.available_seats = input("Number of Available Seats: ")
        self.price = input("Price: ")
        self.status = input("Travel Status: ")
        
      

    def travel_dict(self):
        return {
            "ID": Travel.travel_id,
            "origin": self.travel_origin,
            "destination": self.travel_destination,
            "time": self.travel_time,
            "duration": self.travel_duration,
            "capacity": self.travel_capacity,
            "seats": self.available_seats,
            "price": self.price,
            "status": self.status,
        }
    def check_id(self,data):
        last_id =1
        if data:
            last_id = max(item.get("ID",0) for item in data)
        Travel.travel_id = last_id+ 1
        
    
    def add_travel(self):     
        if User.user_auth == True:     
            if User.user_role:
                print(f"Travel {self.travel_origin} to {self.travel_destination} added")
                try:
                    with open("Travel.json", "r") as travel_json:
                        try:
                            data = json.load(travel_json)
                        except json.JSONDecodeError:
                           data = []
                    Travel.check_id(self,data)
                    data.append(Travel.travel_dict(self))
                    with open("Travel.json", "w") as travel_json:
                        json.dump(data, travel_json, indent=2)
                except FileNotFoundError:
                    with open("Travel.json", "w") as travel_json:
                        Travel.travel_id = 1
                        data = ([Travel.travel_dict(self)])
                        json.dump(data, travel_json, indent=2)
                
                
            else:
                print("Access Denied!")
        else:
            print("Access Denied")

    def show_travel_info(self):
        print(Travel.travel_lst)


class Ticket:
    def __init__(self, ticket_id: int, seat_no: int, status: str, create_date):
        self.ticket_id = ticket_id
        self.seat_no = seat_no
        self.status = status
        self.create_date = create_date
        self.user_id = User
        self.tarvel_id = Travel


class Payment:
    def __init__(
        self, payment_id: int, total_price: int, payment_time, payment_status: str
    ):
        self.payment_id = payment_id
        self.total_price = total_price
        self.payment_time = payment_time
        self.payment_status = payment_status
        self.user_id = User
        self.travel_id = Travel


a=User()
# a.add_user()
a.add_admin()
# a.login()
# a.show_user_lst()
# a.add_admin()