#include<iostream>
using namespace std;

typedef struct node
{
	int data;
	struct node *next;
}NODE,*PNODE;

class SinglyCL
{
	private:
		PNODE first;
		PNODE last;
		int size;
	public:
		
		SinglyCL()
		{
			first = NULL;
			last = NULL;
			size = 0;
		}
		void Display()
		{
			PNODE temp = first;
			if((first == NULL) && (last == NULL))
			{
				return;
			}
			do
			{
				cout<<"|"<<temp->data<<"|->";
				temp = temp->next;
			}while(temp != last->next);
			cout<<"\n";
		}
		
		int count()
		{
			return size;
		}
		
		void InsertFirst(int no)
		{
			PNODE newn = new NODE;		//	Dynamic memory allocation
			newn->next = NULL;
			newn->data = no;
			
			if((first == NULL) && (last == NULL))
			{
				first = newn;
				last = newn;
			}
			else
			{
				newn->next = first;
				first = newn;				
			}
			last->next = first;
			size++;
		}
		void InsertLast(int no)
		{
			PNODE newn = new NODE;
			newn->next = NULL;
			newn->data = no;
			
			if((first == NULL) && (last == NULL))
			{
				first = newn;
				last = first;
			}
			else
			{
				last->next = newn;
				last = newn;				
			}
			last->next = first;
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
				newn->next = NULL;
				newn->data = no;
				
				PNODE temp = first;
				for(int i = 1;i < ipos-1;i++)
				{
					temp = temp -> next;
				}
				newn->next = temp->next;
				temp->next = newn;
			}
			last->next = first;
			size++;
		}
		void DeleteFirst()
		{
			if((first == NULL) && (last == NULL))
			{
				return ;
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
				PNODE temp = first;
				while(temp->next != last)
				{
					temp = temp->next;
				}
				delete last;
				last = temp;
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
				
				for(int i = 1; i < ipos - 1;i++)
				{
					temp = temp->next;
				}
				
				PNODE targated = NULL;
				targated = temp->next;
				temp->next = targated->next;	// temp->next = temp->next->next;
				delete targated;
				
				last->next = first;				
				size--;			
			}
		}
		
};

int main()
{
	cout<<"------------Singly Circular Linked list----------\n";
	
	SinglyCL *ptr = NULL;
	ptr = new SinglyCL;
	int ret = 0;
	
	ptr->InsertFirst(21);
	ptr->InsertFirst(11);
	ptr->InsertLast(101);
	ptr->InsertLast(151);
	ptr->InsertLast(251);
	ptr->InsertAtPos(51,3);	
	
	ptr->Display();
	ret = ptr->count();

	cout<<"Elements inside linked list are "<<ret<<"\n";	

	ptr->DeleteFirst();
	ptr->DeleteLast();
	ptr->DeleteAtPos(3);
	
	ptr->Display();
	ret = ptr->count();
	
	cout<<"Elements inside linked list are "<<ret<<"\n";	
	
	delete ptr;
	
	return 0;

}