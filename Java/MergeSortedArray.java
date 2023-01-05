import java.util.Scanner;

class MergeSortedArray
{
    public static void main(String arr[])
    {
        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter size of 1st array:");
        int iSize1 = sobj.nextInt();

        int Arr1[] = new int[iSize1];

        System.out.println("Enter elements");
        for(int i = 0; i < iSize1;i++)
        {
            Arr1[i] = sobj.nextInt();
        }

        System.out.println("Enter size of 2nd array:");
        int iSize2 = sobj.nextInt();

        int Arr2[] = new int[iSize2];

        System.out.println("Enter elements");
        for(int i = 0; i < iSize2;i++)
        {
            Arr2[i] = sobj.nextInt();
        }
        int iSize3 = iSize1 + iSize2;

        ArrayX aobj = new ArrayX();
        aobj.MergeArray(Arr1,Arr2,iSize3);

    }
}

class ArrayX
{
    public void MergeArray(int Arr1[],int Arr2[],int iSize3)
    {
        int Arr3[] = new int[iSize3];

        int i = 0,j = 0,k = 0;
        
        while(i < Arr1.length && j < Arr2.length)
        {
            if(Arr1[i] < Arr2[j])
            {
                Arr3[k] = Arr1[i];
                k++;
                i++;
            }
            else
            {
                Arr3[k] = Arr2[j];
                k++;
                j++;
            }
        }
        while(i < Arr1.length)
        {
            Arr3[k] = Arr1[i];
            k++;
            i++;
        }       
        while(j < Arr2.length)
        {
            Arr3[k] = Arr2[j];
            k++;
            j++;
        }

        for(int c = 0; c < Arr3.length;c++)
        {
            System.out.print("|"+Arr3[c]+"|");
        }
    }

}