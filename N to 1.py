import java.util.Scanner;
public class Program{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,i;
        n=sc.nextInt();
        for(i=n;i>=1;i--)
        {
            System.out.printf("%d ",i);
        }
    }
}