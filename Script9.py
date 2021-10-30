#Tarea 9#
flag = open('flag.txt','r')
print(flag.read())
flag.close()
flag_modified = open('flag.txt','a')
flag_modified.write("Esta línea es nueva!!!")
flag_modified = open('flag.txt','r')
print(flag_modified.read())
flag_modified.close()