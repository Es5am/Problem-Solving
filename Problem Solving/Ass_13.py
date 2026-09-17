

"""
Problem 1: Create A Function Called ( calculate ) That Accepts 3 Parameters ( n1 , n2 , calc ) And 
The Default Value Of The n2 Is ( 0 ) And The Default Value Of The calc Is ( Add ) And The Function Should Return The Result Of The Calculation Between n1 And n2 Based On The calc Value

Problem 2: Create A Function Called ( addition ) That Accepts A Variable Number Of Arguments And 
Return The Total Of All Arguments Except The Number ( 10 ) And If The Number ( 5 ) Is Found In The Arguments It Should Be Subtracted From The Total.

Problem 3: Create A Function Called ( get_score ) That Accepts A Variable Number Of Keyword Arguments And Print The Subject And The Degree For Each Subject.

"""
#                         Solution


############################ Ass_1 ################################

def get_score(**score) :

    for subject,degree in score.items():
        print(f"{subject} => {degree}")

get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)

print("="*50)

############################ Ass_2 ################################

def get_people_scores(name="",**score) :

        if not score :
            print(f"Hello {name} You Have No Scores To Show")
        
        elif name == "" or name == None:
             for subject,degree in score.items():
              print(f"{subject} => {degree}")
        else:
            print(f"Hello {name} This Is Your Score Table : ")
            for subject,degree in score.items():
                print(f"{subject} => {degree}")
        

get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores("Ahmed")
get_people_scores(Logic=70, Problems=60)


print("="*50)

############################ Ass_3 ################################

scores_list =  {
    "Math": "90",
    "Science": "80",
    "Language": "70",
    }



def get_the_scores(name="",**score) :
        if not score :
            print(f"Hello {name} You Have No Scores To Show")
        
        elif name == "" or name == None:
             for subject,degree in score.items():
              print(f"{subject} => {degree}")
        else:
            print(f"Hello {name} This Is Your Score Table : ")
            for subject,degree in score.items():
                print(f"{subject} => {degree}")


get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)