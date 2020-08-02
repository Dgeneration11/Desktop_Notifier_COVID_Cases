#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier


# In[10]:


header  = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
html = urlopen(req)


# In[11]:


html.status


# In[12]:


obj = bs(html)


# In[44]:


No_of_New_Cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]


# In[45]:


No_of_Deaths = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]


# In[ ]:





# In[49]:


notifier = ToastNotifier()


# In[50]:


message = "New Cases - "+No_of_New_Cases+"\nDeaths - "+No_of_Deaths


# In[51]:


message


# In[56]:


notifier.show_toast(title="COVID - 19 Live Update", msg = message, duration = 5, icon_path =r"virus1.ico" )


# In[ ]:




