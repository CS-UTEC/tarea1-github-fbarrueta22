def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True   

number=int(input())
result = isPrime(number)
if result==True:
    print('The number '+ str(number)+ ' is prime')
else:
    print('The number '+str(number)+ ' is not prime')


