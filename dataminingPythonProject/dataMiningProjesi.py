import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df= pd.read_csv("C:/Users/ezgie/OneDrive/Masaüstü/dataminingPythonProject/AB_NYC_2019.csv")
df.info()

df.head(10)

#Im not going to work with the whole data so i filter the colmns i want to work with
selected_columns = ['host_id', 'neighbourhood_group', 'neighbourhood', 'room_type', 'price', 'number_of_reviews', 'reviews_per_month']
newdf = df[selected_columns]

# I'm counting the datas in neighbourhood_group 
neighbourhood_group_counts = newdf["neighbourhood_group"].value_counts()
# neighbourhood_group Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(neighbourhood_group_counts, labels=neighbourhood_group_counts.index, startangle=140,
        colors=["#48516E","#F4F4F4", "#9AAEC4", "#5B4D47", "#C6A687","#F4F4F4"])
plt.title("Neighbourhood Group Distribution")
plt.show()

# I'm counting the data in neighbourhood column
neighbourhood_counts = newdf["neighbourhood"].value_counts()
top_neighbourhoods = neighbourhood_counts.head(30)
# Neighbourhood Bar Chart
plt.figure(figsize=(10, 10))
plt.bar(top_neighbourhoods.index, top_neighbourhoods.values, color="#9AAEC4")
plt.title("Neighbourhood Distribution")
plt.ylabel("Number of Housings")
plt.xticks(rotation=45, ha="right")
plt.subplots_adjust(bottom=0.3, left=0.1, right=0.9, top=0.9)
plt.show()

# I'm counting the datas in room_type 
room_type_counts = newdf["room_type"].value_counts()

# room_type Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(room_type_counts, labels=room_type_counts.index, startangle=140,
        colors=["#B3534A", "#C4ACC0", "#A5C694"])
plt.title("Room Type Distribution")
plt.show()


host_id_counts = newdf["host_id"].value_counts()
filtered_host_ids = host_id_counts[host_id_counts >= 2]
print("The number of hosts that who has more than 2 housings in the system:")
print(filtered_host_ids.count())

filtered_host_ids = host_id_counts[host_id_counts >= 10]
print("The number of hosts that who has more than 10 housings in the system:")
print(filtered_host_ids.count())

filtered_host_ids = host_id_counts[host_id_counts >= 20]
print("The number of hosts that who has more than 20 housings in the system:")
print(filtered_host_ids.count())

print("The host who has the most housings in the system:")
print(host_id_counts.head(1))

#I want to see avarage prices for Manhattan
manhattan_data = newdf[newdf["neighbourhood_group"] == "Manhattan"]
#Calculating mean of the price of Manhattan
mean_price = manhattan_data["price"].mean()
print(f"The mean of the price of Manhattan: ${mean_price:.2f}")
#Calculating median of the price of Manhattan
median_price = manhattan_data["price"].median()
print(f"The median of the price of Manhattan: ${median_price:.2f}")

#I want to see avarage prices for Brooklyn
brooklyn_data = newdf[newdf["neighbourhood_group"] == "Brooklyn"]
#Calculating mean of the price of Brooklyn
mean_price = brooklyn_data["price"].mean()
print(f"The mean of the price of Brooklyn: ${mean_price:.2f}")
#Calculating median of the price of Brooklyn
median_price = brooklyn_data["price"].median()
print(f"The median of the price of Brooklyn: ${median_price:.2f}")

#I want to see avarage prices for Queens
queens_data = newdf[newdf["neighbourhood_group"] == "Queens"]
#Calculating mean of the price of Queens
mean_price = queens_data["price"].mean()
print(f"The mean of the price of Queens: ${mean_price:.2f}")
#Calculating median of the price of Queens
median_price = queens_data["price"].median()
print(f"The median of the price of Queens: ${median_price:.2f}")

#I want to see avarage prices for Bronx
bronx_data = newdf[newdf["neighbourhood_group"] == "Bronx"]
#Calculating mean of the price of Bronx
mean_price = bronx_data["price"].mean()
print(f"The mean of the price of Bronx: ${mean_price:.2f}")
#Calculating median of the price of Bronx
median_price = bronx_data["price"].median()
print(f"The median of the price of Bronx: ${median_price:.2f}")

