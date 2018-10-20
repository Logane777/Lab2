import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import cmath
razner=400

k=np.zeros((razner, razner), dtype=np.complex)

for kx in range (razner):
    for ky in range (razner):

        k[kx,ky]=kx+(ky)*1j       

data = pd.read_csv(r"v.csv")
data.head()
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
data.replace(['?'], 1, inplace = True)
data.replace(['L'], 1, inplace = True)
data.replace(['B'], 2, inplace = True)
data.replace(['R'], 3, inplace = True)


Z =np.sin(0.1*np.abs((L)))+np.sin(0.1*np.abs((B)))+np.sin(0.1*np.abs((R)))


im = plt.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
               origin='lower', extent=[-3, 3, -3, 3],
               vmax=abs(Z).max(), vmin=-abs(Z).max())

plt.savefig("d:\V4.pdf")
plt.show()