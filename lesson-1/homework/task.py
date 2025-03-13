def pr1():
    side = 5
    perimeter = 4 * side
    area = side * side
    print("perimeter:", perimeter, ", area:", area)
def pr2(diameter):
    print(3.14 * diameter)
def pr3(a,b):
    mean = (a+b)/2
    print(mean) 
def pr4(a, b):
    sum_ = a + b
    product = a * b
    square_a = a ** 2
    square_b = b ** 2

    print("Sum:", sum_)
    print("Product:", product)
    print(f"Square of {a}:", square_a)
    print(f"Square of {b}:", square_b)
pr1()
pr2(4)
pr3(6,7)
pr4(6,7)