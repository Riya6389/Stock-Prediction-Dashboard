import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Create a simple model
model = Sequential([
    Dense(10, activation='relu', input_shape=(1,)),
    Dense(1)  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Dummy training data
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Train the model (quick dummy training)
model.fit(X, y, epochs=10, verbose=1)

# Save the model as 'stock_model.h5'
model.save('stock_model.h5')

print("✅ Dummy model saved as 'stock_model.h5'")
