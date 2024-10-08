import java.util.Scanner;
public class Amicable{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,m,j,i,sum=0,add=0;
        n=sc.nextInt();
        m=sc.nextInt();
        for(i=1;i<n;i++)
        {
           if(n%i==0)
           {
            sum=sum+i;
           }
        }
        for(j=1;j<m;j++)
        {
            if(m%j==0)
            {
                add=add+j;
            }
        }
        if(sum==m && add==n)
        {
            System.out.println("Amicable");
        }
        else
        {
            System.out.println("Not Amicable");
        }
    }
}