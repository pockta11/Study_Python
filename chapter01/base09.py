#변수
year=0

#메인
year=int(input("연도를 입력하세요 : "))

if(((year % 4 ==0)and(year % 100 !=0)) or (year %400==0) ):
    print("%d 년은 윤년의 해 입니다." % year)
else :
    print("%d 년은 윤년이 아닙니다." % year)
