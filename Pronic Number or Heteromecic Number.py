import java.util.Scanner;
public class Number{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n,i,flag=1;
        n=sc.nextInt();
        for(i=1;i<=n;i++)
        {
            if(i*(i+1)==n)
            {
               flag=1;
               break;
            }
            else{
                flag=0;
            }
        }
        if(flag==1)
        {
            System.out.println("YES");
        }
            else
            {
                System.out.println("NO");
            }
        
    }
}