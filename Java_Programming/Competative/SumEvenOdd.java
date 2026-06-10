//Program to find the sum of even and odd digits seperately in a number

class Logic
{
    void SumEvenOddDigits(int iNum)
    {
        int iEvenSum = 0;
        int iOddSum = 0;
        int iDigit = 0;

        while(iNum != 0)
        {
            iDigit = iNum % 10;
            
            if(iDigit % 2 == 0)
            {
                iEvenSum = iEvenSum + iDigit;
            }
            else
            {
                iOddSum = iOddSum + iDigit;
            }

            iNum = iNum/10;
        }
        
        System.out.println(iEvenSum);
        System.out.println(iOddSum);
    }
}

class SumEvenOdd
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.SumEvenOddDigits(123456);
    }    
}

