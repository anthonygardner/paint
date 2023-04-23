from __future__ import annotations

import numpy as np


class Array:
    array: np.ndarray


class Vector3(Array):
    x: float
    y: float
    z: float
    
    @staticmethod
    def zeros(self) -> Vector3:
        return np.zeros((3, 1))


class Quaternion(Array):
    w: float
    x: float
    y: float
    z: float


class Matrix3(Array):
    xx: float
    xy: float
    xz: float

    yx: float
    yy: float
    yz: float

    zx: float
    zy: float
    zz: float


class Matrix4(Array):
    ww: float
    wx: float
    wy: float
    wz: float

    xw: float
    xx: float
    xy: float
    xz: float
    
    yw: float
    yx: float
    yy: float
    yz: float
    
    zw: float
    zx: float
    zy: float
    zz: float
