import os
import skrf as rf
from matplotlib import pyplot as plt
from matplotlib import style

folder_name = "s2p"
with style.context('seaborn-ticks'):
    plt.title('Smith Chart With Legend Room');

#Plot each s2p file on the same graph
for filename in os.listdir(folder_name):
    ntwk = rf.Network(folder_name + '\\' + filename)
    Mag = ntwk['2ghz'].s21.s_db[0][0][0]
    ntwk.plot_s_db(m=0, n=1, label=filename[:-4])
    with style.context('seaborn-ticks'):
        plt.text(2e9, Mag, str(round(Mag, 3)));


    loop = 'done'

done = 0