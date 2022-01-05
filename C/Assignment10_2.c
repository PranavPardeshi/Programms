#include<stdio.h>

void Pattern(int iRow,int iCol)
{
	int iCnt = 0;
	
	for(iCnt=1; iCnt <= iRow; iCnt++)
	{
		for(iRow = 1;iRow <= iCol; iRow++)
		{
			printf("%d\t",iCnt);
		}
		printf("\n");	
	}
}
int main()
{
	int iValue1 = 0, iValue2 = 0;
	
	printf("Enter number of rows and columns");
	scanf("%d %d",&iValue1,&iValue2);
	
	Pattern(iValue1,iValue2);
	
	return 0;	
}