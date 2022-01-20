import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing


df = pd.read_csv("./dataset/spotify_dataset_train.csv")

pd.set_option('display.max_columns', 500)

X_data = df.iloc[:, 1:-1]
y_data = df.iloc[:, -1:]

le = preprocessing.LabelEncoder()
enc = preprocessing.OneHotEncoder()

X_data['explicit'] = le.fit_transform(X_data['explicit'])

y_data = y_data.apply(le.fit_transform)
enc.fit(y_data)
y_data = enc.transform(y_data).toarray()

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2)


scaler = preprocessing.StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)
