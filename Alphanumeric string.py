str="aamya8880@gmail.com"  #An alphanumeric string
ls=[]  #list of all elements in given string
ch=[]  #list of all characters in the string
dg=[]  #list of digits in the string
sc=[]  #list of special characters in the string
print(str.isalnum()) #to check whether given string is alphanumeri or not
for i in str: #iteration applied to the given string
    ls.append(i) #step to insert each elements in string into provided list
for j in ls: #iteration applied to ls list(list of elements of string)
    if j.isalpha(): #checks only alphabets in list
        ch.append(j) #inserting matched elements into appropriate list
    if j.isdigit(): #checkls only digits elements in string
        dg.append(j)
    if j not in ch and j not in dg: #checks the elements apart from alpha & digits
        sc.append(j) #inserting special characters like '@','$' etc.

print("/n Given string:",str)
print("/n list of elements:",ls)
print("/n list of characters:",ch)
print("/n list of digits:",dg)
print("/n list of special charaters",sc)



