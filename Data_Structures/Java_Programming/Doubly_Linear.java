//Doubly Linear Linkedlist

class node
{
    public int data;
    public node next;
    public node prev;

    node(int no)
    {
        this.data = no;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLL
{
    private node first;
    private int iCount;

    public DoublyLL()
    {
        this.first = null;
        this.iCount = 0;
    }

    public void Display()
    {
        node temp = null;
        temp = first;

        System.out.print("\nNULL");

        while(temp != null)
        {
            System.out.print("| "+temp.data+" | <=> ");
            temp = temp.next;
        }

        System.out.print("NULL\n");

    }

    public int Count()
    {
        return iCount;
    }

    public void InsertFirst(int iNo)
    {
        node newn = null;
        newn = new node(iNo);

        if(first == null)
        {
            first = newn;
        }
        else
        {
            newn.next = first;
            first.prev = newn;
            first = newn;   
        }
        iCount++;
    }

    public void InsertLast(int iNo)
    {
        node newn = null;
        newn = new node(iNo);

        if(first == null)
        {
            first = newn;
        }
        else
        {
            node temp = null;
            temp = first;

            while(temp.next != null)
            {
                temp = temp.next;
            }

            temp.next = newn;
            newn.prev = temp;
    
        }
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
            for(i = 1; i < iPos-1; i++)
            {
                temp = temp.next;
            }   

            newn.next = temp.next;
            temp.next.prev = newn;
            temp.next = newn;
            newn.prev = temp;

            iCount++;
        }
    }

    public void DeleteFirst()
    {
        if(first == null)
        {
            return;
        }
        else if(first.next == null)
        {
            first = null;
        }
        else 
        {
            first = first.next;
            first.prev = null;
        }
        iCount--;
    }

    public void DeleteLast()
    {
        if(first == null)
        {
            return;
        }
        else if(first.next == null)
        {
            first = null;
        }
        else 
        {
            node temp = null;
            temp = first;

            while(temp.next.next != null)
            {
                temp = temp.next;
            }

            temp.next = null;
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

        if(iPos == 1)
        {
            DeleteFirst();
        }
        else if(iPos == iCount)
        {
            DeleteLast();
        }
        else
        {
            for(i = 1; i < iPos-1; i++)
            {
                temp = temp.next;
            }   

            temp.next = temp.next.next;
            temp.next.prev =  temp;
           

            iCount--;
        }
    }
}
class Doubly_Linear
{
    public static void main(String A[])
    { 
        int Ret = 0;

        DoublyLL dobj = new DoublyLL();

        dobj.InsertFirst(51);
        dobj.InsertFirst(21);
        dobj.InsertFirst(11);

        dobj.Display();
        Ret = dobj.Count();
        System.out.println("Number of nodes are : "+Ret);

        dobj.InsertLast(101);
        dobj.InsertLast(111);
        dobj.Display();
        Ret = dobj.Count();
        System.out.println("Number of nodes are : "+Ret);

        dobj.DeleteFirst();
        dobj.Display();
        Ret = dobj.Count();
        System.out.println("Number of nodes are : "+Ret);

        dobj.DeleteLast();
        dobj.Display();
        Ret = dobj.Count();
        System.out.println("Number of nodes are : "+Ret);

        dobj.InsertAtPos(105, 4);
        dobj.Display();
        Ret = dobj.Count();
        System.out.println("Number of nodes are : "+Ret);

        dobj.DeleteAtPos(3);
        dobj.Display();
        Ret = dobj.Count();
        System.out.println("Number of nodes are : "+Ret);
    }
}
