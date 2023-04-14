import numpy as np

from typing import Union

def euler_to_rotation_matrix(euler_angles: Union[tuple, list]):
    """
    Converts euler angles (omega phi kappa) in degrees (rotated axis) into a rotation matrix (Luhmann, 2014: 40, 2.26)

    Parameters
    ----------
    euler_angles : tuple | list
        euler angles omega, phi, kappa in degrees as sequence

    Returns
    -------
    _ : np.ndarray
        Rotation matrix (3x3) as array
    """
    s_o, s_p, s_k = [np.sin(i*np.pi/180.0) for i in euler_angles]
    c_o, c_p, c_k = [np.cos(i*np.pi/180.0) for i in euler_angles]
    return np.array([[c_p*c_k, -c_p*s_k, s_p],
                     [c_o*s_k + s_o*s_p*c_k, c_o*c_k - s_o*s_p*s_k, -s_o*c_p],
                     [s_o*s_k - c_o*s_p*c_k, s_o*c_k + c_o*s_p*s_k, c_o*c_p]])



def rotation_matrix_to_euler(r):
    """
    Converts a rotation matrix into omega phi and kappa [deg] (rotated axis) (Craig, 1989)

    Parameters
    ----------
    r : np.ndarray
        Rotation matrix

    Returns
    -------
    _ : list
        Euler angles [omega, phi, kappa] in degree.
    """
    p = np.atan2(r[0, 2], (r[1, 2]**2 + r[2, 2]**2)**0.5)
    c_p = np.cos(p)
    if c_p != 0.0:
        o = np.atan2(-r[1, 2]/c_p, r[2, 2]/c_p)
        k = np.atan2(-r[0, 1]/c_p, r[0, 0]/c_p)
    else:  # singularity
        o = 0.0
        k = np.atan2(r[1, 1], r[2, 1]) * [1 if p == np.pi/2 else -1][0]
    return np.array([i*180.0/np.pi for i in [o, p, k]])
