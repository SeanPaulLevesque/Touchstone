import os
import skrf as rf
from matplotlib import pyplot as plt
from matplotlib import style

folder_name = "s2p"
freq_s = '3.6ghz'
freq_v = float(freq_s[:-3]) * 1e9

#Plot each s2p file on the same graph
for filename in os.listdir(folder_name):
    ntwk = rf.Network(folder_name + '\\' + filename)
    MagPoint = ntwk[freq_s]
    MagVal = ntwk[freq_s].s21.s_db[0][0][0]
    ntwk.plot_s_db(m=0, n=1, label=filename[:-4])

    # Mag1.plot_s_db(m=0, n=1, marker = 'o')
    with style.context('seaborn-ticks'):
        plt.title('ADRF5545 AH Board Trace Loss');
        plt.text(freq_v, MagVal, str(round(MagVal, 3)));

    loop = 'done'

done = 0