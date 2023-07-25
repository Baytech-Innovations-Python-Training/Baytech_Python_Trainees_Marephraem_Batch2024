name = []
marks = []
count = int(input('Enter the count of students : '))
sub_count = int(input('Enter the count of subjects : '))
for i in range(count):
    name.append(input(f'Enter student {i + 1} name : '))
    for j in range(sub_count):
        marks.append(int(input(f'Enter sub {j + 1} mark for student {i + 1} : ')))


def find_grade(avg):
    
    """ This function accepts average marks
        and returns the grade as per the avg """
    
    if avg >= 90 and avg <= 100:
        return 'Grade : A'
    elif avg >= 80 and avg <= 89:
        return 'Grade : B'
    elif avg >= 70 and avg <= 79:
        return 'Grade : C'
    else:
        return 'Grade : D'


for i in range(count): 
    mark = 0
    result = []
    print(f'Student name is {name[i]}')
    for j in range(i * 2, i * 2 + sub_count):
        print(f'mark of sub {j + 1} {marks[j]}')
        mark += marks[j]
        if not marks[j] > 35:
            result.append(False)
        else:
            result.append(True)

    avg = mark/sub_count
    print(f'Tot of {name[i]} is {mark}')
    print(f'Avg of {name[i]} is {avg}')
    for j in result:
        if not j:
            fresult = False
            break
        else:
            fresult = True
    # print(f'Result is {result}')
    
    if fresult:
        print(f'You have passed')
        grade = find_grade(avg=avg)
        print(grade)
    else:
        print('you\'re failed')