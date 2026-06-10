//Program check whether a number is positive, negative or zero

class Logic
{
    void CheckSign(int iNum)
    {
        if(iNum > 0)
        {
            System.out.println("Number is Positive");
        }
        else if( iNum < 0)
        {
            System.out.println("Number is Negative");
        }
        else
        {
            System.out.println("Number is Zero");
        }

    }
}

class CheckNumber 
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.CheckSign(-8);
    }    
}

