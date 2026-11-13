//Design Patterem starts - Builder 

class ParkingTicket
{
    private int ticketNumber;
    private String vehicleNumber;
    private int floorNumber;
    private int spotNumber;
    private String entryTime;
    
    /*public ParkingTicket(int a, String b, int c, int d, String e)
    {
        this.ticketNumber = a;
        this.vehicleNumber = b;
        this.floorNumber = c;
        this.spotNumber = d;
        this.entryTime = e;
    }*/

    private ParkingTicket(Builder builder)
    {
        this.ticketNumber = builder.ticketNumber;
        this.vehicleNumber = builder.vehicleNumber;
        this.floorNumber = builder.floorNumber;
        this.spotNumber = builder.spotNumber;
        this.entryTime = builder.entryTime;
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
public static class Builder
{
    private int ticketNumber;
    private String vehicleNumber;
    private int floorNumber;
    private int spotNumber;
    private String entryTime;
    
    //setter methods - it should be public
    public Builder setTicketNumber(int ticketNumber)
    {
        this.ticketNumber = ticketNumber;
        return this;
    }

    public Builder setVehicleNumber(String vehicleNumber)
    {
        this.vehicleNumber = vehicleNumber;
        return this;
    }

    public Builder setFloorNumber(int floorNumber)
    {
        this.floorNumber = floorNumber;
        return this;
    }

    public Builder setSpotNumber(int spotNumber)
    {
        this.spotNumber = spotNumber;
        return this;
    }

    public Builder setEntryTime(String entryTime)
    {
        this.entryTime = entryTime;
        return this;
    }

    public ParkingTicket build()
    {
        return new ParkingTicket(this);
    }
}

class program986
{
    public static void main(String A[])
    {
       
    }
}

/*
C:\Users\mdman\Desktop\LB\System_Design>java program986.java
program986.java:41: error: modifier static not allowed here
public static class Builder
              ^
program986.java:22: error: ticketNumber has private access in Builder
        this.ticketNumber = builder.ticketNumber;
                                   ^
program986.java:23: error: vehicleNumber has private access in Builder
        this.vehicleNumber = builder.vehicleNumber;
                                    ^
program986.java:24: error: floorNumber has private access in Builder
        this.floorNumber = builder.floorNumber;
                                  ^
program986.java:25: error: spotNumber has private access in Builder
        this.spotNumber = builder.spotNumber;
                                 ^
program986.java:26: error: entryTime has private access in Builder
        this.entryTime = builder.entryTime;
                                ^
program986.java:82: error: ParkingTicket(Builder) has private access in ParkingTicket
        return new ParkingTicket(this);
               ^
7 errors
error: compilation failed

*/