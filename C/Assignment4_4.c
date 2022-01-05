#include<stdio.h>

int SumNonFact(int iNo)
{
	int iCnt = 0;
	int iNonFact = 0; 
	
	for(iCnt=1;iCnt<iNo;iCnt++)
	{
		if((iNo % iCnt) != 0)
		{
			printf("%d\n",iCnt);
			
			iNonFact = iNonFact + iCnt;
		}		
	}
	return iNonFact;
}	

int main()
{
	int iValue = 0;
	int iRet = 0;
	
	printf("Enter number");
	scanf("%d",&iValue);
	
	iRet = SumNonFact(iValue);
	
	printf("%d",iRet);
	 
	return 0;
}

