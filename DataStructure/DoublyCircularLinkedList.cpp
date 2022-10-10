#include<iostream>
using namespace std;

typedef struct node 
{
	int data;
	struct node *next;
	struct node *prev;
}NODE,* PNODE;

class DoublyCL
{
	private:
		int size;
		PNODE first;
		PNODE last;
		
	public:
		DoublyCL()
		{
			size = 0;
			first = NULL;
			last = NULL;
		}
		
		void InsertFirst(int no)
		{
			PNODE newn = new NODE;
			
			newn->data = no;
			newn->prev = NULL;
			newn->next = NULL;
			
			if((first == NULL) && (last==NULL))
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
			last->next = first;
			first->prev = last;
			size++;
		}
		void InsertLast(int no)
		{
			PNODE newn = new NODE;
			
			newn->data = no;
			newn->next = NULL;
			newn->prev = NULL;
			
			if((first == NULL)&&(last == NULL))
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
			last->next = first;
			first->prev = last;
			size++;
		}
		void InsertAtPos(int no,int ipos)
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
				for(int i = 1; i < ipos-1 ; i++)
				{
					temp = temp->next;
				}
				newn->next = temp->next;
				temp->next->prev = newn;
				temp->next = newn;
				newn->prev = temp;
				
				size++;
			}
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
				first = first->next;
				delete last->next;
				first->prev = last;
				last->next = first;
			}
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
				last = last->prev;
				delete last->next;
				first->prev = last;
				last->next = first;
			}
			size--;
		}
		void DeleteAtPos(int ipos)
		{
			if((ipos < 1) || (ipos > size))
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
				
				for(int i = 1; i < ipos-1; i++)
				{
					temp = temp->next;
				}
				temp->next = temp->next->next;
				delete temp->next->prev;
				temp->next->prev = temp;
				
				size--;
			}
				
		}
		void Display()
		{
			PNODE temp = first;
			
			for(int i = 1; i <= size; i++)
			{
				cout<<"|"<<temp->data<<"|->";
				temp = temp->next;
			}
			cout<<"\n";
		}
		int Count()
		{
			return size;
		}
};

int main()
{
	cout<<"----------Doubly Circular linked list----------\n";
	
	DoublyCL *ptr = NULL;
	ptr = new DoublyCL;
	int iret = 0;
	
	
	ptr->InsertLast(101);
	ptr->InsertFirst(21);
	ptr->InsertFirst(11);
	ptr->InsertAtPos(51,3);
	ptr->InsertAtPos(111,5);
	
	ptr->Display();
	iret = ptr->Count();
	
	cout<<"Elements in linkedlist are "<<iret<<"\n";
		
	ptr->DeleteLast();
	ptr->DeleteFirst();
	ptr->DeleteAtPos(3);
	
	ptr->Display();
	iret = ptr->Count();
	cout<<"Elements in linkedlist are "<<iret<<"\n";
	
	delete ptr;
	
	return 0;
}