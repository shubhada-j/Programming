//System Design start

class Demo
{
    public int i,j;

    public Demo()
    {
        System.out.println("Object Created");

        this.i = 0;
        this.j = 0;
    }

}

class program970
{
    public static void main(String A[])
    {
        Demo obj1 = new Demo();     //object
        Demo obj2 = new Demo();     //object
    }
}

/*
C:\Users\mdman\Desktop\LB\System_Design>java program970.java
Object Created
Object Created
*/