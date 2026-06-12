class Logic
{
    void CheckPerfect(int iNum)
    {
        int itemp = iNum;
        int iCnt = 0;
        int iSum = 0;
        int iNo = 0;

        for(iCnt = 1;iCnt < iNum; iCnt++)
        {
            iNo = iNum % iCnt;
            if(iNo == 0)
            {
                iSum = iSum + iCnt;
            }
        }

        if(iSum == itemp)
        {
            System.out.println("Number is perfect number");
        }
        else
        {
            System.out.println("Number is not perfect number");
        }
    }
}

class PerfectNumber
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.CheckPerfect(6);
    }    
}

