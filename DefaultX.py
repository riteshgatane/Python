def Area(Pi = 3.14 ,Radius):  #error
    Ans = Pi * Radius * Radius
    return Ans


def main():
    Ret = Area(10.45)
    print("Area of Circle is :",Ret)

    Ret = Area(3.123 ,17.23)
    print("Area of Circle is :",Ret)
 
if __name__ == "__main__":
    main()