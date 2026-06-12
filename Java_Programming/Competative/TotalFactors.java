class Logic
{
    void Countfactors(int iNum)
    {
        int iCnt = 0;
        int iNo = 0;
        int iCount = 0;

        for(iCnt = 1;iCnt < iNum; iCnt++)
        {
            iNo = iNum % iCnt;

            if(iNo == 0)
            {
                iCount++;
            }
        }

        System.out.println("Total numbers of Factor is : " + iCount);
    }
}

class TotalFactors
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.Countfactors(20);
    }    
}

