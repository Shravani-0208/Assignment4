Name = "Python"
print(Name)
print(Name[2])
print(Name[-2])
print(Name[1:4])

#Multiline String
print('Multline String')
Message = '''My name is Shravani
Python'''
print(Message)

#Compare two String
print('Comparing two strings')
Str1 = "Hello World"
Str2 = "Hello Shravani"
Str3 = "Hello World"
print(Str1 == Str2)
print(Str2 == Str3)
print(Str1 == Str3)

#Adding strings
print('Addition of strings:')
S1 = "Hello"
S2 = " Shravani"
S3 = S1+S2
print(S3)

#Iterate through Strings
print('Iterate through Strings')
String = "HELLO"
for letter in String:
    print(letter)
print('Length of String:')
print(len(String))    