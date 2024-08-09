# IF/ELSE STATEMENTS

def drink(money):
    if money >= 2:
        return "You've got a drink"
    else:
        return "No drink for you"

print(drink(1))
print(drink(3))

def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "You got a drink"
    elif (age >= 21) and (money < 5):
        return "Come back with more money"
    else:
        return "No drink for you"

print(alcohol(21, 6))
print(alcohol(21, 3))
print(alcohol(20, 9))