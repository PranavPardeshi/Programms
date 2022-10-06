#include<iostream>
using namespace std;

typedef struct node 
{
	int data;
	struct node *next;
}NODE,*PNODE;

class Stack
{
	private:
		PNODE first;
		int size;
	public:
		
		Stack()
		{
			first = NULL;
			size = 0;
		}
		void Push(int no)			// InsertFirst(int no)
		{
			PNODE newn = new NODE; 		// dynamic memory allocation
			newn->data = no;
			newn->next = NULL;
			
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
		int Pop()				// DeleteFirst()
		{
			int no = 0;
			PNODE temp = first;			
			
			if(size == 0)
			{
				cout<<"Stack is empty\n";
				return -1;
			}
			else if(size == 1)
			{
				no = first->data;
				delete first;
				first = NULL;
			}
			else
			{
				no = first->data;
				first=first->next;
				delete temp;
			}
			size--;
			return no;
		}
		void Display()
		{
			PNODE temp = first;
			while(temp != NULL)
			{
				cout<<"|"<<temp->data<<"|\n";
				temp = temp->next;
			}
		}
		int Count()
		{
			return size;
		}
};

int main()
{
	Stack *ptr = NULL;
	ptr = new Stack;
	int ret = 0;
	
	ptr->Push(11);
	ptr->Push(21);
	ptr->Push(51);
	ptr->Push(101);
	
	ptr->Display();
	ret = ptr->Count();
	
	cout<<"Size of stack is"<<ret<<"\n";
	
	ret = ptr->Pop();
	cout<<"Poped element is "<<ret<<"\n";
	ret = ptr->Pop();
	cout<<"Poped element is "<<ret<<"\n";
	
	ptr->Display();
	ret = ptr->Count();
	
	cout<<"Size of stack is "<<ret<<"\n";
	
	return 0;
}


