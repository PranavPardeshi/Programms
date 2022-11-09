#include<iostream>
using namespace std;

typedef struct node
{
    int data;
    struct node *next;
    struct node *prev;
}NODE,*PNODE;

class DoublyLL
{
    private:
        int size;
        PNODE first;
        PNODE last;

    public:
        DoublyLL()
        {
            size = 0;
            first = NULL;
            last = NULL;
        }

        int Count()
        {
            return size;
        }
        void Display()
        {
            PNODE temp = first;
            while(temp!=NULL)
            {
                cout<<"|"<<temp->data<<"|->";
				temp = temp->next;
            }
            cout<<"\n";
        }

        void InsertFirst(int no)
        {
            PNODE newn = new NODE;
            newn->data = no;
            newn->next = NULL;
            newn->prev = NULL;

            if((first == NULL) && (last == NULL))
            {
                first = newn;
                last = newn;
            }
            else
            {
                newn->next = first;
                first->prev = newn;
                first = newn;
            }
            first->prev = NULL;
            last->next = NULL;
            size++;
        }
        void InsertLast(int no)
        {
            PNODE newn = new NODE;
            newn->data = no;
            newn->next = NULL;
            newn->prev = NULL;
            
            if((first == NULL) && (last == NULL))
            {
                first = newn;
                last = newn;
            }
            else 
            {
                last->next = newn;
                newn->prev = last;
                last = newn;
            }
            last->next = NULL;
            first->prev = NULL; 
            size++;       
        }
        void InsertAtPos(int no, int ipos)
        {
            if((ipos < 1) || (ipos > size+1))
            {
                return;
            }
            else if(ipos == 1)
            {
                InsertFirst(no);
            }
            else if(ipos == size+1)
            {
                InsertLast(no);
            }
            else
            {
                PNODE newn = new NODE;
                newn->data = no;
                newn->next = NULL;
                newn->prev = NULL;

                PNODE temp = first;
                for(int i=1; i < ipos-1;i++)
                {
                    temp = temp->next;
                }
                newn->next = temp->next;
                temp->next->prev = newn;
                temp->next = newn;
                newn->prev = temp;
            }
            first->prev = NULL;
            last->next = NULL;
            size++; 
        }
        void DeleteFirst()
        {
            if((first == NULL) && (last == NULL))
            {
                return;
            }
            else if(first == last)
            {
                delete first;
                first = NULL;
                last = NULL;
            }
            else
            {
                PNODE temp = first;
                first = first->next;
                delete temp;
            }
            first->prev = NULL;
            last->next = NULL;
            size--;
        }
        void DeleteLast()
        {
            if((first == NULL) && (last == NULL))
            {
                return;
            }
            else if(first == last)
            {
                delete first;
                first = NULL;
                last = NULL;
            }
            else
            {
                PNODE temp = last;
                last = last->prev;
                delete temp;
            }
            last->next = NULL;
            first->prev = NULL;
            size--;    
        }
        void DeleteAtPos(int ipos)
        {
            if((ipos < 1) || (ipos > size+1))
            {
                return;
            }
            else if(ipos == 1)
            {
                DeleteFirst();
            }
            else if(ipos == size)
            {
                DeleteLast();
            }
            else
            {
                PNODE temp = first;
                for(int i = 1; i < ipos -1; i++)
                {
                    temp = temp->next;
                }
                PNODE targated = temp->next;
                temp->next = targated->next;
                targated->next->prev = temp;
                delete targated;

                first->prev = NULL;
                last->next = NULL;

                size--;
            }
        }
};

int main()
{
    cout<<"----------Doubly Linear linked list----------\n";

    /*DoublyLL obj;
    int iRet = 0;
    obj.InsertFirst(21);
    obj.InsertFirst(11);
    obj.InsertLast(101);
    obj.InsertAtPos(51,3);
    obj.Display();

    iRet = obj.Count();*/

    DoublyLL *ptr = NULL;
    ptr = new DoublyLL;

    int iRet = 0;
    ptr->InsertFirst(21);
    ptr->InsertFirst(11);
    ptr->InsertLast(101);
    ptr->InsertAtPos(51,3);
    ptr->Display();
    
    //ptr->DeleteFirst();
    //ptr->DeleteLast();  
    ptr->DeleteAtPos(3);
    ptr->Display();

    iRet = ptr->Count();
    cout<<"Elements inside linkedlist are : "<<iRet;

    delete ptr;
    return 0;
}