import numpy as np
import math

def read_extrinsic_param(path_to_file):
    """
    Read the extrinsic parameters from a *.ro file.

    Parameters
    ----------
    path_to_file : str
        path of the *.ro file
    Returns
    -------
    _ : float
        X0, Y0, Z0, r11, r12, r13, r21, r22, r23, r31, r32, r33
    """
    parameters = np.loadtxt(path_to_file)

    cam_X0 = float(parameters[1])
    cam_Y0 = float(parameters[2]) #TODO: in m
    cam_Z0 = float(parameters[3])#TODO: in m
    omega = float(parameters[4])*math.pi/180 #TODO: in rad konvertieren
    phi = float(parameters[5])*math.pi/180 #TODO: in rad konvertieren
    kappa = float(parameters[6])*math.pi/180 #TODO: in rad konvertieren

    # Koeffizienten der Rotationsmatrix berechnen
    r11 = np.cos(phi) * np.cos(kappa)
    r12 = -np.cos(phi) * np.sin(kappa)
    r13 = np.sin(phi)
    r21 = (np.cos(omega) * np.sin(kappa)) + (np.sin(omega) * np.sin(phi) * np.cos(kappa))
    r22 = (np.cos(omega) * np.cos(kappa)) - (np.sin(omega) * np.sin(phi) * np.sin(kappa))
    r23 = -np.sin(omega) * np.cos(phi)
    r31 = (np.sin(omega) * np.sin(kappa)) - (np.cos(omega) * np.sin(phi) * np.cos(kappa))
    r32 = (np.sin(omega) * np.cos(kappa)) + (np.cos(omega) * np.sin(phi) * np.sin(kappa))
    r33 = np.cos(omega) * np.cos(phi)

    return cam_X0, cam_Y0, cam_Z0, r11, r12, r13, r21, r22, r23, r31, r32, r33

def read_intrinsic_param(path_to_file):
    """"
    Read the intrinsic parameters from a *.txt file.

    Parameters
    ----------
    path_to_file : str
        path of the *.txt file
    Returns
    -------
    _ : float
        ck_x, ck_y, principal_point_x, principal_point_y
    """
    cam_matrix = np.loadtxt(path_to_file)
    ck_x = float(cam_matrix[0][0])
    ck_y =  float(cam_matrix[1][1]) #TODO: in Pixel
    principal_point_x = float(cam_matrix[0][2])#TODO: in Pixel
    principal_point_y = float(cam_matrix[1][2])#TODO: in Pixel
    return ck_x, ck_y, principal_point_x, principal_point_y