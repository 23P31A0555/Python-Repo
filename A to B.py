import java.util.Scanner;
public class Program{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int a,b,i;
        a=sc.nextInt();
        b=sc.nextInt();
        for(i=a;i<=b;i++)
        {
            System.out.printf("%d ",i);
        }
    }
}