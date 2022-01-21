from model import model
from cleanup_data import X_test, y_test

if __name__ == "__main__":
    print("Evaluate on test data")
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy'],
    )

    model.load_weights('./models/bestmodel.h5')
    results = model.evaluate(X_test, y_test, batch_size=2)
    print("test loss, test acc:", results)
