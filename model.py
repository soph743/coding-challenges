import pandas as pd

df = pd.read_csv('housing.csv')
df.drop(columns='ocean_proximity', inplace=True)
df.dropna(inplace=True)

y = df['median_house_value'] # dtype: float64
X = df.loc[:, df.columns != 'median_house_value']

# model 1: multiple linear regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X1_train, X1_test, y1_train, y1_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X1_train, y1_train)

# get intercepts and coefficients of regression line
print("intercept for linear regression: " + str(model.intercept_))
print("coefficients for linear regression: " + str(model.coef_))

# make predictions on the test set
y1_pred = model.predict(X1_test)

# model 2: random forest regression
from sklearn.ensemble import RandomForestRegressor

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

regressor = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    oob_score=True
)

regressor.fit(X2_train, y2_train)

# make predictions on the test set
print("out-of-bag score: " + str(regressor.oob_score_))

y2_pred = regressor.predict(X2_test)

# evaluation: mean squared error (MSE), R-squared
from sklearn.metrics import mean_squared_error, r2_score

print("----model comparison----")

print("1. multiple linear regression:")
mse_1 = mean_squared_error(y1_test, y1_pred)
print("     mean squared error (MSE): " + str(mse_1))
r2_1 = r2_score(y1_test, y1_pred)
print("     r-squared score: " + str(r2_1))

print("2. random forest regressor:")
mse_2 = mean_squared_error(y2_test, y2_pred)
print("     mean squared error (MSE): " + str(mse_2))
r2_2 = r2_score(y2_test, y2_pred)
print("     r-squared score: " + str(r2_2))

print("comparison:")

mse_scores = {'linear regression': mse_1, 'random forest regressor': mse_2}
r2_scores = {'linear regression': r2_1, 'random forest regressor': r2_2}

best_mse = min(mse_scores.values())
best_r2 = max(r2_scores.values())

best_mse_model = list(mse_scores.keys())[list(mse_scores.values()).index(best_mse)]
best_r2_model = list(r2_scores.keys())[list(r2_scores.values()).index(best_r2)]

worse_mse = [val for val in mse_scores.values() if val != best_mse]
worse_r2 = [val for val in r2_scores.values() if val != best_r2]

print(f"model {best_mse_model} had the better score (-{worse_mse[0] - best_mse}) for mean squared error")
print(f"model {best_r2_model} had the better score (+{best_r2 - worse_r2[0]}) for r-squared")




