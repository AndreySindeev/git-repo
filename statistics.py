#path to logfile with statistics test
file_name = r"/home/andrey/logfile.log"
var = []
#templates by which the script outputs information to another file
phrases = ["Scenario statistics",
           "Total scenarios attempted",
           "Total scenarios succeeded",
           "Total scenarios failed",
           "Total scenarios aborted" ]

with open(file_name) as f:
    f = f.readlines()

for line in f:
    for phrase in phrases:
        if phrase in line:
            var.append(line)
            break

#I make a line from the list to write to a file
myString = '__'.join(var)

output_file = open('/home/andrey/output.txt', 'w')
output_file.write(myString)

