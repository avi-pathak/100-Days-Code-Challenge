if __name__ == '__main__':
    n = int(input())
    Student_marks = {}
    for _ in range(n):
        s=[x for x in input().split()]
        name=s[0]
        Student_marks[name]=eval(s[1])
        Student_marks[s[0]]+=eval(s[2])
        Student_marks[s[0]]+=eval(s[3])
    solution=input()
    Answer=Student_marks[solution] / 3
    print("%.2f"%(Answer))
