% Facts
student(101, sunil).
student(102, bala).
student(103, varunan).

teacher(t1, ramesh).
teacher(t2, priya).
teacher(t3, kumar).

subject(s1, prolog).
subject(s2, python).
subject(s3, java).

% Student-Teacher-Subject relationship
studies(101, t1, s1).
studies(102, t2, s2).
studies(103, t3, s3).

% Display student, teacher and subject details
student_teacher_subject(Student, Teacher, Subject) :-
    student(Student, Name),
    teacher(Teacher, TeacherName),
    subject(Subject, SubjectName),
    studies(Student, Teacher, Subject),
    write('Student Name: '), write(Name), nl,
    write('Teacher Name: '), write(TeacherName), nl,
    write('Subject Name: '), write(SubjectName), nl.