import random
offices = [[], [], []]
teacher_name = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for n in teacher_name:
    index = random.randint(0, 2)
    offices[index].append(n)
i = 1
for office in offices:
    print(office, end=" ")
    print(f"办公室{i}的人数为:", len(office))
    i += 1
