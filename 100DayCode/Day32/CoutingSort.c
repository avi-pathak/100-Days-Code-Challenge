#include<stdio.h>
#include<conio.h>
void main()
{
	int a[]={6,6,6,5,5,2,1,0,0},n=9,i;
	int Result[]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},temp[6]={0};
	clrscr();
	for(i=0;i<n;i++)
	{
		temp[a[i]]+=1;
	}
	for(i=1;i<=6;i++)
		temp[i]+=temp[i-1];
	printf("Before Sorting\n");
	for(i=0;i<n;i++)
		printf("%d  ",a[i]);
	n=9;
	for(i=0;i<n;i++)
	{
		Result[temp[a[i]]]=a[i];
		temp[a[i]]=temp[a[i]]-1;
	}
	printf("After Sorting");
	for(i=1;i<=10;i++)
		if(Result[i]>=0)
			printf("%d  ",Result[i]);
       getch();
}
