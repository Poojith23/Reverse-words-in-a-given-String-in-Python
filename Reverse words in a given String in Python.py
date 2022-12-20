#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Python code
# To reverse words in a given string
 
# input string
string = "How are you?"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
    # apending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))


# In[4]:


# Function to reverse words of string
 
def rev_sentence(sentence):
 
    # first split the string into words
    words = sentence.split(' ')
 
    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))
 
    # finally return the joined string
    return reverse_sentence
 
if __name__ == "__main__":
    input = 'Hello everyone welcome to github'
    print (rev_sentence(input))


# In[ ]:




