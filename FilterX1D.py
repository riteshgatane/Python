def CheckEven(No):
    return (No % 2 == 0 )

def Map(No):
    return (No >= 10)

def Reduce(No):
    sum = 0 
    for i in No:
        sum = sum + No

    return sum 


def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)
    FData = list(filter(CheckEven,Data))
    print("Data After Reduce:",FData)

    MData = list(filter(Map,FData))
    print("Data After Reduce:",MData)

    RData = (filter(Reduce,MData))
    print("Data After Filter :",RData)



if __name__ == "__main__":
    main()