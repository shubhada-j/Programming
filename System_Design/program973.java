//Design Patteren - Singleton

class ParkingLot
{
    private static ParkingLot instance;         //self referncing structure

    private ParkingLot()
    {
        System.out.println("ParkingLot Object gets created");
    }

    //            return value  method name
    public static ParkingLot getInstance()
    {
        if(instance == null)
        {
            instance = new ParkingLot();
        }
        return instance;
    }
}

class program973
{
    public static void main(String A[])
    {
       //ParkingLot pobj1 = new ParkingLot();

       ParkingLot pobj1 = ParkingLot.getInstance();
       ParkingLot pobj2 = ParkingLot.getInstance();
       ParkingLot pobj3 = ParkingLot.getInstance();
    }
}

/*
C:\Users\mdman\Desktop\LB\System_Design>java program973.java
ParkingLot Object gets created
*/