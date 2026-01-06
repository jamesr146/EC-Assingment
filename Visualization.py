import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

def plot(placements, CONTAINER_W, CONTAINER_H, CYLINDERS, com_x=None):
    
    """   Week 7 style visualization  """

    fig, ax = plt.subplots(figsize=(10, 8))

    ax.set_facecolor("#01364C")
    fig.patch.set_facecolor("#01364C")
    ax.grid(True, alpha=0.3, color="white")



#Container
    container = Rectangle(
        (0,0),
        CONTAINER_W, 
        CONTAINER_H, 
        fill=False, 
        linewidth=3,
        edgecolor="#F4BA02",
        label="Container"
    )
    ax.add_patch(container)

    
    
#SafeZone
    safe_x = 0.2 * CONTAINER_W
    safe_w = 0.6 * CONTAINER_W
    safe_zone = Rectangle(
        (safe_x, 0),
        safe_w,
        CONTAINER_H,
        fill=False,
        linestyle="--",
        linewidth=2,
        edgecolor="#4CAF50",
    )
    ax.add_patch(safe_zone)




    for cid, x, y in placements:
        r = CYLINDERS[cid]["diameter"] / 2.0

        circle = Circle(
            (x, y), 
            r, 
            fill=False, 
            facecolor="#99D9DD",
            edgecolor="white",
            alpha=0.6,
            linewidth=2
        )
        ax.add_patch(circle)



        ax.text(x, y, str(cid), ha='center', va='center', fontsize=10)



    if com_x is not None:
        ax.axvline(com_x, color="red", linestyle='--', linewidth=1)
        ax.text(com_x, CONTAINER_H * 0.95, "COM", color="red", ha = 'center')


    ax.set_aspect('equal')
    ax.set_xlim(0, CONTAINER_W)
    ax.set_ylim(0, CONTAINER_H)
    
    ax.set_title("Cargo Loading Solution")
    ax.set_xlabel("Container Width")
    ax.set_ylabel("Container Height")

    ax.tick_params(color="white")
    for spine in ax.spines.values():
        spine.set_color("white")

    ax.legend(facecolor="#01364C", edgecolor="white", labelcolor="white")

    plt.tight_layout
    plt.show

