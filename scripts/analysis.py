import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

results_dir = './results'
os.makedirs(results_dir, exist_ok=True)


df =  pd.read_csv("./data/winequality.csv")

# specify target and feature variables
target = ['quality']
features = [
    'fixed acidity',
    'volatile acidity',
    'citric acid',
    'residual sugar',
    'chlorides',
    'free sulfur dioxide',
    'total sulfur dioxide',
    'density',
    'pH',
    'sulphates',
    'alcohol'
]

# create numpy arrays
X = df[features].to_numpy()
y = df[target].to_numpy().ravel()

# scale the data
scale = StandardScaler()
scale.fit(X)
X = scale.transform(X)

# create train and test datasets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)


# create a linear classificiation model
lr = LinearRegression()

# fit the models
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# Data Analysis
print(df.describe())

# Calculate accuracy
mse = mean_squared_error(y_test, lr_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, lr_pred)


# Data Visualization for linear model
fig, (ax) = plt.subplots(1, 1)
fig.set_size_inches(5, 5)
fig.set_dpi(100)

# add overall title
fig.suptitle('Predicted versus Actual')

# create subplot for linear model
ax.scatter(y_test, lr_pred, color="dodgerblue")
ax.set_xlabel("Actual")
ax.set_ylabel("Predicted")
ax.grid(True, linestyle='--', color='lightgrey')
ax.axline((0, 0), slope=1, color="black")

# shot plot
plt.show()

output_directory = results_dir
output_file = 'model_accuracy.txt'
plot_file = 'plot.png'

with open(os.path.join(output_directory, output_file), 'w') as file:
    file.write(f'Mean Squared Error: {mse}\n')
    file.write(f'Root Mean Squared Error: {rmse}\n')
    file.write(f'R-squared: {r2}\n')
    
plt.savefig(os.path.join(output_directory, plot_file))