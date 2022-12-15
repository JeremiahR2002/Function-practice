# Write a Python function called max_num()to find the maximum of three numbers.

def max_num (a, b, c):
    list = [a, b, c]
    return max(list)

a = 20
b = 40
c = 70

print(max_num(a, b, c))

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(myList):
    answer = 1
    for x in myList:
        answer = answer * x
    return answer

numbers = [7,6,9]
print(mult_list(numbers))

# Write a Python function called rev_string() to reverse a string.

def rev_string(x):
    return x[::-1]

text = rev_string("looc repus si sihT")

print(text)

# Write a Python function called num_within() to check whether a number falls in a given range

def num_within(x,a,b):
    if x in range (1,9):
        print("we hit the dot!")
    else:
     print("we just missed it!")

num_within(6,12,14)

# Write a Python function called num_within() to check whether a number falls in a given range. I had to do extensive research to figure this one out

x = 8

for i in range(x):
    print(' '*(x-i), end='')

    print(' '.join(map(str, str(11**i))))

