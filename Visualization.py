import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

def plot(placements, CONTAINER_W, CONTAINER_H, CYLINDERS, com_x=None):
    
    """   Week 7 style visualization  """

    fig, ax = plt.subplots(figsize=(10, 8))

    container = Rectangle((0,0), CONTAINER_W, CONTAINER_H, fill=False, linewidth=2)
    ax.add_patch(container)




    

    for cid, x, y in placements:
        r = CYLINDERS[cid]["diameter"] / 2.0

        circle = Circle((x, y), r, fill=False, linewidth=2)
        ax.add_patch(circle)



        ax.text(x, y, str(cid), ha='center', va='center', fontsize=10)



    if com_x is not None:
        ax.axvline(com_x, linestyle='--', linewidth=1)
        ax.text(com_x, CONTAINER_H * 0.95, "COM", ha = 'center')


    ax.set_aspect('equal')
    ax.set_xlim(0, CONTAINER_W)
    ax.set_ylim(0, CONTAINER_H)
    
    ax.set_title("Cargo Loading Solution")
    ax.set_xlabel("Container Width")
    ax.set_ylabel("Container Height")


   
    plt.tight_layout
    plt.show