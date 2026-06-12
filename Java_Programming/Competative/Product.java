class Logic
{
    void ProductOfDigit(int iNum)
    {
        int iDigit = 0;
        int iProduct = 1;

        while(iNum != 0)
        {
            iDigit = iNum % 10;
            iProduct = iProduct * iDigit;
            iNum = iNum/10;
        }

        System.out.println("Product of Digits is : "+iProduct);
    }
}

class Product
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.ProductOfDigit(234);
    }    
}

