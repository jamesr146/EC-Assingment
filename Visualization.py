import matplotlib.pyplot as plt

def plot(placements, CONTAINER_W, CONTAINER_H, CYLINDERS, com_x=None):

    fig, ax = plt.subplots()

    ax.add_patch(plt.Rectangle((0, 0), CONTAINER_W, CONTAINER_H, fill=False, linewidth=2))

    for cid, x, y in placements:
        r = CYLINDERS[cid]["diameter"] / 2.0
        ax.add_patch(plt.Circle((x, y), r, fill=False, linewidth=2))

        ax.text(x, y, str(cid), ha='center', wa='center')



    if com_x is not None:
        ax.axvline(com_x, linestyle='--')
        ax.text(com_x, CONTAINER_H * 0.95, "COM", ha = 'center')



    ax.set_aspect('equal')
    ax.set_xlime(0, CONTAINER_W)
    ax.set_ylim(0, CONTAINER_H)
    ax.set_title("Cargo Loading Solution")

    ax.set_xlabel("Container Width")
    ax.set_ylabel("Container Height")


    plt.show