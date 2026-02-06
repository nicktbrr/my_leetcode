from typing import List
import math

def min_3_dist(cords: List[List[int]]) -> List[List[int]]:

    coordinate_dict = {tuple(point): (point[0] ** 2 + point[1] ** 2) ** .5 for point in cords}
    res = []
    for key in sorted(coordinate_dict, key=coordinate_dict.get):
        res.append(list(key))

    return res[:3]
    # return sorted(cords, key=lambda x: (x[0]**2 + x[1]**2)**.5)[:3]

print(min_3_dist([[2,-1],[3,2],[4,1],[-1,-1],[-2,2]]))
