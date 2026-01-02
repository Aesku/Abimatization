from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm

def get_colors(nfiles,colormap='rainbow'):
    cmap = cm.get_cmap(colormap)
    colors = []
    for j in range(nfiles):
        colors.append(cmap( 1.0*(j+1.0)/nfiles ) )
    return colors


fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.15,0.15,0.8,0.8])

NORMALIZE = True
norm = 0.0
FS = 16
CMAP = 'Reds'
Qs = [1,2,3,4,7,5,1]
path = '.'
x_array = np.arange(len(Qs))
JOBS = [
'Xc10RyXb1-200Bc5RyBb60-80_GW',
'Xc20RyXb1-200Bc5RyBb60-80_GW',
'Xc20RyXb1-100Bc5RyBb60-80_GW',
'Xc20RyXb1-200Bc5RyBb60-80',
]
#JOBS = [
#'Xc20RyXb1-200Bc5RyBb60-80_GW'
#]
colors = get_colors(len(JOBS), colormap = CMAP)
states = 4
for i,JOB in enumerate(JOBS):
    modes = []
    for s in np.arange(states): modes.append([])
    if NORMALIZE: norm = np.loadtxt(path + '/o-%s.Esort_q1_slepc_bse'%JOB)[0,0]
    for j,q in enumerate(Qs):
        energies = []
        BSEtype = 'Esort_q%s_slepc_bse'%q
        data = np.loadtxt(path + '/o-%s.%s'%(JOB,BSEtype))
        counter_data = 0
        counter_states = 0
        break_states = False
        for s in np.arange(states):
            #1. Start from the first state
            deg = data[counter_data,1]
            for c in np.arange(deg):
#                ax.scatter(j,((data[counter_data,0]-norm)*1000),color = colors[i], label = JOB)
                modes[counter_states].append((data[counter_data,0]-norm)*1000)
                counter_states = counter_states+1
                if counter_states == states:
                   break_states = True
                   break
            if break_states: break
            counter_data = counter_data+1
    for s in np.arange(states):
        ax.plot(x_array,modes[s],'-o',color = colors[i])
    ax.plot(x_array[0],modes[s][0],'-o',color = colors[i],label = JOB)
ax.legend(fontsize=FS)
plt.show()
exit()        
