import java.util.Scanner;
public class Program{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,a,b,i,s;
        n=sc.nextInt();
        a=sc.nextInt();
        b=sc.nextInt();
        for(i=a;i<=b;i++)
        {
           s=n*i;
           System.out.printf("%d x %d = %d\n",n,i,s);
        }
    }
}