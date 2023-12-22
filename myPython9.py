"""
A lot of the code here is error prone. The codes here are the codes I wrote for the reeborg.co website, you can enter there and write the code to play the game!
"""

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

#for number in range(a, b):
#    print(number)

#while something_is_true

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



def jump1():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()

fruits = ["Apelsin", "Banana", "Peach"]
for step in range(6):
    jump1()
while 5 > 3:
    jump1()
  

def turn_left3():
    print("Left")
def turn_right3():
    print("Right")
def move3():
    print("Move")


def turn_right3():
    turn_left3()
    turn_left3()
    turn_left3()
def jump():
    turn_left3()
    move3()
    turn_right3()
    move3()
    turn_right3()
    move3()
    turn_left3()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

i = 1
j = 1
while i <= 5:
    print("Hello!")
    i=i+1
while j <= 6:
    print(f"{j}. Hi!")
    j=j+1









