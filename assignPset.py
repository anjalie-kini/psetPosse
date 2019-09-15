class Student(object):
    def __init__(self, name, dorm, current, past):
        self.name = name
        self.dorm = dorm
        self.current = current
        self.past = past

    def __str__(self):
        return self.name


students = []
input = open('test.csv', 'r')
for line in input:
    line = line.rstrip()
    line = line.split(', ')
    name = line[0] + ' ' + line[1]
    dorm = line[2]

    current = []
    past  = []
    # adding current classes for each person
    index = 4
    while(line[index] != 'past'):
        current.append(line[index])
        index += 1

    for i in range(index + 1, len(line)):
        past.append(line[i])

    student = Student(name, dorm, current, past)
    print(student)
    students.append(student)
    print(current)
    print(past)


learn = {}
tutor = {}
test = []
for s in students:
    print(s)
    for i in s.current:
        if i in learn.keys():
            learn[i].append(s)
        else:
            learn[i] = [s]

    for j in s.past:
        if j in tutor.keys():
            tutor[j].append(s)
        else:
            tutor[j] = [s]

print(learn)
print(tutor)
