import java.util.Scanner;
public class Automorphic {
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,s;
        n=sc.nextInt();
        int r=n*n;
        int p=r%10;
        int a=r%100;
        int b=r%1000;
        if(a==n || b==n || p==n)
        {
            System.out.println("Automorphic Number");
        }
        else{
            System.out.println("Not an Automorphic Number");
        }
    }
}