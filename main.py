"""Render one image summarizing 25 November 2026 world news.

Reads headlines.json shipped in this repo (no network access) and draws
a single poster PNG to out/news-image-20261125.png. Deterministic output.
"""
import json
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
DATE = "25 November 2026"


def main() -> Path:
    data = json.loads((ROOT / "headlines.json").read_text(encoding="utf-8"))
    fig, axes = plt.subplots(1, len(data["stories"]), figsize=(16, 9))
    fig.suptitle(f"The World in One Image - {DATE}", fontsize=26, fontweight="bold", y=0.97)
    fig.text(0.5, 0.91, "\n".join(textwrap.wrap(data["summary_line"], 110)),
             ha="center", fontsize=13, color="#444444")
    for ax, story in zip(axes, data["stories"]):
        ax.set_facecolor(story["color"])
        ax.set_xticks([]); ax.set_yticks([])
        ax.text(0.5, 0.90, story["tag"], ha="center", fontsize=13, fontweight="bold",
                color="white", transform=ax.transAxes)
        wrapped = "\n".join(textwrap.wrap(story["headline"], 22))
        ax.text(0.5, 0.58, wrapped, ha="center", va="center", fontsize=15,
                color="white", transform=ax.transAxes)
        ax.text(0.5, 0.16, "\n".join(textwrap.wrap(story["context"], 26)),
                ha="center", fontsize=11, color="#f0f0f0", transform=ax.transAxes)
    out = ROOT / "out"
    out.mkdir(exist_ok=True)
    path = out / "news-image-20261125.png"
    fig.savefig(path, dpi=120, facecolor="#101820")
    plt.close(fig)
    print(f"WROTE {path}")
    return path


if __name__ == "__main__":
    main()
