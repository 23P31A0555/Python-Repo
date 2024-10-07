import java.util.Scanner;
public class Count{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,c=0,r;
        n=sc.nextInt();
        while(n!=0)
        {
            r=n%10;
            c=c+1;
            n=n/10;
        }
        System.out.println(c);
    }
}