import scipy
import numpy as np

def basis_fn(degree, order, polar, azimuth):
    """ Creates a basis function based on spherical harmonics.
    Parameters:
        degree - Degree of spherical harmonic (l) [int]
        order  - Order of spherical harmonic (m) [int]
        polar  - Polar angle for evaluation (alpha') [rad]. Can be numpy array.
        azimuth - Azimuth angle for evaluation (phi') [rad]. Can be numpy array.

    Returns f, an
    """

    l = degree; m = order

    if m < 0:
        Y_mode = scipy.special.sph_harm(abs(m), l, azimuth, polar) 
        y_lm = 2 ** (0.5) * (-1) ** m * Y_mode.imag

    elif m == 0:
        Y_mode = scipy.special.sph_harm(m, l, azimuth, polar)
        y_lm = Y_mode.real

    else:
        Y_mode = scipy.special.sph_harm(m, l, azimuth, polar)
        y_lm =  2 ** (0.5) * (-1) ** m * Y_mode.real

    return y_lm

