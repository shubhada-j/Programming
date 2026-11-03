class Demo
{
    public int i,j;

    private Demo()
    {
        System.out.println("Object Created");

        this.i = 0;
        this.j = 0;
    }

}

class program971
{
    public static void main(String A[])
    {
        Demo obj1 = new Demo(); //ERROR
        Demo obj2 = new Demo(); //ERROR
    }
}

/*
C:\Users\mdman\Desktop\LB\System_Design>java program971.java
program971.java:21: error: Demo() has private access in Demo
        Demo obj1 = new Demo();
                    ^
program971.java:22: error: Demo() has private access in Demo
        Demo obj2 = new Demo();
                    ^
2 errors
error: compilation failed
*/