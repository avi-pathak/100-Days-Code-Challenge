echo "Enter any number"
read n
fact=1
while [ $n -gt 0 ]
do
fact=`expr $n \* $fact`
n=`expr $n - 1`
done
echo "Factorial "$fact
