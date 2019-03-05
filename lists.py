cars = ['BMW', 'Audi', 'Honda']

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1, "Jeep")
print(cars)
x = cars.index("Benz")
print(x)

y = cars.pop()
print(y)

cars.remove("Jeep")
print(cars)

print("*#"*20)
print(cars)

cars.sort()
print(cars)