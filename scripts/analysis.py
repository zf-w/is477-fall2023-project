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
    'alcohol',
    'is red or white wine'
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

output_directory = results_dir

# save plot
plot_file = 'plot.png'
plt.savefig(os.path.join(output_directory, plot_file))

# summary statistics utility function

def df_to_string(df):
    col_names = df.columns
    def cal_col_width(col_values: pd.core.series, col_name: str):
        max_val = len(col_name)
        for values in col_values.values:
            curr_len = len(str(values))
            if max_val < curr_len:
                max_val = curr_len
        return max_val
    col_widths = np.zeros(len(col_names), dtype=int)

    index_width = cal_col_width(df.index, 'Index')
    index_template = "| {:<" + str(index_width) + "} |"
    values_template = ""
    for i, col_name in enumerate(col_names):
        col_widths[i] = cal_col_width(df[col_name], col_name)
        values_template += " {:>" + str(col_widths[i]) + "} |"

    def row_to_str(values, index):
        return index_template.format(index) + values_template.format(*values) + '\n'
    
    
    str_ans = ""
    str_ans += row_to_str(col_names, 'Index')
    str_ans += row_to_str(['-' * w for w in col_widths], '-' * index_width)
    for i in range(len(df)):
        str_ans += row_to_str(df.iloc[i].values, df.index[i])
    return str_ans


# simple regression result
output_file = 'summary_stats_and_regression_result.md'

with open(os.path.join(output_directory, output_file), 'w') as file:
    file.write('# Summary Statistics\n\n')
    file.write(df_to_string(df.describe().T))
    file.write('\n\n# Regression Results\n\n')
    file.write(f'Mean Squared Error: {mse}\n')
    file.write(f'Root Mean Squared Error: {rmse}\n')
    file.write(f'R-squared: {r2}\n')
