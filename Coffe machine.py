#cofee

has_water = input('Write how many ml of water the coffee machine has:')
has_milk = input('Write how many ml of milk the coffee machine has:')
has_beans = input('Write how many grams of coffee beans the coffee machine has:')

def has_cofee_cups(has_water, has_milk, has_beans):
    water_to_cups = int(has_water) // 200
    milk_to_cups = int(has_milk) // 50
    coffee_beans_to_cups = int(has_beans) // 15
    has_cofee_cup = min (water_to_cups, milk_to_cups, coffee_beans_to_cups)
    return has_cofee_cup
has_cofee_cup = has_cofee_cups(has_water, has_milk, has_beans)

print('Write how many cups of coffee you will need:')
need_coffe_cups = input()


if int(need_coffe_cups) < has_cofee_cup:
    print('Yes, I can make that amount of coffee')
elif int(need_coffe_cups) == has_cofee_cup:
    print('Yes, I can make that amount of coffee')
else:
    print(f"No, I can make only {has_cofee_cup} cups of coffee")



print('For ' + str(need_coffe_cups) + ' cups of coffee you will need:')

def calculate_cofee(need_coffe_cups):
 water = int(need_coffe_cups)*200
 milk = int(need_coffe_cups)*50
 coffee_beans = int(need_coffe_cups)*15
 return water, milk, coffee_beans

water, milk, coffee_beans = calculate_cofee(need_coffe_cups)  # Returning Multiple Values in Python

print(str(water) + ' ml of water')
print(str(milk) + ' ml of milk')
print(str(coffee_beans) + ' g of coffee beans')

print('Starting to make a coffee')
print('Grinding coffee beans')
print('Boiling water')
print('Mixing boiled water with crushed coffee beans')
print('Pouring coffee into the cup')
print('Pouring some milk into the cup')
print('Coffee is ready!')


