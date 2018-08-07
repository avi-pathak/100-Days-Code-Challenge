class A
{
	int a=10;
	int b=20;
	A(int a,int b)
	{
		System.out.println(a+"   "+b);//print the local variable
		System.out.println(this.a+"   "+this.b);//it will print the class level variable
	}
}
class test1
{
	public static void main(String [] args)
	{
		A a=new A(50,60);
	}
}
