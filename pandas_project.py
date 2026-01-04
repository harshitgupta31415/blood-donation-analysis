#AFTER EDITING BY AI 
# NOTE:- yet to learn matplotlib and seaborn 
# =============================================================
# PROJECT: BLOOD DONATION ANALYSIS
# Dataset Source:
# https://www.kaggle.com/datasets/tarekmasryo/blood-donor-registry-dataset
#
# Objective:
# - Clean and explore blood donor data
# - Aggregate donor behavior by blood type
# - Visualize key patterns for insights
# =============================================================


# -------------------------------------------------------------
# STEP 1: IMPORT REQUIRED LIBRARIES
# -------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# -------------------------------------------------------------
# STEP 2: LOAD DATA INTO DATAFRAME
# -------------------------------------------------------------
# Read the CSV file into a pandas DataFrame
df = pd.read_csv("./blood_donation_registry_ml_ready.csv")

print("\n------------------------------------------------------------\n")
print("< Sample rows (row index 1 to 4) >\n")
print(df.iloc[1:5])
print("\n------------------------------------------------------------\n")

print("< Dataset Information >\n")
print(df.info())
print("\n------------------------------------------------------------\n")


# -------------------------------------------------------------
# STEP 3: DATA CLEANING
# Tasks:
# - Check missing values
# - Remove duplicate rows
# -------------------------------------------------------------

# Check number of missing values in each column
# Note:
# isnull().sum() never throws an error;
# it returns 0 if no values are missing.
print("< Missing values per column >\n")
print(df.isnull().sum())
print("\n------------------------------------------------------------\n")

# Remove duplicate records to reduce bias
df.drop_duplicates(inplace=True)

print("< Dataset info after removing duplicates >\n")
print(df.info())
print("\n------------------------------------------------------------\n")

# Re-check missing values after cleaning
print("< Missing values after duplicate removal >\n")
print(df.isnull().sum())
print("\n------------------------------------------------------------\n")


# -------------------------------------------------------------
# STEP 4: DATA AGGREGATION
# Purpose:
# Summarize donor behavior by blood type
# -------------------------------------------------------------

blood_type_summary = df.groupby("blood_type").agg(
    donor_count=("donor_id", "count"),                 # Total donors
    avg_bmi=("bmi", "mean"),                           # Health indicator
    avg_donations_12m=("donation_count_last_12m", "mean"),
    regular_donor_rate=("is_regular_donor", "mean"),   # Loyalty rate
    eligibility_rate=("eligible_to_donate", "mean"),   # Readiness to donate
    avg_propensity=("donation_propensity_score", "mean"),
    future_donation_rate=("donated_next_6m", "mean")   # Target variable
).reset_index()

print("< Blood Type Summary Table >\n")
print(blood_type_summary)
print("\n------------------------------------------------------------\n")


# =============================================================
# STEP 5: FINAL 6 VISUALIZATIONS (BEST SET)
# =============================================================

# Set clean theme and palette for all graphs
sns.set_theme(style="whitegrid", palette="Set2")


# -------------------------------------------------------------
# 1️⃣ Donor Distribution by Blood Type
# Why:
# Shows which blood groups have the most donors.
# Essential for planning blood bank inventory.
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.barplot(
    data=blood_type_summary,
    x="donor_count",
    y="blood_type",
    palette="viridis"
)
plt.title("Donor Distribution by Blood Type", fontsize=14)
plt.xlabel("Number of Donors")
plt.ylabel("Blood Type")
plt.tight_layout()
plt.show()


# -------------------------------------------------------------
# 2️⃣ Future Donation Likelihood by Blood Type
# Why:
# Indicates which blood groups are most likely to donate
# in the next 6 months (important predictive insight).
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.barplot(
    data=blood_type_summary,
    x="future_donation_rate",
    y="blood_type",
    palette="coolwarm"
)
plt.title("Future Donation Likelihood by Blood Type", fontsize=14)
plt.xlabel("Probability of Donation")
plt.ylabel("Blood Type")
plt.tight_layout()
plt.show()


# -------------------------------------------------------------
# 3️⃣ Regular vs Non-Regular Donors
# Why:
# Shows donor loyalty. Regular donors are critical for
# sustainable blood supply.
# -------------------------------------------------------------
plt.figure(figsize=(8, 6))
sns.countplot(
    data=df,
    x="is_regular_donor",
    palette="Set1"
)
plt.title("Regular vs Non-Regular Donors", fontsize=14)
plt.xlabel("Donor Type (0 = Not Regular, 1 = Regular)")
plt.ylabel("Number of Donors")
plt.tight_layout()
plt.show()


# -------------------------------------------------------------
# 4️⃣ BMI Distribution by Blood Type
# Why:
# Violin plot shows full BMI distribution, density, and median.
# Helps compare health variation across blood groups.
# -------------------------------------------------------------
plt.figure(figsize=(12, 6))
sns.violinplot(
    data=df,
    x="blood_type",
    y="bmi",
    palette="Set2",
    inner="quartile"
)
plt.title("BMI Distribution Across Blood Types", fontsize=14)
plt.xlabel("Blood Type")
plt.ylabel("BMI")
plt.tight_layout()
plt.show()


# -------------------------------------------------------------
# 5️⃣ Donation Outcome in Next 6 Months (Target Variable)
# Why:
# Shows proportion of donors who donated vs did not donate.
# Pie chart makes it visually easy to understand.
# -------------------------------------------------------------
donation_counts = df["donated_next_6m"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(
    donation_counts,
    labels=["Did Not Donate", "Donated"],
    autopct="%1.1f%%",
    startangle=90,
    colors=sns.color_palette("Set2")
)
plt.title("Donation Outcome in Next 6 Months", fontsize=14)
plt.tight_layout()
plt.show()


# -------------------------------------------------------------
# 6️⃣ Eligibility Rate by Blood Type
# Why:
# Shows which blood groups have higher eligible donors.
# Useful for immediate blood collection planning.
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.barplot(
    data=blood_type_summary,
    x="eligibility_rate",
    y="blood_type",
    palette="magma"
)
plt.title("Eligibility Rate by Blood Type", fontsize=14)
plt.xlabel("Eligibility Rate")
plt.ylabel("Blood Type")
plt.tight_layout()
plt.show()




# -------------------------------------------------------------
# END OF PROJECT
# -------------------------------------------------------------




'''
INITIAL CODE BEFORE MAKING IT EDIT BY AI:

#project:- blood donation analysis
#step1: import library
#data from https://www.kaggle.com/datasets/tarekmasryo/blood-donor-registry-dataset?resource=download
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#step 2 : load data as data frame
df= pd.read_csv("./blood_donation_registry_ml_ready.csv")
print("\n\n---------------------------------------------------------------------------\n\n")
print("< row no 2 to 5 > \n\n")
print(df.iloc[ 1:5 , ], "\n\n")
print("---------------------------------------------------------------------------\n\n")
print(" < info about the csv >\n\n")
print(df.info() , "\n\n")
print("---------------------------------------------------------------------------\n\n")
#step3 : data cleaning
#handel missing value . correct data type, remove duplicate 
print(" < no. of null values in a specefic column > \n\n")
print(df.isnull().sum() , "\n\n") 
# this is used to find the sum of the column that how many in them are missing and will
#  give error is nothing is missing like all spaces are occupied or we can say "It never throws an error, it only returns zeros if no values are missing."
print("---------------------------------------------------------------------------\n\n")
print("< now droping the duplicate data  and will give info about the change >\n\n")
df.drop_duplicates(inplace=True)# this will remive all the repeating data that will make the data less biased
print(df.info(),"\n\n")
print("---------------------------------------------------------------------------\n\n")
print(" < no. of null values in a specefic column > \n\n")
print(df.isnull().sum() , "\n\n") 
# this is used to find the sum of the column that how many in them are missing after removing duplicates
print("---------------------------------------------------------------------------\n\n") 

#step4: data agrigation: group by or pivot using pandas
print("<  printing the total no. of bmi in specefic blood group i.e, no of people and average bmi of each group >\n\n")
blood_type_summary = df.groupby("blood_type").agg(
    donor_count=("donor_id", "count"),
    avg_bmi=("bmi", "mean"),
    avg_donations_12m=("donation_count_last_12m", "mean"),
    regular_donor_rate=("is_regular_donor", "mean"),
    eligibility_rate=("eligible_to_donate", "mean"),
    avg_propensity=("donation_propensity_score", "mean"),
    future_donation_rate=("donated_next_6m", "mean")
).reset_index()

print(blood_type_summary,"\n\n")

print("---------------------------------------------------------------------------\n\n") 

#step 5: visualization: like bar chart , histogram ans so on..............
plt.figure(figsize=(10,6))
sns.barplot(x="donor_count",y="blood_type",data=blood_type_summary)
plt.title("Donor count by blood type")
plt.show()


'''

