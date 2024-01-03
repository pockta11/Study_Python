class Car:
    color="" #인스턴스 변수
    speed=0 #인스턴스 변수
    count=0  #클래스 변수 = (자바 : static)

    def printMessage():
        print("테스트 출력")

    #생성자
    def __init__(self):
        self.speed=0
        Car.count += 1

#변수 선언
myCar1, myCar2=None, None

#메인
myCar1=Car()
myCar1.speed=30
print("자동차1의 속도는 %d Km이고, 생상된 자동차의 수는 %d대 입니다. " % (myCar1.speed, Car.count))

myCar2=Car()
myCar2.speed=60
print("자동차2의 속도는 %d Km이고, 생상된 자동차의 수는 %d대 입니다. " % (myCar2.speed, Car.count))

myCar3=Car()
myCar3.speed=50
print("자동차3의 속도는 %d Km이고, 생상된 자동차의 수는 %d대 입니다. " % (myCar3.speed, Car.count))
