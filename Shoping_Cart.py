class Cart:
    def __init__(self):
        self._contents = dict()

    def add_item(self, item):
        if not item in self._contents:
            self._contents[item] = 0
        self._contents[item] += 1

    def remove_item(self, item):
        if item in self._contents:
            if self._contents[item] == 1:
                del self._contents[item]
            else:
                self._contents[item] -= 1

    def contains(self, item):
        flag = False
        if (item in self._contents):
            flag = True
        return flag

    def print_cart(self):
        print(self._contents)
        
        
def get_order():
    print("[command] [item] (Command is A to Add, D to Delete, Q to Quit, P to Print)")
    line = input()

    command = line[:1]
    item = line[2:]
    return (command, item)
      
def process_order(order, cart):
    flag = True
    command, item = order

    if (command == 'A'):
        cart.add_item(item)
    if (command == 'D') and (cart.contains(item)):
        cart.remove_item(item)
    if command == 'P':
        cart.print_cart()
    if command == 'Q':
        flag = False

    return flag

def go_shopping():
    cart = Cart()
    while True:
        if not process_order(get_order(), cart):
            break
    print("Finished Shopping")


go_shopping()
