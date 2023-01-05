class DataStructure
{
    public int getPivot(int Arr[])
    {
        int start,end,mid;
        start = 0;
        end = Arr.length-1;
        mid = 0;

        mid = (start + end) / 2;

        while(start < end)
        {
            if(Arr[mid] >= Arr[0])
            {
                start = mid + 1;
            }
            else
            {
                end = mid;
            }
            mid = (start + end)/2;
        }
        return start;
    }
}

class PivotElement
{
    public static void main(String arr[])
    {
        int iret = 0;
        Scanner sobj = new Scanner(System.in);

        System.out.println("Enter size of an array: ");
        int iSize = sobj.nextInt();

        int Arr[] = new int[iSize];
        for(int i = 0;i < Arr.length;i++)
        {
            Arr[i] = sobj.nextInt();
        }
        DataStructure dobj = new DataStructure();
        iret = dobj.getPivot(Arr);

        System.out.println("Pivot element is "+iret);
    }
}