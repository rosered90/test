# _*_ coding:_*_
# 大数求和
import time
num1="1234567890123"
num2="11"

#长度强行扭转到一致 不够前面补0
max_len= len(num1) if len(num1)>len(num2) else len(num2)
num1=num1.zfill(max_len)
num2=num2.zfill(max_len)

a1=list(num1)
a2=list(num2)
a3=[0]*(max_len+1)

for index in range(max_len-1,-1,-1):
    index_sum=a3[index+1]+int(a1[index])+int(a2[index])
    less=index_sum-10
    a3[index+1]=index_sum%10
    a3[index]=1 if less>=0 else 0
if(a3[0]==0):
    a3.pop(0)
a33=[str(i) for i in a3]
print(''.join(a33))
print('耗时{0}ms'.format(time.time()-startTime))