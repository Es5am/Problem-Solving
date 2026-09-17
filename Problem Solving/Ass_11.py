"""
Problem Solving Assignment 11

Problem 1 : Create A List Called ( my_nums ) And Assign It With Some Numbers, Then Use The For Loop To Print All Numbers That Are Divisible By 5 And Print The Count Of Numbers Printed Successfuly.

Problem 2 : Use The For Loop To Print All Numbers From 1 To 20, But Ignore The Numbers ( 6 , 8 , 12 ) And Print The Count Of Ignored Numbers.

Problem 3 : Create A Dictionary Called ( my_ranks ) And Assign It With Some Subjects And Their Ranks, Then Use The For Loop To Print All Subjects With Their Ranks And The Points Of Each Rank, Then Print The Total Points.

Problem 4 : Create A Dictionary Called ( students ) And Assign It With Some Students Names As Keys And Their Subjects With Their Ranks As Values,
Then Use The For Loop To Print All Students Names With Their Subjects And Ranks And The Points Of Each Rank, Then Print The Total Points For Each Student.
"""



#                         Solution



################################### Ass_1 ##########################################

my_nums = sorted([15, 81, 5, 17, 20, 21, 13], reverse=True)
count=0
for number in my_nums:
    if number % 5 == 0 :
       count+=1
       print(f"{count} => {number} ")
else : print("All Numbers Printed")

print("="*50)

################################### Ass_2 ##########################################

for i in range(1,21) :
    if i == 6 or i==8 or i==12:
     continue
    print(str(i).zfill(2))
    # print(f"{i:02}") Another Method

print("="*50)

################################### Ass_3 ##########################################

my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
total_points=0

for rank_key , rank_value in my_ranks.items(): 
   if rank_value == "A" :
      points= 100
   elif rank_value == "B" :
      points= 80
   elif rank_value == "C" :
      points= 40
   total_points+=points
   print(f"My Rank in {rank_key} Is {rank_value} And This Equal {points} Points")
print(f"Total Points Is {total_points}")
print("="*50)

total_points=0   
################################### Ass_4 ##########################################

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

for student_key , student_value in students.items():

   print("-"*50)

   print(f"-- Stident Name => {student_key}")

   print("-"*50)

   total_points=0

   for child_key , child_value in student_value.items():
    
    points=0

    if child_value == "A" :
       points=100
    elif child_value=="B":
       points=80
    elif child_value=="C":
       points=40
    elif child_value=="D":
       points=20

    total_points+=points

    print(f"- {child_key} => {points} points")

   print(f"Total Points For {student_key} Is {total_points}")

print("#"*50)

######################## Another Method ########################

POINTS_MAP = {
    "A": 100,
    "B": 80,
    "C": 40,
    "D": 20
}

students = {
    "Ahmed": {"Math": "A", "Science": "D", "Draw": "B", "Sports": "C", "Thinking": "A"},
    "Sayed": {"Math": "B", "Science": "B", "Draw": "B", "Sports": "D", "Thinking": "A"},
    "Mahmoud": {"Math": "D", "Science": "A", "Draw": "A", "Sports": "B", "Thinking": "B"}
}

for name, subjects in students.items():
    
    print("-" * 50)

    print(f"-- Student Name => {name}")

    print("-" * 50)

    total_points = 0  

    for subject, grade in subjects.items():
        
        points = POINTS_MAP[grade]

        total_points += points

        print(f"- {subject} => {points} points")
        
    print(f"Total Points For {name} Is {total_points}")

print("#"*50)

######################## Another Method ########################

POINTS_MAP = {
    "A": 100,
    "B": 80,
    "C": 40,
    "D": 20
}

students = {
    "Ahmed": {"Math": "A", "Science": "D", "Draw": "B", "Sports": "C", "Thinking": "A"},
    "Sayed": {"Math": "B", "Science": "B", "Draw": "B", "Sports": "D", "Thinking": "A"},
    "Mahmoud": {"Math": "D", "Science": "A", "Draw": "A", "Sports": "B", "Thinking": "B"}
}

for name in students:
    
    print("-" * 50)

    print(f"-- Student Name => {name}")

    print("-" * 50)

    total_points = 0 

    subjects=students[name] 

    for sub_name in subjects:
        
        points = POINTS_MAP[subjects[sub_name]]

        total_points += points

        print(f"- {sub_name} => {points} points")
        
    print(f"Total Points For {name} Is {total_points}")


    