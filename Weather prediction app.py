#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[17]:


import requests
import re  # For extracting temperature from the text response

# Asking the user to input the location (city or region)
location = input("Enter the location (city or region): ")

# Passing entered location to the URL to get weather data
url = 'https://wttr.in/{}?m&n=5'.format(location)
res = requests.get(url)

# Printing chematic weather details of the location
print(res.text)

# Extracting temperature from the weather response using regex
temperature_pattern = r'(-?\d+)\s*°C'  # Regex to match temperature in °C
temperature_match = re.search(temperature_pattern, res.text)

if temperature_match:
    temperature = int(temperature_match.group(1))
    print(f"Current Temperature in {location}: {temperature}°C")

    # Determine if the day is hot or cold based on temperature
    if temperature > 30:
        print("It's a hot day!")
    elif temperature < 15:
        print("It's a cold day!")
    else:
        print("The weather is moderate.")
else:
    print("Could not extract the temperature.")



# In[ ]:




