from sys import argv
script, filename = argv

print ("We're going to arase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit return.")

input("? ")

print ("Opening the file...")
target = open(filename, 'w') 
#进入‘W’模式（打开一个文档若不存在则新建），因为原来的open默认是只读模式（‘r'）

print ("Truncating the file. Goodbye!")
target.truncate() 
#这货作用是清除，如果文档是新建的，没什么卵用

print ("Now I'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print ("I'm going to write these to the file.")
a = """%s \n%s \n%s \n""" %(
 line1,line2,line3) 
 #这样就可以跳过repetition啦。

target.write(a)

print ("And finally,we close it.")
target.close()