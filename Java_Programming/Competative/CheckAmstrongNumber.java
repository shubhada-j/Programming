import java.util.*;

class CheckAmstrongNumber
{
    public static void main(String A[])
    {
        int num = 0, temp = 0,iDigit = 0,iCount = 0, value = 0;

        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter number : ");
        num = sobj.nextInt();

        temp = num;

        while(num != 0)
        {
            iDigit = num % 10;
            iCount++;
            num = num/10;
        }

        value = temp;

        int iNum = 0, iSum = 0;

        while(temp != 0)
        {
            iNum = temp % 10;

            iSum = iSum + (int)(Math.pow(iNum, iCount));
            
            temp = temp / 10;
        }

        if(iSum == value)
        {
            System.out.println("Number is Amstrong number");
        }
        else
        {
            System.out.println("Number is not Amstrong number");

        }
    }
}