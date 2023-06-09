import os


def test_mnist_dataset(A_dataset):
    dataset_path = A_dataset

    train_images_path = os.path.join(dataset_path, "train-images-idx3-ubyte")
    assert os.path.isfile(train_images_path)

    train_labels_path = os.path.join(dataset_path, "train-labels-idx1-ubyte")
    assert os.path.isfile(train_labels_path)

    test_images_path = os.path.join(dataset_path, "t10k-images-idx3-ubyte")
    assert os.path.isfile(test_images_path)

    test_labels_path = os.path.join(dataset_path, "t10k-labels-idx1-ubyte")
    assert os.path.isfile(test_labels_path)

    assert True
