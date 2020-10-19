#Read the file and split lines into data variable
with open('./data.txt', 'r') as file:
    data = []
    data = file.read().split("\n")
#Create an .sh for append the lines
output = open("bathMail.sh","w")
output.write("#!/bin/bash \n")
for mail in data:
    #Write the script .sh for run in a GNU/Linux server with the data variable information
    #In this case I use a script for create emails accounts for postfix with other script.
    output.write("./script.sh -u " + mail + "\n")
#Close the File
output.close()