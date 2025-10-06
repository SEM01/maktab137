from datetime import datetime

hour = datetime.now().hour

def restrict_hours(start, end):
    def wrapper(func):
        def check_time(*args):
            if start<hour<end:
                func(*args)
            else:
                print("Not Allowed....")
        return check_time
    return wrapper
    
@restrict_hours(start=9, end=17)
def do_work():
    print("working....")

do_work()