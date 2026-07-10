//Count Frequency of Given Number - Count how many times a number appears

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
        printf("| %d | -> ",first->data);
        first = first->next;
    }

    printf("NULL\n");
}

void InsertFirst(PPNODE first, int iNo)
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

int Frequency(PNODE first, int iNo)
{
    PNODE temp = NULL;
    temp = first;
    int iCount = 0;

    while(temp != NULL)
    {
        if(temp->data == iNo)
        {
            iCount++;
        }
        
        temp = temp -> next;
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
    InsertFirst(&head,51);

    Display(head);

    iRet = Frequency(head,51);
    printf("Frequency is : %d",iRet);

    return 0;
}