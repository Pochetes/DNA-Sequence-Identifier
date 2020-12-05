import csv, sys
    # program that matches DNA sequence counts to a person in a database of DNA sequences
    # argv[1] is the csv database, argv[2] is the DNA sequence txt file
    # open the csv and DNA sequence, and read the contents into memory
    # count the longest repeat of DNA sequences of one code base, [AGAT], [AATG], [TATC]
    # iterate through the rows of people and their data and compare it with the STR counts
def main():
    arg = sys.argv
    DNAdict = {}

    if len(arg) != 3:
        print("Usage: python dna.py (database) (DNA sequence)")
        return 1
    else:
        database = arg[1]
        dnaSeq = arg[2]

    strands = opendata(database, DNAdict)
    DNAcount(dnaSeq, DNAdict, strands)
    match(DNAdict, strands)
    """if match(DNAdict, strands):
        print("Match found.")
    else:
        print("No matches found.")"""

def opendata(data, dt):
    strands = {}
    # open the file to read
    with open(data) as csvfile:
        datareader = csv.reader(csvfile)
        
        for k, v in enumerate(datareader):
            if k == 0:
                # parse out the strands to iterate through for the DNA sequence
                for strand in v[1:]:
                    strands[strand] = 0
            else:
                # 
                dt[v[0]] = v[1:]
    return strands
            
def DNAcount(sequence, dt, dnastrands):
    # open the DNA sequence file and count the highest no. of repeated sequences for each code base
    with open(sequence) as seqfile:
        # find the highest number of repeated sequences for [AGAT], [AATG], [TATC]
        txtreader = seqfile.read()
        # iterate through each dna strand
        for strand in dnastrands.keys():
            counter = 0
            index = 0
            maxnum = 0
            size = len(strand)
            # for each strand check for each position of DNA sequence
            while index < len(txtreader):
                seqnum = txtreader[index: index + size]
                # checks if strand in queue == next set of strands
                if seqnum == strand:
                    counter += 1
                    index += size
                # does not repeat anymore
                else:
                    if counter > maxnum:
                        maxnum = counter
                    counter = 0
                    index += 1
            dnastrands[strand] = maxnum
        
def match(database, dnastrands):
    temp = []
    
    for num in dnastrands.values():
        temp.append(str(num))
    
    for names, values in database.items():
        if temp == values:
            print(names)
            return 0
    
    print("No match.")
    return 1
    



if __name__ == "__main__":
    main()