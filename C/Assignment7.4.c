#include<stdio.h>

double FhtoCs(float fTemp)
{
	float fCels = 0.0;
	
	fCels = (fTemp - 32) * 0.5555556;
		
	return fCels;
}
int main()
{
	float fValue = 0.0;
	double dRet  = 0.0;
	
	printf("Enter temperature in Fahrenheit");
	scanf("%f",&fValue);
	
	dRet = FhtoCs(fValue);
	
	printf("%f",dRet);	
	
	return 0;
}