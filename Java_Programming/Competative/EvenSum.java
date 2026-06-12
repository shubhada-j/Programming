//Program to find the sum of all even numbers

class Logic
{
    void SumEvenNumbers(int iNum)
    {
        int iCnt = 0;
        int iSum = 0;

        for(iCnt = 0; iCnt <iNum; iCnt++)
        {
            if(iCnt % 2 == 0)
            {
                iSum = iSum +iCnt;
            }
        }

        System.out.println("Summation is : "+iSum);
    }
}

class EvenSum
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.SumEvenNumbers(10);
    }    
}

