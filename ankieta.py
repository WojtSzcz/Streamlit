import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


    


df =  pd.read_csv("35__welcome_survey_cleaned.csv", sep=";")
df_pl_descr = df.copy()

df_pl_descr.rename(columns={
    "age": "Przedział wiekowy",
    "edu_level": "Wykształcenie",
    "fav_animals": "Ulubione zwierzę",
    "fav_place": "Ulubione miejsce",
    "gender": "Płeć",
    "hobby_art": "hobby sztuka",
    "hobby_books": "hobby książki",
    "hobby_movies": "hobby filmy",
    "hobby_other": "hobby inne",
    "hobby_sport": "hobby sport",
    "hobby_video_games": "hobby gry wideo",
    "industry": "Branża",
    "learning_pref_books": "preferowany sposób nauki książki",
    "learning_pref_chatgpt": "preferowany sposób nauki chatgpt",
    "learning_pref_offline_courses": "preferowany sposób nauki kursy offline",
    "learning_pref_online_courses": "preferowany sposób nauki kursy online",
    "learning_pref_personal_projects": "preferowany sposób nauki projekty osobiste",
    "learning_pref_teaching": "preferowany sposób nauki nauczanie",
    "learning_pref_teamwork": "preferowany sposób nauki praca zespołowa",
    "learning_pref_workshops": "preferowany sposób nauki warsztaty",
    "motivation_career": "motywacja kariera",
    "motivation_challenges": "motywacja wyzwania",
    "motivation_creativity_and_innovation": "motywacja kreatywność i innowacje",
    "motivation_money_and_job": "motywacja pieniądze i praca",
    "motivation_personal_growth": "motywacja rozwój osobisty",
    "motivation_remote": "motywacja praca zdalna",
    "sweet_or_salty": "Słony czy słodki",
    "years_of_experience": "Lata doświadczenia"
}, inplace=True)









st.title('Ankieta uczestników kursu')
num_rows = len(df)
#st.subheader("Ilość uczestników: {num_rows}") - nie działa
st.markdown(f"**Ilość uczestników ankiety:** {num_rows}")


st.text("Przykładowe rekordy w data frame:")
st.dataframe(df_pl_descr.sample(5), hide_index=True)

st.text("Informacja jeset przeważnie pełna. Brakujące rekordy odnoszą się do **branża**  oraz prefejencji **słony czy słodki** i **ulubione miejsce**. Zobacz poniżej:" )


missing_values = df_pl_descr.isnull().sum()
df_missing = pd.DataFrame(missing_values[missing_values > 0])

df_missing.columns = ['Ilość brakujących wartości']
st.dataframe(df_missing)

st.markdown(f"  > Duża ilość brakujących rekordów w **Branża** może sugerować nieuwzględnienie istotnych branż w przypadku listy wyboru, lub niezastosowanie listy wyboru ")

unique_values = df['industry'].unique()
st.write(unique_values)




#wykres pie chart

df['industry'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)

fig, ax = plt.subplots()
df['industry'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)


plt.title('Rozkład procentowy Branża')
plt.ylabel('')  
st.pyplot(fig)

#wykres pie chart be IT
df_no_it = df[df['industry'] != 'IT']
fig, ax = plt.subplots()
df_no_it['industry'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
plt.title('Rozkład procentowy Branża bez IT')
plt.ylabel('')
st.pyplot(fig)





#Tutaj rozpoznajemy wartości w przedzialach wieku 

st.title('Wykształcenie i hobby  w wybranym przedziale wieku')


age_range = st.selectbox('Wybierz przedział wiek:', ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>=65'])
df_filtered = df[df['age'] == age_range]

# Dla poziomu edukacji 
value_counts = df_filtered['edu_level'].value_counts()
fig, ax = plt.subplots()
value_counts.plot(kind='bar', ax=ax)
ax.set_title(f'Poziom edukacji: {age_range}')
ax.set_xlabel('')
ax.set_ylabel('Ilość')
st.pyplot(fig)





# Dla hobby
hobby_columns = [
    'hobby_art', 'hobby_books', 'hobby_movies', 'hobby_other', 
    'hobby_sport', 'hobby_video_games'
]

hobby_names = {
    'hobby_art': 'Hobby: Sztuka',
    'hobby_books': 'Hobby: Książki',
    'hobby_movies': 'Hobby: Filmy',
    'hobby_other': 'Hobby: Inne',
    'hobby_sport': 'Hobby: Sport',
    'hobby_video_games': 'Hobby: Gry wideo'
}


presence_counts = df_filtered[hobby_columns].apply(lambda x: (x == 1).sum(), axis=0)
presence_counts.rename(hobby_names, inplace=True)
fig, ax = plt.subplots()
presence_counts.plot(kind='bar', ax=ax, color='lightgreen')
ax.set_title(f'Popularne hobby dla grupy wiekowej: {age_range}')
ax.set_xlabel('Hobby')
ax.set_ylabel('Ile rekordow')


st.pyplot(fig)
