questions = [
    ["What is the output of print(type([]))?", 
     "<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>", 1],

    ["Which keyword is used to define a function in Python?", 
     "func", "define", "def", "function", 3],

    ["What will print(2 ** 3) output?", 
     "6", "8", "9", "5", 2],

    ["Which data type is immutable?", 
     "list", "set", "dictionary", "tuple", 4],

    ["What is the correct file extension for Python files?", 
     ".pt", ".pyt", ".py", ".python", 3],

    ["Which function is used to get user input?", 
     "get()", "input()", "scan()", "read()", 2],

    ["What is the output of print(len('Python'))?", 
     "5", "6", "7", "Error", 2],

    ["Which operator is used for floor division?", 
     "/", "//", "%", "**", 2],

    ["Which of these is a Python tuple?", 
     "[1, 2, 3]", "{1, 2, 3}", "(1, 2, 3)", "None", 3],

    ["What is the output of print(bool(0))?", 
     "True", "False", "None", "Error", 2],

    ["Which keyword is used for loops in Python?", 
     "loop", "iterate", "for", "repeat", 3],

    ["What will print(type({})) output?", 
     "<class 'list'>", "<class 'set'>", "<class 'dict'>", "<class 'tuple'>", 3],

    ["Which method adds an item to a list?", 
     "append()", "add()", "insert()", "extend()", 1],

    ["What is the output of print(10 % 3)?", 
     "3", "1", "0", "10", 2],

    ["Which of the following is used to handle exceptions?", 
     "try-except", "if-else", "for-while", "def-return", 1]
]

prizes = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500]
i = 0

print("Lets start the Quiz....")

for question in questions:
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}\n")

    ans = int(input("Enter the correct ans"))
    if(question[5] == ans):
        print("Correct answer2")
        print(f"You won {prizes[i]}\n")
    else:
        print(f"Incorrect answer, the correct answer is {question[5]}.")
        print(f"You won {prizes[i-1]}\n")
        break

    i = i + 1

