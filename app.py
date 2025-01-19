
import streamlit as st
import pandas as pd 
from time import sleep


st.title('refresh cycle!')
# country = st.selectbox('wybierz kraj', ['Polska','Niemcy', 'Francja'])


# df = pd.read_csv("population_gdp_data.csv")

# c0, c1 = st.columns(2)

# sleep(1)
# with c0:
#     if country:
#         st.image(
#             f"{country.lower()}_kultura.webp", 
#             use_container_width=True,
#             )


# country_df = df[df["Kraj"] == country]

# sleep(1)
# with c1:
#     st.dataframe(
#         country_df, 
#         use_container_width=True, 
#         hide_index=True,
#     )

# what = st.selectbox('Co narysować?', ['PKB', 'Populacja'])

# sleep(1)
# st.bar_chart(data=country_df, x="Rok", y=what)