import java.util.*;

class FirstOccurance
{
    public static void main(String arr[])
    {
        int iSize = 0,iNo = 0;
        int iFirst = 0;
        int iLast = 0;

        Scanner sobj = new Scanner(System.in);
        
        System.out.println("Enter length of array: ");
        iSize = sobj.nextInt(); 
        
        int Arr[] = new int[iSize];
        for(int i = 0; i < Arr.length;i++)
        {
            Arr[i] = sobj.nextInt();
        }

        System.out.println("Enter number : ");
        iNo = sobj.nextInt();
        
        BinaryX bobj = new BinaryX();
        
        iFirst = bobj.FirstOccuranceX(Arr,iNo);
        System.out.println("First occurance of "+iNo+" is at index "+iFirst);

        iLast = bobj.LastOccarance(Arr,iNo);
        System.out.println("Last occurance of "+iNo+" is at index "+iLast);
    }
}
class BinaryX
{
    public int FirstOccuranceX(int Arr[],int iNo)
    {
        int start,end,mid,ans;
        start = 0;
        end = Arr.length - 1;
        mid = start + (end - start) / 2;

        ans = -1;

        while(start <= end)
        {
            if(Arr[mid] == iNo)
            {
                ans = mid;
                end = mid - 1;
                break;
            }
            else if(Arr[mid] < iNo)
            {
                start = Arr[mid] + 1;
            }
            else if(Arr[mid] > iNo)
            {
                start = Arr[mid] - 1;
            }
            mid = start + (end - start) / 2;
        } 
        return ans;
    }
    
    public int LastOccarance(int Arr[],int iNo)
    {
        int start,end,mid,ans;
        start = 0;
        end = Arr.length - 1;
        mid = start + (end - start) / 2;
        ans = -1;

        while(start <= end)
        {
            if(Arr[mid] == iNo)
            {
                ans = mid;
                start = mid + 1;
                break;
            }
            else if(Arr[mid] < iNo)
            {
                start = mid + 1;
            }
            else if(Arr[mid] > iNo)
            {
                start = mid - 1;
            }
            mid = start + (end - start) / 2;
        }
        return ans;
    }
}