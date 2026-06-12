//Program to display the grade of a student based on marks

class Logic
{
    void DisplayGrade(int iMarks)
    {
        if(iMarks >= 80)
        {
            System.out.println("Grade of Student is A");
        }
        else if(iMarks >= 60)
        {
            System.out.println("Grade of Student is B");
        }
        else
        {
            System.out.println("Grade of Student is C");
        }
    }
}

class StudentGrade
{
    public static void main(String A[])
    {
        Logic obj = new Logic();
        obj.DisplayGrade(72);
    }    
}

