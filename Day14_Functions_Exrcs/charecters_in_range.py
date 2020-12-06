#def convert_to_ascii(char):
#
# ch = input("Enter any character: ")
#
# print("The ASCII value of char " + ch + " is: ",ord(ch))
#
# chr(104)

char1=input()
char2=input()

char1_asci=ord(char1)
char2_asci=ord(char2)



for i in range (char1_asci+1,char2_asci,1):
    print(chr(i), end=" ")