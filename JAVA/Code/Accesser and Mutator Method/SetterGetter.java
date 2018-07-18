class Employee
{
	private String ename;
	private float esal;
	private String eaddr;
	private String eid;
	//Mutator Method
	public void setEname(String name)
	{
		ename=name;
	}
	public void setEid(String id)
	{
		eid=id;
	}
	public void setEsal(float sal)
	{
		esal=sal;
	}
	public void setEaddr(String Adrr)
	{
		eaddr=Adrr;
	}

	//Accesser Method 
	public String getEname()
	{
		return ename;
	}
	public String getEadrr()
	{
		return eaddr;
	}
	public float getEsal()
	{
		return esal;
	}
	public String getEid()
	{
		return eid;
	}
}
class Test
{
	public static void main(String[] args)
	{
		Employee emp = new Employee();
		emp.setEname("Avinash");
		emp.setEaddr("lucknow");
		emp.setEid("Avinashhdskk");
		emp.setEsal(15000.0f);
		System.out.println("Employee Detail");
		System.out.println("----------------------------------");
		System.out.println("Employee Name\t"+emp.getEname());
		System.out.println("Employee ID\t"+emp.getEid());
		System.out.println("Employee Address\t"+emp.getEadrr());
		System.out.println("Employee Sallary\t"+emp.getEsal());
		
	}
}
