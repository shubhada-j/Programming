//Design Patterem starts - Builder 

class ParkingTicket
{
    private int ticketNumber;
    private String vehicleNumber;
    private int floorNumber;
    private int spotNumber;
    private String entryTime;
    
    public ParkingTicket(int a, String b, int c, int d, String e)
    {
        this.ticketNumber = a;
        this.vehicleNumber = b;
        this.floorNumber = c;
        this.spotNumber = d;
        this.entryTime = e;
    }

    public void display()
    {
        System.out.println("Ticket Number : "+this.ticketNumber);
        System.out.println("Vehicle Number : "+this.vehicleNumber);
        System.out.println("Floor Number : "+this.floorNumber);
        System.out.println("Spot Number : "+this.spotNumber);
        System.out.println("Entry Time : "+this.entryTime);

    }
}

class program985
{
    public static void main(String A[])
    {
        ParkingTicket p1 = new ParkingTicket(11,"MH12VL7172",3,89,"9:30 AM");
        ParkingTicket p2 = new ParkingTicket(12,"MH14VL7020",4,32,"9:50 AM");

        p1.display();

        p2.display();
    }
}
/*
C:\Users\mdman\Desktop\LB\System_Design>java program985.java
Ticket Number : 11
Vehicle Number : MH12VL7172
Floor Number : 3
Spot Number : 89
Entry Time : 9:30 AM
Ticket Number : 12
Vehicle Number : MH14VL7020
Floor Number : 4
Spot Number : 32
Entry Time : 9:50 AM

*/