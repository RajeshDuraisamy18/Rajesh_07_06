# number = int(input("Enter the number:"))
# i = 1
# while i <=10:
    # j = i * number
    # print("Your value is:",j)
    # i += 1
# number = int(input("Enter the number:"))
# while number <=100:
    # if (number%2 == 0):
        # print(number)
        # number += 1
    # else:
        # number += 1
        
total_sum = 0        
while True:       
    number = int(input("Enter a number: "))
    if number > 0:
        print("The number is positive.")
        total_sum += number
    else:
        print("The number is not positive. Sorry Rajesh better luck next time")
        print("Sum of positive numbers:", total_sum)
        break
        
    
        

        

    
