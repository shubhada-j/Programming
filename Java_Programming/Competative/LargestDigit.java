//Program to find the largest digit in a given number

class Logic
{
    void FindLargestDigit(int iNum)
    {
        int iLargest = 0;
        int iDigit = 0;

        while(iNum != 0)
        {
            iDigit = iNum % 10;

            if(iDigit > iLargest)
            {
                iLargest = iDigit;
            }

            iNum = iNum/10;
        }

        System.out.println("Largest Digit is : "+iLargest);

    }
}

class LargestDigit
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.FindLargestDigit(83429);
    }    
}

