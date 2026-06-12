//Program to find the smallest digit in a given number

class Logic
{
    void FindSmallestDigit(int iNum)
    {
        int iSmallest = 9;
        int iDigit = 0;

        while(iNum != 0)
        {
            iDigit = iNum % 10;

            if(iDigit < iSmallest)
            {
                iSmallest = iDigit;
            }

            iNum = iNum/10;
        }

        System.out.println("Smallest Digit is : "+iSmallest);
    }
}

class SmallestDigit
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.FindSmallestDigit(45872);
    }    
}

