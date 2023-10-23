import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import generateDatasets as gd
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

# Create the datasets
gd.generate_train_data()
gd.generate_test_data()
