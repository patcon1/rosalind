# the sum of odd integers between a and b inclusive

a = int(input("please enter an integer a:"))
b = int(input("please enter an integer b:"))
result = 0

while a<=b:
    if a%2 != 0:
        result +=a
    a +=1
print("the sum of odd numbers between a and b is",result)
