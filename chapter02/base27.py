#일반 메서드

def plus_one(x):
    return x+1

print(plus_one(1))
print()

#=========================================
#람다식 
plus_two=lambda x:x+2
print(plus_two(1))
print()
#==========================================
#일반메서드 + 람다식

def plus_list(x):
    return x+1

a=[1,2,3]

print(list(map(plus_list, a)))
print()
#lambda 
print(list(map(lambda x:x+1,a)))




