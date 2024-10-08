import java.util.Scanner;
public class Adam{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,r,rev=0;
        n=sc.nextInt();
        int s=n*n;
        while(n!=0)
        {
            r=n%10;
            rev=rev*10+r;
            n=n/10;
        }
        int p=rev*rev,a,pr=0;
        while(p!=0)
        { 
            a=p%10;
            pr=pr*10+a;
            p=p/10;
        }
        if(pr==s)
        {
            System.out.println("True");
        }
        else
        {
            System.out.println("False");
        }
    }
}