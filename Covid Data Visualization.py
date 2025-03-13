#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
#%%
url = 'https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/refs/heads/main/CONVENIENT_global_confirmed_cases.csv'
df = pd.read_csv(url)
#%%
nan_per_column = df.isna().sum()
print("\nNaN values per column:")
print(nan_per_column)
#%%
nan_percentage = (df.isna().sum() / len(df)) * 100
print("\nPercentage of NaN values per column:")
print(nan_percentage)
#%%
df.dropna(inplace=True)
#%%
nan_percentage = (df.isna().sum() / len(df)) * 100
print("\nPercentage of NaN values per column:")
print(nan_percentage)
#%%

china_sums = [col for col in df.columns if col.startswith('China')]
for col in china_sums:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # This will convert to numeric, handling any errors

# Now create the sum column
df['China_sum'] = df[china_sums].sum(axis=1)

# Display the result
print(df)
#%%

#%%
uk_sums = [col for col in df.columns if col.startswith('United Kingdom')]
for col in uk_sums:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['UK_sum'] = df[uk_sums].sum(axis=1)
#%%
#%%
# Question 4
import matplotlib.dates as mdates
covid_us = df.loc[:, ['Country/Region','US']]
covid_us['Country/Region'] = pd.to_datetime(covid_us['Country/Region'])

fig, ax = plt.subplots(figsize=(10,8))
ax.plot(covid_us['Country/Region'],covid_us['US'],color='#1f77b4', linewidth=2,label='US')
locator =mdates.MonthLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
ax.set_title('US Confirmed COVID-19 cases')
ax.set_xlabel('Year')
ax.legend()
ax.set_ylabel('Confirmed COVID-19 cases')
plt.grid()
plt.show()
plt.tight_layout()
#%%
# Question 5

rest_world = df.loc[:, ['Country/Region','US','UK_sum',"China_sum","Germany","Brazil","India","Italy"]]
rest_world['Country/Region'] = pd.to_datetime(rest_world['Country/Region'])
selected_columns = ['US','UK_sum', 'China_sum', 'Germany', 'Brazil', 'India', 'Italy']
fig, ax = plt.subplots(figsize=(10,8))
ax.plot(rest_world['Country/Region'],rest_world[selected_columns], linewidth=2)
locator =mdates.MonthLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
ax.set_title('Global Confirmed COVID-19 cases')
ax.set_xlabel('Year')
ax.legend(selected_columns)
ax.set_ylabel('Confirmed COVID-19 cases')
plt.grid()
plt.show()
plt.tight_layout()

#%%
# Question 6
us_cases = covid_us

plt.figure(figsize=(12, 6))

plt.hist(us_cases, bins=30, alpha=0.6, edgecolor='black')

plt.title('Distribution of COVID-19 Cases in the US', fontsize=14, pad=20)
plt.xlabel('Number of Cases', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.grid(True, alpha=0.3, linestyle='--')

plt.xticks(rotation=45)

current_values = plt.gca().get_xticks()
plt.gca().set_xticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.tight_layout()
plt.show()
#%%

import matplotlib.dates as mdates


countries = ['US','UK_sum',"China_sum","Germany","Brazil","India","Italy"]
fig, axes = plt.subplots(3, 2, figsize=(15, 20))
axes = axes.ravel()


dates = []
for value in df['Country/Region']:
    try:
        date = pd.to_datetime(value)
        if pd.notna(date):
            dates.append(date)
    except:
        continue


countries = {
    'United Kingdom': 'UK_sum',  # Using the main UK column
    'China': 'China_sum',
    'Italy': 'Italy',
    'Brazil': 'Brazil',
    'Germany': 'Germany',
    'India': 'India'
}


for idx, (country_name, column_name) in enumerate(countries.items()):

    cases = []
    for date_str in df['Country/Region']:
        try:
            if pd.notna(pd.to_datetime(date_str)):
                value = df[df['Country/Region'] == date_str][column_name].iloc[0]
                cases.append(float(value) if pd.notna(value) else 0)
        except:
            cases.append(0)


    axes[idx].bar(dates, cases, color='blue', alpha=0.6, edgecolor='black')


    axes[idx].set_title(f'{country_name} confirmed COVID19 cases', pad=20)
    axes[idx].set_xlabel('Date')
    axes[idx].set_ylabel('Confirmed COVID19 cases')


    axes[idx].tick_params(axis='x', rotation=45)


    axes[idx].grid(True, alpha=0.3, linestyle='--')


    axes[idx].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))


    axes[idx].xaxis.set_major_locator(plt.AutoLocator())
    axes[idx].xaxis.set_major_formatter(plt.FixedFormatter('%Y-%m'))


