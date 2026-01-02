import matplotlib.pyplot as plt
import numpy as np

FS = 20
MERGED = True
first_band = 14
PRINT_DATA = True
SAVE_DATA = True

fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.15,0.15,0.8,0.8])

clr_up = 'r'
clr_dn = 'b'

#data = np.loadtxt('o.qp_gw_ppa')
data = np.loadtxt('o.qp_gw_ppa_04')
en_ip_dn = data[1::2,2]
en_ip_up = data[0::2,2]
en_qp_dn = data[1::2,3]
en_qp_up = data[0::2,3]

if SAVE_DATA:
   data_up = np.column_stack((en_ip_up, en_qp_up))
   data_dn = np.column_stack((en_ip_dn, en_qp_dn))
   np.savetxt("data_up.txt", data_up, fmt='%.7f', delimiter='\t', header="#ip\tqp", comments='')
   np.savetxt("data_dn.txt", data_dn, fmt='%.7f', delimiter='\t', header="#ip\tqp", comments='')

if PRINT_DATA:
   print(en_qp_up)
   print('GW(15-16)|up = ', en_qp_up[2]-en_qp_up[1])
   print('KS(15-16)|up = ', en_ip_up[2]-en_ip_up[1])
   print('GW(18-19)|up = ', en_qp_up[5]-en_qp_up[4])
   print('KS(18-19)|up = ', en_ip_up[5]-en_ip_up[4])
   print('GW(14-15)|dn = ', en_qp_dn[1]-en_qp_dn[0])
   print('KS(14-15)|dn = ', en_ip_dn[1]-en_ip_dn[0])
   print('GW(17-18)|dn = ', en_qp_dn[4]-en_qp_dn[3])
   print('KS(17-18)|dn = ', en_ip_dn[4]-en_ip_dn[3])
   print('Str@vb|up = ',(en_qp_up[2]-en_qp_up[1])/(en_ip_up[2]-en_ip_up[1]))
   print('Str@cb|up = ',(en_qp_up[5]-en_qp_up[4])/(en_ip_up[5]-en_ip_up[4]))
   print('Str@vb|dn = ',(en_qp_dn[1]-en_qp_dn[0])/(en_ip_dn[1]-en_ip_dn[0]))
   print('Str@cb|dn = ',(en_qp_dn[4]-en_qp_dn[3])/(en_ip_dn[4]-en_ip_dn[3]))


if MERGED:
   for i,en in enumerate(en_ip_dn):
#       print(i+first_band,'IP|up: %s'%en_ip_up[i],'IP|dn: %s'%en_ip_dn[i])
#       print(i+first_band,'QP|up: %s'%en_qp_up[i],'QP|dn: %s'%en_qp_dn[i])
       if i == 0:
          ax.scatter(en,en_qp_dn[i],color = clr_dn, label = 'dn')
          ax.scatter(en_ip_up[i],en_qp_up[i], color = clr_up, label = 'up')
       else:
          ax.scatter(en,en_qp_dn[i],color = clr_dn)
          ax.scatter(en_ip_up[i],en_qp_up[i], color = clr_up)
else:
    BANDS = ['15-17','18-18']
    for j,b in enumerate(BANDS):
        print(b)
        data = np.loadtxt('o-Gb1-30_CorrBnds%s.qp'%b)
        en_ip_dn = data[1::2,2]
        en_ip_up = data[0::2,2]
        en_qp_dn = data[1::2,3]+data[1::2,2]
        en_qp_up = data[0::2,3]+data[0::2,2]
    
        for i,en in enumerate(en_ip_dn):
    #        print(i,'up: %s'%en_qp_up[i],'dn: %s'%en_qp_dn[i])
            print(i,'IP|up: %s'%en_ip_up[i],'IP|dn: %s'%en_ip_dn[i])
            print(i,'QP|up: %s'%en_qp_up[i],'QP|dn: %s'%en_qp_dn[i])
            if j == 0 and i == 0:
               ax.scatter(en,en_qp_dn[i],color = clr_dn, label = 'dn')
               ax.scatter(en_ip_up[i],en_qp_up[i], color = clr_up, label = 'up')
            else:
               ax.scatter(en,en_qp_dn[i],color = clr_dn)
               ax.scatter(en_ip_up[i],en_qp_up[i], color = clr_up)

ax.legend(fontsize=FS, loc = 'lower right')
ax.set_xlabel('IP (eV)',fontsize=FS)
ax.set_ylabel('QP (eV)', fontsize=FS)
ax.set_title('GW correction',fontsize=FS)
ax.tick_params(labelsize=FS)
ax.set_xlim(-2,7)
ax.set_ylim(-2,7)
ax.grid(visible=True)

plt.savefig('gw_corr-bands.pdf',format='pdf')
plt.show()
exit()
