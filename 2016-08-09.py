def getprim(n):
    p=2
    x=0
    while(x<n):
        result=True
        for i in range(2,p-1):
            if(p%i==0):
                result=False
        if result==True:
            print(p)
            x=x+1
        p+=1

getprim(100)
