__author__ = 'karthikb'


input_file = 'Data\\Code Jam\\B-large-practice.in'
out_file = 'Data\\Code Jam\\B-large-practice.out'
f = open(input_file)
out_file = open(out_file,'w')
n = f.next()
for count,line in enumerate(f):
    words = line.split()

    result = ' '.join([word for word in words[::-1]])
    out_file.write('Case #'+str(count+1)+': '+result+'\n')


