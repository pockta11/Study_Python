class Car :
    speed=0
    def upSpeed(self, value):
        self.speed += value

        print("현재 속도(슈퍼클래스) : %d" % self.speed)

# 오버라이딩 구현부가 있음
class Sedan(Car): #부모 클래스인 Car를 상속받음 
    def upSpeed(self, value):
        self.speed += value

        if self.speed > 240 :
            self.speed=240

        print("현재 속도(서브 클래스) : %d" % self.speed)

# 오버라이딩 구현부가 없음
class Truck(Car):
    pass #pass는 자바에서는 인터페이스 

#변수
sedan1, truck1 =None, None


#메인
truck1=Truck()
sedan1=Sedan()


print("트럭 ---> ", end="")
truck1.upSpeed(300)

print("승용차  ---> ", end="")
sedan1.upSpeed(300)
