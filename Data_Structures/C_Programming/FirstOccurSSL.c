#include<stdio.h>
#include<stdlib.h>

#pragma pack(1)
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
        printf("| %d | -> ",first->data);
        first = first->next;
    }
    printf("NULL\n");
}

int Count(PNODE first)
{
    int iCount = 0;
    while(first != NULL)
    {
        iCount++;
        first = first->next;
    }
    return iCount;
}

void InsertLast(PPNODE first,int iNo)
{
    PNODE temp = NULL;
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
        temp = *first;

        while(temp->next != NULL)
        {
            temp = temp->next;
        }

        temp->next = newn;
        newn->next = NULL;

    }
}

int FirstOcuur(PNODE first, int iNo)
{
    int iPos = 1;

    while(first != NULL)
    {
        if(first->data == iNo)
        {
            return iPos;
        }

        iPos ++;
        first = first->next;
    }

}

int main()
{
    int iRet = 0;
    int iNum = 0;

    PNODE head = NULL;

    InsertLast(&head,11);
    InsertLast(&head,21);
    InsertLast(&head,51);
    InsertLast(&head,101);
    

    Display(head);

    iRet = Count(head);

    printf("Number of nodes are : %d\n",iRet);

    iNum = FirstOcuur(head, 21);
    
    printf("Position is : %d\n",iNum);

    return 0;
}