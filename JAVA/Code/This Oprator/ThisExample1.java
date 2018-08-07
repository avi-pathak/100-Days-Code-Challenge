class A
{
	int a=10;
	int b=20;
	A(int a,int b)
	{
		System.out.println(a+"   "+b);
		System.out.println(this.a+"   "+this.b);
	}
}
class test1
{
	public static void main(String [] args)
	{
		A a=new A(50,60);
	}
}
