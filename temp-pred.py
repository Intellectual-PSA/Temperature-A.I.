from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Assume we have a DataFrame 'df' with historical data
# The 'features' columns could include data like time of day, weather conditions, etc.
# The 'temperature' column would include the observed temperature of the object

features = df.drop('temperature', axis=1)
target = df['temperature']

# Split the data into a training set and a test set
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=0)

# Train a linear regression model on the training data
model = LinearRegression()
model.fit(features_train, target_train)

# Use the model to predict the temperature for the next day/week
# 'new_data' would be a DataFrame with the same structure as 'features', but with data for the future
new_data = pd.DataFrame(...)  # Fill this in with your actual data
predictions = model.predict(new_data)

# If the predicted temperature is below 98, print a message
for prediction in predictions:
    if prediction < 98:
        print("The temperature is predicted to be below 98 degrees")
