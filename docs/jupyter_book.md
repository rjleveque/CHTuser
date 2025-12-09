(jupyter_book)=
# Building this Jupyter Book

These webpages are build using
[Jupyter Book 2](https://jupyterbook.org/stable/).
These notes are not needed by users of these notes or the notebooks in this
repository, but may be useful to others with similar needs for other projects.

Building the book requires running any Jupyter notebooks, which in turn
requires data from a directory `CHTdata` that is assumed to exist.

The Jupyter book could be built and [deployed on Github using Github
Actions](https://jupyterbook.org/stable/get-started/publish/#github-pages),
but that would require transferring all the data needed to run the notebooks
to Github, and we anticipate large datasets in the future from simulations
performed on [TACC](https://tacc.utexas.edu/) and stored
on [DesignSafe](https://designsafe-ci.org/).

## Build on Design Safe and deploy

Instead we can build the html pages on Design Safe, using data stored there,
and deploy them manually to the website.

A conda environment `geoclaw4` is used that includes many Python packages
that may be needed in the notebooks, along with `jupyter-book`, see
[](python_env).

To build the book and create html and other required files in `_build/html`:

    conda activate geoclaw4  # environment used by rjl
    export BASE_URL=/ptha/CHTuser
    jupyter book build --html --execute

Then deploy the resulting html pages to the web server, so that they
appear on https://depts.washington.edu/ptha/CHTuser (where you are probably
now reading them).

This requires logging on to ptha@homer.u.washington.edu and then:

    cd public_html
    rsync -avz rjl@designsafe.data.tacc.utexas.edu:/data/designsafe/mydata/rjl/CHTuser/_build/html/ CHTuser/
    chmod -R og+rX CHTuser

The `rsync` step requires rjl's TACC login credentials.

## Build on laptop and deploy:

If all the required data is in a local `$HOME/CHTdata` directory,
this also works:

    activate geo4  # environment used by rjl
    export BASE_URL=/ptha/CHTuser
    jupyter book build --html --execute

    rsync -avz _build/html/ ptha@homer.u.washington.edu:public_html/CHTuser/

## Build on laptop for testing:

To build locally to test the book structure or develop a new markdown file
or notebook, you can do:

    activate geo4  # environment used by rjl
    export BASE_URL=
    jupyter book start --execute

and then open http://localhost:3000/.  Some notebooks will contain error
messages if the required data is missing.
