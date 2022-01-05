#include<stdio.h>

int KMtoMeter(int iNo)
{
	int iCnv = 0;
	
	iCnv = iNo * 1000;
	
	return iCnv;
	
}

int main()
{
	int iValue = 0,iRet = 0;
	
	printf("Enter distance");
	scanf("%d",&iValue);
	
	iRet = KMtoMeter(iValue);
	
	printf("%d",iRet);
	
	return 0;
}