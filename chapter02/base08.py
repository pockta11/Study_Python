# 변수
foods={"쭈꾸미":"삼겹살",
       "떡볶이":"김말이",
       "곱창":"소주",
       "감자탕":"석박지",
       "치킨":"맥주",
       "회":"쏘맥",
       "피자":"콜라",
       "라면":"김치"}

#메인
# str:String / chr:chracter /ord : ASCII코드
while(True):
    myfood=input(str(list(foods.keys())) + "중 오늘의 메뉴는 : ")
    if myfood in foods:
        print("<%s>에 맞는 궁합 음식은 <%s>입니다." % (myfood, foods.get(myfood)))
    elif myfood == "끝":
        break
    else :
        print("메뉴에 없는 음식입니다. 다시 주문하세요~")