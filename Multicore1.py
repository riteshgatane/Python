import os

def SumCube(No):
    Sum = 0 

    for i in range(1, No+1):
        Sum = Sum + (i*i*i)
    
    return Sum
    
    


def main():
    ret = SumCube(5)
    print(f"Cube is {ret} ")

if __name__ == "__main__":
    main()