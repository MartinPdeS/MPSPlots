import numpy
from scipy import ndimage
import re

from MPSPlots.Utils import ToList


class Angle(object):

    def __init__(self, input, Unit='degree'):
        if Unit.lower() == 'degree':
            self.Degree = ToList([i if i is not None else numpy.nan for i in input])
            self.Radian = ToList([numpy.deg2rad(i) if i is not None else numpy.nan for i in input])

        if Unit.lower() == 'radian':
            self.Radian = ToList([i if i is not None else numpy.nan for i in input])
            self.Degree = ToList([numpy.rad2deg(i) if i is not None else numpy.nan for i in input])

        if len(self.Degree) == 1:
            self.Degree = ToList([self.Degree[0]])
            self.Radian = ToList([self.Radian[0]])


def Deg2Rad(Value):
    if Value is None: 
        return numpy.nan
    else: 
        return numpy.deg2rad(Value)


def Norm(Scalar):
    return numpy.sqrt(numpy.sum(numpy.abs(Scalar)**2))


def Normalize(Scalar):
    norm = Norm(Scalar)
    if norm == 0 or numpy.isnan(norm):
        return [0, 0, 0]
    else:
        return Scalar / norm


def InterpFull(Meshes, Scalar, Shape):

    Phi, Theta = numpy.mgrid[-numpy.pi / 2:numpy.pi / 2:complex(Shape[0]),
                          -numpy.pi:numpy.pi:complex(Shape[1])]

    Scalar = interp_at(Meshes.Phi.Radian,
                       Meshes.Theta.Radian,
                       Scalar.astype(numpy.complex).flatten(),
                       Phi.flatten(),
                       Theta.flatten(),
                       algorithm='linear',
                       extrapolate=True)

    return Scalar.reshape(Shape), Phi, Theta


def RescaleComplex(Input, Num):
    Scale = Num/Input.shape[0]
    InputReal = ndimage.interpolation.zoom(input=Input.real, zoom=(Scale), order=2)
    InputImag = ndimage.interpolation.zoom(input=Input.imag, zoom=(Scale), order=2)
    return InputReal + 1j * InputImag


def RotateComplex(Input, Rotation):
    InputReal = ndimage.rotate(Input.real, Rotation, reshape=False)
    InputImag = ndimage.rotate(Input.imag, Rotation, reshape=False)
    return InputReal + 1j * InputImag


def Angle2Direct(AngleVec: numpy.ndarray, k: float,) -> numpy.ndarray:

    RadSpace = numpy.deg2rad(AngleVec)

    FourierSpace = numpy.sin(RadSpace) * k / (2 * numpy.pi)

    fourier_unit = (FourierSpace[1] - FourierSpace[0]).__abs__()

    DirectSpace = numpy.fft.fftshift(numpy.fft.fftfreq(AngleVec.shape[0], d=fourier_unit))

    return DirectSpace


def Direct2Angle(DirectVec: numpy.ndarray, k: float) -> numpy.ndarray:

    direct_unit = (DirectVec[1] - DirectVec[0]).__abs__()

    FourierSpace = numpy.fft.fftshift(numpy.fft.fftfreq(DirectVec.shape[0], d=direct_unit))

    AngleVec = numpy.arcsin(2 * numpy.pi * FourierSpace / k) # conversion spatial frequency to angular space

    if numpy.isnan(AngleVec).any():
        raise Exception("Magnification too large.")

    return AngleVec * 180 / numpy.pi


def NA2Angle(NA: float) -> numpy.ndarray:
    if NA <= 1.0: 
        return numpy.arcsin(NA)
    if NA >= 1.0: 
        return numpy.arcsin(NA - 1) + numpy.pi / 2


def Direct2spherical(X, Y, MaxAngle):
    Z = 50 / numpy.tan(MaxAngle)

    _, Phi, Theta = Cart2Sp(X, Y, X * 0 + Z)

    return Phi, Theta


def Direct2Angle(X, Y, MaxAngle):
    MaxZ = numpy.max(X) / numpy.cos(MaxAngle)


def AngleUnit2DirectUnit(Angle, k):
    FourierSpace = numpynpnumpy.sin(Angle) * k / (2 * numpy.pi)

    fourier_unit = (FourierSpace[1] - FourierSpace[0]).__abs__()

    DirectSpace = numpy.fft.fftshift(numpy.fft.fftfreq(Angle.shape[0], d=fourier_unit))

    return DirectSpace


def Cart2Sp(x, y, z):
    R = numpy.sqrt(x**2 + y**2 + z**2)
    Phi = numpy.arcsin(z/R)
    Theta = numpy.arctan2(y, x)
    return R, Phi, Theta


def Sp2Cart(Phi, Theta, R=None):
    R = R if R is not None else Phi * 0 + 1
    x = R * numpy.cos(Phi) * numpy.cos(Theta)
    y = R * numpy.cos(Phi) * numpy.sin(Theta)
    z = R * numpy.sin(Phi)
    return x, y, z


def RotateY(Phi, Theta, Angle):
    x, y, z = Sp2Cart(Phi=Phi, Theta=Theta)
    xp = x * numpy.cos(Angle) + z * numpy.sin(Angle)
    yp = y
    zp = z * numpy.cos(Angle) - x * numpy.sin(Angle)
    return Cart2Sp(x=xp, y=yp, z=zp)


def RotateZ(Phi, Theta, Angle):
    x, y, z = Sp2Cart(Phi=Phi, Theta=Theta)
    xp = x * numpy.cos(Angle) - y * numpy.sin(Angle)
    yp = x * numpy.sin(Angle) + y * numpy.cos(Angle)
    zp = z
    return Cart2Sp(x=xp, y=yp, z=zp)


def RotateX(Phi, Theta, Angle):
    x, y, z = Sp2Cart(Phi=Phi, Theta=Theta)

    xp = x
    yp = y * numpy.cos(Angle) - z * numpy.sin(Angle)
    zp = y * numpy.sin(Angle) + z * numpy.cos(Angle)
    return Cart2Sp(x=xp, y=yp, z=zp)


def FormatStr(function):
    def wrapped(*args, **kwargs):
        args = (re.sub(r"\s+", "", arg.lower()) if isinstance(arg, str) else arg for arg in args)

        kwargs = {k: re.sub(r"\s+", "", v.lower()) if isinstance(v, str) else v for k, v in kwargs.items()}

        return function(*args, **kwargs)
    return wrapped


def GetSphericalMesh(Sampling, MaxAngle):

    x, y = numpy.mgrid[-50: 50: complex(Sampling), -50: 50: complex(Sampling)]
    z = 50 / numpy.tan(MaxAngle)
    _, theta, phi = Cart2Sp(x, y, x * 0 + z)

    return phi, theta


def Angle2Jones(Delta):
    val = numpy.exp(1j * Delta) * 2
    JonesVector = numpy.array([1, val])
    Norm = (numpy.sqrt(1 + numpy.abs(val)**2))
    return JonesVector / Norm


#-