#cofee

print('Write how many cups of coffee you will need:')
need_coffe = input()

#check input type?

print('For ' + str(need_coffe) + ' cups of coffee you will need:')

def calculate_cofee(need_coffe):
 water = int(need_coffe)*200
 milk = int(need_coffe)*50
 coffee_beans = int(need_coffe)*15
 return water, milk, coffee_beans

water, milk, coffee_beans = calculate_cofee(need_coffe)  # Returning Multiple Values in Python

print(str(water) + ' ml of water')
print(str(milk) + ' ml of milk')
print(str(coffee_beans) + ' g of coffee beans')


