#5) program to count no. of odd or even elements

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_even = 0
count_odd = 0
for i in numbers:
    if i%2==0:
        count_even += 1
    else:
        count_odd += 1
print("Number of even number : ", count_even)
print("Number of odd number : ", count_odd)
