import glob

#use this line to filter out the files you are interested in
interesting_files = glob.glob("*out.csv") 

header_saved = False
with open('salaries.csv','wb') as fout:
    for filename in interesting_files:
        with open(filename) as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            for line in fin:
                fout.write(line)
print "Done"
