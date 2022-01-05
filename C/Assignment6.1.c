#include<stdio.h>
//Time Complacity : n , n for number of digits. 

int CountEven(int iNo)
{
	int iDigit = 0;
	int iCnt = 0;
	
	if(iNo < 0)
	{
		iNo = -iNo;
	}
	
	while(iNo > 0)	//O(N) Where N is number of digits (N >= 0).
	{
		iDigit = iNo % 10;
		iNo = iNo / 10;
		
		if((iDigit % 2) == 0)
		{
			iCnt++;
		}
	}
	return iCnt;
}

int main()
{
	int iValue = 0;
	int iRet = 0;
	
	printf("Enter Number");
	scanf("%d",&iValue);
	
	iRet = CountEven(iValue);
	
	printf("%d",iRet);
	
	return 0;
	
}



