//Accept the number from user and check wheather it is divisible by 3 and 5
//Type 2

import java.util.Scanner;

class program41
{
    //we can call this method from main class so we have to declare this method as static beacause from static non static not called 
    static void CheckDivisible(int iNo)
    {
        if((iNo % 3 == 0)&&(iNo % 5 == 0))
        {
            System.out.println("Number is divisible by 3 & 5");
        }
        else
        {
            System.out.println("Number is not divisible by 3 & 5");
        }
    }
    public static void main(String A[]) 
    {
        Scanner sobj = new Scanner(System.in);
      
        int iValue = 0;

        System.out.println("Enter number : ");
        iValue = sobj.nextInt();

        CheckDivisible(iValue); 
    }
    
}
