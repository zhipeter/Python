from turtle import *
def main():
    setup(800,600,0,0)
    setpen(5,"red",3,"turtle")
    result=readFile("data.txt")
    dynamicDraw(result)
if __name__=='__main__':
    main()
