# DNA-Sequence-Identifier

This project uses Python to find a person through their DNA sequence/structure.

This takes in a CSV file argument of DNA sequences and calculates the highest number of repeated sequences or something known as Short Tandem Repeats (STR). This is how the FBI can track down a person with a criminal record in their database. It also takes the parameter a database where all of these people's STRs are stored. This Python script opens the file and reads it into memory. Also, it scrapes through all of the information and stores it into a dictionary with names as the keys and STRs for values. 

With this information, I wrote an algorithm that iterates through the whole database given and tries to match it with the person's DNA structure. If found, it prints the name of the person. If not found, it provides a message saying "Not Found."

This was a small script that utilizes data structures such as dictionaries and advanced operations such as csvReader to properly check every row of the CSV file. 
