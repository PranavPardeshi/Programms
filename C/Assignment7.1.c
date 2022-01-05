#include<stdio.h>

double CircleArea(float fRadius)
{
	double dArea = 0.0;
	float fPi = 3.14;
	
	dArea = fPi * fRadius * fRadius;
	
	return dArea;	
}

int main()
{
	float fValue = 0.0;
	double dRet = 0.0;
	
	printf("Enter radius");
	scanf("%f",&fValue);
	
	dRet = CircleArea(fValue);
	
	printf("Area of circle is %f",dRet);
	
	return 0;
}
