import numpy as np

def calculate(list):

    # helloooooooooooo
    # i'm trying to work
    if(len(list) < 9):
        raise ValueError('List must contain nine numbers.')

    arr = np.array(list)
    arr1 = arr.reshape(3, 3)

    calculations = {'mean': [np.mean(arr1, axis=0).tolist(), np.mean(arr1, axis=1).tolist(), np.mean(arr1).tolist()],
        'variance': [np.var(arr1, axis=0).tolist(), np.var(arr1, axis=1).tolist(), np.var(arr1).tolist()],
        'standard deviation': [np.std(arr1, axis=0).tolist(), np.std(arr1, axis=1).tolist(), np.std(arr1).tolist()],
        'max': [np.max(arr1, axis=0).tolist(), np.max(arr1, axis=1).tolist(), np.max(arr1).tolist()],
        'min': [np.min(arr1, axis=0).tolist(), np.min(arr1, axis=1).tolist(), np.min(arr1).tolist()],
        'sum': [np.sum(arr1, axis=0).tolist(), np.sum(arr1, axis=1).tolist(), np.sum(arr1).tolist()]
    }

    return calculations