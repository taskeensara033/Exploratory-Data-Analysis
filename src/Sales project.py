import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('sales_data(1).csv', encoding='ISO-8859-1')
print(df) 

# Displaying all the rows
pd.set_option('display.max_rows',None)
print(df)


# Displaying all the columns
pd.set_option('display.max_columns',None)
print(df)


#Finding null values in Amount column
print(df[df['Amount'].isnull()])


#droping status and unnammed1 column
df.drop(['Status','unnamed1'],axis=1,inplace=True)    ## by default axis is 0 it considers rows
print(df)

#Deleting nan values
pd.set_option('display.max_rows',None)
print(df.dropna(inplace=True))


#Renaming columns
df.rename(columns={'Marital_Status':'Marital'},inplace=True)
print(df)


# change values of marital 0-->single  1-->married
df['Marital']=df['Marital'].replace({0:'Single',1:'Married'})
print(df)

df['Gender']=df['Gender'].replace({'F':'Female','M':'Male'})
print(df)


#Visualise counts pf male and female
v=sns.countplot(x='Gender',data=df,palette='dark')
for i in v.containers:
    v.bar_label(i)
plt.show() 
plt.savefig('Count')


#Group By Age Group
a=df.groupby('Age Group')['Amount'].sum()
Agroup=pd.DataFrame(a)
# plt.figure(figsize=(22,5))
sns.barplot(x=Agroup.index,y=Agroup.Amount,palette='bright')
plt.title('Amount Spent by Age Group')
plt.ylabel('Amount Spent')
plt.show()


#Group By State
a=df.groupby('State')['Amount'].sum()
state=pd.DataFrame(a)
plt.figure(figsize=(12,6))
sns.barplot(x=state.index,y=state.Amount,palette='bright')
plt.title('Amount Spent by State')
plt.ylabel('Amount Spent')
plt.xticks(rotation=60,ha='center')
plt.tight_layout()
plt.show()
plt.savefig('State')


#Group By Occupation
a=df.groupby('Occupation')['Amount'].sum()
state=pd.DataFrame(a)
sns.barplot(x=state.index,y=state.Amount,palette='coolwarm')
plt.title('Amount Spent by Occupation')
plt.ylabel('Amount Spent')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()
plt.savefig('Occupation')


#Group By Product category
a=df.groupby('Product_Category')['Amount'].sum()
state=pd.DataFrame(a)
sns.barplot(x=state.index,y=state.Amount,palette='dark')
plt.title('Amount Spent based on Product_Category')
plt.ylabel('Amount Spent')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()
plt.savefig('Product_Category')


#Group By Marital Status
a=df.groupby('Marital')['Amount'].sum()
state=pd.DataFrame(a)
sns.barplot(x=state.index,y=state.Amount,palette='dark')
plt.title('Amount Spent based on Marital_Status')
plt.ylabel('Amount Spent')
plt.show()
plt.savefig('Marital')


#Group By Gender
a=df.groupby('Gender')['Amount'].sum()
gender=pd.DataFrame(a)
plt.figure(figsize=(5,5))
sns.barplot(x=gender.index,y=gender.Amount,palette='dark')
plt.title('Total Spending by Gender')
plt.ylabel('Amount Spent')
plt.show()
plt.savefig('Gender')