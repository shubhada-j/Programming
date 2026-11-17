//anonimus object creation

class Demo
{
    public int i,j;

    public Demo setI(int no)
    {
        this.i = no;
        return this;
    }

    public Demo setJ(int no)
    {
        this.j = no;
        return this;
    }

    public void display()
    {
        System.out.println("i : "+i);
        System.out.println("j : "+j);

    }
}

class program993
{
    public static void main(String A[])
    {
        new Demo()                          //anonimus object
        .setI(11)
        .setJ(21)
        .display();
    }
}

/*

C:\Users\mdman\Desktop\LB\System_Design>java program993.java
i : 11
j : 21
*/