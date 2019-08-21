import skrf as rf
import os
from matplotlib import pyplot as plt
from matplotlib import style

start = 0

freq_s = '3.6ghz'
freq_v = float(freq_s[:-3]) * 1e9

ff1 = rf.Network("..\\Adapters\\ff1.s2p")
ff2 = rf.Network("..\\Adapters\\ff1.s2p")
# cascade 2 f-f adapters
ff_total = ff1 ** ff2
#ff_total.plot_s_db(m=0, n=0)

for chan in range(1,4):
    plt.figure("Bad Adapters")

    mm = rf.Network("..\\Adapters\\" + str(chan) + ".s2p")
    # mm.plot_s_db(m=0, n=1)


    #deembed the 2 adapters from the m-m measurement
    adapter = mm ** ff_total.inv
    adapter.plot_s_db(m=1, n=0)


# label the plot
# plt.figure("Good Adapter")
good_adapter = rf.Network("..\\Adapters\\goodmm.s2p")
good_adapter = good_adapter ** ff_total.inv
good_adapter.plot_s_db(m=1, n=0)

MagVal = good_adapter[freq_s].s21.s_db[0][0][0]

with style.context('seaborn-ticks'):
    plt.title('ADRF5545 AH Board Trace Loss');
    plt.axes.axvline(x=3.6e9,ymax=2, ymin=-2)
    plt.text(freq_v, MagVal, str(round(MagVal, 3)));

done = 0