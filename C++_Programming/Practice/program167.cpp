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
        ArrayX(int X = 5)           
        {
            iSize = X;                  
            Arr = new int[iSize];       
        }

        ~ArrayX()              
        {
            delete []Arr;             
        }
};

int main()
{
    ArrayX *aobj1 = new ArrayX();       //parametrized constructors call
    ArrayX *aobj2 = new ArrayX(15);      // parametrized constructors call

    //Function call

    delete aobj1;
    delete aobj2;

    return 0;
}