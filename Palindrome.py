import java.util.Scanner;
public class Palindrome{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,rev=0,r;
        n=sc.nextInt();
        int temp=n;
        while(temp!=0)
        {
            r=temp%10;
            rev=rev*10+r;
            temp=temp/10;
        }
        if(n==rev)
        {
            System.out.println("Palindrome");
        }
        else
        {
            System.out.println("Not Palindrome");
        }
    }
}