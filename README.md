# Is477 Fall2023 Final Project

IS477-Fall2023 final project repository.

## Members:

- Jacquelin Lai (shanrou2@illinois.edu)
- Zhifeng Wang (zhifeng5@illinois.edu)

## Overview:

## Contributions:

- Jacquelin: Complete Step 6, 7, 8, 10, 14(a,b,c,f), 15, 16, 17, and 18
- Zhifeng: Complete Step 1, 2, 3, 4, 5, 9, 11, 12 13, 14(d,e,g), profreed, and Step 19 (submission)

## Analysis:
We firstly made a directory "./result" in the repositary to store the output of the analysis.py. By reading the file winequality.csv into a dataframe, we are able to classify the numpy arrays of target variable and the feature variables. Later, we split the data into training data and testing data. By using the training data, we are able to utilize it to fit the Linear Regression model. We calculated that the Mean Squared Error, Root Mean Squared Error, and R-squared, and we exported them as a text file and stored in the result file. Finally, we created a plot graph, exported it as a plot.png file, and stored it in the result file.

## Workflow:

## Reproducing:

6. When using ydata-profiling, we need to install it through pip at terminal first.
    `pip install ydata-profiling`

## License:

### UCI Wine Quality Dataset License

License Selection: [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/legalcode)
This work is licensed under a Creative Commons Attribution 4.0 International License. This license allows others to remix, tweak, and build upon the work, as long as they credit me and license their new creations under the identical terms.

## References:

Cortez,Paulo, Cerdeira,A., Almeida,F., Matos,T., and Reis,J.. (2009). Wine Quality. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T.
