import java.util.Scanner;

class CheckPalindromeNumber
{
    public static void main(String A[])
    {
        int num = 0, value = 0, result = 0, temp = 0;

        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter the number : ");
        num = sobj.nextInt();

        temp = num;

        while(num != 0)
        {
            value = num % 10;

            result = (result * 10) + value;

            num = num / 10;
        }
        
        if(temp == result)
        {
            System.out.println("Number is palindeome");
        }
        else
        {
            System.out.println("Number is not palindeome");
        }

    }
}