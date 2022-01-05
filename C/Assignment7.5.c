#include<stdio.h>

double SquareMeter(int iValue)
{
	float fSquareMeter = iValue * 0.0929;
	
	return fSquareMeter;
	
}

int main()
{
	int iValue = 0;
	double dRet = 0.0;
	
	printf("Enter area in square feet");
	scanf("%d",&iValue);
	
	dRet = SquareMeter(iValue);
	
	printf("%f",dRet);
	
	return 0;
}