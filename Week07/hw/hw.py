from argon2 import PasswordHasher
import time
import json
from tabulate import tabulate
from operator import itemgetter



'''/---------------------User Section---------------------------/'''
class User:
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
        with open("Users.json","r") as users_file:
            data = json.load(users_file)
            if data["role"] == "admin":
                return True
            else:
                return False
    
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
    @staticmethod  
    def add_admin():
        with open("Users.json", "r") as users_file:
            data = json.load(users_file)
            user_input = input("User ID: ")
            if int(user_input) in [d['user ID'] for d in data]:
                user_info = [d for d in data if d["user ID"] == int(user_input)][0]
                user_info["role"]="admin"
        with open("Users.json", "w") as users_file:
            json.dump(data, users_file, indent=2)
        print(f"{user_info["user name"]} {user_info["last name"]} change to Admin")
    @staticmethod
    def login():
        print("Login".center(50, "*"))
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
    @staticmethod  
    def search():
        print("Ticket Search".center(50,"*"))
        if User.user_auth == True:
            user_travel_origin = input("Origin: ").lower()
            user_travel_destination = input("Destination: ").lower()
            user_travel_date = input("Date: ").lower()
            try:
                with open("Travel.json", "r") as travel_file:
                    data = json.load(travel_file)
                    filtered_data = [item for item in data if item["origin"] == user_travel_origin and item["destination"]==user_travel_destination and item["date"]>= user_travel_date ]
                    sorted_data = sorted(filtered_data, key=itemgetter("date", "time", "price"))
                    if filtered_data:
                        print(tabulate(sorted_data,headers="keys"))
                    if filtered_data ==[]:
                        print("No result")
            except FileNotFoundError:
                print("Sorry, No Flight availabe")
        else:
            print("Access Denied, Please Login First")
    @staticmethod
    def show_user_lst():
        if User.user_auth == True:
            if User.user_role:
                with open("Users.json", "r") as user_file:
                    data = json.load(user_file)
                    final = []
                    for item in data:
                        filter_data = {k:v for k,v in item.items() if k not in {"password"}}
                        final.append(filter_data)
                    print(tabulate(final,headers="keys"))
        else:
            print("Access Denied")

'''/---------------------Travel Section---------------------------/'''
class Travel:
    def __init__(self):
        self.travel_id = 0
        self.travel_origin = input("Origin: ")
        self.travel_destination = input("Destination: ")
        self.travel_time = input("Travel Time: ")
        self.travel_duration = input("Travel Duration: ")
        self.travel_capacity = input("Travel Capacity: ")
        self.available_seats = int(input("Number of Available Seats: "))
        self.price = input("Price: ")
        self.status = input("Travel Status: ")
        self.date = input("Date: ") 

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
            "Date": self.date
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
    @staticmethod
    def show_travel_info():
        with open("Travel.json","r") as travel_file:
            data = json.load(travel_file)
            final = []
            for item in data:
                final.append(item)
            print(tabulate(final,headers="keys"))

    def edit_travel(self):
        if User.user_auth == True:
            if User.user_role:
                print("Edit Flight Info".center(50,'*'))
                with open("Travel.json", "r") as travel_file:
                    data = json.load(travel_file)
                    user_input = input("Travel ID for Edit: ")
                    if int(user_input) in [d['ID'] for d in data]:
                        travel_info = [d for d in data if d['ID'] == int(user_input)][0]
                        travel_info['origin']=input("Origin: ")
                        travel_info['destination']=input("destination: ")
                        travel_info['time']=input("time: ")
                        travel_info['duration']=input("dusration:")
                        travel_info['capacity']=input("capacity: ")
                        travel_info['seats']=input("seats:")
                        travel_info['price']=input("price: ")
                        travel_info['status']=input("status: ")
                with open("Travel.json", "w") as tarvel_file:
                    json.dump(data,tarvel_file, indent=2)
                print(f"Flight ID:{travel_info["ID"]} Edited")

    def cancel_travel(self):
        if User.user_auth == True:
            if User.user_role:
                print("Flight Canceling".center(50,"*"))
                with open("Travel.json", "r") as travel_file:
                    data = json.load(travel_file)
                    user_input = input("Travel ID for Canceling: ")
                    if int(user_input) in [d['ID'] for d in data]:
                        travel_info = [d for d in data if d['ID'] == int(user_input)][0]
                        travel_info['status']="Cancel"
                with open("Travel.json", "w") as travel_file:
                    json.dump(data, travel_file, indent=2)
                print(f"Travel ID: {travel_info['ID']} Canceled")

