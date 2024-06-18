import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as ss

#loading data
@st.cache_data
def load_data():
    df = pd.read_csv('./data/MyTransaction.csv')
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
    # Change the date format to 'dd-mm-yy' for display
    df['FormattedDate'] = df['Date'].dt.strftime('%d-%m-%y')
    df['FormattedDate'] = pd.to_datetime(df['FormattedDate'])
    df['Date']=pd.to_datetime(df['FormattedDate'], format='%d-%m-%y')
    return df

df = load_data()

# Sidebar for user interaction
st.sidebar.header('Filters')
analysis_type = st.sidebar.selectbox('Analysis type', ('Daily analysis', 'Weekly analysis', 'Monthly analysis'))

min_start_date = df['Date'].min()
start_date = st.sidebar.date_input('Start Date', value=min_start_date, min_value=min_start_date, max_value=df['FormattedDate'].max())

if analysis_type == 'Daily analysis':
    min_end_date = pd.to_datetime(start_date) + pd.DateOffset(days=5)
elif analysis_type == 'Weekly analysis':
    min_end_date = pd.to_datetime(start_date) + pd.DateOffset(weeks=2)
elif analysis_type == 'Monthly analysis':
    min_end_date = pd.to_datetime(start_date) + pd.DateOffset(months=2)

end_date = st.sidebar.date_input('End Date', value=min_end_date, min_value=min_end_date, max_value=df['Date'].max())


category = st.sidebar.multiselect('Transaction Category', options=df['Category'].dropna().unique(), default=df['Category'].dropna().unique())

logo_img, heading = st.columns([1,4])
with logo_img:
    st.image('./images/bb_logo.png', width=80)
with heading:
    st.markdown('# BachatBuddy : Dashboard')
st.write('Hey there, savvy spender! 🌟'
        'Ready to take control of your finances and see where all those pennies are going?\n'
        "Whether you're saving up for your dream vacation, tracking daily coffee expenses, or just curious about your spending habits, this dashboard has got you covered.\n\n"
        "Dive in and let's turn those numbers into insights! 🚀\n\n"
        "Happy tracking! 📝✨\n\n")
st.divider()

filtered = df[(df['Date']>=pd.to_datetime(start_date)) & (df['Date']<=pd.to_datetime(end_date))]
if category:
    filtered = df[df['Category'].isin(category)]

#################################### Spending v/s Savings based on analysis type ###############################

## WITHDRAWAL ANALYSIS
if(analysis_type == 'Daily analysis'):
    filtered = filtered[(filtered['Date'] >= pd.to_datetime(start_date)) & (filtered['Date'] <= pd.to_datetime(end_date))]
    withd = filtered.groupby(['Date','Category']).agg({'Withdrawal':'sum'}).reset_index()
    col1, col2 = st.columns([1,3])
    with col2:
        st.write(withd[withd['Withdrawal']!=0].reset_index(drop=True))
    with col1:
        st.markdown('## *Daily Withdrawal Analysis*')
        st.write('The following line plot examines the daily withdrawal amounts across various categories, providing a granular view of spending patterns.')
    fig, ax = plt.subplots()
    for ctg in category:
        data = withd[withd['Category'] == ctg]
        ax.plot(data['Date'], data['Withdrawal'], label=ctg, marker='o')
    plt.xticks(rotation=90)
    ax.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    ax.set_xlabel('Date')
    ax.set_ylabel('Withdrawal Amount')
    ax.set_title('Daily Withdrawal Analysis')
    st.pyplot(fig)
