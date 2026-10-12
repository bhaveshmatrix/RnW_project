print("Welcome To The Interactive Presonal Data Collecter!")

Name = str(input("Please Enter Your Name : "))
Age = int(input("PLease Enter Your Age : "))
height = float(input("Please Enter Your Height in meters : "))
Fav_num = int(input("Please Enter Your Fav Number : "))
print(" ")
print("Thank you! Here is the information we collected:")
print(" ")
print("Name  :",Name ,"(type :",type(Name),"Memory address",id(Name),")" )
print("Age  :",Age  ,"(type :",type(Age),"Memory address",id(Age),")" )
print("Height  :",height ,"(type :",type(height),"Memory address",id(height),")" )
print("Favourite_Number",Fav_num ,"(type :",type(Fav_num),"Memory address",id(Fav_num),")" )
print(" ")
Year =  2026 - Age
print("Your birth year is approximately: ",Year,"(based on your age of",Age,")")





