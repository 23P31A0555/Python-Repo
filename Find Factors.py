import java.util.Scanner;
public class Factors{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,i;
        n=sc.nextInt();
        for(i=1;i<=n;i++)
        {
            if(n%i==0)
            {
                System.out.printf("%d ",i);
            }
        }
    }
}