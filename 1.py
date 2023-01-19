import pandas as pd
from sklearn.model_selection import train_test_split

# Load data from a tab-separated file
data = pd.read_csv("data.txt", sep="\t")

# Split the data into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2)

# Create a mapping between a label and a value
label_mapping = {'label1': 1, 'label2': 2, 'label3': 3}

# Use the mapping to convert labels in the data to numeric values
train_data['label'] = train_data['label'].map(label_mapping)
test_data['label'] = test_data['label'].map(label_mapping)

# Print the training and test data
print(train_data)
print(test_data)
