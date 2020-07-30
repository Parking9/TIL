# 0730 Daily Homework

## 1번. Circle 인스턴스 만들기

```python
# =============================================================================
# class Circle:
#     pi=3.14
#     x=0
#     y=0
#     r=0
#     
#     def __init__(self, r, x,y):
#         self.r=r
#         self.x=x
#         self.y=y
#         
#     def area(self):
#         return self.pi * self.r * self.r
#     
#     def circumference(self):
#         return 2*self.pi*self.r
#     def center(self):
#         return (self.x,self.y)
# =============================================================================

# 넓이
Circle(3,2,4).area() # 28.259999999999998
# 둘레
Circle(3,2,4).circumference() # 28.259999999999998
```



## 2번.  Dog과 Bird는 Animal이다

```python
# =============================================================================
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def walk(self):
#         print(f'{self.name}! 걷는다!')
#     def eat(self):
#         print(f'{self.name}! 먹는다!')
# =============================================================================


class Dog(Animal):
    def bark(self):
        print(f'{self.name}! 짖는다!')
        
class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')        

dog=Dog('멍멍이')
dog.walk() # 멍멍이! 걷는다!
dog.bark() # 멍멍이! 짖는다!

bird=Bird('구구')
bird.walk() # 구구! 걷는다!
bird.eat() # 구구! 먹는다!
bird.fly() # 구구! 푸드덕!
```



## 3번. 오류의 종류

- `ZeroDivisionError` -  어떤 수를 0으로 나눴을 때 발생하는 오류
- `NameError` - 변수가 지정이 안되어 있을 경우에 발생하는 오류
- `TypeError` - 특정 연산을 수행할 때, 데이터 유형이 잘못 되었을 경우
- `IndexError` - 불러오는 index가 지정된 범위를 벗어났을 경우
- `KeyError` - Key가 존재 하지 않을 경우
- `ModuleNotFoundError` - import한 모듈을 찾을 수 없을 경우
- `ImportError` - 불러올 모듈을 찾을 수 없을 경우

