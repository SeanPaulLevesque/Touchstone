import skrf as rf
import os
from matplotlib import pyplot as plt
from matplotlib import style

folder_name = "s2p"
freq_s = '3.6ghz'
freq_v = float(freq_s[:-3]) * 1e9


for chan in range(1,7):

    # grab files
    trace = rf.Network(folder_name + '\\' + str(chan) + '.s2p')
    cable = rf.Network(folder_name + '\\port' + str(chan) + '_cable.s2p')

    # slice it to the same ranges
    trace = trace['2-5ghz']
    cable = cable['2-5ghz']

    # interpolate to the same number of samples
    trace.resample(301)
    cable.resample(301)


    #trace.plot_s_db(m=0, n=1, label='trace')
    #cable.plot_s_db(m=0, n=1, label='cable')
    total = trace ** cable
    total.plot_s_db(label='total')

    total.write_touchstone("port" + str(chan))
    new = rf.Network("port" + str(chan) + '.s2p')
    new.plot_s_db(label='new')
    loop = 'done'

done = 0