class A
{
	void varArg(int ... a)
	{
		System.out.println("total No of Argument"+a.length);
		System.out.println("Content of Var Arg Method");
		for (int i=0;i<a.length ;i++)
		{
			System.out.print(a[i]+"\t");
		}
		
	}
}
class test1 
{
	public static void main(String[] args) 
	{
		A a =new A();
		a.varArg(10);
		a.varArg(110,200);
	}
}
