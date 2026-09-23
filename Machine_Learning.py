#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


# In[5]:


x = np.array([[20], [25], [30], [35]])
y = np.array([[200], [250], [300], [350]])

model = LinearRegression()
model.fit(x,y)

w = model.coef_[0]
b = model.intercept_
print(f"Model fonud  -> Weight (w): {w}")
print(f"MOdel found -> Bias (b): {b}")
today_temp = np.array([[40]])
predicted_sales = model.predict(today_temp)
print(f"\n40°C temperature  predicted sales: {predicted_sales[0]} Ice Creams!")


# In[ ]:





# In[ ]:




