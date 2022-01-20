from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(256, activation='relu', input_shape=(15,)),
    Dense(777, activation='relu'),
    Dense(22, activation='softmax'),
])
