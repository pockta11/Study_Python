## 변수 선언 부분
inStr, outStr="", ""
ch = ""
count, i = 0,0

# 메인코드
inStr=input("문자열을 입력하세요 : ") #Soldesk 2024
count=len(inStr) # 11

for i in range(0, count):
    ch=inStr[i] #SolDesk 2024
    if(ord(ch) >= 65 and ord(ch) <= ord("Z")):  #대문자면
        newCh=ch.lower()
    elif(ord(ch) >= ord("a") and ord(ch) <= ord("z")):  #소문자면
        newCh=ch.upper()
    else :
        newCh=ch

    outStr += newCh

print("대소문자 변환 : %s" % outStr)