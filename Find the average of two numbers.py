import java.util.Scanner;
public class Average{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        double a,b;
        a=sc.nextDouble();
        b=sc.nextDouble();
        double c=(a+b)/2;
        System.out.printf("%.4f",c);
    }
}