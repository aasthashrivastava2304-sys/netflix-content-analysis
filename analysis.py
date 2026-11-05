import pandas as pd # pandas bulao, naam pd rakho
import matplotlib.pyplot as plt   # chart banane wala tool bulao, naam plt rakho
df = pd.read_csv("netflix_titles.csv") # CSV padh ke table banao
print(df.shape)  # rows aur columns kitne hain size ke liye
print(df.head()) # pehli 5 rows andar data kaisa hai
print(df.columns) # column ke naam
print(df.isnull().sum())  # har column mein kitni values khali hain
print(df["type"].value_counts())  # Movie aur TV Show kitne hain

# data cleaning 

df = df.dropna(subset = ["country"])  # jinki country khali hai, sirf wo rows hatao
df ["main_country"] = df["country"].str.split(",").str[0] # country ko comma pe todo, pehli country naye column mein
df["main_genre"] = df["listed_in"].str.split(",").str[0]  # genre ko comma pe todo, pehla genre naye column mein
print(df.shape)   # cleaning ke baad rows aur column
print(df[["country", "main_country", "listed_in", "main_genre"]].head())   # purane aur naye columns saath mein

# insights ----------

total = len(df)                 # cleaning ke baad kitne titles bache
counts = df["type"].value_counts()   # Movie aur TV Show ki ginti

print("Total titles:", total)
print("Movies:", counts["Movie"])
print("TV Shows:", counts["TV Show"])
print("Movies %:", round(counts["Movie"] / total * 100, 1))   # movies kitne percent hain
print("Countries:", df["main_country"].nunique())   # kitne alag-alag desh
print("Top genre:", df["main_genre"].value_counts().idxmax())   # sabse zyada wala genre


# chart 1 : movies vs tv shows 
plt.figure(figsize=(6,6)) # chart kisize
plt.pie(counts , labels = counts.index , autopct = "%1.1f%%") # pie chart , saath mein percent
plt.title("Movies vs TV Shows") # chart ka title
plt.savefig("chart1_movies_vs_tv.png")
plt.show() # chart screen par dikhao

# ---------- Chart 2: Top 10 countries ----------

top_countries = df["main_country"].value_counts().head(10)   # har country ki ginti, sirf top 10

plt.figure(figsize=(10, 6))                          # chart ki size
plt.bar(top_countries.index, top_countries.values)   # bar chart: naam neeche, ginti upar
plt.title("Top 10 Countries")                        # chart ka title
plt.xlabel("Country")                                # neeche wali line ka naam
plt.ylabel("Number of titles")                       # side wali line ka naam
plt.xticks(rotation=45, ha="right")                  # naam tirche karo taaki overlap na ho
plt.tight_layout()                                   # sab kuch window mein fit karo
plt.savefig("chart2_top_countries.png")
plt.show()                                           # chart dikhao

# ---------- Chart 3: Top 10 genres ----------

top_genres = df["main_genre"].value_counts().head(10)   # har genre ki ginti, sirf top 10

plt.figure(figsize=(10, 6))                             # chart ki size
plt.barh(top_genres.index, top_genres.values)           # lete hue (horizontal) bars
plt.title("Top 10 Genres")                              # chart ka title
plt.xlabel("Number of titles")                          # neeche wali line ka naam
plt.ylabel("Genre")                                     # side wali line ka naam
plt.gca().invert_yaxis()                                # sabse bada genre upar rakho
plt.tight_layout()                                      # sab kuch window mein fit karo
plt.savefig("chart3_top_genres.png")
plt.show()                                              # chart dikhao

# ---------- Chart 4: Titles by release year ----------

yearly = df["release_year"].value_counts().sort_index()   # har saal ki ginti, saal ke order mein

plt.figure(figsize=(10, 6))                  # chart ki size
plt.plot(yearly.index, yearly.values)        # line chart: saal neeche, ginti upar
plt.title("Titles by Release Year")          # chart ka title
plt.xlabel("Release year")                   # neeche wali line ka naam
plt.ylabel("Number of titles")               # side wali line ka naam
plt.tight_layout()                           # sab kuch window mein fit karo
plt.savefig("chart4_release_year.png")       # chart ko image file mein save karo
plt.show()                                   # chart dikhao
