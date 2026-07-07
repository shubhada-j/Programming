def ChkPrime(No):
    if No <= 1:
        return False
    
    for i in range(2,No):
        if(No % i == 0):
            return False
    return True

def SumPrime(Data):
    Sum = 0

    for Value in Data:
        if ChkPrime(Value):
            Sum = Sum + Value
    return Sum