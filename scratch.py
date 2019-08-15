import skrf as rf
from matplotlib import pyplot as plt
from matplotlib import style

folder_name = "s2p"
freq_s = '3.6ghz'
freq_v = float(freq_s[:-3]) * 1e9


for chan in range(1, 7):

    # grab files
    new = rf.Network("port" + str(chan) + '.s2p')
    new.plot_s_db(label='new')

    loop = 'done'

done = 0