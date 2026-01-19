import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def b64_fig(fig: Figure):
    from base64 import b64encode
    from io import BytesIO
    from IPython.display import Markdown, display

    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    b64 = b64encode(buf.read()).decode()
    md = Markdown(f"![](data:image/png;base64,{b64})")
    display(md)


def init():
    plt.style.use("seaborn-v0_8")
