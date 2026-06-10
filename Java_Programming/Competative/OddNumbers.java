//Program to print all odd numbers up to N


class Logic
{
    void PrintOddNumbers(int iNum)
    {
        int iCnt = 0;

        for(iCnt = 1; iCnt < iNum; iCnt++)
        {
            if(iCnt % 2 != 0)
            {
                System.out.println(iCnt);
            }
        }
    }
}

class OddNumbers 
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.PrintOddNumbers(20);
    }    
}

