#include<stdio.h>

int FactDiff(int);

int main(int iNo)
{
	int iValue = 0;
	int iRet = 0;
	
	printf("Enter number");
	scanf("%d",&iValue);
	
	iRet = FactDiff(iValue);
	printf("%d\n",iRet);
	
	return 0;
}

int FactDiff(int iNo)
{
	int iCnt = 0;
	int iTemp = 0;
	int iTemp1 = 0;
	int iDiff = 0;
	for(iCnt = 1;iCnt<(iNo/2);iCnt++)
	{
		if((iNo%iCnt)!=0)
		{
			iTemp = iCnt;
			if((iNo%iCnt)==0)
			{
				iTemp1 = iCnt; 
			}
		}
		iDiff = iTemp - iTemp1;
		
	}
	return iDiff;
	
	/*int iFactSum = 0;
	int iNonFactSum = 0;
	int iDiff = 0;
	
	for(iCnt = 1;iCnt<(iNo/2);iCnt++)
	{
		if((iNo%iCnt) == 0)
		{
			//printf("%d\n",iCnt);
			printf("%d\n",iFactSum);
		}
		while((iNo%iCnt) != 0 )
		{
				
			iDiff = iFactSum - iNonFactSum;
		}
	}
	return iDiff;
	
	*/
}