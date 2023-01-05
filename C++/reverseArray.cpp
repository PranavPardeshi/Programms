#include<iostream>
using namespace std;

void ReverseArray(int Arr[],int iSize)
{
    int s = 0;
    int e = iSize - 1;
    int temp = 0;
    
    while(s <= e)
    {
        temp = Arr[s];
        Arr[s] = Arr[e];
        Arr[e] = temp;
        s++;
        e--;
    }
    for(int j = 0; j < iSize;j++)
    {
        cout<<"|"<<Arr[j]<<"|";
    }
}

int main()
{
    int iSize = 0;
    cout<<"Enter size of an array: \n";
    cin>>iSize;

    int Arr[iSize];

    cout<<"Enter elements: \n";
    for(int i = 0;i < iSize;i++)
    {
        cin>>Arr[i];
    }

    ReverseArray(Arr,iSize);

    return 0;

}