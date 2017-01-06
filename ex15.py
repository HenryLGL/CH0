from sys import argv#quote the module

script, filename = argv#unpacking

txt = open(filename)#open the file

print ("Here's your file %r:" % filename)
print (txt.read())



print (txt.close())

