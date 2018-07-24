import java.util.*; 
class Employee
{
	int age;
	float sallary;
	Employee()
	{
		age=10;
		sallary=100.0f;
	}
	public String toString()
	{
		System.out.println("This Is Class A");
		return "";
	}
}
class test 
{
	public static void main(String[] args) 
	{
		System.out.println("Hello World!");
		Employee emp= new Employee();
		System.out.println(emp.hashCode());
		System.out.println(emp.toString());
		System.out.println(emp);//emp.toString()
		/*Remember
		hashCode ProtoType is
		public native int hashCode()
		toString() ProtoType
		public String toString()
		*/
	}
}
