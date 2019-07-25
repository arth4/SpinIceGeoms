import lsystem
import turtle
import itertools
def main(edges,gridDelta,magnetDelta,gridInit,magInit,skipMag=itertools.cycle([0])):
    
    #3 = hex, 4 = square
   
    #main rule
#    lsystem.SYSTEM_RULES["X"] = "X+X-X-X-X+X+X+X-X"
    lsystem.SYSTEM_RULES["F"] = "F+F" + "-F"*(edges-1) + "+F"*(edges-1) +"-F"
#    lsystem.SYSTEM_RULES["F"] = "F+F-F-F+F+F-F"

    #lsystem.SYSTEM_RULES["U"] = "UHV-X-X+X+X+X-X"
    
    
    axiom = "F"
#    axiom = "X"
    iterations=4
    model= lsystem.derivation(axiom,iterations)
    
    pitch, magH, magW = 35, 15 ,8
#    pitch, magH, magW = 100, 40 , 20
#    pitch, magH, magW = 20, 12 ,6
    turtle.clearscreen()
    
    squirtle = lsystem.set_turtle(gridInit)#lsystem.NORTH)  # create turtle object
    turtle_screen = turtle.Screen()  # create graphics window
    turtle_screen.screensize(10000, 10000)
    
    
    turtle.delay(0)
    
#    squirtle.ht()
#    turtle.tracer(0, 0)
    lsystem.draw_l_system(squirtle, model[-1], pitch, gridDelta,magH,magW,magnetDelta,magInit,skipMag)  # draw model
    
    
    return model, turtle_screen


skipMag = [1,1,0]
edges = 3
#magDelta = [60]#[-60,-60,-60,-120,-120,-60,-60,-60]
magDelta = [360/edges]#[137.5077640500378546463487]
#skipMag = [1]*(edges-1) + [0]#[1,1,0,1,1,0,1,1,0]#[0,0,0,0,1,0,0,0,0]

gridDelta = 360/edges

#gridDelta = 120
magDelta=[60]
initMag = 30
initGrid =0
model,ts = main(edges,gridDelta,magDelta,initGrid,initMag,skipMag)
#ts.getcanvas().postscript(file=f'geom_{edges},{gridDelta},{magDelta},{initGrid},{initMag},{skipMag}).ps')

        
print(f"geom_{edges},{gridDelta},{magDelta},{initGrid},{initMag},{skipMag}")
ts.exitonclick()
exit()