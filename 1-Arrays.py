#Arrays
strings = ['a','b','c','d']
# 4*4 = 16 bytes of storage is used

print(strings[2])

#push  
strings.append('e')      # O(1)
#pop  
strings.pop() 
strings.pop()            # O(1)

#addfirstelement 
strings.insert(0,'x')    #O(n)

#splice
strings.insert(2,'alien')   #O(n)

print(strings)

#%%
#Data Structures Excercise - Revese a String

def reverse_string(text):
    text_list = list(text)
    rev_text_list = []
    print(len(text_list))
    for i in range(len(text_list)):
        rev_text_list.append(text_list[len(text_list)-i-1])
    rev_text = ''.join(rev_text_list)
    return rev_text


text = "Hello, my name is Erick"
print(text)
reversed_text = reverse_string(text)

print(reversed_text)

