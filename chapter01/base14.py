## 변수
select, answer, numStr, num1, num2=0,0,"",0,0

## 메인
select=int(input("1. 수식 계산기 2. 두수 사이의 합계 : "))

if select ==1 :
    numStr=input("수식을 입력하세요 : ") # 49%6
    answer=eval(numStr)
    print("%s 결과는 %5.1f 입니다" % (numStr, answer))
elif select==2:
    num1=int(input("1. 시작될 숫자를 입력하세요 : ")) # 2
    num2=int(input("1. 마지막 숫자를 입력하세요 : ")) # 8
    for i in range(num1, num2+1):
        answer=answer+i

    print("%d + ... + %d는 %d 입니다" % (num1,num2,answer))

else:
    print("1 또는 2만 입력이 가능합니다.")