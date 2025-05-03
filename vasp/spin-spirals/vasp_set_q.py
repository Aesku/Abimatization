import numpy as np
from os import path, system, mkdir, system
import shutil

def get_path(path):
    vectors = []
    vectors.append(path[0])
    for i,v in enumerate(path):
        if i == len(path)-2:
           np.savetxt('Path.txt',vectors)
           return vectors[:-1]
        else:
           v_diff = [] 
           for v_i, v_f in zip(v,path[i+1]):
               v_diff.append(v_f-v_i)
           Nsteps = path[-1][i]
           for j in np.arange(Nsteps):
               new_vector = []
               for v_i, p in zip(v,v_diff):
                   new_vector.append(v_i + ((1.0*j+1.0)/Nsteps)*p)
               vectors.append(new_vector)
    return vectors[:-1]

Path = [[0.5,0.5,0.0],
        [0.5,0.0,0.0],
        [0.0,0.0,0.0],
        [0.0,0.5,0.0],
        [0.5,0.5,0.0],
        [0.0,0.0,0.0],[8,8,8,8,8]]

Qs = get_path(Path)
#print(Qs)
m_0 = 3.00

def set_qspiral_string(q):
    qspiral_string = 'QSPIRAL = %8.4lf  %8.4lf  %8.4lf' % (q[0],q[1],q[2])
    return qspiral_string

def set_incar(qspiral_string):
    incar = open('INCAR','r').readlines()
    incar.append('%s \n' % qspiral_string)
    return incar

def set_run_folder(q,incar):
#    folder_name = 'q%s_%s_%s' %(q[0],q[1],q[2])
    folder_name = 'q%.4f_%.4f_%.4f' %(q[0],q[1],q[2])
    print(folder_name)
    print(path.isdir(folder_name))
    if not path.isdir(folder_name):
       print('creating folder..')
       mkdir(folder_name)
    shutil.copy('POTCAR',folder_name)    
    shutil.copy('POSCAR',folder_name)    
    shutil.copy('KPOINTS',folder_name)    
#    shutil.copy('CHGCAR',folder_name)   #Only for bands calculations 
    shutil.copy('run.sh',folder_name)
    f = open('%s/INCAR' % folder_name,'w')
    for line in incar:
        f.write('%s' % line)
    f.close()
    return folder_name

def run_jobs(q):
#    folder_name = 'q%s_%s_%s' %(q[0],q[1],q[2])
    folder_name = 'q%.4f_%.4f_%.4f' %(q[0],q[1],q[2])
    print('running job for q %s' % folder_name[1:])
    system('cd %s ; sbatch run.sh' % folder_name)

folders = []

for q in Qs:
    qspiral_string = set_qspiral_string(q)
    incar = set_incar(qspiral_string)
    folders.append(set_run_folder(q,incar))
#    run_jobs(q)
f = open('qorder.txt','w')
for l in folders:
    f.write('%s' % l)
    f.write('\n')
f.close()
