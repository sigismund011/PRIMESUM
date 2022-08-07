#write a code to calculate the sum of n prime numbers
prime = int(input("Enter any number:"))
sum = 2

for num in range(prime+1):
    if int(num > 1):
        for i in range(2, num):
            if (num % i)== 0:
                break
            elif i == (num - 1):
                sum += num

print("The prime sum is" , str(sum))