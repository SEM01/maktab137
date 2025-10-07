'''
Write a function that converts seconds into format
hour:minute:second
3670->1:1:10
'''

def time_convertor(time_in_second):
    hour = time_in_second//3600
    minute = (time_in_second%3600)//60
    second = (time_in_second%3600)%60
    return f'{time_in_second} ---> {hour}:{minute}:{second}'


