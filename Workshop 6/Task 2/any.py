'''
Open a file names example.txt to write in the file.
Add 'Wrote this to the file' as a string. 
close the file. 
'''

f = open('example.txt', 'w')
f.write('Write this to the file.')
f.close()