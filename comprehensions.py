from math import sqrt

def is_prime(num):
    count = 2
    flag = True
    while count <= int(sqrt(num)):
        if num % count == 0:
            flag = False
            break
        else:
            count +=1
    return flag

l = [x for x in range(1,101) if is_prime(x)] #create a list of all primes from 1 - 100 using Python Comprehension
print(l,end='\n\n')

sum_of_primes = sum(x for x in range(1,101) if is_prime(x)) #summing all prime numbers from 1 to 100 using a Generator Expression, using virtually no memory
print(sum_of_primes, end='\n\n')

list_of_lists = [[x for x in range(1, y) if is_prime(x)] for y in range(2,11)] #creating a list of lists using a nested comprehension
print(list_of_lists)