'''/---------------------Ticket Section---------------------------/'''
class Ticket:
    def ticket_status(self):
        return self.status
    
    @staticmethod
    def reservation():
        try:
            with open("Travel.json", "r") as travel_file:
                data = json.load(travel_file)
            travel_id = int(input("Travel id: "))
            filter_data = [item for item in data if item["ID"]==travel_id][0]
            if filter_data["status"]=="available":
                if filter_data["seats"] > 1 :
                    try:
                        with open("Ticket.json", "r") as ticket_file:
                            try:
                                data = json.load(ticket_file)
                            except json.JSONDecodeError:
                                data = []
                        Ticket.ticket_status="Reserved"
                        filter_data["seats"] -= 1
                        last_id =1
                        if data:
                            last_id = max(item.get("ticket ID",0) for item in data)
                        Ticket.ticket_id = last_id+ 1
                        print(f"Your Ticket with ID:{Ticket.ticket_id} Reserved")
                        data_json = {
                            "ticket ID":Ticket.ticket_id,
                            "Origin":filter_data["origin"],
                            "Destination":filter_data["destination"],
                            "Status":Ticket.ticket_status,
                            "Date":time.ctime(),
                        }
                        data.append(data_json)
                        with open("Ticket.json" , "w") as ticket_file:
                            json.dump(data, ticket_file, indent=2)
                        with open("Travel.json","w") as travel_file:
                            json.dump(filter_data, travel_file, indent=2)
                    except FileNotFoundError:
                        with open("Ticket.json", "w") as ticket_file:
                            Ticket.ticket_id = 1
                            Ticket.ticket_status="Reserved"
                            print(f"Your Ticket with ID:{Ticket.ticket_id}  Reserved")
                            data_json = {
                            "ticket ID":Ticket.ticket_id,
                            "Origin":filter_data["origin"],
                            "Destination":filter_data["destination"],
                            "Status":Ticket.ticket_status,
                            "Date":time.ctime(),
                            }
                            json.dump(data_json, ticket_file, indent=2)
                else:
                    print("Capacity is Full")
            else:
                print("Flight not available")
        except FileNotFoundError:
            print("No Flight Exist")
                
 
'''/---------------------Payment Section---------------------------/'''       

class Payment:
    def __init__(self):
        self.payment_id = 1
        self.total_price = None
        self.payment_time = time.ctime()
        self.payment_status = None
        self.user_id = None
        self.travel_id = None

    def payment_dict(self):
        return {
            "ticket ID": Ticket.ticket_id,
            "Ticket price":self.total_price,
            "Status":self.payment_status,
        }
    @staticmethod
    def pay():
        try:
            with open("Ticket.json","r") as ticket_file:
                ticket_data = json.load(ticket_file)
            ticket_id = int(input("Ticket ID: "))
            filter_data = [item for item in ticket_data if item["ticket ID"]==ticket_id][0]
            if filter_data["Status"] == "Reserved":
                pay = int(input("pay? (1.yes 2.no): "))
                if pay == 1:
                    print("-------------------------")
                    print("|Thanks for your purchase|")
                    print("--------------------------")
                    filter_data["Status"] = "Sold"
                    filter_data["Date"] = time.ctime()
                else:
                    print("Cancel")
            else:
                print(f"ticket with ID: -{ticket_id}- not exist for sale")
            with open("Ticket.json","w") as ticket_file:
                json.dump(ticket_data, ticket_file, indent=2)
        except FileNotFoundError:
            print("No Ticket Exist")   
                





        

