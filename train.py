import datetime

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import TensorBoard

from cleanup_data import X_train, X_test, y_train, y_test

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
    epochs=100,
    batch_size=25,
    callbacks=[tensorboard_callback]
)

model.save_weights(f'models/{datetime.datetime.now()}-model.h5')

model.evaluate(
    X_test,
    y_test
)
