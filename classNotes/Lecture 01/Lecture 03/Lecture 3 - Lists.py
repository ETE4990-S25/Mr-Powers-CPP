#!/usr/bin/env python
# coding: utf-8

# # Lists

# Refresher: What Is a List? 
# 
# A list is a collection of items.  A list can include anything you want and do not need to be related in any way.
# 
# Lists are normaly more than one element.

# In[1]:


aList = [1, 2, 3, "word1", "word2"]


# In[2]:


print(aList)


# ## Accessing Elements in a List
# 
# Since lists are a collection of elements you want to access the information in that list. To do that you use what is called the index.
# 
# In python Lists start at index 0 

# In[3]:


print(aList[0])


# You are able to perform all the same action of a list as you would just using the information at that indexed location

# In[4]:


aList[3].title()


# In[5]:


aList[1] + aList[2]


# In[6]:


aList[1] + aList[3]


# In[7]:


aList[4] + aList[3]


# In[8]:


print(aList[-1])


# In[10]:


print("My list contains the following at index 3:", aList[3], aList[3])


# # Testing Multiple conditions
# 
# The if-elif-else chain is widly use. 
# 
# An if-elif-else is looking to satisfy one condition and once found it skips the rest of the tests. 
# 
# 
# 

# In[16]:


brands = [ ["Jeep", "BMW"], "Audi", "Kia"]


# In[17]:


if "BMW" in brands:
    print("BMW is in brands")
elif "Jeep" in brands:
    print ("Jeep is in brands")
else:
    print ("Audi is in brands")


# Sometimes we need to check if there are more than one condition. 
# 
# To do this you remove the elif or else blocks. This helps when looking for more than one condition to be True.

# In[18]:


if "BMW" in brands:
    print("BMW is in brands")
if "Jeep" in brands:
    print ("Jeep is in brands")
if "Audi" in brands:
    print ("Audi is in brands")



# As you can see all of the if statments have been ran.

# In[21]:


if "BMW" in brands:
    print("BMW is in brands", end = " ")
if "Jeep" in brands:
    print ("Jeep is in brands", end = " ")
if "Subaru" in brands:
    print ("Subaru is in brands")
else:
    print("Subaru is not in brans", end = " ")



# ## Changing, Adding, and Removing Elements
# 
# Lists that you create will be dynamic. You will add, remove, and minipulate the list.
# 
# ## Modifying a List
# Modifying a list is very simple. The syntax for modifying is the same as accessing the list.

# In[86]:


brands = ["BMW", "Jeep", "Audi", "Kia"]


# In[23]:


brands[7] = "Honda"


# In[63]:


brands = []
#brands.count(1)


# In[47]:


print(brands)


# In[64]:


brands.append("Honda")


# In[65]:


brands.append("BMW")
brands.append("Jeep")
brands.append("Audi")


# While the above code looks a little strange this is very common way to build a list because we often won't know the data that will be sent to us. 
# 
# ## Inserting
# Another way to add information to a list is by Inserting the elements

# In[77]:


brands.insert(3, "Toyota")
brands[3]= "hello"
brands


# ## Removing
# There are many ways to remove an item from a list. 
#     
#     Note: While obvious remember once an item has been removed it can no longer be accessed
# 
# ### If you know the index: 
# 

# In[49]:


del brands()


# ### Using the pop() Method
# 
# The pop() Method will remove an item from the list then allow you to use it. 
# 
# The pop method removes the last item in the list but lets you work with that item after removing it. 
# 
# Think of a pez despenser, and the candy pops out of the stack. In a list the tops of the stack is the last item of the list. 

# In[60]:


brands = [["BMW", "Jeep"], "Audi", "Kia"]


# In[58]:


popped_brands = brands.pop(2)
print(brands)
print(popped_brands)


# In[62]:


#popped_brands = brands.pop(1) # you can also pop at an index
#print(popped_brands)
print(type(brands[0]))


# ## Removing by item value
# 
# you may not know the location of an item you want to remove but you know its value.

# In[88]:


#brands.remove("Toyota")
print(brands) #what do you think happens if I do this again?


# In[113]:


brands = [["BMW", "Jeep"], "Audi", "Kia"]


# In[95]:


disliked_brands = ["BMW", "Jeep"]
brands.remove(disliked_brands)
brands


# # Will this work?

# In[100]:


brands = ["BMW", "Jeep", "Audi", "Kia"]


# In[101]:


disliked_brands = ["BMW", "Jeep"]
brands.remove(disliked_brands)


# In[99]:


disliked_brands
print(type(disliked_brands))


# In[105]:


def disliked_brands (aList):
    global brands
    for i in aList:
        brands.remove(i)


# In[107]:


brands = ["BMW", "Jeep", "Audi", "Kia"]
disliked_brands(["J","BMW"])
print(brands)


# # Organizing a List
# 
# Often you will need to organize a list due to not being able to control its order. This is called Sorting.

# In[108]:


favorite_numbers = [2, 4, 7, 1, 6, 3]

favorite_numbers.sort()
print(favorite_numbers)


# In[109]:


favorite_numbers.sort(reverse=True) #the sort method also takes arguments
print(favorite_numbers)


# In[110]:


print("this is temporarily sorted:", sorted(favorite_numbers))
print(favorite_numbers)


# In[111]:


favorite_numbers = [2, 4, 7, 1, 6, 3]
favorite_numbers.reverse()
print(favorite_numbers)


# ## Length of a list
# 
# to quickly find the length of a list use use the len

# In[115]:


print(len(favorite_numbers))
print(len(brands))
brands


# Knowing the length of you list will help you to reduce the odds of reciving an index Error

# In[116]:


print(favorite_numbers[6])


# ## Other ways to create a List

# In[117]:


numbers = list(range(1,6)) #if we need a quick list of numbers you can use this
print(numbers)


# In[118]:


numbers = list(range(1,14,3)) # Or you can perfrom the following (Start, end, add)
print(numbers)


# In[119]:


numbers = numbers*numbers


# In[120]:


squares = numbers**2 


# In[121]:


squares = []
for i in range(1,11):
    squares.append(i**2) # what is wrong here
print(squares)


# ## Simple operators

# In[122]:


print(min(numbers))
print(max(numbers))
print(sum(numbers))


# In[123]:


square = [i**2 for i in range(1,11)] # here is another way to perform the same action as above
print(square)


# # Slicing a list
# To make a slice of a list all you need to do is include the index of the list.

# In[124]:


square[3:5]


# In[126]:


square[1:]


# In[128]:


square[1:3,5:7] #will not work 


# As you can see above we do not recive the end index.

# ## Copying a list
# In many cases you will need to copy a list as you do not want to edit an exsiting list (or posible tuple) so you will need to copy the contents.

# In[129]:


print(square)
bak_square = square


# In[130]:


bak_square[1] = 0 # will this work?
print(square)


# In[131]:


bak_square is square


# As you can see from above bak_square is square to make it more clear.

# In[132]:


hex(id(bak_square))


# In[133]:


hex(id(square))


# In[134]:


bac_square = square[:]
bac_square is square


# In[135]:


bac_square.append("hello")
print(bac_square)


# In[136]:


print(square)


# In[137]:


del square[] = 0


# In[139]:


get_ipython().system('jupyter nbconvert --to script "Lecture3 - Lists.ipynb"')


# In[ ]:




