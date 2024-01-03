sel=int(input("입력진수 결정(16/10/8/2) : ")) ##16
num=input('값 입력 : ') ##CA72

if sel==16 :
    num10=int(num,16)
if sel==10 :
    num10=int(num,10)
if sel==8 :
    num10=int(num,8)
if sel==2 :
    num10=int(num,2)


print("16진수 ==> ", hex(num10)) #hex() : 10진수를 16진수로 변환하는 메소드
print("10진수 ==> ", num10)
print("8진수 ==> ", oct(num10)) #oct() : 10진수를 8진수로 변환하는 메소드
print("2진수 ==> ", bin(num10)) #bin() : 10진수를 2진수로 변환하는 메소드

# BIN (Binary) : 2진수 · OCT (Octal) : 8진수 · DEC (Decimal) : 10진수 · HEX (Hexadecimal) : 16진수.