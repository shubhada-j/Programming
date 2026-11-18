/*
    ParkingLot Automation System

    Step 1 : Create required enums
    Step 2 : Vehicle Hierarchy creation
    Step 3 : VehicleFactory creation(Factory Pattern)
    Step 4 : Parking Hierarchy
    Step 5 : ParkingObserver Class
    Step 6 : ParkingFloor Class
    Step 7 : ParkingDisplayBoard (Observer Patteren)
    Step 8 : ParkingStrategy Class (Strategy Patteren)
    Step 9 : PricingStrategy Class (Strategy Patteren)
    Step 10 : PaymentStrategy Class
    Step 11 : ParkingTicket Class
    Step 12 : EntryGate Class
    Step 13 : ExitGate Class
    Step 14 : ParkingLot Class (Singleton Patteren)
    Step 15 : Main Class(Controller)

*/

import java.util.*;
import java.time.Duration;
import java.time.LocalDateTime;

////////////////////////////////////////////////////////////
// Step 1 : Create Enums
// It is used to create fixed constants which are required 
// throughout the project
////////////////////////////////////////////////////////////

//Represents the different types of vehicle supported by the project
enum VehicleType
{
    BIKE,
    CAR,
    TRUCK
}

//Represents different types of parking spots
enum SpotType
{
    BIKE,
    CAR,
    TRUCK
}

//Represents current state of parking ticket
enum TicketStatus
{
    ACTIVE,
    CLOSED
}

class program996 
{
    public static void main(String A[])
    {

    }
}
