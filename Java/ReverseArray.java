import java.util.Scanner;

class ReverseArray
{
    public static void main(String arr[])
    {
        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter size of array:");
        int iSize = sobj.nextInt();

        int Arr[] = new int[iSize];

        System.out.println("Enter elements");
        for(int i = 0; i < iSize;i++)
        {
            Arr[i] = sobj.nextInt();
        }

        ArrayX aobj = new ArrayX();
        aobj.ReverseArrayX(Arr);

    }
}
class ArrayX
{
    public void ReverseArrayX(int Arr[])
    {
        int s = 0;
        int e = Arr.length - 1;
        int temp = 0;

        while(s <= e)
        {
            temp = Arr[s];
            Arr[s] = Arr[e];
            Arr[e] = temp;

            s++;
            e--;
        }

        for(int i = 0; i < Arr.length;i++)
        {
            System.out.print("|"+Arr[i]+"|");
        }
        
    }
}
