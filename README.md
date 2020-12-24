# CSV
Write & read comma delimited data in a csv file by python
## Quick Start
Run *"Run.py"* by typing **Python Run.py** in the Terminal

```Bash
Python Run.py
```
If it's print something in the terminal without an *error* follow **Usage** Section
## Usage
### Creating a csv file object
First import csv class from Csv library
Create a csv file object by passing *File Name*
```Python
from Csv import csv
File = csv("File Name")
```
### Write data into a csv file
First create a list contain data
```Python
Data = [["Dineth", "De", "Silva"], ["Mike", "Dane"]]
```
Write that data into the csv file created
```Python
File.write(Data)
```
### Read data from the csv file
Read the data in the csv file and store data in a variable
```Python
Read_Data = File.read()
```
Printing the variable
```Python
print(Read_Data)
```
### Delete the csv file created
```Python
File.close()
```
