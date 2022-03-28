#Reverse a string Edyoda

s = input("Enter a string to be reversed : ")
i = len(s)-1
result = " "
while i >= 0:
    result = result+s[i]
    i = i-1
print(result)
