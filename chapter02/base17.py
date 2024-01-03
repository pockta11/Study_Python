#numpy : C언어로 구현되어 있으므로 빠른속도와 고성능의 수치 계산을 지원함
import numpy as np 

# 수치 계산용 배열 사용 np.array 
arr=np.array([1,2,3])
print(arr)
print(type(arr)) 

matrix=np.array([[1,2,3],[4,5,6]])
print(matrix)
print("------------------------")
A=np.array([[1,2],[3,4]])
B=np.array([[1,1],[1,1]])

C=A+B
print(C)
print("------------------------")
A=np.array([[1,2],[3,4],[5,6]])
B=np.array([[2,3],[2,3]])

C=np.matmul(A,B)
print(C)

print("------------------------")
A=np.array([[1,2],[3,4]])
k=10
C=k*A
print(C)