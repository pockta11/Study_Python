#변수
inFp, outFp = None, None
inStr, outStr="",""
i=0
secu = 0

#메인
secuYN = input("1.암호화 2.암호해석 중 선택 : ")
inFname = input("파일명을 입력하세요 :  ") # test.txt
outFname=input("출력 파일명을 입력하세요 : ") # scu.txt 

inFp=open(inFname, 'r', encoding='utf-8') 
outFp=open(outFname, 'w', encoding='utf-8') 

if secuYN == "1":
    secu=100
elif secuYN == "2":
    secu=-100

while True:
    inStr=inFp.readline()
    if not inStr:
        break

    outStr=""
    for i in range(0,len(inStr)):
        ch=inStr[i] #한글자씩 읽어옴
        chNum=ord(ch) #ACSII
        chNum=chNum + secu # 문자 -> 숫자(암호화된 숫자)

        ch2=chr(chNum) #암호화한 코드를 다시 문자로 변경 => 암호 완성
        outStr=outStr+ch2

    outFp.write(outStr) # 저장

outFp.close()
inFp.close()

print('%s ------> %s 변환완료' % (inFname, outFname))