if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    c=0    
    for values in student_marks:
        if values==query_name:
         for i in student_marks[query_name]:
             c=c+i
    s= c/len(student_marks[query_name])
    formated="{:.2f}".format(s)
    print(formated)