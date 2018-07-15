 class Student
{
	String stuName;
	String stuRoll;
	public void setData(String name,String roll_no)
	{
		stuName=name;
		stuRoll=roll_no;
	}
	public void dispData()
	{
		System.out.println("Student Detail");
		System.out.println("-----------------------");
		System.out.println("student Name "+stuName);
		System.out.println("Student Roll Numebr Is :"+stuRoll);
	}

}
public class  test
{
	public static void main(String[] args) 
	{
		Student st1=new Student();
		st1.setData("Avinash","A-111");
		st1.dispData();
	}
}
