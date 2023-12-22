#Functoins
def my_hello():
    print("Hello :)")
def my_bye():
    print("Bye :(")
def my_meet():
    my_hello()
    my_bye()
print(my_meet())
print("-----------------------------------------")
#Reeborg's World === reeborg.ca

def turn_left():
    print("Left")
def turn_right():
    print("Right")
def move():
    print("Move")

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
for step in range(6):
    jump()

def my_function():
    sky = input("Bugun osmon qanday holatda? ")
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("grey")
    print("HELLO")
print("WORLD")
print(my_function())

#While Loops!
'''
for number in range(a, b):
    print(number)

while something_is_true
'''
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)









