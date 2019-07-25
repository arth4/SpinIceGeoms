import turtle
import random
import numpy as np
import itertools

SYSTEM_RULES = {}  # generator system rules for l-system
EAST,NORTH,WEST,SOUTH = 0,90,180,270
RN =0
def deg2rad(angle):
    return angle*np.pi /180
def rad2deg(angle):
    return angle*180/np.pi
def sinDegrees(angle):
    return np.sin(deg2rad(angle))

def derivation(axiom, steps):
    derived = [axiom]  # seed
    for _ in range(steps):
        next_seq = derived[-1]
        next_axiom = [rule(char) for char in next_seq]
        derived.append(''.join(next_axiom))
        print(_)
    return derived


def rule(sequence):
    if sequence in SYSTEM_RULES:
        return SYSTEM_RULES[sequence]
    return sequence
def uncoupledDrawForward(turtle,magH,magW,distance,mangle=0):
    turtle.pu()
    saveHead = turtle.heading()
    halfDist = 0.5*distance
    turtle.forward(halfDist)
    turtle.setheading(mangle)
    
    draw_rect(turtle,magH,magW)
    turtle.pu()
    turtle.setheading(saveHead)
    turtle.forward(distance-halfDist)#combat rounding errors
    
    
    
def drawMagAndForward(turtle,magH,magW,distance,mangle=0):
    global RN
    gap = distance- magH
#    angle = random.random()*360
#    turtle.left(angle)
    
    #adjust position/heading
    x = 0.5*(180-mangle)
    dist = distance/2 *sinDegrees(mangle)/sinDegrees(x)
    turtle.pu()
    #print(1);input("")
    turtle.left(x);
    #print(2);input("")
    turtle.forward(dist);
   # print(3);input("")
    turtle.right(x)
    #print(4);input("")
    
    
    #drawMagnet
    turtle.pu();turtle.forward(gap);turtle.pd()
    turtle.right(90);turtle.forward(0.5*magW)
    turtle.left(90);turtle.forward(magH)
    turtle.left(90);turtle.forward(magW)
    turtle.left(90);turtle.forward(magH)
    turtle.left(90);turtle.forward(0.5*magW)
    turtle.left(90);turtle.pu();turtle.forward(magH+gap)
   
    #re-adjust position/heading1
    turtle.left(x); turtle.forward(dist);turtle.right(x)   

    input("")

    RN+=1;print(mangle)#RN)

#    turtle.right(angle)

def draw_rect(turtle,h,w):
    global RN
    """
    draws rectangle with turtle's current pos as centrepoint;
    height (h) is in direction of the turtle's heading;
    preserves heading and pos            
    """
#    angle = random.random()*360
#    turtle.left(angle)
    
    turtle.pu();turtle.forward(0.5*h);turtle.pd()
    turtle.left(90);turtle.forward(0.5*w)
    turtle.left(90);turtle.forward(h)
    turtle.left(90);turtle.forward(w)
    turtle.left(90);turtle.forward(h)
    turtle.left(90);turtle.forward(0.5*w)
    turtle.left(90);turtle.pu();turtle.forward(0.5*h)
    turtle.left(180)   
    RN+=1;print(RN)

#    turtle.right(angle)
def draw_l_system(turtle, SYSTEM_RULES, seg_length, angle,magH=20,magW=10,magAngleDelta=[90],magInit=0,skipMag=None):
    stack = []
    magAngle=magInit
    skipMag = itertools.cycle(skipMag)
    magAngleDelta = itertools.cycle(magAngleDelta)
    for command in SYSTEM_RULES:
        #angle = random.random()*360
        turtle.pd()
        if command in ["G", "R", "L"]: #"F"
            draw_rect(turtle,magH,magW)
            turtle.pu()
            turtle.forward(seg_length)
            
        elif command in ["u","d","l","r"]:
            turtle.pu()
            saveHeading = turtle.heading()
            tempHeading = NORTH if command == "u" else(
                            EAST if command == "r"else(
                                SOUTH if command =="d"else WEST))
            turtle.setheading(tempHeading)
            turtle.forward(seg_length)
            turtle.setheading(saveHeading)    
        elif command in ["M","m"]:
            draw_rect(turtle,magH,magW)
            
        elif command == "F" or command=="X":
            if(next(skipMag)):
                turtle.pu()
                turtle.forward(seg_length)
            else:
                uncoupledDrawForward(turtle,magH,magW,seg_length,magAngle)
#            draw_rect(turtle,magH,magW)
#            turtle.pu()  # pen up - not drawing
#                turtle.forward(seg_length)
        
        elif command == "f":
            turtle.pu()  # pen up - not drawing
            turtle.forward(seg_length)
            #turtle.payRespects()
            
        elif command == "+":
            turtle.right(angle)
            magAngle= (magAngle- next(magAngleDelta))%360 
        elif command == "-":
            turtle.left(angle)
            magAngle= (magAngle+ next(magAngleDelta))%360 
            
        elif command == "[":
            stack.append((turtle.position(), turtle.heading()))
        elif command == "]":
            turtle.pu()  # pen up - not drawing
            position, heading = stack.pop()
            turtle.goto(position)
            turtle.setheading(heading)
        else: assert command=="I"
    


def set_turtle(alpha_zero):
    r_turtle = turtle.Turtle()  # recursive turtle
    r_turtle.screen.title("L-System Derivation")
    r_turtle.speed(0)  # adjust as needed (0 = fastest)
    r_turtle.setheading(alpha_zero)  # initial heading
    return r_turtle


def main():
    rule_num = 1
    while True:
        rule = input("Enter rule[%d]:rewrite term (0 when done): " % rule_num)
        if rule == '0':
            break
        key, value = rule.split("->")
        SYSTEM_RULES[key] = value
        rule_num += 1

    axiom = input("Enter axiom (w): ")
    iterations = int(input("Enter number of iterations (n): "))

    model = derivation(axiom, iterations)  # axiom (initial string), nth iterations

    segment_length = int(input("Enter step size (segment length): "))
    alpha_zero = float(input("Enter initial heading (alpha-0): "))
    angle = float(input("Enter angle increment (i): "))

    # Set turtle parameters and draw L-System
    r_turtle = set_turtle(alpha_zero)  # create turtle object
    turtle_screen = turtle.Screen()  # create graphics window
    turtle_screen.screensize(1500, 1500)
    draw_l_system(r_turtle, model[-1], segment_length, angle)  # draw model
    turtle_screen.exitonclick()


if __name__ == "__main__":
    pass
    #main()
