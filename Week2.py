# class activity
#numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#count_odd = 0
#count_even = 0
# for x in numbers:
#     if not x % 2:
#  	     count_even+=1
#       else:
#    	     count_odd+=1
#print("Number of even numbers :",count_even)
#print("Number of odd numbers :",count_odd)

# even calculation and Average
n = input("Enter Number to calculate average... ")

n = int(n)

sum = 0

num = 0

for num in range(n):

    if((num % 2) == 0):
        sum += num
        average = sum / n
        print("Average of even numbers is: ", average)

    else:
        print("Average of Odd numbers is: ", average)

   # if (not (num % 2) == 0):
    #    sum += num;
     #   average  = sum / n
        #  print("SUM of Odd numbers is: ", sum )
       # print("Average of Odd numbers is: ", average )
