def get_order():
    print("[command] [item] (Command is A to Add, D to Delete, Q to Quit, P to Print)")
    line = input()

    command = line[:1]
    item = line[2:]
    return (command, item)
    
def add_cart(item, cart):
    if not item in cart:
        cart[item] = 0
    cart[item] += 1

def remove_cart(item, cart):
    if item in cart:
        if cart[item] == 1:
            del cart[item]
        else:
            cart[item] -= 1

def process_order(order, cart):
    flag = True
    command, item = order

    if (command == 'A'):
        add_cart(item, cart)
    if (command == 'D') and (item in cart):
        remove_cart(item, cart)
    if command == 'P':
        print(cart)
    if command == 'Q':
        flag = False

    return flag

def go_shopping():

    cart = dict();

    while True:
        order = get_order()
        if not process_order(order, cart):
            break
 
    print(cart)
    print('Finished')

go_shopping()
