//Display Even Number - Display nodes containing even values

#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node * next;
};

typedef struct node NODE;
typedef struct node * PNODE;
typedef struct node ** PPNODE;

void Display(PNODE first)
{
    while(first != NULL)
    {
        if(first->data % 2 == 0)
        {
            printf("| %d | -> ",first->data);
        }
        
        first = first->next;
    }
    
    printf("NULL\n");
}

void InsertFirst(PPNODE first,int iNo)
{
    PNODE newn = NULL;

    newn = (PNODE)malloc(sizeof(NODE));

    newn->data = iNo;
    newn->next = NULL;

    if(*first == NULL)
    {
        *first = newn;
    }
    else
    {
        newn->next = *first;
        *first = newn;
    }
}

int CountEven(PNODE first)
{
    int iCount = 0;
    PNODE temp = NULL;

    temp = first;

    while(temp != NULL)
    {
        if((temp->data) % 2 == 0)
        {
            iCount++;
        }

        temp = temp->next;
    }

    return iCount;
}

int main()
{
    PNODE head = NULL;
    int iRet = 0;
    
    InsertFirst(&head,101);
    InsertFirst(&head,51);
    InsertFirst(&head,21);
    InsertFirst(&head,11);
    InsertFirst(&head,22);

    Display(head);

    iRet = CountEven(head);
    printf("Count of Even nodes is : %d",iRet);

    return 0;
}