plt.tight_layout()
plt.show()
#%%
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%%
df = sns.load_dataset('titanic')
#%%
df
#%%
# Question 1
print("\nNumber of NaN values in each column before cleaning:")
print(df.isnull().sum())

#%%
df = df.dropna()
#%%
df.head(5)
#%%
female_count =int(( df['sex'] == 'female').sum())
male_count = int((df['sex'] == 'male').sum())
#%%
counts = [male_count, female_count]
#%%
gender_counts = df['sex'].value_counts()
#%%
# Question 2
print("\nGender Distribution on Titanic:")
print("-" * 30)
print(f"Number of Males: {gender_counts['male']}")
print(f"Number of Females: {gender_counts['female']}")
print(f"Total Passengers: {len(df)}")

#%%
label = [f'Male ({gender_counts["male"]})', f'Female ({gender_counts["female"]})']
plt.figure(figsize=(10,10))
plt.pie(gender_counts.values,
        labels= label,
        autopct = '%1.2f%%',
        startangle=90,
        colors=['skyblue', 'orange'])
plt.title('Gender Distribution on Titanic')
plt.axis('equal')
plt.legend()
plt.tight_layout()
plt.show()

#%%
# Question 3
total = sum(gender_counts)
male_percentage = round(gender_counts['male'] / total,2)
female_percentage = round(gender_counts['female'] / total,2)
print("\nPercentage of the Male and Female Passengers:")
print("-" * 30)
print(f"Male Percentage:{male_percentage}%, Female Percentage:{female_percentage}%")

#%%
male_df = df[df['sex'] == 'male']
male_survival = male_df['survived'].value_counts()
male_survival_percent = (male_survival / len(male_df) * 100).round(1)
plt.figure(figsize=(10, 8))
labels = [f'Did Not Survive\n({male_survival[0]} passengers, {male_survival_percent[0]}%)',
          f'Survived\n({male_survival[1]} passengers, {male_survival_percent[1]}%)']
plt.pie(male_survival.values,
        labels=labels,
        colors=['lightcoral', 'lightgreen'],
        autopct='%1.1f%%')
plt.title('Male Passenger Survival Distribution on Titanic',fontsize=15)

plt.title("Number of male survived")
plt.tight_layout()
plt.show()

print("\nMale Survival Statistics:")
print("-" * 30)
print(f"Number of Males who Survived: {male_survival[1]}")
print(f"Number of Males who Did Not Survive: {male_survival[0]}")
print(f"Total Number of Males: {len(male_df)}")
print("\nPercentages:")
print(f"Percentage of Males who Survived: {male_survival_percent[1]}%")
print(f"Percentage of Males who Did Not Survive: {male_survival_percent[0]}%")
#%%
female_df = df[df['sex'] == 'female']
female_survival = female_df['survived'].value_counts()
female_survival_percent = (female_survival / len(male_df) * 100).round(1)
plt.figure(figsize=(10, 8))
labels = [f'Survived\n({female_survival[0]} passengers, {female_survival_percent[0]}%)',
          f'Did not survive\n({female_survival[1]} passengers, {female_survival_percent[1]}%)']
plt.pie(female_survival.values,
        labels=labels,
        colors=['lightcoral', 'lightgreen'],
        autopct='%1.1f%%')
plt.title('Female Passenger Survival Distribution on Titanic',fontsize=15)

plt.title("Number of female survived")
plt.tight_layout()
plt.show()

