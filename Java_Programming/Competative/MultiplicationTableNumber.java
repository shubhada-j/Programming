//Program to print the multiplication table of a number

class Logic
{
    void PrintTable(int iNum)
    {
        int iCnt = 0;
        int iTable = 0;

        for(iCnt = 1; iCnt <= 10; iCnt++)
        {
            iTable = iNum * iCnt;
            System.out.println(iTable);
        }
    }
}

class MultiplicationTableNumber 
{
    public static void main(String args[])
    {
        Logic obj = new Logic();
        obj.PrintTable(5);
    }  
}
