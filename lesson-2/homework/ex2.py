txt = 'LMaasleitbtui'
car_names= ["Tesla", "BMW", "Audi", "Toyota", "Mazda", "Lexus", "Subaru"]
found_cars= [car for car in car_names if all(txt.lower().count(c.lower()) >= car.lower().count(c.lower()) for c in car)
            
]
print(found_cars)