import java.util.Scanner;
public class Abundant{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,i,sum=0;
        n=sc.nextInt();
        for(i=1;i<n;i++)
        {
            if(n%i==0)
            {
                sum=sum+i;
            }
        }
        if(sum>n)
        {
            System.out.println("True");
        }
        else
        {
            System.out.println("False");
        }
    }
}