import numpy as np

ab = 65.27 #https://doi.org/10.1557/s43578-021-00113-9
ac = 70.32 #https://doi.org/10.1016/j.tsf.2014.02.044
r = 0.13826
h = 1.0
d = 2.0

ab *= np.pi/180
ac *= np.pi/180

print('2D geometry:')
print('Fillet x = ', r*np.sin(np.pi/2-ac))
print('Fillet y = ', r*(1-np.cos(np.pi/2-ac)))
print('Edge y = ', r*(1-np.cos(np.pi/2-ac))+(d-r*np.sin(np.pi/2-ac))/np.tan(ac))

print('3D geometry:')
ab2 = np.arctan(np.tan(ab)/np.cos(60*np.pi/180))
print('Top tip x = ', (h+r/np.sin(ab2)-r)*np.tan(ab2))
print('Bottom radius: ', r*np.cos(ab2))
print('Translate: ', r/np.sin(ab2)-r)