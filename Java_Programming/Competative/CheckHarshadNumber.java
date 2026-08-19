import java.util.Scanner;

class CheckHarshadNumber 
{
    public static void main(String a[])
    {
        int num = 0, temp = 0, iDigit = 0, iSum = 0, result = 0;

        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter the number : ");
        num = sobj.nextInt();

        temp = num;

        while(num != 0)
        {
            iDigit = num % 10;

            iSum = iSum + iDigit;

            num = num / 10;
        }

        result = temp % iSum;

        if(result == 0)
        {
            System.out.println("Number is Harshad number");
        }
        else
        {
            System.out.println("Number is not Harshad number");

        }
    }    
}
