import math
def main():
    print("LET us find the solutiion to a quaddratic\n")
    a,b,c=eval(input("do rnter the coefficients (a,b,c)："))
    delta=b*b-4*a*c
    if a==0:
        x=2
        print("\nthere is an solution",x)
    elif delta<0:
        print("\nthere is no real roots")
    elif delta==0:
        x=-b/(2*a)
        print("\nthe same roots",x)
    else:
        d=math.sqrt(delta)
        x1=(-b+d)/(2*a)
        x2=(-b-d)/(2*a)
        print("\ntwo roots",x1,x2)
main()
