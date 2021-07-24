import pandas as pd
import numpy as np


def get_circumcircle_area(l, h):
    r = np.sqrt(l ** 2 + h ** 2) / 2
    return r ** 2 * np.pi


def wrapper(row):
    return get_circumcircle_area(row['Length'], row['Height'])


rects = pd.read_excel('C:/Temp/Rectangles.xlsx', index_col='ID')
rects['Circumcircle Area'] = rects.apply(wrapper, axis=1)
print(rects)