print("\nMale Survival Statistics:")
print("-" * 30)
print(f"Number of females who Survived: {female_survival[1]}")
print(f"Number of females who Did Not Survive: {female_survival[0]}")
print(f"Total Number of females: {len(female_df)}")
print("\nPercentages:")
print(f"Percentage of females who Survived: {female_survival_percent[1]}%")
print(f"Percentage of females who Did Not Survive: {female_survival_percent[0]}%")
#%%
class_counts = df['pclass'].value_counts().sort_index()

class_percentages = (class_counts / len(df) * 100).round(1)

print("\nPassenger Class Distribution:")
print("-" * 30)
print(f"First Class (1): {class_counts[1]} passengers")
print(f"Second Class (2): {class_counts[2]} passengers")
print(f"Third Class (3): {class_counts[3]} passengers")
print(f"Total Passengers: {len(df)}")
print("\nPercentages:")
print(f"First Class: {class_percentages[1]}%")
print(f"Second Class: {class_percentages[2]}%")
print(f"Third Class: {class_percentages[3]}%")

plt.figure(figsize=(10, 8))

labels = [f'First Class\n({class_counts[1]} passengers, {class_percentages[1]}%)',
          f'Second Class\n({class_counts[2]} passengers, {class_percentages[2]}%)',
          f'Third Class\n({class_counts[3]} passengers, {class_percentages[3]}%)']

colors = ['#FFD700', '#C0C0C0', '#CD7F32']  # Gold, Silver, Bronze

plt.pie(class_counts.values,
        labels=labels,
        colors=colors,
        explode=(0.1, 0.05, 0),
        autopct='%1.1f%%')

plt.title('Passenger Class Distribution on Titanic')
plt.axis('equal')

