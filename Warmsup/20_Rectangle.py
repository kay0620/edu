#Rectangle 클래스의 인스턴스 생성
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width + self.height) * 2
        

#Rectangle 클래스의 인스턴스 생성
rect1 = Rectangle(5,3)

print(rect1.get_area()) #넓이 반환
print(rect1.get_perimeter()) #둘레 반환

rect2 = Rectangle(3,7)

print(rect2.get_area()) #넓이 반환
print(rect2.get_perimeter()) #둘레 반환
