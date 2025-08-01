import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('sales_data(1).csv', encoding='ISO-8859-1')
# print(df)
# pd.set_option('display.max_rows',None)
# print(df)
# print(df['Amount'],df['Gender'])


# pd.set_option('display.max_columns',None)

#**********************Finding null values in Amount column************
# print(df[df['Amount'].isnull()])

#**********************droping status and unnammed1 column************
df.drop(['Status','unnamed1'],axis=1,inplace=True)    ## by default axis is 0 it considers rows
# print(df)

#**********************Deleting nan values************************
# pd.set_option('display.max_rows',None)
# print(df.dropna(inplace=True))


#**********************Renaming columns************************
df.rename(columns={'Marital_Status':'Marital'},inplace=True)
# print(df)


# #**********************change values of marital 0-->single  1-->married************************
df['Marital']=df['Marital'].replace({0:'Single',1:'Married'})
# # # print(df)

df['Gender']=df['Gender'].replace({'F':'Female','M':'Male'})
# print(df)

# #**********************Visualise counts pf male and female************************
# sns.countplot(x='Gender',data=df,palette='bright')
# plt.show()

# v=sns.countplot(x='Gender',data=df,palette='dark')
# for i in v.containers:
#     v.bar_label(i)
# plt.show() 

# #**********************Group By************************
# v1=sns.countplot(x='Age Group',data=df,hue='Gender',palette='dark')
# for i in v1.containers:
#     v1.bar_label(i)
# plt.show()

# a=df.groupby('Age Group')['Amount'].sum()
# Agroup=pd.DataFrame(a)
# # plt.figure(figsize=(22,5))
# sns.barplot(x=Agroup.index,y=Agroup.Amount,palette='bright')
# plt.title('Amount Spent by Age Group')
# plt.ylabel('Amount Spent')
# plt.show()



# #**********************Group By************************
# plt.figure(figsize=(22,5))
# v2=sns.countplot(x='State',data=df,palette='bright')
# for i in v2.containers:
#     v2.bar_label(i)
#     v2.set_label('State')
# plt.show()


# a=df.groupby('State')['Amount'].sum()
# state=pd.DataFrame(a)
# plt.figure(figsize=(12,6))
# sns.barplot(x=state.index,y=state.Amount,palette='deep')
# plt.title('Amount Spent by State')
# plt.ylabel('Amount Spent')
# plt.xticks(rotation=60,ha='center')
# plt.tight_layout()
# plt.show()


# #**********************Group By************************
# plt.figure(figsize=(22,5))
# v3=sns.countplot(x='Occupation',data=df,palette='bright')
# for i in v3.containers:
#     v3.bar_label(i)
# plt.show()

# a=df.groupby('Occupation')['Amount'].sum()
# state=pd.DataFrame(a)
# sns.barplot(x=state.index,y=state.Amount,palette='coolwarm')
# plt.title('Amount Spent by Occupation')
# plt.ylabel('Amount Spent')
# plt.xticks(rotation=45,ha='right')
# plt.tight_layout()
# plt.show()



# #**********************Group By************************

# a=df.groupby('State')['Amount'].sum()
# state=pd.DataFrame(a)
# plt.figure(figsize=(22,5))
# sns.barplot(x=state.index,y=state.Amount)
# plt.show()




# #**********************Group By************************

# a=df.groupby('Product_Category')['Amount'].sum()
# state=pd.DataFrame(a)

# sns.barplot(x=state.index,y=state.Amount,palette='dark')
# plt.title('Amount Spent based on Product_Category')
# plt.ylabel('Amount Spent')
# plt.xticks(rotation=45,ha='right')
# plt.tight_layout()
# plt.show()

# #**********************Group By************************

# a=df.groupby('Marital')['Amount'].sum()
# state=pd.DataFrame(a)
# sns.barplot(x=state.index,y=state.Amount,palette='dark')
# plt.title('Amount Spent based on Marital_Status')
# plt.ylabel('Amount Spent')
# plt.show()

# a=df.groupby('Gender')['Amount'].sum()
# gender=pd.DataFrame(a)
# plt.figure(figsize=(5,5))
# sns.barplot(x=gender.index,y=gender.Amount,palette='dark')
# plt.title('Total Spending by Gender')
# plt.ylabel('Amount Spent')
# plt.show()