plt.legend(labels, title="Passenger Classes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()

plt.show()
#%%

survival_by_class = df.groupby('pclass')['survived'].agg(['count', 'sum'])
survival_by_class['survival_rate'] = (survival_by_class['sum'] / survival_by_class['count'] * 100).round(1)

print("\nSurvival Statistics by Passenger Class:")
print("-" * 40)
for pclass in [1, 2, 3]:
    total = survival_by_class.loc[pclass, 'count']
    survived = survival_by_class.loc[pclass, 'sum']
    rate = survival_by_class.loc[pclass, 'survival_rate']
    print(f"\nClass {pclass}:")
    print(f"Total Passengers: {total}")
    print(f"Survived: {survived}")
    print(f"Did Not Survive: {total - survived}")
    print(f"Survival Rate: {rate}%")

plt.figure(figsize=(12, 8))

labels = [f'First Class\n({survival_by_class.loc[1, "survival_rate"]}% survived)',
          f'Second Class\n({survival_by_class.loc[2, "survival_rate"]}% survived)',
          f'Third Class\n({survival_by_class.loc[3, "survival_rate"]}% survived)']

sizes = survival_by_class['survival_rate']
colors = ['#FFD700', '#C0C0C0', '#CD7F32']  # Gold, Silver, Bronze

plt.pie(sizes,
        labels=labels,
        colors=colors,
        explode=(0.1, 0.05, 0),
        autopct='%1.1f%%')

plt.title('Survival Rate Distribution by Passenger Class on Titanic')
plt.axis('equal')

plt.legend(labels,
          title="Passenger Classes",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()

plt.show()
#%%

plt.figure(figsize=(15, 5))

# Process each class
for pclass in [1, 2, 3]:

        class_data = df[df['pclass'] == pclass]


        survival_counts = class_data['survived'].value_counts()
        total_passengers = len(class_data)
        survival_percentages = (survival_counts / total_passengers * 100).round(1)


        print(f"\nClass {pclass} Statistics:")
        print("-" * 30)
        print(f"Total Passengers: {total_passengers}")
        print(f"Survived: {survival_counts.get(1, 0)} ({survival_percentages.get(1, 0)}%)")
        print(f"Did Not Survive: {survival_counts.get(0, 0)} ({survival_percentages.get(0, 0)}%)")

        plt.subplot(1, 3, pclass)

        labels = [f'Did Not Survive\n({survival_counts.get(0, 0)} passengers)',
                  f'Survived\n({survival_counts.get(1, 0)} passengers)']


        plt.pie(survival_counts,
                labels=labels,
                colors=['red', 'green'],
                explode=(0.05, 0.05),
                autopct='%1.1f%%')

        plt.title(f'Class {pclass} Survival Distribution')


plt.suptitle('Survival Distribution by Passenger Class on Titanic', fontsize=14, y=1.05)
plt.tight_layout()


plt.show()
#%%

print("\nOverall Statistics:")
print("-" * 30)
total_survival = df['survived'].value_counts()
total_percentages = (total_survival / len(df) * 100).round(1)
print(f"Total Passengers: {len(df)}")
print(f"Total Survived: {total_survival[1]} ({total_percentages[1]}%)")
print(f"Total Did Not Survive: {total_survival[0]} ({total_percentages[0]}%)")
#%%

fig, axes = plt.subplots(3, 3, figsize=(16, 8))
fig.suptitle('Titanic Passenger Analysis Dashboard', fontsize=16, y=0.95)

# 1. Overall Gender Distribution (Row 1, Col 1)
gender_counts = df['Sex'].value_counts()
axes[0, 0].pie(gender_counts.values,
               labels=[f'{gender}\n({count} passengers)' for gender, count in gender_counts.items()],
               colors=['lightblue', 'pink'],
               autopct='%1.1f%%')
axes[0, 0].set_title('Gender Distribution')

# 2. Male Survival Distribution (Row 1, Col 2)
male_df = df[df['Sex'] == 'male']
male_survival = male_df['Survived'].value_counts()
axes[0, 1].pie(male_survival.values,
               labels=[f'Did Not Survive\n({male_survival[0]} passengers)',
                      f'Survived\n({male_survival[1]} passengers)'],
               colors=['red', 'green'],
               autopct='%1.1f%%')
axes[0, 1].set_title('Male Survival Distribution')

# 3. Female Survival Distribution (Row 1, Col 3)
female_df = df[df['Sex'] == 'female']
female_survival = female_df['Survived'].value_counts()
axes[0, 2].pie(female_survival.values,
               labels=[f'Did Not Survive\n({female_survival[0]} passengers)',
                      f'Survived\n({female_survival[1]} passengers)'],
               colors=['red', 'green'],
               autopct='%1.1f%%')
axes[0, 2].set_title('Female Survival Distribution')

# 4. Passenger Class Distribution (Row 2, Col 1)
class_counts = df['Pclass'].value_counts().sort_index()
axes[1, 0].pie(class_counts.values,
               labels=[f'Class {i}\n({count} passengers)' for i, count in class_counts.items()],
               colors=['#FFD700', '#C0C0C0', '#CD7F32'],
               autopct='%1.1f%%')
axes[1, 0].set_title('Passenger Class Distribution')

# 5-7. Survival Distribution by Class (Row 2, Col 2-3 and Row 3, Col 1)
for idx, pclass in enumerate([1, 2, 3]):
    class_data = df[df['Pclass'] == pclass]
    survival_counts = class_data['Survived'].value_counts()
    row = 1 + idx // 2
    col = 1 + idx % 2
    axes[row, col].pie(survival_counts.values,
                      labels=[f'Did Not Survive\n({survival_counts[0]} passengers)',
                             f'Survived\n({survival_counts[1]} passengers)'],
                      colors=['red', 'green'],
                      autopct='%1.1f%%')
    axes[row, col].set_title(f'Class {pclass} Survival Distribution')

# 8. Overall Survival Distribution (Row 3, Col 2)
total_survival = df['Survived'].value_counts()
axes[2, 2].pie(total_survival.values,
               labels=[f'Did Not Survive\n({total_survival[0]} passengers)',
                      f'Survived\n({total_survival[1]} passengers)'],
               colors=['red', 'green'],
               autopct='%1.1f%%')
axes[2, 2].set_title('Overall Survival Distribution')
axes[2, 0].remove()

plt.tight_layout()
plt.show()q