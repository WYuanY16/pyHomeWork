class Shape: 
    def __init__(self,l,w=-1):
        self.length = l
        self.width = w
        self.area = self.calcArea()
        print(self.__class__.__name__+" length：%d"%(self.length)+"  width：%d"%(self.width)+" \n   面积是：%d"%(self.area))
        return self.area;
    def calcArea(self):
        if(self.width==-1):
            return self.length*self.length;
        else:
            return self.width*self.length;


PI = 3.14;

class Ellipse(Shape):
    def __init__(self,l,w):
        super(Ellipse, self).__init__(l,w)
      
    def calcArea(self):
        return PI*self.width*self.length;

class Circle(Shape):
    def __init__(self,l):
        super(Circle, self).__init__(l)

    def calcArea(self):
        return PI*self.length*self.length;
    
class Square(Shape):
    def __init__(self,l):
        super(Square, self).__init__(l)
    
class Rectangle(Shape):
    def __init__(self,l,w):
        super(Rectangle,self).__init__(l,w)
       

def compute_area(shapes):
    total=0
    for shape in shapes:
        total += shape.area
    return total;   
        
shapes = [Ellipse(10, 20), Square(15),Circle(5),Rectangle(20,15),
          Circle(5), Square(15), Ellipse(10,20)]


total_area = compute_area(shapes)
print("面积和为：%d"%(total_area))
