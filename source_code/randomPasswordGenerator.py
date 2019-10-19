import random as r

is_lower_ascii = True
is_upper_ascii = not True
is_number = True
is_symbol = True
string_length = 20

lower_ascii_list = [chr(x) for x in range(ord('a'),ord('z')+1)]
upper_ascii_list = [chr(x) for x in range(ord('A'),ord('Z')+1)]
number_list = [str(x) for x in range(0,10)]
symbol_list = ['~','!','@','#','$','%','^','&','*','-','_','=','+','?',',','.','(',')','[',']',':',';','"',"'"]

enable_list = []
result = ""

if(is_lower_ascii):
    enable_list += lower_ascii_list
if(is_upper_ascii):
    enable_list += upper_ascii_list
if(is_number):
    enable_list += number_list
if(is_symbol):
    enable_list += symbol_list

for i in range(string_length):
    result += r.choice(enable_list)

print(result)

