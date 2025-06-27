name = "js_stickyMod"

version = "0.1.05-r.1"

authors = [
    "Josh Sobel",
    "Jeremy Andriambolisoa",
]

description = \
    """
    Ride-along soft mod for quick deformation adjustments.
    """


requires = [
    "python-3+",
    "maya-2025+"
]

uuid = "fRiggingAwesome.stickyMod"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python/")
    