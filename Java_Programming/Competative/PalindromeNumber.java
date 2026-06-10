//Program to check wheather a number is a palindrome or not

class Logic
{
    void CheckPalindrome(int iNum)
    {
        int iTemp = iNum;
        int iDigit = 0;
        int iNo = 0;

        while(iNum != 0)
        {
            iDigit = iNum % 10;
            iNo = iNo * 10 + iDigit;
            iNum = iNum/10;
        }

        if(iTemp == iNo)
        {
            System.out.println("Number is Palindrome");
        }
        else
        {
            System.out.println("Number is not Palindrome");
        }
        
    }
}

class PalindromeNumber 
{
    public static void main(String args[])
    {
        Logic obj = new Logic();
        obj.CheckPalindrome(121);
    }    
}
