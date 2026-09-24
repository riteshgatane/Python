def Area(Radius,Pi = 3.14):
    Ans = Pi * Radius * Radius
    return Ans

def main():
    Ret = Area(10.45)
    print("Area of Circle is :",Ret)

    Ret = Area(3.123 ,17.23)
    print("Area of Circle is :",Ret)
 
if __name__ == "__main__":
    main()