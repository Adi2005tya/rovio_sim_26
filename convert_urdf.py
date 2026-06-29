import numpy as np
from scipy.spatial.transform import Rotation as R
import xml.etree.ElementTree as ET

# Load the URDF
tree = ET.parse('/home/podalanga/Codes/ros/stonefish_trial/src/stonefish_ros2/resources/scenes/rovio_v3_urdf.urdf')
root = tree.getroot()

# Transformation matrix from ENU to NED
R_enu_to_ned = np.array([[0, 1, 0],
                         [1, 0, 0],
                         [0, 0, -1]])

# Function to transform position
def transform_position(xyz):
    p = np.array([float(x) for x in xyz.split()])
    p_ned = R_enu_to_ned @ p
    return ' '.join(f'{v:.12e}' for v in p_ned)

# Function to transform inertia
def transform_inertia(ixx, ixy, ixz, iyy, iyz, izz):
    I = np.array([[float(ixx), float(ixy), float(ixz)],
                  [float(ixy), float(iyy), float(iyz)],
                  [float(ixz), float(iyz), float(izz)]])
    I_ned = R_enu_to_ned @ I @ R_enu_to_ned.T
    return I_ned

# Iterate over all inertial elements
for inertial in root.findall('.//inertial'):
    origin = inertial.find('origin')
    if origin is not None:
        xyz = origin.get('xyz')
        if xyz:
            origin.set('xyz', transform_position(xyz))
        # rpy is 0 0 0, so no change
    
    inertia = inertial.find('inertia')
    if inertia is not None:
        ixx = inertia.get('ixx')
        ixy = inertia.get('ixy')
        ixz = inertia.get('ixz')
        iyy = inertia.get('iyy')
        iyz = inertia.get('iyz')
        izz = inertia.get('izz')
        if ixx and ixy and ixz and iyy and iyz and izz:
            I_ned = transform_inertia(ixx, ixy, ixz, iyy, iyz, izz)
            inertia.set('ixx', f'{I_ned[0,0]:.12e}')
            inertia.set('ixy', f'{I_ned[0,1]:.12e}')
            inertia.set('ixz', f'{I_ned[0,2]:.12e}')
            inertia.set('iyy', f'{I_ned[1,1]:.12e}')
            inertia.set('iyz', f'{I_ned[1,2]:.12e}')
            inertia.set('izz', f'{I_ned[2,2]:.12e}')

# Change robot name to urdf_v3
root.set('name', 'urdf_v3')

# Write to new file
tree.write('/home/podalanga/Codes/ros/stonefish_trial/src/stonefish_ros2/resources/scenes/urdf_v3.urdf', encoding='utf-8', xml_declaration=True)