# 0730 Daily Workshop

## 1번. 도형 만들기

```python
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Rectangle(Point):
    def __init__(self,p1,p2):
        self.p1=(p1.x,p1.y)
        self.p2=(p2.x,p2.y)
        self.width=abs(self.p1[0]-self.p2[0])
        self.height=abs(self.p1[1]-self.p2[1])
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return self.width*2 + self.height*2
    def is_square(self):
        if (self.width!=0)&(self.width==self.height):
            return True
        else:
            return False
            

p1=Point(1,3)
p2=Point(3,1)

r1=Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3=Point(3,7)
p4=Point(6,4)
r2=Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())


#4
#8
#True
#9
#12
#True
```

