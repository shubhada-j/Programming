//Program to count how many even odd numbers are present between 1 to N

class Logic
{
    void CountEvenOddRange(int iNum)
    {
        int iCnt = 0;
        int iEvenCount = 0;
        int iOddCount = 0;

        for(iCnt = 1; iCnt <= iNum; iCnt++)
        {
            if(iCnt % 2 == 0)
            {
                iEvenCount++;
            }
            else
            {
                iOddCount++;
            }
        }

        System.out.println("Even numbers are : "+iEvenCount);
        System.out.println("Odd numbers are : "+iOddCount);
    }
}

class Count
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.CountEvenOddRange(50);
    }    
}

