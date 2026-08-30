#include<iostream>
using namespace std;

class ArrayX
{
    // Access specifier of summation is Private -> due to this it is not accessible to main function
    int Summation(int Arr[],int iSize)
    {
        int iCnt = 0;
        int iSum = 0;

        for(iCnt = 0; iCnt < iSize; iCnt++)
        {
            iSum = iSum + Arr[iCnt];
        }

        return iSum;
    }
};

int main()
{
    int *Brr = NULL;
    int iLength = 0;
    int iCnt = 0;
    int iRet = 0;
    ArrayX aobj;            //objext creation static without new keyword(new use in java for object creation)

    cout<<"Enter the number of elements : \n";
    cin>>iLength;

    //C    : Brr = (int *)malloc(sizeof(int) * iLength);
    //Java : Brr = new int[iLength];

    Brr = new int[iLength];

    cout<<"Enter the elements : \n";
    for(iCnt = 0; iCnt < iLength; iCnt++)
    {
        cin>>Brr[iCnt];
    }

    cout<<"Elements of the array are :\n";
    for(iCnt = 0; iCnt < iLength; iCnt++)
    {
        cout<<Brr[iCnt]<<endl;
    }

    iRet = aobj.Summation(Brr,iLength);
    cout<<"Summation is : "<<iRet<<endl;

    delete []Brr;

    return 0;

    return 0;
}