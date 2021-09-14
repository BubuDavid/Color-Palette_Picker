import numpy as np
import cv2
from sklearn.cluster import KMeans

def get_palette(img_path, n_colors):
    # Loading the image and transform it
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

    # Flat the image
    flat_img = img.reshape((img.shape[0] * img.shape[1], 3))
    
    # Define and train the model
    clt = KMeans(n_colors)
    clt.fit(flat_img)

    # Get the colors
    colors = clt.cluster_centers_.astype(int).tolist()
    
    # Make an histogram
    n_bins = np.arange(0, clt.n_clusters + 1)
    data_hist = clt.labels_
    (hist, _) = np.histogram(data_hist, bins=n_bins)
    hist = hist.astype(float)
    
    # Normalize the data
    hist /= hist.sum()

    return colors, list(hist)
