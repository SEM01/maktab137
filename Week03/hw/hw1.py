
from itertools import permutations
import copy


words = input("Enter a statement: ")

words_lst = words.split()

def posible():
    start = 2
    while start <5:
        yield list(permutations(words_lst,start))
        start +=1

lst_pos = posible()
final_lst=[]
for word in lst_pos:
    final_lst.append(word)


shallow_copy = copy.copy(final_lst)
deep_copy = copy.deepcopy(final_lst)
final_lst[0][0]='maktab137'
print("shallow_copy".center(100,'*'))
print(shallow_copy)
print("deep_copy".center(100,'*'))
print(deep_copy)
print(len(final_lst[2]))