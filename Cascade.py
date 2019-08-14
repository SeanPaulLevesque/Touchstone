import os
import skrf as rf

folder_name = "s2p"

#Plot each s2p file on the same graph
for filename in os.listdir(folder_name):
    ntwk = rf.Network(folder_name + '\\' + filename)
    # Mag = ntwk['2ghz'].s21.s_db[0][0][0]
    kwargs = {"marker": "o"}
    ntwk.plot_s_db(m=0, n=1, label=filename[:-4], **kwargs)
    loop = 'done'

done = 0