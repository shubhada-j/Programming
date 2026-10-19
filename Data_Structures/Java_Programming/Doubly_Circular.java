//Doubly Circular Linkedlist

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

class DoublyCL
{
    private node first;
    private node last;
    private int iCount;

    DoublyCL()
    {
        this.iCount = 0;
        this.first = null;
        this.last = null;
    }

    public void Display()
    {   
        node temp = null;
        temp = first;

        if(temp == null && last == null)
        {
            return;
        }
        do
        {
            System.out.print("| "+temp.data+" | <=>");
            temp = temp.next;
        }while(temp != last.next);

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
            first.prev = newn;
            first = newn;
        }

        last.next = first;
        first.prev = last;

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
            last.next = newn;
            newn.prev = last;
            last = newn;
        }

        last.next = first;
        first.prev = last;

        iCount++;
    }

    public void InsertAtPos(int iNo,int iPos)
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
            first.prev = last;
        }
        iCount--;
    }

    public void DeleteLast()
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
            last = last.prev;
            last.next = first;
            first.prev = last;
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
           
            iCount++;
        }
    }
}

class Doubly_Circular
{
    public static void main(String A[])
    {
        int Ret = 0;

        DoublyCL dobj = new DoublyCL();

        dobj.InsertFirst(51);
        dobj.InsertFirst(21);
        dobj.InsertFirst(11);

        dobj.InsertLast(101);
        dobj.InsertLast(111);

        dobj.Display();

        Ret = dobj.Count();
        System.out.println("Number of nodes : "+Ret);

        dobj.DeleteFirst();

        dobj.Display();

        Ret = dobj.Count();
        System.out.println("Number of nodes : "+Ret);

        dobj.DeleteLast();

        dobj.Display();

        Ret = dobj.Count();
        System.out.println("Number of nodes : "+Ret);

        dobj.InsertAtPos(105,4);

        dobj.Display();

        Ret = dobj.Count();
        System.out.println("Number of nodes : "+Ret);

        dobj.DeleteAtPos(4);

        dobj.Display();

        Ret = dobj.Count();
        System.out.println("Number of nodes : "+Ret);
    }
}
