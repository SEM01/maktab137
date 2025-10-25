from argon2 import PasswordHasher
import time
import json


class User:
    Admin = []
    Passenger = []
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

    def __eq__(self, other):
        if self.user_name == other.user_name:
            print("User name Exist")

    def to_dict(self):

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

    # def add_passenger(self):
    #     if any(value["user name"] == self.user_name for value in User.Passenger):
    #         print("User name exist")
    #     else:
    #         User.user_id += 1
    #         self.role = "passenger"
    #         User.Passenger.append(User.to_dict(self))

    #     print(User.Passenger)

    def add_admin(self):
        User.user_id += 1000
        self.role = "admin"
        User.Admin.append(User.to_dict(self))
        print(User.Admin)

    # def add_user(self):

    #     self.user_id = User.user_id + 1
    #     if self.role == "admin":
    #         if self.user_name not in User.Admin:
    #             User.Admin.append(self.user_name)
    #         else:
    #             print("User name Exist")
    #     elif self.role == "passenger":
    #         if self.user_name not in User.Passenger:
    #             if self.user_name not in User.Passenger:
    #                 User.Passenger.append(self.user_name)
    #             else:
    #                 print("User name Exist")
    #     else:
    #         print("Register Failed.")
    #     print(self.user_id)


class Travel:
    def __init__(
        self,
        travel_id: int,
        travel_origin: str,
        travel_destination: str,
        travel_time,
        travel_duration,
        travel_capacity,
        availabel_seats,
        price,
        travel_status,
    ):
        self.travel_id = travel_id
        self.travel_origin = travel_origin
        self.travel_destination = travel_destination
        self.travel_time = travel_time
        self.travel_duration = travel_duration
        self.travel_capacity = travel_capacity
        self.available_seats = availabel_seats
        self.price = price
        self.status = travel_status


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


a = User()
# a.add_passenger()
b = User()
# b.add_passenger()
