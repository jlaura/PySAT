import numpy as np

from libpysat.derived.m3 import pipe_funcs as pf
from libpysat.utils.utils import generic_func
from libpysat.utils.utils import get_band_numbers

def bd620(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [419, 619, 749]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.bd620_func)

def bd1900(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [1408, 1898, 2498]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.bd1900_func)

def bd2300(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [1578, 2298, 2578]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.bd2300_func)

def h2o1(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [1578, 2538, 2978]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.h2o1_func)

def iralbedo(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [1578]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.iralbedo_func)

def mafic_abs(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [749, 950]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.mafic_abs_func)

def omh(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [749, 889]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.omh_func)

def olindex(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [650, 860, 1047, 1230, 1750]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.olindex_func)

def oneum_min(data, wv_array, continuum = None, continuum_args = ()):
    raise NotImplementedError()

def oneum_slope(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [699, 1579]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.oneum_slope_func)

def reflectance1(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [540]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.reflectance_func)

def reflectance2(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [749]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.reflectance_func)

def reflectance3(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [2778]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.reflectance_func)

def reflectance4(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [1578]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.reflectance_func)

def thermal_ratio(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [2538, 2978]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.thermal_ratio_func)

def thermal_slope(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [2538, 2978]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.thermal_slope_func)

def twoum_ratio(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [1578, 2538]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.twoum_ratio_func)

def twoum_slope(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [1578, 2538]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.twoum_slope_func)

def uvvis(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [419, 749]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.uvvis_func)

def visslope(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [419, 749]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.visslope_func)

def visuv(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [419, 749]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.visuv_func)

def visnir(data, wv_array, continuum = None, continuum_args = ()):
    wavelengths = [699, 1579]
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    return generic_func(data, wv_array, wavelengths, func = pf.visnir_func)

def calc_bdi_band(iteration, initial_band, step, data, wv_array):
    y = initial_band + (step*iteration)
    y_idx = get_band_numbers(wv_array, [y])[0]
    wavelengths = [wv_array[y_idx - 3], y, wv_array[y_idx + 3]]

    return generic_func(data, wv_array, wavelengths, func = bdi_func)

def bdi_generic(upper_limit, initial_band, step, data, wv_array, continuum = None, continuum_args = ()):
    limit = range(0, upper_limit)
    if continuum:
        continuum(data, wavelengths, continuum, continuum_args)
    band_list = [calc_bdi_band(i, initial_band, step, data, wv_array) for i in limit]
    return 1 - np.sum(band_list, axis = 0)


def bdi1000(data, wv_array, continuum = None, continuum_args = ()):
    return bdi_generic(27, 789, 20, data, wv_array, continuum=continuum, continuum_args=continuum_args)

def bdi2000(data, wv_array, continuum = None, continuum_args = ()):
    return bdi_generic(22, 1658, 40, data, wv_array, continuum = continuum, continuum_args=continuum_args)
