def product_rating(user, products):
    best_rating = 0
    best_product = None
    for product in products:
        rating = sum ((user[x] * product[x]) for x in range(0, len(product)))
        if rating > best_rating:
            best_rating = rating
            best_product = products.index(product)
    return best_product


users = { 1: [1.73, 0.01, 5.22],
          2: [0.03, 4.41, 2.05],
          3: [1.13, 0.89, 3.76]
        }

products = { 1: [3.29, 3.44, 3.67],
             2: [0.82, 9.71, 3.88],
             3: [8.34, 1.72, 0.02]
           }


print(products.items())


rev = {v:k for k,v in products.items()}
print(rev)

#user_key = 1
#print("The Best Product for User> {} is Product> {}".format(user_key, product_rating(users[user_key], products)))
