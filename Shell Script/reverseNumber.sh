echo "enter any Number"
read a
rev=0
while [ $a -gt 0 ]
do
	rem=`expr $a % 10`
	rev=`expr $rev \* 10 + $rem`
	a=`expr $a / 10`
	done
echo $rev
