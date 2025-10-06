'''
برنامه ای که با اسنفاده از تابع بازگشتی عناصر یک لیست تو در تو را جمع کند
'''
def nested_sum(number_list):
    sum = 0
    for item in range(len(number_list)):
        if type(number_list[item])==list:
            sum += nested_sum(number_list[item])
        else:
            sum +=number_list[item]
    return sum

list1=[1,[2,3,[4,1]]]
print(nested_sum(list1))