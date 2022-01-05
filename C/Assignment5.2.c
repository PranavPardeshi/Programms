#include<stdio.h>
#define TRUE 1
#define FALSE 0

typedef int BOOL;

BOOL ChkZero(int iNo)
{
	int iDigit = 0;

	while(iNo > 0)
	{
		iDigit = iNo % 10;
		//printf("%d\n",iDigit);
		iNo = iNo / 10;
		
		if(iDigit == 0)		
		{
			return TRUE;
		}
	}

}

int main()
{
	int iValue = 0;
	BOOL bRet = FALSE;
	
	printf("Enter Number: ");
	scanf("%d",&iValue);
	
	bRet = ChkZero(iValue);
	
	if(bRet == TRUE)
	{
		printf("It Contains Zero");
	}
	else
	{
		printf("There is no zero");
	}
	return 0;
}
