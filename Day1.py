a=int(input())
k=int(input())
b=a
for i in range(1,k):
    if str(b)==str(b)[::-1]:
        print(i,a)
        break

    b=a+int(str(a)[::-1])
    a=b


    
