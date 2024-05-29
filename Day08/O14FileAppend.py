
FA = open("myfile.txt", "a")

# txt = input("Enter the contents of the file :")
# FA.write(txt + "\n")

l1 = input("Enter the contents of the file :")
l2 = input("Enter the contents of the file :")
l3 = input("Enter the contents of the file :")

FA.writelines([l1 , "\n", l2+"\n", l3+"\n"])

FA.close()
