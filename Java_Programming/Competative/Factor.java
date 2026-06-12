//Program to display all factors of a given number


class Logic
{
    void DisplayFactors(int iNum)
    {
        int iCnt = 0;
        int iNo = 0;

        for(iCnt = 1;iCnt < iNum; iCnt++)
        {
            iNo = iNum % iCnt;

            if(iNo == 0)
            {
                System.out.println(iCnt);
            }
        }
    }
}

class Factor 
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.DisplayFactors(10);
    }    
}

