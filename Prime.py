import java.util.Scanner;
public class Prime{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,c=0,i;
        n=sc.nextInt();
        for(i=1;i<=n;i++)
        {
            if(n%i==0)
            {
                c=c+1;
            }
        }
        if(c==2)
        {
            System.out.println("Prime");
        }
        else
        {
            System.out.println("Not Prime");
        }
    }
}