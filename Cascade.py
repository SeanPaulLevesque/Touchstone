import os
import skrf as rf

folder_name = "s2p"

for filename in os.listdir(folder_name):
    #Plot each s2p file on the same graph
    ntwk = rf.Network(folder_name + '\\' + filename)
    Mag = ntwk['2ghz'].s21.s_db[0][0][0]
    kwargs = {"marker": "o"}
    ntwk.plot_s_db(m=0, n=1, label=filename[:-4] + " " + str(round(Mag, 3)) + "dB", **kwargs)
    loop = 'done'

done = 0