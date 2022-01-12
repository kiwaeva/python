lstnums=[1,2,5,10,15,18,21,27,36]
lstresult= list(filter(lambda num: num>17,lstnums))
print("nums that are greater than 17", lstresult)

lstnums2=[1,2,8,12,15,18,24,27,32]
lstresult2= list(filter(lambda num: num<16,lstnums2))
print("nums that are less than 16", lstresult2)

lstnums3=[1,2,8,12,15,18,24,27,32]
lstresult3= list(filter(lambda num: num==15,lstnums3))
print("filter num ", lstresult3)

lstnums4=[1,2,8,12,15,18,24,27,32]
lstresult4= list(filter(lambda num: num!=27,lstnums4))
print("filter num ", lstresult4)

lstnums4=[1,2,8,12,15,18,24,27,32]
lstresult4= list(filter(lambda num: num%2!=0,lstnums4))
print("filter num ", lstresult4)


# from functools import reduce
table=[1,2,3,4,5,6,7,8,9]
multiplynum1 = list(map(lambda num1,num2: num1*num2+1,table))

print(multiplynum1)