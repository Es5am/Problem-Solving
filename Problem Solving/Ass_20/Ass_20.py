# ######################################## Ass_1 ########################################


# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []
# storage=[]

# for data in zip(my_list, my_tuple):
#     storage.append(data)

# for tup in storage :
#     for item in tup:
#         my_data.append(str(item)) 

# final_string="".join(my_data)
# print(final_string) 

# print("-"*50)

# ######################################## Ass_1_another Method ########################################

# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for item1,item2 in zip(my_list, my_tuple):
#   my_data.append(item1)
#   my_data.append(item2)

# final_string="".join(my_data)
# print(final_string) # Elzero

# print("-"*50)

# ######################################## Ass_1_another Method ########################################

# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list, my_tuple):
#   my_data.append(data[0])
#   my_data.append(data[1])

# final_string="".join(my_data)
# print(final_string) # Elzero

# print("-"*50)


# ######################################## Ass_2 ########################################


# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
#     if type(item2)==int:
#        break
#     my_data.append(item2)
#     my_data.append(item3)

# final_string="".join(my_data)
# print(final_string)

# print("-"*50)


# ######################################## Ass_3 ########################################

# from PIL import Image

# My_Image= Image.open(r"D:\Work\Elzero\Python\Ass\20\elzero-pillow.png")

# My_Image.show()

# croped_Image = (400, 0, 800, 400)
# Litter_L_Image = My_Image.crop(croped_Image)

# Litter_L_Image.show()


# Litter_L_Converted=Litter_L_Image.convert("L")
# Litter_L_Converted.show()

# croped_Image_2= (0, 400, 1200, 800)

# row_2=My_Image.crop(croped_Image_2)
# row_2_converted=row_2.convert("L").rotate(180)

# row_2.show()
# row_2_converted.show()

# print("-"*50)

# ######################################## Ass_4 ########################################


# def say_hello_to(name):
    
#     """parameter(someone) => Person Name
#     Function To Say Hello To Anyone"""
    
#     return f"Hello {name}"

# print(say_hello_to.__doc__)
# help(say_hello_to)
# print(say_hello_to("Osama")) 

# print("-"*50)
















