#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import pyarrow


# In[3]:


import pandas as pd
from sqlalchemy import create_engine

def load_store_data():
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"

    try:
        engine = create_engine(
            "postgresql+psycopg2://admin:admin123@localhost:5432/sial_database"
        )
        print("Connection established successfully")

        df = pd.read_parquet(url)

        df.to_sql(
            name="taxi_data_set",
            con=engine,
            if_exists="replace",
            index=False
        )

        print("Your data loaded successfully")

    except Exception as e:
        print(f"Something went wrong: {e}")


load_store_data()


# In[6]:


jupyter nbconvert --to script practise.ipynb


# In[5]:


get_ipython().system(' uv add nbconvert')


# In[ ]:




