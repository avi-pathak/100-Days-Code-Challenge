def marks_summation(marks,number_of_students,gender):
     sum = 0;
     i = 0 if gender == 'b' else  1
     while i<number_of_students:
          sum +=marks[i]
          i+=2
     return sum;
