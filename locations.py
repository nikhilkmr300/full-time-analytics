import matplotlib.pyplot as plt

from utils.filepath import DATA_FILEPATH
from utils.loader import load_data

if __name__ == "__main__":
    data = load_data(DATA_FILEPATH)
    locations = data["location"]
    locations = locations[(locations != "Multiple") & (locations != "Remote")]

    location_counts = locations.value_counts().sort_values(ascending=False)

    ax = location_counts[:15].plot.bar()
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    plt.show()

    states = locations.str.split(",", expand=True)[1].str.lstrip()
    states = states.rename("state")
    state_counts = states.value_counts(ascending=False)

    ax = state_counts.plot.bar()
    plt.show()
