"""
Problem 1: Create 50 Text Files In A Folder Called ( Python ) And Write In Each File ( Elzero Web School => File Number ) And Make The File Number From 1 To 50.

Problem 2: Append The Text ( Appended => Elzero Web School ) 50 Times In The First File ( 1.txt ) Only.

Problem 3: Read The First File ( 1.txt ) And Count The Number Of Lines, Words, Characters, And The Number Of Times The Character ( l ) Is Found In The File.

Problem 4: Delete The Last 10 Files From The Folder ( Python ) And Print A Message For Each File Deleted.
"""

#                         Solution


# ############################## Ass_1 ##############################

# # For -> files range (1,51)
# # file number 
# # file 25 -> spical-text emty
# # print Current Working Directory
# # print path of file
# # print Name of file
# # print Number of files 


import os 

for i in range(1,51) :
    
    filename = fr"D:\Work\Elzero\Python\Ass\Ass_14\Python\{i}.txt"
    
    if i == 25 :
        file = open (r"D:\Work\Elzero\Python\Ass\Ass_14\Python\special-text.txt","w")
        file.close()
    else :
        file = open(filename,"w")
        file.write(f"Elzero Web School => {i}")
        file.close()

print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))
# print(os.path.basename(__file__))
print(len(os.listdir(os.path.dirname(os.path.abspath(__file__)))))


# ############################## Ass_2 ##############################

file=open(r"D:\Work\Elzero\Python\Ass\Ass_14\Python\1.txt","a")
file.write("\nAppended => Elzero Web School"*50)
file.close()

############################## Ass_3 ##############################

file=open(r"D:\Work\Elzero\Python\Ass\Ass_14\Python\1.txt","r")
content = file.read()

count_lines = len(content.splitlines())
count_words = len(content.split())
count_chars = len(content) - content.count(" ") - content.count("=>")
count_chars_l = content.count("l")

print(f"Number Of Lines Is => {count_lines}")
print(f"Number Of Words Is => {count_words}")
print(f"Number Of Chars Is => {count_chars}")
print(f"Number Of 'l' Chars Is => {count_chars_l}")

file.close()

############################## Ass_4 ##############################

for i in range(41,51):
    file_name = fr"D:\Work\Elzero\Python\Ass\Ass_14\Python\{i}.txt"
    if os.path.exists(file_name) :
        os.remove (file_name)
        print(f"Deleted {file_name}")

print("Done Deleting Last 10 Files")
