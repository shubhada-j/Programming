import java.util.*;

class CheckStrongNumber 
{
    public static void main(String A[])
    {
        int num = 0, iDigit = 0,temp = 0;
        int i = 0, iFact = 0, iSum = 0;

        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter the number : ");
        num = sobj.nextInt();

        temp = num;

        while(num != 0)
        {
            iDigit = num % 10;

            iFact = 1;

            for(i = 1; i <= iDigit; i++)
            {
                iFact = iFact * i; 
            }

            iSum = iSum + iFact;

            num = num / 10;

        }

        if(iSum == temp)
        {
            System.out.println("Number is a Strong number");
        }
        else
        {
            System.out.println("Number is not a Strong number");
            
        }
    }
}
