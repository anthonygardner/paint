class Array:
    data: List[float]

class Vector3(Array):
    x: float
    y: float
    z: float


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
