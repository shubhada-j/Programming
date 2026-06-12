//Program to print numbers from N down to 1 in reverse order

class Logic
{
    void PrintReverse(int iNum)
    {
        int iCnt = 0;

        for(iCnt = iNum; iCnt >= 1; iCnt --)
        {
            System.out.println(iCnt);
        }
    }
}

class ReverseOrder
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.PrintReverse(21);
    }    
}

