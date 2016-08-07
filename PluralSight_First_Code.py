import random

minInt = 1
maxInt = 10
rand = random.randint(minInt, maxInt)

def process(num):
    flag = False
    if num == rand:
        print('You got it!')
        flag = True
    elif (num > rand):
        print('Close! Youre Above by: ' + str(num - rand))
    else:
        print('Close! Youre below by: ' + str(rand - num))
    return flag

found = False
while not found:
    message = "Please pick a number between {0} and {1}"
    print(message.format(minInt, maxInt))
    found = process (int(input()))
    


