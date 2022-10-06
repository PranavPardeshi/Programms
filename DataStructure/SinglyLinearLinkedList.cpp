#include<iostream>
using namespace std;

typedef struct node
{
	int data;
	struct node *next;		//	self referencial pointer
}NODE,*PNODE;

class SinglyLL
{
	private:
		PNODE first;
		int size;
	
	public:		
		SinglyLL()
		{
			first = NULL;
			size = 0;
		}
		// Step 1 : Allocate the memory
		// Step 2 : Initialise the memory
		// step 3 : Insert the node

		void InsertFirst(int no)
		{
			PNODE newn = new NODE;		// Dynamic memory allocation
			
			newn -> data = no;
			newn -> next = NULL;
			
			if(first == NULL)
			{
				first = newn;
			}
			else
			{
				newn->next = first;
				first = newn;
			}
			size++;
		}
		void InsertAtPos(int no,int ipos)
		{
			if((ipos < 1) || (ipos > (size+1)))
			{
				return;
			}
			else if(ipos == 1)
			{
				InsertFirst(no);
			}
			else if(ipos == (size+1))
			{
				InsertLast(no);
			}
			else
			{
				PNODE newn = new NODE;
				newn -> data = no;
				newn -> next = NULL;
				
				PNODE temp = first;
				for(int i = 1; i < ipos-1; i++)
				{
					temp = temp->next;
				}
				newn->next = temp->next;
				temp->next = newn;
				
				size++;
			}
		}
		void InsertLast(int no)
		{
			PNODE newn = new NODE;
			
			newn -> data = no;
			newn -> next = NULL;
			
			if(first == NULL)
			{
				first = newn;
			}
			else
			{
				PNODE temp = first;
				while(temp->next != NULL)
				{
					temp = temp->next;
				}
				temp->next = newn;
			}
			size++;		
		}
		
		void DeleteFirst()
		{
			PNODE temp = first;
			if(first != NULL)
			{
				first = first->next;
				delete temp;
				size--;
			}
		}
		void DeleteLast()
		{
			PNODE temp = first;
			
			if(first == NULL)
			{
				return;
			}
			else if(temp->next == NULL)
			{
				delete first;
				first = NULL;
				size--;
			}
			else
			{
				while(temp->next->next != NULL)
				{
					temp = temp->next;
				}
				delete temp->next;
				temp->next = NULL;
				size--;
			}
		}
		void DeleteAtPos(int ipos)
		{
			if((ipos < 1) || (ipos > size))
			{
				return;
			}
			else if(ipos == 1){DeleteFirst();}

			else if(ipos == size){DeleteLast();}
			
			else
			{
				PNODE temp = first;
				PNODE targated = NULL;
				
				for(int i = 1;i < ipos-1;i++)
				{
					temp = temp->next;
				}
				targated = temp->next;
				temp->next = targated->next;
				delete targated;
				
				size--;
			}
		}
		
		
		
		void Display()
		{
			PNODE temp = first;
			while(temp != NULL)
			{
				cout<<"|"<<temp->data<<"|->";
				temp = temp->next;
			}
			cout<<"\n";
		}
		int count()
		{
			return size;
		}
};

int main()
{
	cout<<"-----------Singly Linear Linked List-----------\n";

	SinglyLL *ptr = NULL;
	ptr = new SinglyLL;
	int ret = 0;
	
	ptr->InsertFirst(21);
	ptr->InsertFirst(11);
	ptr->InsertFirst(1);
	ptr->InsertLast(51);
	ptr->InsertLast(151);
	ptr->InsertAtPos(101,5);

	ptr->Display();
	ret = ptr->count();
	cout<<"Number of elements inside linkedlist are "<<ret<<"\n";
	
	ptr->DeleteFirst();
	ptr->DeleteLast();

	ptr->Display();

	ptr->DeleteAtPos(3);
	ptr->Display();
	ret = ptr->count();
	cout<<"Number of elements inside linkedlist are "<<ret<<"\n";
	
	delete ptr;
	
	return 0;

}
