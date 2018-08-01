echo "Enter the term"
read n
a=1
b=0
if [ $n -ne 0 ]
then
	if [ $n -eq 1 ]
	then
		echo "0"
	else
		if [ $n -eq 2 ]
		then
			echo " 0 1"
		else
			echo $a
			echo $b
			while [ $n -gt 0 ]
			do
				c=`expr $a + $b`
				echo $c
				b=$a				
				a=$c
				n=`expr $n - 1`
				done
		fi
	fi
else
	echo "Zero Is not allowed"
fi
