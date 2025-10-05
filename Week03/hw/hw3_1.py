def bubble_sort(number_list):
    for i in range(len(number_list)-1):
        for j in range(len(number_list)-i-1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
    return number_list


number_list = [36,10,5,66,7]
print(bubble_sort(number_list))