#I want to see avarage prices for Staten Island
statenisland_data = newdf[newdf["neighbourhood_group"] == "Staten Island"]
#Calculating mean of the price of Staten Island
mean_price = statenisland_data["price"].mean()
print(f"The mean of the price of Staten Island: ${mean_price:.2f}")
#Calculating median of the price of Staten Island
median_price = statenisland_data["price"].median()
print(f"The median of the price of Staten Island: ${median_price:.2f}")

#I want to see avarage number of reviews for Manhattan
avg_review_manhattan= manhattan_data["number_of_reviews"].mean()
print(f"Mean of number of reviews for Manhattan: {avg_review_manhattan:.1f}")

#I want to see avarage number of reviews for Brooklyn
avg_review_brooklyn= brooklyn_data["number_of_reviews"].mean()
print(f"Mean of number of reviews for Brooklyn: {avg_review_brooklyn:.1f}")

#I want to see avarage number of reviews for Queens
avg_review_queens= queens_data["number_of_reviews"].mean()
print(f"Mean of number of reviews for Queens: {avg_review_queens:.1f}")

#I want to see avarage number of reviews for Bronx
avg_review_bronx= bronx_data["number_of_reviews"].mean()
print(f"Mean of number of reviews for Bronx: {avg_review_bronx:.1f}")

#I want to see avarage number of reviews for Staten Island
avg_review_statenisland= statenisland_data["number_of_reviews"].mean()
print(f"Mean of number of reviews for Staten Island: {avg_review_statenisland:.1f}")


roomtype_counts = manhattan_data["room_type"].value_counts()
# Room Types In Manhattan Bar Chart
plt.figure(figsize=(6, 6))
plt.bar(roomtype_counts.index, roomtype_counts.values, color="#B3534A")
plt.title("Room Type Distribution In Manhattan")
plt.ylabel("Number of Room Types")
plt.xticks(rotation=45, ha="right")
plt.subplots_adjust(bottom=0.3, left=0.2, right=0.9, top=0.9)
plt.show()

roomtype_counts = brooklyn_data["room_type"].value_counts()
# Room Types In Brooklyn Bar Chart
plt.figure(figsize=(6, 6))
plt.bar(roomtype_counts.index, roomtype_counts.values, color="#C4ACC0")
plt.title("Room Type Distribution In Brooklyn")
plt.ylabel("Number of Room Types")
plt.xticks(rotation=45, ha="right")
plt.subplots_adjust(bottom=0.3, left=0.2, right=0.9, top=0.9)
plt.show()

roomtype_counts = queens_data["room_type"].value_counts()
# Room Types In Manhattan Bar Chart
plt.figure(figsize=(6, 6))
plt.bar(roomtype_counts.index, roomtype_counts.values, color="#9AAEC4")
plt.title("Room Type Distribution In Queens")
plt.ylabel("Number of Room Types")
plt.xticks(rotation=45, ha="right")
plt.subplots_adjust(bottom=0.3, left=0.2, right=0.9, top=0.9)
plt.show()

roomtype_counts = bronx_data["room_type"].value_counts()
# Room Types In Bronx Bar Chart
plt.figure(figsize=(6, 6))
plt.bar(roomtype_counts.index, roomtype_counts.values, color="#9AAEC4")
plt.title("Room Type Distribution In Bronx")
plt.ylabel("Number of Room Types")
plt.xticks(rotation=45, ha="right")
plt.subplots_adjust(bottom=0.3, left=0.2, right=0.9, top=0.9)
plt.show()

roomtype_counts = statenisland_data["room_type"].value_counts()
# Room Types In Staten Island Bar Chart
plt.figure(figsize=(6, 6))
plt.bar(roomtype_counts.index, roomtype_counts.values, color="#BAA8EF")
plt.title("Room Type Distribution In Staten Island")
plt.ylabel("Number of Room Types")
plt.xticks(rotation=45, ha="right")
plt.subplots_adjust(bottom=0.3, left=0.2, right=0.9, top=0.9)
plt.show()

