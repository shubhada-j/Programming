//Program to find the maximum of two numbers

class Logic
{
    void FindMax(int a,int b)
    {
        if(a > b)
        {
            System.out.println("a is maximum than b");
        }
        else
        {
            System.out.println("b is maximum than a");
        }
    }
}
class MaximumNumber 
{
    public static void main(String args[])
    {
        Logic obj = new Logic();
        obj.FindMax(20,15);
    }
}
