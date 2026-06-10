//Program to print all even numbers up to N

class Logic
{
    void PrintEvenNumbers(int iNum)
    {
        int iCnt = 0;

        for(iCnt = 1; iCnt < iNum; iCnt++)
        {
            if(iCnt % 2 == 0)
            {
                System.out.println(iCnt);
            }
        }
    }
}

class EvenNumbers 
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.PrintEvenNumbers(16);
    }    
}

