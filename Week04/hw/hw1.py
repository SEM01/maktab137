from datetime import datetime


'''
دکوراتوری بنویسید که تابع مورد نظر را فقط در محدوده زمانی مشخصی اجرا کند
'''


hour = datetime.now().hour

def restrict_hours(start, end):
    def wrapper(func):
        def check_time():
            if start<hour<end:
                func()
            else:
                print("Not Allowed....")
        return check_time
    return wrapper
    
@restrict_hours(start=9, end=17)
def do_work():
    print("working....")

do_work()