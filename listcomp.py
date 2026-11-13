# List comprehension

list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
comp_list = [num for num in list]
print(comp_list)

# doubling the numbers and assigning in the comp_list1 variable

comp_list1 = [num*2 for num in list]
print(comp_list1)

# square the numbers using exponential oprerator

comp_list2 = [num**2 for num in list]
print(comp_list2)


# List comprehension with range()

list2 = [x for x in range(1,51)]
even_num = [x*2 for x in list2 if x%2 == 0]
print(even_num)

# printing even number

even_num1 = [x for x in list2 if x%2 != 0]
print(even_num1) 

# accessing lettrs using list coprehension

string = ["google", "infosys", "microsoft"]
access_string = [x[2] for x in string]
print(access_string)

# slicing (start:stop:step)

slice_string = [x[:3:2] for x in string]
print(slice_string)

# uppercasing city names

cities = ["gadag", "haveri", "dharwad", "koppal"]
uppercase_city = [city.upper() for city in cities if city == "gadag"]
print(uppercase_city) 
uppercase_city = [city.upper() for city in cities]
print(uppercase_city)

# lowercasing food names

food_names = ["DOsA", "iDLI", "RICe", "cHAptI"]
lowercase_food = [food.lower() for food in food_names]
print(lowercase_food) 


