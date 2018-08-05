class A
{
	int i,j,k;
	A()
	{

	}
	A(int i1)
	{
		i=i1;
	}
	A(int i1,int j1)
	{
		i=i1;
		j=j1;
	}
	A(int i1,int j1,int k1)
	{
		i=i1;
		j=j1;
		k=k1;
	}
	void add()
	{
		System.out.println("Addtion"+(i+j+k));
	}

}
class Test1s 
{
	public static void main(String[] args) 
	{
		A a1 =new A();
		a1.add();
		A a2 = new A(20);
		a2.add();
		A a3 = new A(20,30);
		a3.add();
		A a4 = new A(20,30,40);
		a4.add();
	}
	/*
	OUTPUT
		0 beacuse default intialze value is 0
		20
		50
		90
	*/
}
