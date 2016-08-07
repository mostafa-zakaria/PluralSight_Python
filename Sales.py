class Cart:
    def __init__(self):
        self._contents = dict()
        self.quit = False

    def __repr__(self):
        return "{0} {1}".format(Cart, self.__dict__)

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

    def process_order(self, order):
        if(order.add):
            self.add_item(order.item)
        elif (order.delete) and (self.contains(order.item)):
            self.remove_item(order.item)
        elif (order.printC):
            print(self)
        elif(order.quit):
            self.quit = True
        
class Order:
    def __init__(self):
        self.quit = False
        self.add = False
        self.delete = False
        self.printC = False
        self.item = None

    def get_order(self):
        print("[command] [item] (Command is A to Add, D to Delete, Q to Quit, P to Print)")
        line = input()

        command = line[:1]
        self.item = line[2:]

        if(command == 'A'):
            self.add = True
        elif (command == 'D'):
            self.delete = True
        elif (command == 'Q'):
            self.quit = True
        else:
            self.printC = True
