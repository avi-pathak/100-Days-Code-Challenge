echo "enter a no."
read a
if [ `expr $a % 2` -eq 0 ]
then
 echo "even no."
else
 echo "odd no."
fi
