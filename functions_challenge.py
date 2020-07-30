def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("What maff you finna do?")
print("+")
print("-")
print("*")
print("/")

choice = input("Enter choice hurr:")
x = int(input("What's da first numba?"))
y = int(input("What's da second numba?"))
if choice == '+':
    print(x,"+",y,"=", add(x,y))
elif choice == '-':
    print(x,"-",y,"=", subtract(x,y))
elif choice == '*':
    print(x,"*",y,"=", multiply(x,y))
elif choice == '/':
    print(x,"/",y,"=", divide(x,y))

