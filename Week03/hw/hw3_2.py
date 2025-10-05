def numbers_category(numbers, low, high):
    
    pivot = numbers[high]
    print("pivot: ", pivot)
    
    i = low -1
    for j in range(low,high):
        
        if numbers[j] <= pivot:
            i +=1
            numbers[i],numbers[j]=numbers[j],numbers[i]
    numbers[i+1],numbers[high] = numbers[high],numbers[i+1]
    
    return i+1

def quick_sort(numbers, low=0, high=None):
    if high is None:
        high = len(numbers) - 1

    if low < high:
        pivot_index = numbers_category(numbers, low, high)
        print("1:" ,numbers, low, high)
        quick_sort(numbers, low, pivot_index-1)
        print("high:",high)
        quick_sort(numbers, pivot_index+1, high)
        print("2: ",numbers, low, high)

list1=[23,12,25,10,1]
quick_sort(list1)
print(list1)