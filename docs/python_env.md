(python_env)=
# Python Environment

Running the notebooks requires a variety of Python packages.  See
[](python_env:requirements) below for the current list that is used for
the `geoclaw4` conda environment currently used by `rjl` on
[DesignSafe](https://designsafe-ci.org/).

To create a similar environment on the [DesignSafe JupyterHub](https://designsafe-ci.org/user-guide/tools/jupyterhub/#jupyterhub-guide),
follow these steps, as
adapted from the [documentation on installing software and
kernels](https://designsafe-ci.org/user-guide/tools/jupyterhub/#installing):

Log into Design Safe and start a Jupyter Hub server.

Create a `requirements.txt` file listing packages to be pip installed, e.g.
using the list below.

Open a terminal window and do the following:

        mkdir -p ~/MyData/Python_Envs
        conda config --add envs_dirs ~/MyData/Python_Envs
        conda create --name geoclaw4 -y -c conda-forge pip python
        conda activate geoclaw4
        pip install -r requirements.txt

This will take a while to run.

Then do the following (also whenever logging into Design Safe again):

        conda activate geoclaw4
        ipython kernel install --user --name=geoclaw4

The last step should ensure that the kernel `geoclaw4` can be selected when
running a notebook.  You may have to wait a few minutes before it is
available.

See also the .

(python_env:requirements)=
## Requirements

The current contents of the `requirements.txt` file is listed below.
Most of these are not currently needed, but may be for some future projects.

    numpy
    matplotlib
    netCDF4
    scipy
    xarray
    pandas
    cartopy
    folium
    ffmpeg
    pyproj
    utm
    obspy
    obspyh5
    sympy
    pyvista
    ninja
    cloudpathlib
    meson-python
    pytest
    torch
    torchvision
    ipykernel
    ipython
    ipywidgets
    jupyterlab
    trame
    trame_jupyter_extension
    trame-vuetify
    trame-vtk
    myst-parser
    mystmd
    jupyterlab_myst
    myst-nb
    jupytext
    jupyter-book
    nbstripout
    nbdime
    clawpack
