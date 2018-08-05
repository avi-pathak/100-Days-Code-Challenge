class A
{
	int i=10;
	A()
	{
		System.out.println("A-Constructor");
	}
}
class test 
{
	public static void main(String[] args) 
	{
		A a = new A();
		System.out.println(a.i);//10
		//System.out.println(A.i);    ERORR
		A a1=null;

		//System.out.println(a1.i);   ERROR REFER last point in notes
	}
}

//For theory part u can refer to the Notes For me folder
