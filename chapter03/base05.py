#클래스 정의 부분
class Car:
    color=""
    speed=0
    # 생성자 
    def __init__(self, value1, value2):
        self.color=value1
        self.speed=value2

#메인
myCar1=Car("빨강", 30)
myCar2=Car("파랑", 60)

print("자동차1의 색상은 %s이며, 현재속도는 %d Km입니다" % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s이며, 현재속도는 %d Km입니다" % (myCar2.color, myCar2.speed))
