//Program to check whether a number is divisible by 5 and 11 or not

class Logic
{
    void CheckDivisible(int iNum)
    {
        if((iNum % 5 == 0)&&(iNum % 11 == 0))
        {
            System.out.println("Number is divisible by 5 and 11");
        }
        else
        {
            System.out.println("Number is not divisible by 5 and 11");   
        }
    }
}

class DivisibleByFiveEleven
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.CheckDivisible(55);
    }    
}

