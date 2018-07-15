interface I
{
	int x = 40;// public static final
	void m1();//public abstract
	void m2();
	void m3();
}
class A implements I
{
	public void m1()
	{
		System.out.println("M1-A");
	}
	public void m2()
	{
		System.out.println("M2-A");
	}
	public void m3()
	{
		System.out.println("M3-A");
	}
	public void m4()
	{
		System.out.println("m4");
	}
}
 public class  test
{
	public static void main(String[] args) 
	{
		//I i =new I(); give the Error
		I i=new A();
		i.m1();//correct
		i.m2();//correct
		i.m3();//coorrect
		//i.m4(); is incoorect wil give error 
		A a=new A();
		a.m1();//correct
		a.m2();//correct
		a.m3();//coorrect
		a.m4();//correct
		System.out.println(I.x);
		System.out.println(i.x);
		System.out.println(A.x);
		System.out.println(a.x);
	}
}
