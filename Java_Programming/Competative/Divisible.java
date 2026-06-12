//Program to print all numbers from 1 to N that are divisible by both 2 and 3

class Logic
{
    void PrintDivisibleBy2and3(int iNum)
    {
        int iCnt = 0;

        for(iCnt = 1; iCnt <= iNum; iCnt++)
        {
            if((iCnt % 2 == 0) && (iCnt % 3 == 0))
            {
                System.out.println(iCnt);
            }
        }
    }
}

class Divisible
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.PrintDivisibleBy2and3(30);
    }    
}

