#include<stdio.h>
void DisplayEvenFactor(int iNo);

int main()
{
	int iValue = 0;
	
	printf("Enter number\n");
	scanf("%d",&iValue);
	
	DisplayEvenFactor(iValue);
	
	return 0;
}

void DisplayEvenFactor(int iNo)
{
	int i = 0;
	
	if(iNo <= 0)
	{
		iNo = - iNo;		
	}
	for(i = 1;i <= (iNo/2); i++)
	{
		if((i%2) && (iNo%i)!= 0)
		{
			printf("%d\n",i);
		}
	}
}