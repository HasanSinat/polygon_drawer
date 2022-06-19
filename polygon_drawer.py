import turtle

"""

A polygon drawer as an oop practice.

"""

class Polygon:
    def __init__(self, sides, name, size, color = "black", line_thickness = 1) :
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

    def draw(self):
        turtle.pencolor("black")
        #turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180-self.angle)
        turtle.end_fill()
       

class Square (Polygon):
    def __init__(self, size=100, color="black", line_thickness=1):
        super().__init__(4, "Square", size, color, line_thickness)

    
    def draw(self):   
        super().draw()

class Triangle(Polygon):
    def __init__(self, size, color="black", line_thickness=1):
        super().__init__(3, "Triangle", size, color, line_thickness)

    def draw(self):
        super().draw()
 

if __name__== "__main__":
    print("What do you want to draw? ")
    print("1-Triangle")
    print("2-Square")
    print("3-Custom Polygon")
    selection = int(input("Your Selection is: "))

    if selection == 3:
        sides = int(input("Input Side Count: "))
        name = input ("What do you want to call it: ")
        size = int(input("How big you want it to be: "))
        line_thickness = int(input("How thick you want it to be: "))
        color= input("And color is: ")
        customPolygon = Polygon(sides,name,size,color,line_thickness)

        customPolygon.draw()
        turtle.done()

    elif selection ==2 :
        name = input ("What do you want to call it: ")
        size = int(input("How big you want it to be: "))
        line_thickness = int(input("How thick you want it to be: "))
        color= input("And color is: ") 
        customSquare = Square(size,color,line_thickness)
        customSquare.draw()
        turtle.done()

    elif selection ==1 :
        name = input ("What do you want to call it: ")
        size = int(input("How big you want it to be: "))
        color= input("And color is: ")
        line_thickness = int(input("How thick you want it to be: ")) 
        customSquare = Triangle(size,color,line_thickness)
        customSquare.draw()
        turtle.done()





