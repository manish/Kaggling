import matplotlib.pyplot as plt

def show_mnist_image(data):
    if data.shape != (28, 28):
        raise Exception ("'data' shape is {} when expected to be (28, 28)".format(data.shape))
    _, axes = plt.subplots()
    axes.imshow(data, cmap='gray', interpolation='nearest')