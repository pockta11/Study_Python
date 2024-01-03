a=[23,12,36,63,19]

#인덱스 값 출력
for i in enumerate(a):
    print(i)
print("-------------------")

for x in enumerate(a):
    print(x[0], x[1])
print("-------------------")

for index, value in enumerate(a):
    print(index, value)
print("-------------------")

##a=[23,12,36,63,19]
## and
if all(60>x for x in a):
    print("YES")
else :
    print("NO")
print("--------------")
## 하나라도 만족하면 OR
if any(60>x for x in a):
    print("YES")
else :
    print("NO")

