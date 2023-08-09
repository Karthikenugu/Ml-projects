#!/usr/bin/env python
# coding: utf-8

# ## Importing the necessary libraries

# In[1]:


from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox


# ## Create the main window

# In[2]:


root = Tk()
root.title('Language Translator')
root.geometry('870x320')
root.configure(bg='#C4DFDF')


# ## Adding colors to the GUI

# In[3]:


primary_color = 'black'
secondary_color = '#E3F4F4'


# ## Translate fucntion to translate the text and display the translated function

# In[4]:


def translate():
    translated_text.delete(1.0, END)

    try:
        original_lang = original_combo.get()
        translated_lang = translate_combo.get()

        words = textblob.TextBlob(original_text.get(1.0, END))

        words = words.translate(from_lang=original_lang, to=translated_lang)

        translated_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)


# ## Interchange fucntion to interchange the langugaes easily 

# In[5]:


def interchange():  
    original_value = original_combo.get()
    translate_value = translate_combo.get()

    original_combo.set(translate_value)
    translate_combo.set(original_value)

    original_text_value = original_text.get(1.0,END)
    translated_text_value = translated_text.get(1.0,END)

    original_text.delete(1.0,END)   
    translated_text.delete(1.0,END)

    original_text.insert(1.0, translated_text_value)
    translated_text.insert(1.0, original_text)


# ## Clear function to clear the text with a single click

# In[6]:


def clear():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)


# In[7]:


languages = googletrans.LANGUAGES
language = ['te', 'en']


# ## Create a frame for the original text

# In[8]:


original_text = Text(root, height = 10, width = 40)
original_text.grid(row = 0, column = 0, padx = 10, pady = 20)


# ## Translate Button for calling the translate function

# In[9]:


translate_button = Button(root,text='Translate', font=("Times New Roman",24),command=translate,bg=secondary_color, fg=primary_color)
translate_button.grid(row=0,column=1,padx=5)


# ## Interchange button for calling the interchange function

# In[10]:


interchange_button = Button(root,text="< -- >",font=("Times New Roman",12),command=interchange,bg=secondary_color, fg=primary_color)
interchange_button.grid(row=1,column=1,padx=10)


# ## Create a frame for the translation text

# In[11]:


translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0,column=2,padx=10,pady=20)


# ## Create a combo for drop-down to select the languages

# In[12]:


original_combo = ttk.Combobox(root, width=50, value=['en', 'te'])
original_combo.current(0)
original_combo.grid(row=1, column=0)

translate_combo = ttk.Combobox(root, width=50, value=['en', 'te'])
translate_combo.current(1)
translate_combo.grid(row=1, column=2)


# ## Create a clear button for clearing the text

# In[13]:


clear_text = Button(root,text="Clear",font=("Times New Roman",16),command=clear,bg=secondary_color, fg=primary_color)
clear_text.grid(row=3,column=1, padx=15)


# 

# In[14]:


root.mainloop()


# In[ ]:




