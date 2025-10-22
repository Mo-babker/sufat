# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:21:37 2024

Mohamed babker Ahmed
"""
from datetime import datetime
import pandas as pd
import numpy as np
import csv 
import matplotlib.pyplot as plt
import os
import time
from tabulate import tabulate
import sys
#for decorating
def dico():
    print("\n#***************************************************#")
    return

#The answer to the "Is there another subscriber?" question.
while True:
    try:
        subscriber_count = int(input("\nHow many subscribers do you have? (Ex: 3) "))
        if subscriber_count <= 0:
            print("\nPlease make sure the value you entered is a natural number greater than zero.")
        else:
            break
    except ValueError:
        print("\nPlease make sure the value you entered is a natural number greater than zero.")

for i in range(1, subscriber_count + 1):
    print(f"\n#***************************************************#\n{i}.Subscriber:")
    if subscriber_count == 1 or subscriber_count==i:
        other_subscriber = "no"
    else:
        if subscriber_count>=i:
            other_subscriber = "yes"
            
            
        
    subscriber_type = {1: "Housing", 2: "Workplace", 3: "Public Institution", 4: "Tourist Facility"}  #Sözcük ataması yapılacağı için dictionary kullanılmalıdır.

    print(" \nOur Current Subscriber Types = (1 -> Housing, 2 -> Workplace, 3 -> Public Institution, 4 -> Tourist Facility)")


    while True:
        try:
            Subscriber = int(input(" \nEnter Your Subscriber Type Code:"))
            if Subscriber >= 5 or Subscriber <= 0:
                print(" \nYou have made an incorrect entry. Try again.")
                print(" \nOur Current Subscriber Types = (1 -> Housing, 2 -> Workplace, 3 -> Public Institution, 4 -> Tourist Facility)")
            else:
                break
        except ValueError:  # Used to prevent invalid entries (e.g., if [an invalid value] is entered)
            print("\nYou have made an incorrect entry. Try again.")

    print("\nThe type of subscription you are using: ", subscriber_type[Subscriber])

    while True:   
        try:
            previous_meter_reading = int(input("\nEnter the Previous Meter Reading: "))
            if previous_meter_reading < 0 :
                print("\nYour Meter Reading Cannot Be Less Than Zero ")
            else:
                break
        except ValueError:  
            print("\nYou have made an incorrect entry. Try again.")
    while True:
        try:
            current_meter_reading = int(input("\nEnter the Current Meter Reading: "))
            if current_meter_reading <0 :
                print("\nYour Meter Reading Cannot Be Less Than Zero ")
            elif current_meter_reading<previous_meter_reading:
                print("\nThe current meter reading cannot be less than the previous meter reading.")
            else:
                break
        except ValueError:  
            print("\nYou have made an incorrect entry. Try again.")
    while True:
        try:
            water_usage = current_meter_reading - previous_meter_reading
            if water_usage <0:
                print("\nYour current meter reading cannot be less than your previous meter reading. Try again.")
            else:
                break
        except ValueError:  
            print("\nYou have made an incorrect entry. Try again.")
        
                        
    print("\nTotal Water Consumption: ",water_usage) 


    while True:        
        while True:
            try:
                previous_date_1 = input("\nEnter the Reading Date of the Previous Meter Reading in YEAR-MONTH-DAY Format (Ex: 2024-11-25): ")
                previous_date = datetime.strptime(previous_date_1, "%Y-%m-%d")
                break
            except ValueError:  
                print("\nYou have made an incorrect entry. Try again.")
        while True:        
            try:
                current_date_1 = input("\nEnter the Reading Date of the Current Meter Reading in YEAR-MONTH-DAY Format (Ex: 2024-12-25): ")
                current_date = datetime.strptime(current_date_1 , "%Y-%m-%d")
                break
            except ValueError:  
                print("\nYou have made an incorrect entry. Try again.")
            
            
        try:
            if current_date < previous_date:
                print("\nThe current date cannot be in the past relative to the previous date. Please try again.")
            else:    
                elapsed_time = (current_date - previous_date).days
                if elapsed_time == 0:
                    print("\nThe number of elapsed days cannot be 0. Please try again.")
                else:
                    break
        except ValueError:  
            print("\nYou have made an incorrect entry. Try again.")
    dico()
    print("\nNumber of Days Elapsed Since the Last Meter Reading: ", elapsed_time) 
    monthly_water_consumption = (water_usage / elapsed_time) *30
    if monthly_water_consumption > water_usage:
        print("\nYour water usage period has not completed one month.")
        print("\nYour Water Consumption So Far: ", f"{water_usage:.2f}", "ton/s")
    else:    
        print("\nMonthly Water Consumption: ", f"{monthly_water_consumption:.2f}", " ton/s")
    if elapsed_time < 30 :
        if Subscriber == 1:
            if water_usage >= 0 and water_usage <= 13:
                fee = water_usage *2.24
                monthly_water_consumption_fee = fee
                print("\n",elapsed_time ,"Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
            elif water_usage > 13 and water_usage <= 20:
                fee = water_usage *5.78
                monthly_water_consumption_fee = fee
                print("\n",elapsed_time ,"Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
            elif water_usage > 20:
                fee = water_usage *9.33
                monthly_water_consumption_fee = fee
                print("\n",elapsed_time ,"Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
        elif Subscriber == 2:
            if water_usage > 0 and water_usage <= 10:
                fee = water_usage *7.71
                monthly_water_consumption_fee = fee
                print("\n",elapsed_time ,"Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
            elif water_usage > 10:
                fee = water_usage *8.88
                monthly_water_consumption_fee = fee
                print("\n",elapsed_time ,"Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
        elif Subscriber == 3:
            fee = water_usage *6.64
            monthly_water_consumption_fee = fee
            print("\n",elapsed_time ,"Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
        elif Subscriber == 4:
            fee = water_usage *5.78
            monthly_water_consumption_fee = fee
            print("\n",elapsed_time ,"Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
        if Subscriber == 1:
            monthly_wastewater_fee = water_usage *1.91
            print("\n",elapsed_time ,"Daily Wastewater Fee (or Charge) ", f"{monthly_wastewater_fee:.2f}","TL." )
        if Subscriber == 2:
            monthly_wastewater_fee = water_usage *3.79
            print("\n",elapsed_time ,"Daily Wastewater Fee (or Charge) ", f"{monthly_wastewater_fee:.2f}","TL." )
        if Subscriber == 3:
            monthly_wastewater_fee = water_usage *2.56
            print("\n",elapsed_time ,"Daily Wastewater Fee (or Charge) ", f"{monthly_wastewater_fee:.2f}","TL." )
        if Subscriber == 4:
            monthly_wastewater_fee = water_usage *1.91
            print("\n", elapsed_time ,"Daily Wastewater Fee (or Charge) ", f"{monthly_wastewater_fee:.2f}","TL." )
        vat_amount = (monthly_wastewater_fee + monthly_water_consumption_fee) *0.08
        print("\nTotal VAT Amount: ", f"{vat_amount:.2f}", "TL")
        invoice_amount = (monthly_wastewater_fee + monthly_water_consumption_fee + vat_amount)
        print("\n", elapsed_time,"Daily Total Invoice Amount (or Bill Amount): ", f"{invoice_amount:.2f}", "TL.")
    else:  
        if Subscriber == 1:
            if monthly_water_consumption >= 0 and monthly_water_consumption <= 13:
                fee = monthly_water_consumption *2.24
                total_water_fee = water_usage *2.24
                print("\n30 Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
                if total_water_fee != fee:
                    print("\n",elapsed_time ,"Your Total Water Consumption Fee to be Paid Daily: ", f"{total_water_fee:.2f}", "TL." )
            elif monthly_water_consumption > 13 and monthly_water_consumption <= 20:
                fee = monthly_water_consumption *5.78
                total_water_fee = water_usage *5.78
                print("\n30 Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
                if total_water_fee != fee:
                    print("\n",elapsed_time ,"Your Total Water Consumption Fee to be Paid Daily: ", f"{total_water_fee:.2f}", "TL." )
            elif monthly_water_consumption > 20:
                fee = monthly_water_consumption *9.33
                total_water_fee = water_usage *9.33
                print("\n30 Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
                if total_water_fee != fee:
                    print("\n",elapsed_time ,"Your Total Water Consumption Fee to be Paid Daily: ", f"{total_water_fee:.2f}", "TL." )
        elif Subscriber == 2:
            if monthly_water_consumption > 0 and monthly_water_consumption <= 10:
                fee = monthly_water_consumption *7.71
                total_water_fee = water_usage *7.71
                print("\n30 Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
                if total_water_fee != fee:
                    print("\n",elapsed_time ,"Your Total Water Consumption Fee to be Paid Daily: ", f"{total_water_fee:.2f}", "TL." )
            elif monthly_water_consumption > 10:
                fee = monthly_water_consumption *8.88
                total_water_fee = water_usage *8.88
                print("\n30 Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
                if total_water_fee != fee:
                    print("\n",elapsed_time ,"Your Total Water Consumption Fee to be Paid Daily: ", f"{total_water_fee:.2f}", "TL." )
        elif Subscriber == 3:
            fee = monthly_water_consumption *6.64
            total_water_fee = water_usage *6.64
            print("\n30 Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
            if total_water_fee != fee:
                print("\n",elapsed_time ,"Your Total Water Consumption Fee to be Paid Daily: ", f"{total_water_fee:.2f}", "TL." )
        elif Subscriber == 4:
            fee = monthly_water_consumption *5.78
            total_water_fee = water_usage *5.78
            print("\n30 Daily Water Consumption Fee (or Charge): ", f"{fee:.2f}","TL." )
            if total_water_fee != fee:
                print("\n",elapsed_time ,"Your Daily Total Water Consumption Fee to be Paid: ", f"{total_water_fee:.2f}", "TL." )
        if Subscriber == 1:
            monthly_wastewater_fee = monthly_water_consumption *1.91
            total_wastewater_fee = water_usage *1.91
            print("\n30 Daily Wastewater Fee (or Charge) ", f"{monthly_wastewater_fee:.2f}","TL." )
            if total_wastewater_fee != monthly_wastewater_fee:
                print("\n",elapsed_time ,"Your Daily Total Wastewater Consumption Fee to be Paid: ", f"{total_wastewater_fee:.2f}", "TL." )
        if Subscriber == 2:
            monthly_wastewater_fee = monthly_water_consumption *3.79
            total_wastewater_fee = water_usage *3.79
            print("\n30 Daily Wastewater Fee (or Charge) ", f"{monthly_wastewater_fee:.2f}","TL." )
            if total_wastewater_fee != monthly_wastewater_fee:
                print("\n",elapsed_time ,"Your Daily Total Wastewater Consumption Fee to be Paid: ", f"{total_wastewater_fee:.2f}", "TL." )
        if Subscriber == 3:
            monthly_wastewater_fee = monthly_water_consumption *2.56
            total_wastewater_fee = water_usage *2.56
            print("\n30 Daily Wastewater Fee (or Charge) ", f"{monthly_wastewater_fee:.2f}","TL." )
            if total_wastewater_fee != monthly_wastewater_fee:
                print("\n",elapsed_time ,"Your Daily Total Wastewater Consumption Fee to be Paid: ", f"{total_wastewater_fee:.2f}", "TL." )
        if Subscriber == 4:
            monthly_wastewater_fee = monthly_water_consumption *1.91
            total_wastewater_fee = water_usage *1.91
            print("\n30 Daily Wastewater Fee (or Charge) ", f"{monthly_wastewater_fee:.2f}","TL." )
            if total_wastewater_fee != monthly_wastewater_fee:
                print("\n",elapsed_time ,"Your Daily Total Wastewater Consumption Fee to be Paid: ", f"{total_wastewater_fee:.2f}", "TL." )
        vat_amount = (total_wastewater_fee + total_water_fee) *0.08
        print("\nTotal VAT Amount: ", f"{vat_amount:.2f}", "TL")
        invoice_amount = (total_wastewater_fee + total_water_fee + vat_amount)
        print("\n", elapsed_time, "Daily Total Invoice Amount (or Bill Amount) ", f"{invoice_amount:.2f}", "TL.")
            
            
# The purpose is to collect the values above and write them to a CSV file   

    file_exists = os.path.isfile("data.csv")


    with open("data.csv", mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(["Subscriber Type", "Previous Meter Reading", "Current Meter Reading", "Number of Days",\
                              "Is There Another Subscriber?", "Water Consumption Amount", "Water Consumption Fee", "Wastewater Fee", "VAT Amount", "Invoice Amount"])
        
        writer.writerow([subscriber_type[Subscriber], previous_meter_reading, current_meter_reading, elapsed_time, other_subscriber, monthly_water_consumption, fee,\
                        monthly_wastewater_fee, vat_amount, invoice_amount])
dico()
print("\nSubscriber information has been successfully added to the CSV file.")
dico()


df=pd.read_csv("data.csv")
 
# Design of the header according to the entered header name

def header(header_name):
    ba = header_name.upper()
    frame_length = 50
    padding = (frame_length - len(ba)) // 2
    title_line = f"{' ' * padding}{ba}{' ' * padding}"
    if len(title_line) < frame_length:
        title_line += ' ' * (frame_length - len(title_line))

    top_bottom_border = f"+{'-' * frame_length}+"
    empty_line = f"|{' ' * frame_length}|"
    title_with_border = f"|{title_line}|"

    print("\n" + top_bottom_border)
    print(empty_line)
    print(title_with_border)
    print(empty_line)
    print(top_bottom_border)

# The process of getting permission from the user to see the details
while True:
    try:
        details=input("\nWould you like to see the details and tables? (yes/no)").strip().lower()

        if details == "no":
            print("\nThank you.")
            time.sleep(1)
            print("\nhave a good day :)")
            sys.exit()
        elif details != "yes" and details!="no":
            print("\nPlease choose between No or Yes.")
        elif details=="yes":
            break
    except ValueError:
        print("\nPlease choose between No or Yes.")
    dico()

# Here, 'round' is used so that there can be 2 decimal places after the comma

df["Water Consumption Amount"] = df["Water Consumption Amount"].round(2)
df["Water Consumption Fee"] = df["Water Consumption Fee"].round(2)
df["Wastewater Fee"] = df["Wastewater Fee"].round(2)
df["VAT Amount"] = df["VAT Amount"].round(2)
df["Invoice Amount"] = df["Invoice Amount"].round(2)

header("Inputs")
print(tabulate(df.iloc[:, :5], headers='keys', tablefmt='grid'))

header("outputs")
print(tabulate(df.iloc[:, 5:], headers='keys', tablefmt='grid'))
dico()

# The task of the function here is to sum the number of Subscribers with 'm' Subscriber Type in the 'n' column.
#  In other words, it is to find the number of each Subscriber Type in the file.
def count(n,m):
    cnt=df[n].str.count(m).sum()
    
    return cnt

# The task of the function here is to get permission from the user before presenting the targeted information or tables.    
def ask(sentence):
    while True:
        try:
            details=input(f"\nPress 'enter' to see the {sentence}").strip().lower()
            
            if details!="":
                print(f"\nPress 'enter' to see the {sentence}")
            if details=="":
                break
        except ValueError:
            print(f"\nPress 'enter' to see the {sentence}")


housing=count("Subscriber Type","Housing")
touristic=count("Subscriber Type","Tourist Facility")       
workplace=count("Subscriber Type","Workplace")    
organization=count("Subscriber Type","Public Institution")  

Subscriber_t=["Housing","Tourist Facility","Workplace","Public Institution"]
Subscriber_s=[housing,touristic,workplace,organization] 

# The purpose of using this is for only the Percentage of the existing Subscriber Type to be shown in the visualization.
filtered_Subscriber_t = [Subscriber for Subscriber, sayı in zip(Subscriber_t, Subscriber_s) if sayı > 0]
filtered_Subscriber_s = [sayı for sayı in Subscriber_s if sayı > 0]

df['Daily Avg. Cons.'] = df['Water Consumption Amount'] / df['Number of Days']
df['Daily Avg. Cons.']=df['Daily Avg. Cons.'].round(2)

grouped = df.groupby('Subscriber Type').agg(
    Subscriber_Number=('Subscriber Type', 'count'),
    total_number_of_days=('Number of Days', 'sum'),
    total_water_consumption=('Water Consumption Amount', 'sum')
).reset_index()

grouped['Daily Avg. Cons.'] = (grouped['total_water_consumption'] / grouped['total_number_of_days']).round(2)

total_Subscriber = grouped['Subscriber_Number'].sum()
grouped['Percentage'] = (grouped['Subscriber_Number'] / total_Subscriber) * 100
grouped['Percentage'] = grouped['Percentage'].round(2)


ask("Information Regarding Subscriber Type")
print(tabulate(grouped, headers='keys', tablefmt='grid'))

plt.figure(figsize=(10, 6))
wedges, texts, autotexts = plt.pie(filtered_Subscriber_s, labels=filtered_Subscriber_t, autopct='%1.1f%%', startangle=140,\
                                     colors=["darkslateblue", "royalblue", "lightblue", "skyblue"], wedgeprops=dict(alpha=0.7))

plt.title("Information Regarding Subscriber Type")
for text in autotexts:
    text.set_color('white')
ask("table")
plt.show() 

# Purpose: To answer the question: "Monthly Water Consumption Amount of housing subscribers who do not exceed the 1st tier: number and Percentage."
housing_df = df[df['Subscriber Type'] == "housing"]
subset_housing = housing_df[housing_df['Water Consumption Amount'] <= 13]
num_subset_housing = len(subset_housing)
percentage_subset_housing = (num_subset_housing / housing) * 100 if housing > 0 else 0

if num_subset_housing > 0:
     print(f"\nMonthly Water Consumption Amount of housing subscribers who do not exceed the 1st tier:\
           \nnumber:{num_subset_housing}, Percentagesi: {percentage_subset_housing:.2f}%")
else:
    print(f"\nMonthly Water Consumption Amount, there are no housing Subscribers who do not exceed the 1st tier.") 

# Purpose: To find the "daily average Water Consumption Amount of the housing type Subscriber with the highest daily average water amount."
highest_daily_avg_cons = housing_df['Daily Avg. Cons.'].max()
print(f"\nDaily average Water Consumption Amount of the housing type Subscriber with\
       the highest daily average Water Consumption Amount:{highest_daily_avg_cons:.2f} ton/s")

# Purpose: To answer the question: "Monthly Water Consumption Amount, 1st tier-exceeding workplace Subscribers: number and Percentage."
workplace_df = df[df['Subscriber Type'] == "workplace"] 
subset_workplace = workplace_df[workplace_df['Water Consumption Amount'] > 10]
num_subset_workplace = len(subset_workplace)
percentage_subset_workplace = (num_subset_workplace / workplace) * 100 if workplace > 0 else 0

if num_subset_workplace > 0:
     print(f"\nMonthly Water Consumption Amount, of workplace Subscribers who exceed the 1st tier:\nnumber: {num_subset_workplace}, Percentagesi: {percentage_subset_workplace:.2f}%")
else:
    print(f"\nMonthly Water Consumption Amount, there are no workplace Subscribers who exceed the 1st tier..")

"""
The purpose of the function:
To find the Subscriber with the highest monthly water consumption (fee, or amount):
(Subscriber Type, Water Consumption Amount, the monthly [water consumption, wastewater] fee paid).
To create a visualization based on it.
"""
def max(column,sentence):
    max_index = df[column].idxmax()
    max_Subscriber = df.loc[max_index] 
    max_height = df[column].max()
    dico()
    ask(f"\nMonthly {sentence} Fee/Charge is the Highest Subscriber")

    print(f"\ninformation of the monthly {sentence} fee/charge is the highest subscriber:\
            \nSubscriber Type: {max_Subscriber['Subscriber Type']}\
            \nMonthly Water Consumption Amount: {max_Subscriber['Water Consumption Amount']} ton/s\
            \nMonthly Fee Paid {sentence} Cost: {max_Subscriber[column]} TL")
    ask("table")

    plt.figure(figsize=(10, 6))
    bars = plt.bar(df['Subscriber Type'], df[column], color="darkslateblue", alpha=0.7)
    plt.xlabel("Subscriber Type")
    plt.ylabel(f"{sentence} Cost (TL)")
    plt.title(f"Monthly {sentence} Fee/Charge is the Highest Subscriber")
    plt.axhline(y=max_Subscriber[column], color='r', linestyle='--')
    plt.text(0, max_Subscriber[column], f"the higher: {max_Subscriber[column]}\
            TL", color='r', ha='left', va='bottom')
    plt.show()

max("Water Consumption Fee","Water Consumption")

max("Wastewater Fee","Wastewater")
# The purpose of the function: To find the [Total Water Consumption amount] for each Subscriber Type and create a visualization.
def toplam(column,sentence,unit):
    total_water_cons = df.groupby('Subscriber Type')[column].sum().reset_index()
    plt.figure(figsize=(10, 6))
    bars = plt.bar(total_water_cons ['Subscriber Type'], total_water_cons [column], color="darkslateblue", alpha=0.7)
    plt.xlabel("Subscriber Type")
    plt.ylabel(f"Total Water Consumption {sentence} (ton/s)")
    plt.title(f"total water consumption by subscriber type {sentence}")

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:.2f} {unit}", ha="center", va="bottom", color="black")
    dico()
    ask(f"Total Water Consumption {sentence}'s table")
    plt.show()

toplam("Water Consumption Amount","amount"," ton/s")

toplam("Water Consumption Fee","Cost"," TL")

# Purpose: To calculate the [total monthly Wastewater Fee, total monthly VAT amount] obtained from all Subscribers.

def tum(column,sentence):
    tasu=df[column].sum().round(2)
    dico()
    ask(sentence)
    print(f"\n{sentence}: {tasu} TL")
    return

tum("Wastewater Fee","The total monthly Wastewater Fee obtained from all Subscribers: ")

tum("VAT Amount","The total monthly VAT amount paid to the state: ")

