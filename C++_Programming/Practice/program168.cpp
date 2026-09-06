#include<iostream>
using namespace std;

#pragma pack(1)
class ArrayX
{
    private:
        int *Arr;
        int iSize;

    public:
        //Parametrised constructor with default argument(value) -> work like parametrised and deafault
        ArrayX(int X =5)           
        {
            iSize = X;                  
            Arr = new int[iSize];       
        }

        ~ArrayX()              
        {
            delete []Arr;             
        }

        void Accept()
        {
            int iCnt = 0;

            cout<<"Enter the elements : "<<endl;

            for(iCnt = 0; iCnt < iSize; iCnt++)
            {
                cin>>Arr[iCnt];
            }
        }

        void Display()
        {
            int iCnt = 0;

            cout<<"Elements of the array are : "<<endl;

            for(iCnt = 0; iCnt < iSize; iCnt++)
            {
                cout<<Arr[iCnt]<<endl;
            }
        }
};

int main()
{
    ArrayX *aobj = NULL;     

    int iLength = 0;

    cout<<"Enter the no of elements : \n";
    cin>>iLength;

    aobj = new ArrayX(iLength);

    aobj->Accept();
    aobj->Display();

    delete aobj;

    return 0;
}