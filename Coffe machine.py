# #coffee

# has_water = input('Write how many ml of water the coffee machine has:')
# has_milk = input('Write how many ml of milk the coffee machine has:')
# has_beans = input('Write how many grams of coffee beans the coffee machine has:')

# def has_cofee_cups(has_water, has_milk, has_beans):
#     water_to_cups = int(has_water) // 200
#     milk_to_cups = int(has_milk) // 50
#     coffee_beans_to_cups = int(has_beans) // 15
#     has_cofee_cup = min (water_to_cups, milk_to_cups, coffee_beans_to_cups)
#     return has_cofee_cup
# has_cofee_cup = has_cofee_cups(has_water, has_milk, has_beans)

# print('Write how many cups of coffee you will need:')
# need_coffe_cups = input()

# more_cups = has_cofee_cup - int(need_coffe_cups)

# if int(need_coffe_cups) < has_cofee_cup:
#     print(f'Yes, I can make that amount of coffee (and even {more_cups} more than that)')
# elif int(need_coffe_cups) == has_cofee_cup:
#     print('Yes, I can make that amount of coffee')
# else:
#     print(f"No, I can make only {has_cofee_cup} cups of coffee")

# print('For ' + str(need_coffe_cups) + ' cups of coffee you will need:')

# def calculate_cofee(need_coffe_cups):
#  water = int(need_coffe_cups)*200
#  milk = int(need_coffe_cups)*50
#  coffee_beans = int(need_coffe_cups)*15
#  return water, milk, coffee_beans
# water, milk, coffee_beans = calculate_cofee(need_coffe_cups)  # Returning Multiple Values in Python

# print(str(water) + ' ml of water')
# print(str(milk) + ' ml of milk')
# print(str(coffee_beans) + ' g of coffee beans')

# print('Starting to make a coffee')
# print('Grinding coffee beans')
# print('Boiling water')
# print('Mixing boiled water with crushed coffee beans')
# print('Pouring coffee into the cup')
# print('Pouring some milk into the cup')
# print('Coffee is ready!')

# new in stage 4/6 CoffeeMachine

default_water = 400
default_milk = 540
default_beans = 120
default_cups = 9
default_money = 550

state_before_actions = str(f"""The coffee machine has 
{default_water} of water
{default_milk} of milk
{default_beans} of coffee beans
{default_cups} of disposable cups
{default_money} of money""")
print(state_before_actions)

user_action = input('Write action (buy, fill, take):')

if user_action == 'buy':
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    coffee_type = input()
    def calc_cofee (coffee_type, default_water, default_milk, default_beans, default_cups, default_money):
        if coffee_type == '1':
            after_action_water = default_water - 250
            after_action_milk = default_milk
            after_action_beans = default_beans - 16
            after_action_cups = default_cups - 1
            after_action_money = default_money + 4
        elif coffee_type == '2':
            after_action_water = default_water - 350
            after_action_milk = default_milk - 75
            after_action_beans = default_beans - 20
            after_action_cups = default_cups - 1
            after_action_money = default_money + 7
        elif coffee_type == '3':
            after_action_water = default_water - 200
            after_action_milk = default_milk - 100
            after_action_beans = default_beans - 12
            after_action_cups = default_cups - 1
            after_action_money = default_money + 6
        return after_action_water, after_action_milk, after_action_beans, after_action_cups, after_action_money
    after_action_water, after_action_milk, after_action_beans, after_action_cups, after_action_money = calc_cofee (coffee_type, default_water, default_milk, default_beans, default_cups, default_money)
    state_after_action = str(f"""The coffee machine has:
    {after_action_water} of water
    {after_action_milk} of milk
    {after_action_beans} of coffee beans
    {after_action_cups} of disposable cups
    {after_action_money} of money""")    
    print(state_after_action)



if user_action == 'fill':
    water_add = input('Write how many ml of water do you want to add:')
    after_action_water = default_water + int(water_add)
    milk_add = input('Write how many ml of milk do you want to add:')
    after_action_milk = default_milk + int(milk_add)
    beans_add = input('Write how many grams of coffee beans do you want to add:')
    after_action_beans = default_beans + int(beans_add)
    cups_add = input('Write how many disposable cups of coffee do you want to add:')
    after_action_cups = default_cups + int(cups_add)
    after_action_money = default_money
    state_after_action = str(f"""The coffee machine has:
    {after_action_water} of water
    {after_action_milk} of milk
    {after_action_beans} of coffee beans
    {after_action_cups} of disposable cups
    {after_action_money} of money""")
    print(state_after_action)
	
