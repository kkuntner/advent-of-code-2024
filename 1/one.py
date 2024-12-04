print("Welcome to Day 1!")

def summarize_distances(input_file):
    list1 = []
    list2 = []
    sum=0
    with open(input_file, 'r') as infile:
        for line_number, line in enumerate(infile, start=1):
            num1, num2 = line.split()
            list1.append(int(num1))
            list2.append(int(num2))
        list1.sort()
        list2.sort()

    for i in range(len(list1)):
        sum +=abs(list1[i] - list2[i])    

    print(f"sum = {sum} ")    

def summarize_distances2(input_file):
    list1 = []
    list2 = []
    sum=0
    with open(input_file, 'r') as infile:
        for line_number, line in enumerate(infile, start=1):
            num1, num2 = line.split()
            list1.append(int(num1))
            list2.append(int(num2))
        list1.sort()
        list2.sort()

    for i in range(len(list1)):
        sum += list1[i] * list2.count(list1[i]) 

    print(f"sum = {sum} ")    



input_file = 'input.txt'   

summarize_distances(input_file)
summarize_distances2(input_file)