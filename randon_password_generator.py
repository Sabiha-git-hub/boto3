from random import choice

len_of_password=10
valid_chars_for_password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password=[]
for each_char in range(len_of_password):
    password.append(choice(valid_chars_for_password))

random_password= "".join(password)    
#this "".join is a way to join the characters in a list as string

print (random_password)
 








