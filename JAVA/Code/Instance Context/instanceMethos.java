class A
{
	int i=m1();
	A()
	{
		System.out.println("A-Constructor");
	}
	int m1()
	{
		System.out.print("m1-A")
		return 10;
	}
}
class test 
{
	public static void main(String[] args) 
	{
		A a = new A();

	}
	/*
	OUTPUT

	m1-A
	A-Constructor

	*/
}

//for theory u can refer to NotesForMe Folder 
