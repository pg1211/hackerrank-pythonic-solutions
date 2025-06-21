def func():
    Student = ("Student", ["ID", "MARKS", "CLASS", "NAME"])

    # first line contains number of students
    num_students = int(input())
  
    # only care about marks: in first line, figure out which place MARKS is in and use that
    marks_placement = next(i for i, x in enumerate(input().split()) if x == "MARKS")

    # now, iterate through rest of students and sum up marks 
    total_marks = 0
    for i in range(num_students):
        total_marks += int(input().split()[marks_placement])
        
    print(total_marks / num_students)
    
    


if __name__ == "__main__":
    func()
