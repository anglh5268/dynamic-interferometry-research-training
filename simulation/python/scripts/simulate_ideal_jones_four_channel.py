import numpy as np
from src.phase_processing import decode_wrapped_phase
from src.polarization import create_opposite_circular_fields, project_to_analyzer

phase_rad = np.array([np.pi/3])

intensity_object = 1.0
intensity_reference = 1.0

jones_object, jones_reference = create_opposite_circular_fields(phase_rad, intensity_object, intensity_reference)

analyzer_angles = [0.0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]

jones_channel = []
scalar_channel = []

for theta_rad in analyzer_angles:
    a_object = project_to_analyzer(jones_object, theta_rad)
    a_reference = project_to_analyzer(jones_reference, theta_rad)

    i_jones = np.abs(a_object + a_reference) ** 2
    i_scalar = 1 + np.cos(phase_rad + 2 * theta_rad)

    jones_channel.append(i_jones)
    scalar_channel.append(i_scalar)

i_0, i_45, i_90, i_135 = jones_channel

phase_decoded = decode_wrapped_phase(i_0, i_45, i_90, i_135)

print("Jones channels:", jones_channel)
print("Scalar channels:", scalar_channel)
print("Decoded phase:", phase_decoded)


