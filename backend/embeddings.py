import numpy as np

def get_embedding(text):
    # Dummy embedding: convert chars to ints, pad to 128
    vec = np.array([ord(c) for c in text[:128]])
    if len(vec) < 128:
        vec = np.pad(vec, (0, 128 - len(vec)))
    return vec.astype('float32')
