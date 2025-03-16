txt = 'MsaatmiazD'
car_names =["Matiz", "Toyota", "Mazda", "Lexus", "Buick", "Subaru"]
found_cars= [car for car in car_names if all(txt.lower().count(c.lower()) >= car.lower().count(c.lower()) for c in car) ]
print(found_cars)