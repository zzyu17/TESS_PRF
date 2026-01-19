import numpy as np
import matplotlib.pyplot as plt

import src.PRF as PRF




# Suppose the following for a TPF of interest
cam = 2
ccd = 2
sector = 1

row = 513.9
col = 45.1

rownum = np.floor(row)
colnum = np.floor(col)

shape = (13,13)
sourcerow = np.floor(shape[0]/2) + row % 1 - 0.5
sourcecol = np.floor(shape[1]/2) + col % 1 - 0.5


if sector < 4:
    localdatadir = "/mnt/d/Python/Research/OptAp/data/tess/models/prf_fitsfiles/start_s0001/"
else:
    localdatadir = "/mnt/d/Python/Research/OptAp/data/tess/models/prf_fitsfiles/start_s0004/"


prf = PRF.TESS_PRF(cam,ccd,sector,colnum,rownum, localdatadir)

# See what this looks like in the center of a TPF
resampled = prf.locate(sourcecol, sourcerow, shape) # Assume integer pixel center

plt.imshow(resampled, origin='lower')
plt.title(f"TESS_PRF\nCamera: {cam}, CCD: {ccd}, Row: {row}, Column: {col}")
plt.savefig(f"TESS_PRF_Cam-{cam}_CCD-{ccd}_Sector-{sector}_Row-{row}_Col-{col}.png")

prf_max = np.max(resampled)
prf_max2 = np.partition(resampled.flatten(), -2)[-2]
ratio = prf_max / prf_max2
print(f"Max PRF value at Row {row}, Col {col}: {prf_max:.8e}")
print(f"Second Max PRF value at Row {row}, Col {col}: {prf_max2:.8e}")
print(f"Ratio of Max to Second Max: {ratio:.8f}")