import pandas as pd
import matplotlib.pyplot as plt

# Exercise 0: Load the dataset
def exercise_0(file):
    return pd.read_csv(transactions.csv)

# Exercise 1: Return column names as a list
def exercise_1(df):
    return df.columns.tolist()

# Exercise 2: Return the first k rows
def exercise_2(df, k):
    return df.head(k)

# Exercise 3: Return a random sample of k rows
def exercise_3(df, k):
    return df.sample(k)

# Exercise 4: Return a list of unique transaction types
def exercise_4(df):
    return df['transaction_type'].unique().tolist()

# Exercise 5: Return the top 10 transaction destinations with frequencies
def exercise_5(df):
    return df['destination'].value_counts().head(10)

# Exercise 6: Return rows where fraud was detected
def exercise_6(df):
    return df[df['is_fraud'] == 1]

# Exercise 7: Return number of distinct destinations for each source, sorted in descending order
def exercise_7(df):
    return df.groupby('source')['destination'].nunique().sort_values(ascending=False)

# Visual 1: Create bar chart for transaction types
def visual_1(df):
    transaction_counts = df['transaction_type'].value_counts()
    transaction_counts.plot(kind='bar')
    plt.title('Transaction Types')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.show()

# Visual 2: Scatter plot for balance deltas in cash out transactions
def visual_2(df):
    cash_out_df = df[df['transaction_type'] == 'CASH_OUT']
    cash_out_df.plot.scatter(x='origin_balance_delta', y='destination_balance_delta')
    plt.title('Balance Delta for Cash Out Transactions')
    plt.xlabel('Origin Account Balance Delta')
    plt.ylabel('Destination Account Balance Delta')
    plt.xlim(-1000, 1000)
    plt.ylim(-1000, 1000)
    plt.show()
