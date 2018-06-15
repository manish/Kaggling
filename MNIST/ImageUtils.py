import matplotlib.pyplot as plt

def show_mnist_image(data):
    if data.shape != (28, 28):
        raise Exception ("'data' shape is {} when expected to be (28, 28)".format(data.shape))
    plt.imshow(data, cmap='gray', interpolation='nearest') 