elif analysis_type == 'Weekly analysis':
    filtered = filtered[(filtered['Date'] >= pd.to_datetime(start_date)) & (filtered['Date'] <= pd.to_datetime(end_date))]
    weekly_summary = filtered.groupby(['Date', 'Category']).agg({'Withdrawal': 'sum'}).reset_index()
    col1, col2 = st.columns([1,3])
    with col2:
        st.write(weekly_summary[weekly_summary['Withdrawal']!=0].reset_index(drop=True))
    with col1:
        st.markdown('## *Weekly Withdrawal Analysis*')
        st.write('This line plot delves into the weekly withdrawal amounts by category, offering insights into the ebb and flow of spending habits over a seven-day period.')
    fig, ax = plt.subplots()
    for ctg in category:
        data = weekly_summary[weekly_summary['Category'] == ctg]
        ax.plot(data['Date'], data['Withdrawal'], marker='o', label=ctg)
    plt.xticks(rotation=45)
    ax.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_xlabel('Week')
    ax.set_ylabel('Total Withdrawal Amount')
    ax.set_title('Weekly Withdrawal Analysis')
    st.pyplot(fig)
elif analysis_type == 'Monthly analysis':
    filtered = filtered[(filtered['Date'] >= pd.to_datetime(start_date)) & (filtered['Date'] <= pd.to_datetime(end_date))]
    monthly_summary = filtered.groupby(['Date', 'Category']).agg({'Withdrawal': 'sum'}).reset_index()
    col1, col2 = st.columns([1,3])
    with col2:
        st.write(monthly_summary[monthly_summary['Withdrawal']!=0].reset_index(drop=True))
    with col1:
        st.markdown('## *Monthly Withdrawal Analysis*')
        st.write('The subsequent line plot presents a broader perspective on withdrawal amounts, aggregating data by category on a monthly basis.')
    fig, ax = plt.subplots()
    for ctg in category:
        data = monthly_summary[monthly_summary['Category'] == ctg]
        ax.plot(data['Date'], data['Withdrawal'], marker='o', label=ctg)
    plt.xticks(rotation=45)
    ax.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Withdrawal Amount')
    ax.set_title('Monthly Withdrawal Analysis')
    st.pyplot(fig)
st.divider()
## DEPOSIT ANALYSIS
if(analysis_type == 'Daily analysis'):
    filtered = filtered[(filtered['Date'] >= pd.to_datetime(start_date)) & (filtered['Date'] <= pd.to_datetime(end_date))]
    dep = filtered.groupby(['Date','Category']).agg({'Deposit':'sum'}).reset_index()
    col1, col2 = st.columns([1,3])
    with col2:
        st.write(dep[dep['Deposit']!=0].reset_index(drop=True))
    with col1:
        st.markdown('## *Daily Deposit Analysis*')
        st.write('This line plot breaks down daily deposit amounts by category, highlighting the most active areas of income.')
    fig, ax = plt.subplots()
    for ctg in category:
        data = dep[dep['Category'] == ctg]
        ax.plot(data['Date'], data['Deposit'], label=ctg, marker='o')
    plt.xticks(rotation=90)
    ax.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    ax.set_xlabel('Date')
    ax.set_ylabel('Deposit Amount')
    ax.set_title('Daily Deposit Analysis')
    st.pyplot(fig)
elif analysis_type == 'Weekly analysis':
    filtered = filtered[(filtered['Date'] >= pd.to_datetime(start_date)) & (filtered['Date'] <= pd.to_datetime(end_date))]
    weekly_summary = filtered.groupby(['Date', 'Category']).agg({'Deposit': 'sum'}).reset_index()
    col1, col2 = st.columns([1,3])
    with col2:
        st.write(weekly_summary[weekly_summary['Deposit']!=0].reset_index(drop=True))
    with col1:
        st.markdown('## *Weekly Deposit Analysis*')
        st.write('The following line plot explores weekly deposit amounts across various categories, revealing patterns and correlations between different income streams.')
    fig, ax = plt.subplots()
    for ctg in category:
        data = weekly_summary[weekly_summary['Category'] == ctg]
        ax.plot(data['Date'], data['Deposit'], marker='o', label=ctg)
    plt.xticks(rotation=45)
    ax.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_xlabel('Week')
    ax.set_ylabel('Total Deposit Amount')
    ax.set_title('Weekly Deposit Analysis')
    st.pyplot(fig)
