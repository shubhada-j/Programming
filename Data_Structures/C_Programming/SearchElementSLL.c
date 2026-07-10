//Search an Element - Check whether a number is present

#include<stdio.h>
#include<stdlib.h>

#pragma pack(1)
struct node 
{
    int data;
    struct node * next ;

};

typedef struct node NODE;
typedef struct node * PNODE;
typedef struct node ** PPNODE;
typedef int BOOL;

#define TRUE 1
#define FALSE 0

void Display(PNODE first)
{
    while(first != NULL)
    {
        printf("| %d | -> ",first->data);
        first = first->next;
    }
    printf("NULL\n");
}

void InsertLast(PPNODE first,int iNo)
{
    PNODE newn = NULL;
    PNODE temp = NULL;

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

BOOL SearchElement(PNODE first, int iNo)
{
    PNODE temp = NULL;

    temp = first;

    while(temp != NULL)
    {
        if(temp->data == iNo)
        {
            return TRUE;
        }

        temp = temp->next;
    }

    return FALSE;  
}

int main()
{
    PNODE head = NULL;
    int iValue = 0;
    BOOL bRet = FALSE;

    InsertLast(&head,11);
    InsertLast(&head,21);
    InsertLast(&head,51);
    InsertLast(&head,101);

    Display(head);

    printf("Enter the element : ");
    scanf("%d",&iValue);

    bRet = SearchElement(head,iValue);

    if(bRet == TRUE)
    {
        printf("Number is found");
    }
    else
    {
        printf("Number is not found");
    }

    return 0;
}