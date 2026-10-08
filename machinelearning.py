import pandas as pd
data=pd.read_csv("health-outcomes-csv-1.csv")
print(data)

#steps 2 -- data analysis
print(data.head())
print(data.tail())
print(data.info())
print(data.describe())

#checking missing values
print(data.isnull().sum())

#check dulicate values
print(data.duplicated().sum())

#step:3 data preproceeing
#1. remove irrelvent data

data=data.drop(["Infants exclusively breastfed (% ages 0Ð5 months) 2008Ð2013","index"],axis=1)
print(data)

#handle missing values
print("------missing value--------")
print(data.isnull().sum())

print(data.columns.tolist())

#fillna()with values
#data[["Infants lacking immunization (% of one-year-olds) DTP 2013 ","Infants lacking immunization (% of one-year-olds) DTP 2013","Mortality rates (per 1,000 live births) Infant 2013","Mortality rates (per 1,000 live births) Under-five 2013 ","Deaths due to Tuberculosis (per 100,000 people) 2012"]] = data[["Infants lacking immunization (% of one-year-olds) DTP 2013 ","Infants lacking immunization (% of one-year-olds) DTP 2013","Mortality rates (per 1,000 live births) Infant 2013","Mortality rates (per 1,000 live births) Under-five 2013 ","Deaths due to Tuberculosis (per 100,000 people) 2012"]].fillna(0)
#print(data)

data[['Infants lacking immunization (% of one-year-olds) DTP 2013', 'Infants lacking immunization (% of one-year-olds) Measles 2013', 'Mortality rates (per 1,000 live births) Infant 2013', 'Mortality rates (per 1,000 live births) Under-five 2013','Deaths due to Tuberculosis (per 100,000 people) 2012']] = data[['Infants lacking immunization (% of one-year-olds) DTP 2013', 'Infants lacking immunization (% of one-year-olds) Measles 2013', 'Mortality rates (per 1,000 live births) Infant 2013', 'Mortality rates (per 1,000 live births) Under-five 2013','Deaths due to Tuberculosis (per 100,000 people) 2012']].fillna(0)
print(data)

print("------missing value--------")
print(data.isnull().sum())

#data["Child malnutrition (% under age 5) Stunting (moderate or severe) 2008Ð2013","Adult mortality rate (per 1,000 people) Female 2013","Adult mortality rate (per 1,000 people) Male 2013","Deaths due to Malaria (per 100,000 people) 2012"] = data["Child malnutrition (% under age 5) Stunting (moderate or severe) 2008Ð2013","Adult mortality rate (per 1,000 people) Female 2013","Adult mortality rate (per 1,000 people) Male 2013","Deaths due to Malaria (per 100,000 people) 2012"].fillna(data["Child malnutrition (% under age 5) Stunting (moderate or severe) 2008Ð2013","Adult mortality rate (per 1,000 people) Female 2013","Adult mortality rate (per 1,000 people) Male 2013","Deaths due to Malaria (per 100,000 people) 2012"].mean())
#print(data.isnull().sum())
print(data.keys())
data["Child malnutrition (% under age 5) Stunting (moderate or severe) 2008Ð2013","Adult mortality rate (per 1,000 people) Female 2013","Adult mortality rate (per 1,000 people) Male 2013","Deaths due to Malaria (per 100,000 people) 2012"] = data["Child malnutrition (% under age 5) Stunting (moderate or severe) 2008Ð2013","Adult mortality rate (per 1,000 people) Female 2013","Adult mortality rate (per 1,000 people) Male 2013","Deaths due to Malaria (per 100,000 people) 2012"].fillna(data["Child malnutrition (% under age 5) Stunting (moderate or severe) 2008Ð2013","Adult mortality rate (per 1,000 people) Female 2013","Adult mortality rate (per 1,000 people) Male 2013","Deaths due to Malaria (per 100,000 people) 2012"].mean())
print(data.isnull().sum())