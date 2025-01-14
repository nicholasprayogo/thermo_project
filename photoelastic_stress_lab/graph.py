import matplotlib.pyplot as plt
import pandas as pd

load8 = pd.read_csv("data/load8.csv")
load10 = pd.read_csv("data/load10.csv")
load12 = pd.read_csv("data/load12.csv")
load14 = pd.read_csv("data/load14.csv")

fig, ax = plt.subplots(2, 2)

for index, load_data in enumerate([load8,load10,load12,load14]):
    ax_dict = {0:ax[0,0],1:ax[0,1],2:ax[1,0],3:ax[1,1]}

    x_null = load_data["null_order"]  # fringe location
    y_null = load_data["null_strain"]
    x_tardy = load_data["tardy_order"]
    y_tardy = load_data["tardy_strain"]

    ax_dict[index].plot(x_null,y_null, label = 'Null', marker='1')
    ax_dict[index].plot(x_tardy,y_tardy, label = 'Tardy', marker = '.')
    ax_dict[index].set_title("Load: {} lb".format(8+index*2))
    ax_dict[index].set_xlabel("Corrected Fringe Order")
    ax_dict[index].set_ylabel("Strain Difference")
    ax_dict[index].legend()
plt.tight_layout()
plt.savefig(fname="all_plots.png")
plt.show()
