#include<iostream>
using namespace std;

typedef struct node
{
	int data;
	struct node *next;
}NODE,*PNODE;

class Queue
{
	private:
		int size;
		PNODE first;
	
	public:
		Queue()
		{
			first = NULL;
			size = 0;
		}
		void Enqueue(int no)
		{
			PNODE newn = new NODE;
			newn->data = no;
			newn->next = NULL;
			
			if(first == NULL)
			{
				first = newn;
			}
			else 
			{
				PNODE temp = first;
				while(temp->next != NULL)
				{
					temp=temp->next;
				}
				temp->next = newn;
			}
			size++;
		}
		int Dequeue()
		{
			int no = 0;
			PNODE temp = first;
			
			if(size == 0)
			{
				cout<<"Queue is empty\n";
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
				first = first->next;
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
				cout<<"|"<<temp->data<<"|"<<"\n";
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
	cout<<"----------Queue----------\n";
	
	Queue obj;
	int ret = 0;
	
	obj.Enqueue(11);
	obj.Enqueue(21);
	obj.Enqueue(51);
	obj.Enqueue(101);
	
	obj.Display();
	ret = obj.Count();
	cout<<"Size of Queue "<<ret<<"\n";
	
	ret = obj.Dequeue();
	obj.Display();
	cout<<"Removed element from queue "<<ret<<"\n";
	ret = obj.Count();
	cout<<"Size of Queue "<<ret<<"\n"
	
	ret = obj.Dequeue();
	obj.Display();
	cout<<"Removed element from queue "<<ret<<"\n";
	ret = obj.Count();
	cout<<"Size of Queue "<<ret<<"\n";
	
	return 0;
}