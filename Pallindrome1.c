#include<stdio.h>
#include<stdio.h>

bool CheckPallindrome(int);
int Reverse(int);

int main()
{
	int iValue = 0;
	bool bRet = false;
	
	printf("Enter a number: ");
	scanf("%d",&iValue);
	
	bRet = CheckPallindrome(iValue);
	
	if(bRet == true)
	{
		printf("Number is Pallindrome!");
	}
	else
	{
		printf("Number is not Pallindrome");
	}
	return 0;
}

bool CheckPallindrome(int iNumber)
{
	int iNo = 0;
	
	iNo = Reverse(iNumber);
	
	if(iNo == iNumber)
	{
		return true;
	}
	else
	{
		return false;
	}
	
}

int Reverse(int iInput)
{
	int iDigit = 0,iRev = 0;
	
	while(iInput != 0)
	{
		iDigit = iInput % 10;
		iRev = (iRev * 10) + iDigit;
		iInput = iInput / 10;
	}
	return iRev;
}	