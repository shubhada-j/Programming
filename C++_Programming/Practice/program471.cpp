//Generic Programming topic start
//but code specific programming

#include<iostream>
using namespace std;

double Addition(double No1, double No2)
{
    double Ans;
    Ans = No1 + No2;
    return Ans;

}

int main()                          //main generic naste kadhich    //main function return value always 1
{
    double Value1 = 10.5, Value2 = 11.2, Ret = 0.0;

    Ret = Addition(Value1,Value2);
    cout<<"Addition is : "<<Ret<<"\n";
    
    return 0;
}

//Addition is : 21.7