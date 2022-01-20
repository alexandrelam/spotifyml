import pandas as pd
import datetime

from sklearn.model_selection import train_test_split
from sklearn import preprocessing

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import TensorBoard


df = pd.read_csv("./dataset/spotify_dataset_train.csv")

pd.set_option('display.max_columns', 500)

X_data = df.iloc[:, 1:-1]
y_data = df.iloc[:, -1:]

le = preprocessing.LabelEncoder()
enc = preprocessing.OneHotEncoder()

X_data['explicit'] = le.fit_transform(X_data['explicit'])
#X_data['release_date'] = le.fit_transform(X_data['release_date'])

y_data = y_data.apply(le.fit_transform)
enc.fit(y_data)
y_data = enc.transform(y_data).toarray()

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2, random_state=777)


min_max_scaler = preprocessing.MinMaxScaler()
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = min_max_scaler.fit_transform(X_train)
X_test = min_max_scaler.fit_transform(X_test)

print(X_train)

model = Sequential([
    Dense(256, activation='relu', input_shape=(15,)),
    Dense(777, activation='relu'),
    Dense(22, activation='softmax'),
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(
    log_dir=log_dir, histogram_freq=1)

model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=25,
    callbacks=[tensorboard_callback]
)

model.save_weights(f'models/{datetime.datetime.now()}-model.h5')

model.evaluate(
    X_test,
    y_test
)
