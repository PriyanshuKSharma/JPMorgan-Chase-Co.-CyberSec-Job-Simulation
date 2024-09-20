import pandas as pd
import matplotlib.pyplot as plt

#Read the dataset
def exercise_0(file):
    df=pd.read_csv("transactions.csv")
    return df

def exercise_1(df):
    # Return the column names as a list
    return df.columns.tolist()

def exercise_2(df, k):
    # Return the first k rows
    return df.head(k)

def exercise_3(df, k):
    # Return a random sample of k rows
    return df.sample(n=k)

# Now, modify the exercise_4 function based on the correct column name
def exercise_4(df):
    # Check if 'transaction_type' exists, or use the actual column name
    if 'transaction_type' in df.columns:
        return df['transaction_type'].unique().tolist()
    else:
        return f"'transaction_type' column not found! Please check the column names."

def exercise_5(df):
    # Return a Pandas series of the top 10 transaction destinations with frequencies
    return df['destination'].value_counts().head(10)

def exercise_6(df):
    # Return all the rows from the dataframe for which fraud was detected
    return df[df['fraud_detected'] == True]

def exercise_7(df):
    # Bonus: Return a dataframe that contains the number of distinct destinations each source has interacted with, sorted in descending order
    return df.groupby('source')['destination'].nunique().sort_values(ascending=False)



def visual_1(df):
    # Example visualization: Plot the distribution of transaction types
    df['transaction_type'].value_counts().plot(kind='bar')
    plt.title('Distribution of Transaction Types')
    plt.xlabel('Transaction Type')
    plt.ylabel('Frequency')
    plt.show()

def visual_2(df):
    # Example visualization: Plot the top 10 transaction destinations
    df['destination'].value_counts().head(10).plot(kind='bar')
    plt.title('Top 10 Transaction Destinations')
    plt.xlabel('Destination')
    plt.ylabel('Frequency')
    plt.show()


def exercise_custom(df):
    # Custom exercise: Example - Count transactions per hour
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    return df['hour'].value_counts().sort_index()

def visual_custom(df):
    # Custom visualization: Example - Plot transaction counts by hour
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    df['hour'].value_counts().sort_index().plot(kind='line')
    plt.title('Transactions by Hour of the Day')
    plt.xlabel('Hour')
    plt.ylabel('Number of Transactions')
    plt.show()

# Example usage:
df = exercise_0('transactions.csv')

# Test exercise_1: Return column names
print("Column names:")
print(exercise_1(df))

# Test exercise_2: Return the first k rows (example with k=5)
k = 5
print(f"\nFirst {k} rows:")
print(exercise_2(df, k))

# Test exercise_3: Return a random sample of k rows (example with k=5)
print(f"\nRandom sample of {k} rows:")
print(exercise_3(df, k))

# Test exercise_4: Return a list of the unique transaction types
print("\nUnique transaction types:")
print(exercise_4(df))

# Test exercise_5: Return the top 10 transaction destinations with frequencies
print("\nTop 10 transaction destinations with frequencies:")
print(exercise_5(df))

# Test exercise_6: Return all the rows where fraud was detected
print("\nRows where fraud was detected:")
print(exercise_6(df))

# Test exercise_7: Bonus - Return the number of distinct destinations each source has interacted with
print("\nDistinct destinations per source, sorted:")
print(exercise_7(df))


def visual_1(df):
    def transaction_counts(df):
        # TODO
        pass
    def transaction_counts_split_by_fraud(df):
        # TODO
        pass

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('TODO')
    axs[0].set_xlabel('TODO')
    axs[0].set_ylabel('TODO')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('TODO')
    axs[1].set_xlabel('TODO')
    axs[1].set_ylabel('TODO')
    fig.suptitle('TODO')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 'TODO'

visual_1(df)



def visual_2(df):
    def query(df):
        # TODO
        pass
    plot = query(df).plot.scatter(x='TODO',y='TODO')
    plot.set_title('TODO')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return 'TODO'

visual_2(df)

