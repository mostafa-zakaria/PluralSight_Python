import Sales

def go_shopping():
    cart = Sales.Cart()
    order = Sales.Order()
    while not cart.quit:
        order.get_order()
        cart.process_order(order)
        order = Sales.Order()

    print("Finished Shopping")


go_shopping()
