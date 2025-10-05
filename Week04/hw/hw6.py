def str_diffrence(string1, string2):
    count = 0
    for letter in range(len(string1)):
        if string1[letter]==string2[letter]:
            pass
        else:
            count +=1
    print(f"Total Difference: {count}")


input1 = "aBcD"
input2 = "ABcd"
str_diffrence(input1, input2)

