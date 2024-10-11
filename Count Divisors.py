import java.util.Scanner;
public class Count{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int l,i,r,k,c=0;
        l=sc.nextInt();
        r=sc.nextInt();
        k=sc.nextInt();
        for(i=l;i<=r;i++)
        {
            if(i%k==0)
            {
                c=c+1;
            }
        }
        System.out.println(c);

    }
}