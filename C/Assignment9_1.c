#include<stdio.h>

void Pattern(int iNo)
{
	int iCnt = 0;
	char ch = 'a';
	for(iCnt = 1; iCnt <= iNo; iCnt++)
	{
		printf("%c\t",ch);
	}
	printf("\n");
}
int main()
{
	int iValue = 0;
	
	printf("Enter number of elements");
	scanf("%d %d",&iValue);

	Pattern(iValue);
	
	return 0;
}