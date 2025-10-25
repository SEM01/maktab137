class User:
    Admin = []
    Passenger = []

    def __init__(
        self,
        user_id: int,
        user_name,
        password,
        first_name: str,
        last_name: str,
        tel,
        birth_date,
        account_create_date,
    ):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.birth_date = birth_date
        self.account_create_date = account_create_date


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
