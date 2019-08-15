import skrf as rf
import os
from matplotlib import pyplot as plt
from matplotlib import style

start = 0


for chan in range(1, 7):

    # grab files
    new = rf.Network("..\\CableLoss\\port" + str(chan) + '.s2p')
    new.frequency
    # new.s.
    # new.plot_s_db(m=0, n=1, label='new')

    loop = 'done'

done = 0