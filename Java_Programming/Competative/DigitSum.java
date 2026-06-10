//Program to find the sum of digits of a number

class Logic
{
    void SumOfDigits(int iNum)
    {
        int iDigit = 0;
        int iSum = 0;

        while(iNum != 0)
        {
            iDigit = iNum % 10;
            iSum = iSum + iDigit;
            iNum = iNum/10;
        }

        System.out.println("Summation of Digits is : "+iSum);
    }
}

class DigitSum
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.SumOfDigits(1234);
        
    }
}