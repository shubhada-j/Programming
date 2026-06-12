//Program to calculate the power of a number using loops

class Logic
{
    void CalculatePower(int iBase, int iExp)
    {
        int iCnt = 1;
        int iResult = 1;

        for(iCnt = 1; iCnt <= iExp; iCnt++)
        {
            iResult = iResult * iBase;
        }

        System.out.println("Power of number is : "+iResult);
    }   
}

class PowerOfNumber
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.CalculatePower(2,5);
    }    
}