if user_action == 'take':
    print(f'I gave you ${default_money}')
    after_action_water = default_water
    after_action_milk = default_milk
    after_action_money = 0
    after_action_beans = default_beans
    after_action_cups = default_cups
    state_after_action = str(f"""The coffee machine has:
    {after_action_water} of water
    {after_action_milk} of milk
    {after_action_beans} of coffee beans
    {after_action_cups} of disposable cups
    {after_action_money} of money""")
    print(state_after_action)

#Stage 5/6: On a coffee loop

water = 400
milk = 540
beans = 120
cups = 9
money = 550

espresso_water = 250
espresso_beans = 16
espresso_milk = 0
espresso_cups = 1
espresso_money = 4

latte_water = 350
latte_beans = 20
latte_milk = 75
latte_cups = 1
latte_money = 7

cappuccino_water = 200
cappuccino_beans = 12
cappuccino_milk = 100
cappuccino_cups = 1
cappuccino_money = 7

def remaining(water, milk, beans, cups, money):
    state_after_action = str(f"""The coffee machine has:
    {water} of water
    {milk} of milk
    {beans} of coffee beans
    {cups} of disposable cups
    {money} of money""")    
    print(state_after_action)

def fill(water, milk, beans, cups, money):
    water_add = int(input('Write how many ml of water do you want to add:'))
    water += water_add
    milk_add = int(input('Write how many ml of milk do you want to add:'))
    milk += milk_add
    beans_add = int(input('Write how many grams of coffee beans do you want to add:'))
    beans += beans_add
    cups_add = int(input('Write how many disposable cups of coffee do you want to add:'))
    cups += cups_add
    return water, milk, beans, cups, money
water, milk, beans, cups, money = fill(water, milk, beans, cups, money)

def take(money):
    print(f'I gave you ${money}')
    money = 0
    return money

def buy(water, milk, beans, cups, money, coffee_type, espresso_water, espresso_beans, espresso_cups, latte_water, latte_beans, latte_cups, cappuccino_water, cappuccino_beans, cappuccino_cups, latte_milk, cappuccino_milk):
    if coffee_type == '1' and water >= espresso_water and beans >= espresso_beans and cups >= 1:
        water -= espresso_water
        beans -= espresso_beans
        cups -= espresso_cups
        money += espresso_money
    elif coffee_type == '2' and water >= latte_water and beans >= latte_beans and cups >= 1:
        water -= latte_water
        beans -= latte_beans
        cups -= latte_cups
        money += latte_money
    elif coffee_type == '3' and water >= cappuccino_water and beans >= cappuccino_beans and cups >= 1:
        water -= cappuccino_water
        beans -= cappuccino_beans
        cups -= cappuccino_cups
        money += cappuccino_money
    elif coffee_type == 'back':
        user_action
    else:
        check_ingr(espresso_water, espresso_beans, espresso_cups, latte_water, latte_beans, latte_cups, cappuccino_water, cappuccino_beans, cappuccino_cups, latte_milk, cappuccino_milk)
    return water, milk, beans, cups, money
water, milk, beans, cups, money = calc_cofee(water, milk, beans, cups, money, coffee_type, espresso_water, espresso_beans, espresso_cups, latte_water, latte_beans, latte_cups, cappuccino_water, cappuccino_beans, cappuccino_cups, latte_milk, cappuccino_milk)

def check_ingr(espresso_water, espresso_beans, espresso_cups, latte_water, latte_beans, latte_cups, cappuccino_water, cappuccino_beans, cappuccino_cups, latte_milk, cappuccino_milk):
    if water < espresso_water or water < latte_water or water < cappuccino_water:
        print("Sorry, not enough water")
    elif milk < cappuccino_milk or milk < latte_milk:
        print("Sorry, not enough milk")
    elif beans < espresso_beans or beans < latte_beans or beans < cappuccino_beans:
        print("Sorry, not enough beans")
    elif cups < 1:
        print("Sorry, not enough cups")

while True:
    user_action = input('Write action (buy, fill, take, remaining, exit):')
    if user_action == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        coffee_type = input()
        buy(water, milk, beans, cups, money, coffee_type, espresso_water, espresso_beans, espresso_cups, latte_water, latte_beans, latte_cups, cappuccino_water, cappuccino_beans, cappuccino_cups, latte_milk, cappuccino_milk)
    if user_action == 'fill':
        fill(water, milk, beans, cups, money)
    if user_action == 'take':
        take(money)
    if user_action == 'remaining':
        remaining(water, milk, beans, cups, money)
    if user_action == 'exit':
        break