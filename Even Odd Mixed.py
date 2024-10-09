import java.util.Scanner;
public class Number{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,r,c=0,d=0,flag=0;
        n=sc.nextInt();
        while(n!=0)
        {
            r=n%10;
            if(r%2==0)
            {
                c=c+1;
            }
            else if(r%2!=0)
            {
                d=d+1;
            }
            n=n/10;
             flag=flag+1;
        }
        if(flag==c)
        {
            System.out.println("Even");
        }
        else if(flag==d)
        {
            System.out.println("Odd");
        }
        else{
            System.out.println("Mixed");
        }
    }
}