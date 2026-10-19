//Singly Circular Linkedlist in java
 
class node
{
    public int data;
    public node next;

    node(int no)
    {
        this.data = no;
        this.next = null;
    }
}

class SinglyCL
{
    private node first;
    private node last;
    private int iCount;

    public SinglyCL()
    {
        this.first = null;
        this.last = null;
        this.iCount = 0;
    }

    public void Display()
    {
        node temp = null;
        temp = first;

        if(first == null)
        {
            return;
        }
        
        do
        {
            System.out.print( "| "+temp.data+" | ->");
            temp = temp.next;
        }while(temp != first);

        System.out.println("\n");
    }
    public int Count()
    {
        return iCount;
    }

    public void InsertFirst(int iNo)
    {
        node newn = null;
        newn = new node(iNo);

        if(first == null && last == null)
        {
            first = newn;
            last = newn;
        }
        else
        {
            newn.next = first;
            first = newn;
        }
        
        last.next = first;
        iCount++;
    }

    public void InsertLast(int iNo)
    {
        node newn = null;
        newn = new node(iNo);

        if(first == null && last == null)
        {
            first = newn;
            last = newn;
        }
        else
        {
            last.next =  newn;
            last = newn;
        }
        
        last.next = first;
        iCount++;   
    }

    public void InsertAtPos(int iNo, int iPos)
    {
        int i = 0;
        node temp = null;
        temp = first;

        node newn = null;
        newn = new node(iNo);

        if(iPos < 1 || iPos > iCount + 1)
        {
            return;
        }

        if(iPos == 1)
        {
            InsertFirst(iNo);
        }
        else if(iPos == iCount + 1)
        {
            InsertLast(iNo);
        }
        else
        {
            for(i = 1; i<iPos-1;i++)
            {
                temp = temp.next;
            }

            newn.next = temp.next;
            temp.next = newn;
            iCount++;
        }
        
    }

    public void DeleteFirst()
    {
        if(first == null && last == null)
        {
            return;
        }
        else if(first == last)
        {
            first = null;
            last = null;
        }
        else
        {
            first = first.next;
            last.next = first;
        }

        iCount--;
    }

    public void DeleteLast()
    {
        node temp = null;
        temp = first;

        if(first == null && last == null)
        {
            return;
        }
        else if(first == last)
        {
            first = null;
            last = null;
        }
        else
        {
            while(temp.next.next != first)
            {
                temp = temp.next;
            }
            
            temp.next = first;
            last = temp;
        }

        iCount--;
    }

    public void DeleteAtPos(int iPos)
    {
        int i = 0;
        node temp = null;
        temp = first;

        if(iPos < 1 || iPos > iCount)
        {
            return;
        }

        if(iPos == iCount)
        {
            DeleteLast();
        }
        else if(iPos == 1)
        {
            DeleteFirst();
        }
        else
        {
            for(i = 1; i < iPos-1; i++)
            {
                temp = temp.next;
            }

            temp.next = temp.next.next;

            iCount--;
        } 
    }
    
}
class Singly_Circular
{
    public static void main(String A[])
    {
        int Ret = 0;

        SinglyCL sobj = new SinglyCL();

        sobj.InsertFirst(51);
        sobj.InsertFirst(21);
        sobj.InsertFirst(11);
        sobj.InsertLast(101);
        sobj.InsertLast(111);
       
        sobj.Display();
        Ret = sobj.Count();
        System.out.println("Number of nodes is : "+Ret);
        
        sobj.InsertAtPos(105, 4);

        sobj.Display();
        Ret = sobj.Count();
        System.out.println("Number of nodes is : "+Ret);

        sobj.DeleteFirst();
        sobj.Display();
        Ret = sobj.Count();
        System.out.println("Number of nodes is : "+Ret);

        sobj.DeleteLast();
        sobj.Display();
        Ret = sobj.Count();
        System.out.println("Number of nodes is : "+Ret);

        sobj.DeleteAtPos(4);
        sobj.Display();
        Ret = sobj.Count();
        System.out.println("Number of nodes is : "+Ret);

    }
}
