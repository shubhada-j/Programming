//Program to check whether a given year is leap year or not

class Logic
{
    void CheckLeapYear(int iYear)
    {
        if(iYear % 4 == 0)
        {
            System.out.println("Year is Leap Year");
        }
        else
        {
            System.out.println("Year is not Leap Year");
        }
    }
}

class CheckLeap
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.CheckLeapYear(2023);
    }    
}

