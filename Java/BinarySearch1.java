import java.util.Scanner;

class Binary
{
    public boolean BinarySearchX(int Arr[],int iNo)
    {
        int start,end,mid;
        start = 0;
        end = Arr.length - 1;
        mid = (start + end) / 2;

        while(start <= end)
        {
            if(Arr[mid] == iNo)
            {
                break;
            }
            else if(iNo > Arr[mid])
            {
                start = mid + 1;
            }
            else if(iNo < Arr[mid])
            {
                start = mid - 1;
            }
            mid = (start + end) / 2;
        }
        if(Arr[mid] == iNo)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
class BinarySearch1
{
    public static void main(String arr[])
    {
        int iSize = 0,iNo = 0;
        boolean bret = false;

        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter length of array: ");
        iSize = sobj.nextInt(); 
        
        int Arr[] = new int[iSize];
        for(int i = 0; i < Arr.length;i++)
        {
            Arr[i] = sobj.nextInt();
        }

        System.out.println("Enter number you want to search: ");
        iNo = sobj.nextInt();
        
        Binary bobj = new Binary();
        
        bret = bobj.BinarySearchX(Arr,iNo);
        if(bret == true)
        {
            System.out.println("Number is present.");
        }
        else
        {
            System.out.println("Number is absent.");
        }
    }
}