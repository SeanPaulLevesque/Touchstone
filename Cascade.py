import skrf as rf
from matplotlib import pyplot as plt

# I don't know how this is supposed to work
plt.interactive(False)

folder_name = "s2p"
freq_s = '3.6ghz'
freq_v = float(freq_s[:-3]) * 1e9

save_files = input("would you like to save the output files?")
for chan in range(1,7):

    # label the plot
    plt.figure("Cable " + str(chan))

    # grab files
    trace = rf.Network(folder_name + '\\' + str(chan) + '.s2p')
    cable = rf.Network(folder_name + '\\port' + str(chan) + '_cable.s2p')

    # slice it to the same ranges
    trace = trace['2-5ghz']
    cable = cable['2-5ghz']

    # interpolate to the same number of samples
    trace.resample(301)
    cable.resample(301)

    # plot traces
    trace.plot_s_db(m=0, n=1, label='trace')
    cable.plot_s_db(m=0, n=1, label='cable')

    # deembed
    total = trace ** cable
    total.plot_s_db(label='total')

    # save file
    if save_files == "y":
        total.write_touchstone("port" + str(chan))

    loop = 'done'

plt.show()
done = 0