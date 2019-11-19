import time
# Write code to read the content of the text file ‘input.txt’.
# For each line in ‘input.txt’, write a new line in the new text file ‘output.txt’ that computes the answer to some operation on a list of numbers.

# Read a file
ifile = open("input.txt")
text = ifile.read().splitlines()
 
# Write a file
ofile = open("output.txt", "w")

# Calculate min
Min = "The min of", text[1].replace(":",",").split(",")[1::], "is", min(text[1].replace(":",",").split(",")[1::])


# Calculate max
Max = "The max of", text[1].replace(":",",").split(",")[1::], "is", max(text[1].replace(":",",").split(",")[1::])



total = 0
for i in (text[1].replace(":",",").split(",")[1::]):
    total += int(i)
    

# Calculate avergae
avg = "The avg of", text[1].replace(":",",").split(",")[1::], "is", total/len(text[1].replace(":",",").split(",")[1::])

# Show result
ofile.write(str(Min).replace("'","").replace(",","").replace("(","").replace(")",""))
ofile.write("\n")
ofile.write(str(Max).replace("'","").replace(",","").replace("(","").replace(")",""))
ofile.write("\n")
ofile.write(str(avg).replace("'","").replace(",","").replace("(","").replace(")",""))

ofile.close() # closes the opened file

time.sleep(50)
