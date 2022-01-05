#include<stdio.h>

double RectArea(float fWidth,float fHeight)
{
	float fArea = 0;
	
	fArea = fWidth * fHeight;
	
	return fArea;	
}

int main()
{
	float fValue1 = 0.0, fValue2 = 0.0;
	double dRet = 0.0;
	
	printf("Enter Width");
	scanf("%f",&fValue1);
	
	printf("Enter Height");
	scanf("%f",&fValue2);
	
	dRet = RectArea(fValue1,fValue2);
	printf("Area of Rectangle is %f",dRet);
	
	return 0;	
}