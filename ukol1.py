car = ['Skoda','Mercedes','Lada','Reno','Hyundai','Tesla']
print(len(car))
for i in range(len(car)):
    print(car[i])
car.append(input("Enter next car "))
car.remove('Skoda')
car.sort()
car.reverse()
print(car)