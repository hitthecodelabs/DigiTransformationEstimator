import numpy as np

def vn_a(list_of_values, tasa_0):
    vna = 0
    for i, m in enumerate(list_of_values):
        vna+=(m/((1+tasa_0)**(i+1)))
    R = list_of_values + [vna]
    return R

def vn_a2(list_of_values, array, tasa_0, inv_0):
    vna = 0
    for i, m in enumerate(list_of_values):
        vna+=(m/((1+tasa_0)**(i+1)))
    return np.array([-inv_0] + list(list_of_values) + [vna + array[0]])


def fevp(arr_vp, tasa_inf):
    LL = []
    values_fen = arr_vp[1:-1]
    for indice, j in enumerate(values_fen):
        v1 = 1+(tasa_inf*100)
        v2 = v1**(-(indice+1))
        v3 = j*v2
        LL += [v3]
    return np.array(LL)

def vp2(list_of_values, tasa_0, tipo=None):
    vna = 0
    for i, m in enumerate(list_of_values):
        vna+=(m/((1+tasa_0)**(i+1)))
    return vna

def vp_e2(inv, arr_anios, tasa):
    arr1 = arr_anios[0, :]
    arr2 = arr_anios[1, :]
    arr3 = list((arr1-arr2)[1:])
    vp_fen = vp2(arr3, tasa)
    diff = vp_fen - inv
    return [-inv] + list(arr2[1:]) + [diff]

def fen2(ti, te, tasa_0):
    arr_ = np.array([ti, te])[:, :]
    arr_1 = arr_[0, :]
    arr_2 = arr_[1, :]
    arr_0 = [-te[0]] + list(arr_1-arr_2)[1:]
    vpe = vp2(list(arr_1-arr_2)[1:], tasa_0)
    return arr_0 + [vpe-te[0]]

def fevp2(arr_vp, tasa_inf):
    LL = []
    values_fen = arr_vp[1:]
    for indice, j in enumerate(values_fen):
        v1 = 1+(tasa_inf)
        v2 = v1**(-(indice+1))
        v3 = j*v2
        LL += [v3]
    return np.array(LL[:-1])

def fe_ac2(flujo_vp):
    cont = 0
    L = []
    for valor in flujo_vp:
        cont+=valor
        L.append(cont)
    return np.array(L)

