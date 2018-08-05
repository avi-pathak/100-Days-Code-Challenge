class A
{
	A()
	{
		System.out.println("A-Constructor");
	}
	{
		System.out.println("Instance Block of A ");
	}
}
class test 
{
	public static void main(String[] args) 
	{
		A a = new A(); //before excuting contrust instance block must be excuted

		/*
		OUTPUT:

		Instance Block of A 
		A-Constructor

		*/
	}
}

//Second Program Of Instance BLOCK

class A
{
	int i=m1();
	{
		System.out.println("Instance Block of a");
	}
	
	int m1()
	{
		System.out.println("m1-A");
		return 10;
	}
	A()
	{
		System.out.println("Instance Block of A ");
	}
}
class test 
{
	public static void main(String[] args) 
	{
		A a = new A(); //before excuting contrust instance block must be excuted buty class level varoable intialize first

		/*
		OUTPUT:
		m1-A
		Instance Block of A 
		A-Constructor

		*/
	}
}
