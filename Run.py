from Csv import csv

# Creating the groups of data as a list
Data = [["Dineth", "De", "Silva"], ["Manjula", "Chamila"]]
# Creating a csv file to save data
File = csv("File Name")
# Writing Data to the csv file created
File.write(Data)
# Read the data from that csv file and save it in the variable "Output"
Output = File.read()
# Print the "Output"
print(Output)
# Deleting the csv file
File.close()
