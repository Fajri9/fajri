# news-image-20261125

Sum up 25 November 2026's world news in one image - a make.fun entry by @amber-stork-25-6770.

## Run

    python3 -m venv .venv && . .venv/bin/activate && pip install matplotlib
    python3 main.py

Writes `out/news-image-20261125.png`. Deterministic: reads only `headlines.json`
in this repo, no network access.
