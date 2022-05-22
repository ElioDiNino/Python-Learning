# Import the pandas and time databases
import pandas as pd
import time

# Code to force Python to display all data
pd.set_option('display.max_columns', 40)
pd.set_option('display.max_rows', 900)
pd.set_option('display.width', 1000)

# Import 2 data files
df = pd.read_csv("train.csv")
df2 = pd.read_csv("test.csv")

# Function to view my data more clearly
def header():
    print('-' * 80)

header()
period = int(input("Set how long you want the delay to be between each step, in seconds: "))
# View my data (fullscreen the Python Shell window to see all the data)
print("View the first spreadsheet ('train.csv')", end = header())
print(df, end=header())
time.sleep(period)
print("View the second spreadsheet ('test.csv')", end = header())
print(df2, end=header())
time.sleep(period)

# Decide what data is important
import matplotlib.pyplot as plt
import seaborn as sn
done = False
print("Use 'matplotlib' with a 'while' loop to display a variety of graphs", end=header())
while done == False:
    print('Select a graph to view', end=header())
    print('A. Sex vs Survival\nB. Class vs Survival\nC. Age vs Survival\nQ. Quit\n')
    choice = input('Select a letter: ')
    if choice.lower() == 'a' or choice.lower() == 'a.':
        sn.countplot(df['Sex'], hue=df['Survived'])
        plt.show()
    elif choice.lower() == 'b' or choice.lower() == 'b.':
        sn.countplot(df['Pclass'], hue=df['Survived'])
        plt.show()
    elif choice.lower() == 'c' or choice.lower() == 'c.':
        sn.countplot(df['Age'], hue=df['Survived'])
        ax = plt.gca()
        ax.axes.get_xaxis().set_ticks([])
        plt.show()
    elif choice.lower() == 'q' or choice.lower() == 'q.':
        done = True
df4 = pd.crosstab(pd.qcut(df['Fare'], 3), columns=df['Pclass'])
print("Compare the class (Pclass) with ranges of fares", end=header())
print(df4, end=header())
time.sleep(period)

# Display only my desired columns
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']]
df2 = df2[['Survived','Pclass', 'Sex', 'Age', 'Fare']]

# Rename column "Pclass" to "Class" and show a preview
df.rename(columns = {'Pclass':'Class'}, inplace=True)
df2.rename(columns = {'Pclass':'Class'}, inplace=True)
print("Rename 'Pclass' to 'Class' and view the top five rows of the first spreadsheet", end=header())
print(df.head(), end=header())
time.sleep(period)
print("Rename 'Pclass' to 'Class' and view the top five rows of the second spreadsheet", end=header())
print(df2.head(), end=header())
time.sleep(period)

# Analyze the data from the first file and replace missing ages
# with the average age then re-analyze to comfirm the changes
print("Check the statistics of the first spreadsheet, fill the blank columns\nwith the average age, re-check the statistics to make sure it worked", end=header())
print(df.describe(), end=header())
df = df.fillna(df.Age.mean())
print(df.describe(), end=header())
time.sleep(period)

# Same thing but with the other file
print("Check the statistics of the second spreadsheet, fill the blank columns\nwith the average age, re-check the statistics to make sure it worked", end=header())
print(df2.describe(), end=header())
df2 = df2.fillna(df.Age.mean())
print(df2.describe(), end=header())
time.sleep(period)

# Set a target I want my algorithm to solve for
target = df['Survived']
target2 = df2['Survived']

# Hide that column
print("Hide the 'Survived' column of the first spreadsheet and confirm it worked", end=header())
df = df.drop(['Survived'], axis='columns')
print(df.head(), end=header())
time.sleep(period)

# Import LabelEncoder to automatically covert words in column "Sex" to values
from sklearn.preprocessing import LabelEncoder
le_sex = LabelEncoder()
print("Convert the values in the 'Sex' column to numerical values for both spreadsheets", end=header()) 
df['Sex'] = le_sex.fit_transform(df['Sex'])
print(df.head(), end=header())
df2['Sex'] = le_sex.fit_transform(df2['Sex'])
print(df2.head(), end=header())
time.sleep(period)

# Import RandomForest and specify how many decision branches to make
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=50, criterion='entropy', min_samples_split=16)

# Specify the data to analyze and train on
print("Use a random forest on the training data (the first spreadsheet)", end=header())
print(model.fit(df, target), end=header())
time.sleep(period)

# Specify the data to test the algorithm on and return an accuracy score
print("Evaluate the random forest by testing it against the testing data (the second\nspreadsheet)", end=header())
pred = df2.loc[:417,['Class', 'Sex', 'Age', 'Fare']]
score = model.score(pred, target2)*100
print('Model Score: ',score,'%', end=header())
time.sleep(period)

# Display what the algorithm determined the most important variables to be
print("Display all the variables in the order of their importance", end=header())
print(pd.concat((pd.DataFrame(df.columns, columns = ['Variable']), 
           pd.DataFrame(model.feature_importances_, columns = ['Importance'])), 
          axis = 1).sort_values(by='Importance', ascending = False)[:20], end=header()) 
time.sleep(period)

# Nicely display the success and results of the algorithm 
from sklearn.metrics import confusion_matrix
y_predicted = model.predict(pred)
cm = confusion_matrix(target2, y_predicted)
plt.figure('Titanic Random Forest Results',figsize=(5,5))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()

# Let the user play around with the algorithm
print('Now it\'s your turn to test the algorithm', end=header())
done = False
while done == False:
    pclass = input('\nPick a class between 1 and 3: ')
    if int(pclass) > 3 or int(pclass) < 1:
        pclass = input('Try again, pick a class between 1 and 3: ')
    sex = input('Pick a sex(0 = female, 1 = male): ')
    if int(sex) > 1 or int(sex) < 0:
        sex = input('Try again, pick a sex(0 = female, 1 = male): ')
    age = input('Pick an age: ')
    fare = input('Pick how much their ticket cost: ')
    predict = model.predict([[pclass, sex, age, fare]])
    if predict == [1]:
        print('\nI\'m',score,'% sure that this alius would\'ve survived\n')
    else:
        print('\nI\'m',score,'% sure that this alius would\'ve died\n')
    choice2 = input('Want to try again? ')
    if choice2.lower() == 'no' or choice2.lower() == 'n':
        done = True
