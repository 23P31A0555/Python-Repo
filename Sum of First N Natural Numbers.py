import java.util.Scanner;
public class First{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,add=0,i;
        n=sc.nextInt();
        for(i=1;i<=n;i++)
        {
          add=add+i;
        }
        System.out.println(add);
    }
}