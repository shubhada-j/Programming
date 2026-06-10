//Program to check wheather a number is prime or not 

class Logic
{
    void CheckPrime(int iNum)
    {
        int iCnt = 0;

        for(iCnt = 2; iCnt < iNum; iCnt++)
        {
            if(iNum % iCnt == 0)
            {
                System.out.println("Number is not Prime");
                return;
            }
        }
            
        System.out.println("Number is Prime");         
    }       
}

class CheckPrimeNumber 
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.CheckPrime(11);
    }    
}

