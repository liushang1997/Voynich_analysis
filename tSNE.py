import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import os

if os.path.exists('X_embedded.npy'):
    X_embedded = np.load('X_embedded.npy')
else:
    X = np.load('vec_array.npy')
    X_embedded = TSNE(n_components=2).fit_transform(X)
    np.save('X_embedded.npy', X_embedded)

np.array(X_embedded)

x_plot, y_plot = [], []
for i in range(len(X_embedded)):
    x_plot.append(X_embedded[i][0])
    y_plot.append(X_embedded[i][1])

plt.scatter(x_plot, y_plot)
plt.title('t-SNE Visualization of High-Dimensional Word Vectors')
plt.savefig('scatter.png', dpi=800)
