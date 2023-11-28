# code name: reconstructSentence.py
# code by: Davis Farrow
# 
# CPE 420 HW 10 problem 1
# this code reads two text files and reconstructs/combines their contents to produce the complete output.
# Each input file contains words that alternate with the other file but the order of the words is
# reversed. The script takes one word from the end of each file and reconstructs the full text.
# Use only the functions we have studied: len, split, del, append, etc. You are allowed to use the
# function strip if needed.
# The two input text file names are provided as command-line arguments. The output file name is
# hard-coded in the Python script
# 
# example invocation and output:
#debian@beaglebone:~$ python3 reconstructSentence.py input1.txt input2.txt
#list1 is: ['Molloy.', 'by', 'Second', 'Embedded', 'Building', 'Techniques', 'Tools', 'Exploring', 'the',
#'site', 'the', 'This\n']
#list1Length: 12
#list2 is: ['Derek', 'Edition', 'Linux', 'with', 'for', 'and', 'BeagleBone:', 'book', 'for', 'companion',
#        'is\n']
#list2Length: 11
#The list out is: ['This', 'is', 'the', 'companion', 'site', 'for', 'the', 'book', 'Exploring', 'BeagleBone:',
#        'Tools', 'and', 'Techniques', 'for', 'Building', 'with', 'Embedded', 'Linux', 'Second', 'Edition', 'by',
#        'Derek', 'Molloy.']

import sys

def main():
    count = 0
    f1 = open(sys.argv[1])
    f2 = open(sys.argv[2])
    f3 = open("output.txt","w")
    out = []
    
    for line1 in f1.readlines():
        list1 = line1.split()
        list1Length = len(list1)
    for line2 in f2.readlines():
        list2 = line2.split()
        list2Length = len(list2)

    n1 = list1Length
    n2 = list2Length
    if (list1Length > list2Length):
        while n1 > 0:
            if (n2 != 0):
                out.append(list1[n1-1])
                out.append(list2[n2-1])
            else: 
                out.append(list1[n1-1])
                break
            n1=n1-1
            n2=n2-1
    else:
        while n2 > 0:
            if (n1 != 0):
                out.append(list1[n1-1])
                out.append(list2[n2-1])
            else:
                break
            n1=n1-1
            n2=n2-1

    print("list1 is: ", list1)
    print("list1Length: ", list1Length)
    print("\n")
    print("list2 is: ", list2)
    print("list2Length: ", list2Length)
    print("\n")
    print("The list out is: ", out) 

    f3.writelines([str(i)+' ' for i in out])
    f3.close()

main()

