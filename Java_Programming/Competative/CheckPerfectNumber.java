import java.util.*;

class CheckPerfectNumber
{
    public static void main(String A[])
    {
        int num = 0, i = 0, ans = 0,sum = 0;;

        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter number : ");
        num = sobj.nextInt();

        for(i = 1; i < num ; i++)
        {
            if(num % i == 0)
            {
                sum = sum + i;
            }
        }

        if(sum == num)
        {
            System.out.println("Number is perfect");
        }
        else
        {
            System.out.println("Number is not perfect");

        }
    }
}