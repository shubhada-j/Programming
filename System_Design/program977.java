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

class program977
{
    public static void main(String A[])
    {
        Car cobj = new Car("MH12VL9080");
        cobj.display();

        Truck tobj = new Truck("MH12WZ9080");
        tobj.display();
    }
}

/*
C:\Users\mdman\Desktop\LB\System_Design>java program977.java
Car : MH12VL9080
Truck : MH12WZ9080
*/