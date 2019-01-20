fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There are', count, 'subject lines in', fname)


##for line in fhand:
##    line = line.rstrip()
##    if line.startswith('From:'):
##        print(line)

##for line in fhand:
##    line = line.rstrip()
##    if line.find('@uct.ac.za') == -1: continue
##    print(line)

##print([line.rstrip() for line in fhand if line.startswith('From:')])
