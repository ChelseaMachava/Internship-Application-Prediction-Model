from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

mydata = loadtxt("CleanData.csv", delimiter=",", skiprows=1)
x = mydata[:,0:6]
y = mydata[:,6]

model = Sequential()
model.add(Dense(4, input_dim=6, activation='relu'))
model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x, y, epochs=100, batch_size=35)

_, accuracy = model.evaluate(x, y)
print("Accuracy: ", accuracy)

predictions = model.predict(x)
for i in range(5):
   print(x[i].tolist(), " predicts", predictions[i], " ACTUAL :", y[i])

model.save("Trained_model.h5")

