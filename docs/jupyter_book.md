(jupyter_book)=
# Building this Jupyter Book

These webpages are build using
[Jupyter Book 2](https://jupyterbook.org/stable/).

The notes below are not needed by users of these notes or the notebooks,
but may be useful to other developers, or those with similar needs for other
projects.

:::{seealso}
[](workflow) for tips geared to users of these
notebooks and CoPes Hub Tsunami data.
:::

Building the book requires running any Jupyter notebooks, which in turn
requires data from a directory `CHTdata` that is assumed to exist.

The Jupyter book could be built and [deployed on Github using Github
Actions](https://jupyterbook.org/stable/get-started/publish/#github-pages),
but that would require transferring all the data needed to run the notebooks
to Github, and we anticipate large datasets in the future from simulations
performed on [TACC](https://tacc.utexas.edu/) and stored
on [DesignSafe](https://designsafe-ci.org/).

Instead we can build the html pages on Design Safe, using data stored there,
and deploy them manually to the website.

A conda environment `geoclaw4` is used on DesignSafe
that includes many Python packages
that may be needed in the notebooks, along with `jupyter-book`, see
[](python_env).



This workflow is complicated by the fact that `ssh` tools such as `scp` or
`rsync` cannot be used on the Jupyter Hub, nor can one push changes to Github.

So the `CHTuser` repository has been cloned into
`~/MyProjects/PRJ-6005/CHTuser`.  This
is a directory that can also be accessed from a TACC login node, as
`/corral/projects/NHERI/projects/7f2e74be-d7ca-4e0e-b69a-22c24840b078/`,
and from which `scp` tools can be used.  

## Workflow to modify notebooks or other files on Design Safe:

**On TACC:**

    export CHTdir=/corral/projects/NHERI/projects/7f2e74be-d7ca-4e0e-b69a-22c24840b078/CHTuser
    cd $CHTdir
    git pull  # to make sure we are up to date

**On the Jupyter Hub:**

    cd ~/MyProjects/PRJ-6005/CHTuser
    conda activate geoclaw4  # Python environment used by rjl
    # modify files, git add and commit any changes

**On TACC:**

    cd $CHTdir
    git push



## Build on Design Safe and deploy

To build the book and create html and other required files in `_build/html`:

    cd ~/MyProjects/PRJ-6005/CHTuser
    conda activate geoclaw4  # environment used by rjl
    export BASE_URL=/ptha/CHTuser  # path needed on server
    jupyter book build --html --execute

Then deploy the resulting html pages to the UW `ptha@homer` web server,
so that they appear on
https://depts.washington.edu/ptha/CHTuser (where you are probably
now reading them).

There are two ways to do this:

**On TACC:**

    cd $CHTdir
    rsync -avz CHTuser/_build/html/ ptha@homer.u.washington.edu:public_html/CHTuser/

The `rsync` step requires rjl's homer login credentials.

**Or log in to homer and transfer the pages from TACC:**

After logging on to ptha@homer.u.washington.edu:

    cd public_html
    rsync -avz rjl@designsafe.data.tacc.utexas.edu:/corral/projects/NHERI/projects/7f2e74be-d7ca-4e0e-b69a-22c24840b078/CHTuser/_build/html/ CHTuser/
    chmod -R og+rX CHTuser

The `rsync` step requires rjl's TACC login credentials.

## Build on laptop and deploy:

If all the required data is in a local `$HOME/CHTdata` directory,
this also works:

    activate geo4  # environment used by rjl
    export BASE_URL=/ptha/CHTuser  # path needed on server
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
