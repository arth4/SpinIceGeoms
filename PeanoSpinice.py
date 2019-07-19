import lsystem
import turtle

def main(gridDelta,magnetDelta,gridInit,magInit):
    

    #main rule
    lsystem.SYSTEM_RULES["X"] = "X+X-X-X-X+X+X+X-X"
    
    #lsystem.SYSTEM_RULES["U"] = "UHV-X-X+X+X+X-X"
    
    
    
    axiom = "X"
    iterations=2
    model= lsystem.derivation(axiom,iterations)
    
    pitch, magH, magW = 30, 20 , 10
    pitch, magH, magW = 80, 40 , 20
#    pitch, magH, magW = 6, 4 , 2
    turtle.clearscreen()
    
    squirtle = lsystem.set_turtle(gridInit)#lsystem.NORTH)  # create turtle object
    turtle_screen = turtle.Screen()  # create graphics window
    turtle_screen.screensize(2000, 2000)
    
    
    turtle.delay(1)
    
#    squirtle.ht()
#    turtle.tracer(0, 0)
    
    lsystem.draw_l_system(squirtle, model[-1], pitch, gridDelta,magH,magW,magnetDelta,magInit)  # draw model
    
    turtle.done()
    return model, turtle_screen

model,ts = main(90,58,45,23)
print("done")
ts.exitonclick()
exit()