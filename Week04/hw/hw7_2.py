'''
تابعی که دو ورودی
name,age
دریافت کند و چاپ کند
ورودی ها از نوع
keyword only
'''
def intro(*,name,age):
    print(f"Hi, {name}. You're {age}")

intro(name="Ali",age=20)