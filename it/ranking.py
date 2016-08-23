students = []
with open("student.txt", encoding='utf8') as infile:
    students = infile.readlines()

students.pop(0)
for st in students:
    data = st.split()
    # print(data[0])
    sum = int(data[2]) + int(data[3]) + int(data[4])
    # print(sum)
    avr = sum / 3


def get_sum(x):
    data = x.split()
    sum = int(data[2]) + int(data[3]) + int(data[4])
    return sum


def get_gender(x):
    data = x.split()
    if data[1] == "남":
        return 1
    else:
        return 0


man_count = 0
for st in students:
    gender = get_gender(st)
    man_count += gender
print("남자수:", man_count)
print("여자수:", len(students) - man_count)

sorted_students = sorted(students, key=get_sum, reverse=True)

for st in sorted_students:
    print(st)
