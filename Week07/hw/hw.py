from argon2 import PasswordHasher
import time


class User:
    users = []
    user_id = 0
    

    def __init__(self, account_create_date=time.ctime()):
        self.user_name = input("User Name: ")
        self.password = PasswordHasher().hash(input("Password: "))
        self.first_name = input("First Name: ")
        self.last_name = input("Last Name: ")
        self.phone = input("Phone Number: ")
        self.birth_date = input("Birth date: ")
        self.account_create_date = account_create_date
        self.role = None

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
        return self.role
    
    def user(self):
       return f"{self.user_name}"

    def add_user(self):
        if list(filter(lambda user: user["user name"] == self.user_name, User.users)):
            print("User name exist")
        else:
            User.user_id += 1
            self.role = "passenger"
            User.users.append(User.user_dict(self))
            print("User Created")

    def add_admin(self):
        user_admin = list(filter(lambda user: user["user name"] == self.user_name, User.users))[0]
        user_admin["role"] = "admin"
        user_admin["user ID"] = User.user_id + 1000

        # User.users.update(User.user_dict(self))
        print(f"{self.user_name} change to Admin")
 
    def login(self):
        print("Site Login".center(50, "*"))
        user_login = list(filter(lambda user: user["user name"] == User.user(self), User.users))[0]
        if input("User name: ") == user_login.get("user name"):
            try:
                PasswordHasher().verify(user_login.get("password"), input("Password: "))
                print("Login Succsefully")
                return True
            except:
                print("Login Failed")
                return False
        else:
            print("User not found")

    def search(self):
        if User.login(self) == True:
            self.user_travel_origin = input("Origin: ")
            self.user_travel_destination = input("Destination: ")
            self.user_travel_date = input("Date: ")

    def show_user_lst(self):
        print(User.users)


class Travel:
    travel_id = 0
    travel_lst = []
    User.login_status = classmethod(User.login)

    def __init__(self):
        self.travel_origin = input("Origin: ")
        self.travel_destination = input("Destination: ")
        self.travel_time = input("Travel Time: ")
        self.travel_duration = input("Travel Duration: ")
        self.travel_capacity = input("Travel Capacity: ")
        self.available_seats = input("Number of Available Seats: ")
        self.price = input("Price: ")
        self.status = input("Travel Status: ")
        print(User.login_status)
      

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
    @staticmethod
    def add_travel():
        print("ok")
        if User.login == True:
            print("1")
            if User.user_role == "admin":
                Travel.travel_id += 1
                Travel.travel_lst.append(Travel.travel_dict())
                print("ok")
                # print(f"Travel {self.travel_origin} to {self.travel_destination} added")
            else:
                print("Access Denied!")

    def show_tarvel_info(self):
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


b = User()
b.add_user()
# b.add_admin()
b.login()
t=Travel()
t.add_travel()
