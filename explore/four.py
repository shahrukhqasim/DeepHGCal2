from models.sofia_model import sofiamodel
import keras
import gzip
import pickle
from keras import backend as K
from visualize.basic_visualizer import BasicVisualizer
from explore.grab_interesting_points import GrabMaximumPoints
import numpy as np


# 6 sensors per big pixel (b)
# In each sensor, position (2), energy, time

# 2 global position

# Initialize and load model
keras_inputs = []
shapes = [(1,),(13, 13, 52, 26), (1,)]
for s in shapes:
    keras_inputs.append(keras.layers.Input(shape=s))
model = sofiamodel(keras_inputs, 5, 2)
model.load_weights('/home/srq2/Models/HGCal/KERAS_check_model_last.h5')
print("Model loaded!")

print(model.summary())

# Load data
with gzip.open('/home/srq2/Datasets/one_hgcal/data_file.pklz', 'rb') as f:
    print("Loading input...")
    input_data = pickle.load(f)
    print("Input loaded!")

X = input_data['x']
Y = input_data['y']

for i in range(len(X)):
    X[i] = X[i][0:2]


# inp = model.input                                           # input placeholder
# outputs = [layer.output for layer in model.layers]          # all layer outputs
#
# print(len(outputs))
names = ['conv3d_3', 'conv3d_4', 'conv3d_5']

outputs = []

for name in names:
    layer_model = keras.Model(inputs=model.input, outputs=model.get_layer(name).output)
    layer_output = layer_model.predict(X)
    outputs.append(layer_output)

visualizer = BasicVisualizer(GrabMaximumPoints())
for o in outputs:
    print(np.shape(o))
    visualizer.add_layer(o[0])
visualizer.show()