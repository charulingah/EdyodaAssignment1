#using for loop

n=9
n1, n2 = 0, 1
for i in range(n):  #for loop upto nth term
      sum = n1 + n2  #Logic for the fibonacci series
      n1 = n2
      n2 = sum
      print(n1)
