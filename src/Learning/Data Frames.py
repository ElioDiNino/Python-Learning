import numpy as np
import pandas as pd

# Use and change end numbers to display all data
pd.set_option('display.max_columns', 40)
pd.set_option('display.max_rows', 900)
pd.set_option('display.width', 1000)

def header(msg):
    print('-' * 191)
    print('[ ' + msg + ' ]')

# Read text file into a dataframe
header("Read text file into a df")
filename = 'train.csv'
df = pd.read_csv(filename)
print(df)

# Show columns and how many values for each
header("df.count()")
print(df.count())

# Print first _ (default of 5) or last _ (in this case 3) rows of df
header("df.head()")
print(df.head())
header("df.tail(3)")
print(df.tail(3))

# Get rid of the rows with empty data
header("df.dropna()") # use (subset = '') to drop NaN based on that column
print(df.dropna())

# Fill empty data
header("df.fillna(' ')")
print(df.fillna(' '))


# Group and review desired information
header("df.groupby('Sex').Survived.value_counts()")
print(df.groupby('Sex').Survived.value_counts())
print(df.groupby(['Sex', 'Survived']).size())

# Column results to column headers
header("df.groupby(['Sex', 'Survived']).size().unstack()")
print(df.groupby(['Sex', 'Survived']).size().unstack())

# Get data types, index, columns, values
header("df.dtypes")
print(df.dtypes)

header("df.index")
print(df.index)

header("df.columns")
print(df.columns)

header("df.values")
print(df.values)

# Statistical summary of each column
header("df.describe")
print(df.describe())

# Summary of each column
header("df.info()")
print(df.info())     

# Sort records by any column
header("df.sort_values('Age', ascending=False)")
print(df.sort_values('Age', ascending=False))

# Slicing records
header("slicing -- df.Name")
print(df.Name)

header("slicing -- df[100:151]")
print(df[100:151])

header(" slicing -- df[['Name', 'Pclass']]")
print(df[['Name', 'Pclass']])

header(" slicing -- df.loc[100:151, ['Name', 'Pclass']]") # df.loc[from_row:to_row,['column1', 'column2']]
print(df.loc[100:151, ['Name', 'Pclass']])

header(" slicing scalar value -- df.loc[100, ['Name']]")
print(df.loc[100, ['Name']])

header(" slicing -- df.iloc[100:151, [0,10]]") 
print(df.iloc[100:151, [0,10]])

# Filtering
header("df[df.Age > 30]")
print(df[df.Age > 30])

# Assignment
header("df.loc[9, ['Age']] = 40")
df.loc[9, ['Age']] = 40
print(df.iloc[9:11])

header("df.loc[9, ['Age']] = np.nan")
df.loc[9, ['Age']] = np.nan
print(df.iloc[9:11])

header("df.loc[:, ['Pclass']] = np.array([1] * len(df))")
df.loc[:, ['Pclass']] = np.array([1] * len(df))
print(df.head())

header("df['Class+Life'] = (df.Pclass + df.Survived)")
df['Class+Life'] = (df.Pclass + df.Survived)
print(df.head())

# Remove Columns
header("df.drop(['Pclass'], axis='columns')")
print(df.drop(['Pclass'], axis='columns'))
# Renaming columns
header("df.rename(columns = {'Pclass':'Class'}, inplace=True)")
df.rename(columns = {'Pclass':'Class'}, inplace=True)
print(df.head())

header("df.columns = ['Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey']")
df.columns = ['Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey', 'Hey']
print(df.head())

# Write to csv file
# df.to_csv('filename.csv')