elif analysis_type == 'Monthly analysis':
    filtered = filtered[(filtered['Date'] >= pd.to_datetime(start_date)) & (filtered['Date'] <= pd.to_datetime(end_date))]
    monthly_summary = filtered.groupby(['Date', 'Category']).agg({'Deposit': 'sum'}).reset_index()
    col1, col2 = st.columns([1,3])
    with col2:
        st.write(monthly_summary[monthly_summary['Deposit']!=0].reset_index(drop=True))
    with col1:
        st.markdown('## *Monthly Withdrawal Analysis*')
        st.write('This line plot presents a monthly view of deposit amounts by category, showcasing the most significant contributors to monthly income. ')
    fig, ax = plt.subplots()
    for ctg in category:
        data = monthly_summary[monthly_summary['Category'] == ctg]
        ax.plot(data['Date'], data['Deposit'], marker='o', label=ctg)
    plt.xticks(rotation=45)
    ax.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Deposit Amount')
    ax.set_title('Monthly Deposit Analysis')
    st.pyplot(fig)
st.divider()
############################################## Category classification analysis ###############################
st.markdown('## *Amount spent on the basis of category*')
cat_dis =  filtered.groupby(['Category']).agg({'Withdrawal':'sum'}).reset_index()
st.write('This pie chart provides a visual representation of the distribution of spending across various categories over a specific period of time. By breaking down the total amount spent into its constituent parts, we can quickly identify the categories that account for the largest proportions of expenditure, allowing for more informed decisions about budget allocation and resource management.')
col1, col2= st.columns([1,2])
with col1:
    st.write('\n\n\n')
    st.write(cat_dis)
with col2:
    fig, ax = plt.subplots(figsize=(4,4))
    ax.pie(cat_dis['Withdrawal'], labels=cat_dis['Category'])
    for text in ax.texts:
        text.set_fontsize(8) 
    plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

st.divider()
###################################### Withdrawal vs Deposit vs Savings ###############################
st.markdown('## *Savings vs Deposits vs Withdrawals*')
filtered['Date'] = pd.to_datetime(filtered['Date'])

if analysis_type == 'Daily analysis':
    comp_data = filtered.groupby(filtered['Date'].dt.date).agg({'Withdrawal':'sum', 'Deposit':'sum'})
elif analysis_type == 'Weekly analyis':
    comp_data = filtered.groupby(filtered['Date'].dt.week).agg({'Withdrawal':'sum', 'Deposit':'sum'})
else:
    comp_data = filtered.groupby(filtered['Date'].dt.month).agg({'Withdrawal':'sum', 'Deposit':'sum'})

comp_data['Savings'] = comp_data['Withdrawal'] - comp_data['Deposit']
comp_data.reset_index(inplace=True)

st.write('This plot provides an overview of your financial transactions over different time periods. By selecting daily, weekly, or monthly analysis, you can see a comparison of your deposits and withdrawals as bar charts and track your savings over time with a line chart. Use this visualization to better understand your spending habits and manage your finances more effectively.')

#creating grouped bar chart
fig, ax1 = plt.subplots()
bar_width = 0.35
index = np.arange(len(comp_data))

bar1 = ax1.bar(index, comp_data['Withdrawal'], bar_width, label='Withdrawal', color='blue')
bar2 = ax1.bar(index+bar_width, comp_data['Deposit'], bar_width, label='Deposit', color='red')

ax2 = ax1.twinx()
ax2.plot(index+(bar_width/2), comp_data['Savings'], label='Savings', marker='o', color='green')

ax1.set_title(f'{analysis_type} Deposits, Withdrawals, and Savings')
ax1.set_xlabel('Date')
ax1.set_ylabel('Amount')
ax2.set_ylabel('Savings')
ax1.set_title(f'{analysis_type} Deposits, Withdrawals, and Savings')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(comp_data['Date'], rotation=45)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

st.pyplot(fig)

st.divider()
st.markdown('#### Concluding Remarks')
st.write('Thank you for using Bachat Buddy to manage your finances. We hope this dashboard has provided you with valuable insights into your spending habits and savings patterns. By regularly monitoring your financial activities, you can make informed decisions, set realistic goals, and achieve better financial stability. Remember, consistent tracking and mindful spending are key to financial success. Happy saving!')
