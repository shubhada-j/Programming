//Design Patterem starts - factory (Same as 980)

enum VehicleType
{
   BIKE,
   CAR,
   TRUCK
}

//abstract class
abstract class Vehicle
{
    private String number;

    public Vehicle(String number)
    {
        this.number = number;
    }

    public String getNumber()
    {
        return this.number;
    }

    public abstract void display();
}

//concreet classes
class Bike extends Vehicle
{
    public Bike(String number)
    {
        super(number);
    }

    public void display()
    {
        System.out.println("Bike : "+getNumber());
    }
}

class Car extends Vehicle
{
    public Car(String number)
    {
        super(number);
    }

    public void display()
    {
        System.out.println("Car : "+getNumber());
    }
}

class Truck extends Vehicle
{
    public Truck(String number)
    {
        super(number);
    }

    public void display()
    {
        System.out.println("Truck : "+getNumber());
    }
}

class VehicleFactory
{
    public static Vehicle creatVehicle(VehicleType type, String number)
    {
        switch(type) 
        {
            case BIKE:
                return new Bike(number);

            case CAR:
                return new Car(number);

            case TRUCK:
                return new Truck(number);

            default:
                throw new IllegalArgumentException("Invalid Vehicle Type");
        }
    }
}

class program980
{
    public static void main(String A[])
    {
        Vehicle v1 = VehicleFactory.creatVehicle(VehicleType.BIKE, "MH12VL9080");
        Vehicle v2 = VehicleFactory.creatVehicle(VehicleType.CAR, "MH12WZ9080");
        Vehicle v3 = VehicleFactory.creatVehicle(VehicleType.TRUCK, "MH12ML9080");
        
        v1.display();
        v2.display();
        v3.display();
    }
}

/*
C:\Users\mdman\Desktop\LB\System_Design>java program980.java
Bike : MH12VL9080
Car : MH12WZ9080
Truck : MH12ML9080
*/