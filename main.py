# first item
cart = []
cart1 = input("what do you want to add? ")
cart1 = cart.append(cart1)

if cart:
    for item in cart:
        print("adding " + item + " to your cart.")
else:
    exit()
# second item
second_cart = []
more = input("do you want to put more to you shopping list? (yes or no) ").lower()
if more == "yes":
    add = input("what would you add? ")
    add = second_cart.append(add)
    for item in second_cart:
        print("adding " + item + " to your cart.")
elif more == "no" or more == "nej":
    print("order is complete")
    exit()
# third item
third_cart = []
more1 = input("do you want to put more to you shopping list? (yes or no) ").lower()
if more1 == "yes":
    add_2 = input("what would you like to add? ")
    add_2 = third_cart.append(add_2)
    for item in third_cart:
        print("adding " + item + " to your cart.")
        print("because i have a lazy ass programmer, you cant add more stuff")
        print("order is complete")
elif more1 == "no":
    print("order is complete")
