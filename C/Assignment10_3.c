/*
	iRow : 3
	iCol : 4
	output :
	*   #    *    #
	*   #    *    #
	*   #    *    #	
*/





#include<stdio.h>

void Pattern(int iRow , int iCol)
{
	int i , j = 0;
	
	for(i = 1; i <= iRow; i++)
	{
		for(j = 1;j <= iCol; j++)
		{
			if((j % 2) == 0)
			{
				printf("#    ");
			}
			else
			{
				printf("*    ");
			}
		}
		printf("\n");
	}
}

int main()
{
	int iValue1 = 0,iValue2 = 0;
	
	printf("Enter number of Rows and Columns");
	scanf("%d %d",&iValue1,&iValue2);
	
	Pattern(iValue1,iValue2);
	
	return 0;
}