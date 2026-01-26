(workflow)=
# Workflow on DesignSafe / TACC

[Cascadia CoPes Hub](https://cascadiacopeshub.org/) researchers (and others
doing data-intensive research related to natural hazards) can get an account
on [DesignSafe](https://www.designsafe-ci.org).

Once logged in, you can start a JupyterHub instance from the
[Tools & Applications](https://designsafe-ci.org/use-designsafe/tools-applications/)
page.  The notebooks in this respository should run on the JupyterHub instance
this opens.

You can also request an allocation of computing time on TACC, which is useful
if you want to run GeoClaw or other codes there. It is also useful if you need
to use `ssh` to `scp` or `rsync` files elsewhere, or to push commits to
Github, since a terminal in the JupyterHub does not support `ssh` tools.

:::{seealso}
See the [DesignSafe User Guide](https://www.designsafe-ci.org/user-guide/)
for more information on accounts and allocations, and for general
information about using the JupyterHub.
:::

## Using the JupyterHub on DesignSafe

In your top level directory you should see

- `CommunityData`  (a read-only directory of data available to any user)
- `MyData`  (the primary directory for your own files)
- `MyProjects` (any DesignSafe projects you are a collaborator on)
- `NHERI-Published` (DesignSafe projects that have been published)
- `Work` (Temporary storage accessible also from TACC)

and possibly other subdirectories.

### Of particular interest for the CoPes Hub:

- `CommunityData/geoclaw` has data posted by `rjl` for general access,
  including some tsunami simulation results (with more to come).
  Notebooks in this repository may read data from
  `CommunityData/geoclaw/CHTdata`.

- `MyProjects/PRJ-6005` is a DesignSafe project that is not published publicly
  but is intended for our collaboration, as a place to put data that you want
  to share with collaborators.  You only have access to this project if your
  DesignSafe username has been added to the list of collaborators for this
  project (contact Randy).  If you are a collaborator, you should also be
  able to view the files from the [Data Depot webpage for
  PRJ-6005](https://designsafe-ci.org/data/browser/projects/PRJ-6005/workdir).

- `NHERI-Published/PRJ-5885` contains all the CoPes Hub ground motion
  data from project PRJ-5885,
  [](https://doi.org/10.17603/ds2-dqrm-dh11).

### Running Jupyter notebooks on DesignSafe

You can create and run your own notebooks, or you can clone this repository
and run the notebooks included:

    git clone https://github.com/rjleveque/CHTuser.git

:::{warning}
You might want to copy notebooks elsewhere before running, to avoid possible
merge conflicts if you later want to do a `git pull` to update the `CHTuser`
files.
:::

Running these notebooks generally requires a number of Python packages that
are not installed in the default Python kernel.  See [](python_env).

## Downloading data

The data found in `CommunityData/geoclaw` can be downloaded to your own
computer if you want to run the notebooks locally, or do your own
analysis/plotting with different tools.  This requires an account on TACC,
and then you can do, e.g.

    scp username@stampede3.tacc.utexas.edu:/corral/projects/NHERI/community/geoclaw/filename ./

(workflow:TACCfiles)=
## Accessing files from TACC

If you have an account/allocation on [TACC](https://tacc.utexas.edu/), e.g.
on `stampede3`, then you can access the `CommunityData/geoclaw` folder
mentioned above as `/corral/projects/NHERI/community/geoclaw`.
Files in the directory `MyProjects/PRJ-6005` on DesignSafe can be accessed
from TACC as
`/corral/projects/NHERI/projects/7f2e74be-d7ca-4e0e-b69a-22c24840b078`

You can access `corral` from a login node, but not from a computational 
job run on an interactive shell created with the `idev`
command, or submitted via Slurm, since compute nodes do
not have access to `/corral`.
So you will first have to copy files to your `$SCRATCH` or `$WORK`
directory to use them.
See the [TACC corral documentation](https://docs.tacc.utexas.edu/hpc/corral/)
for more information.


Files in your `Work` directory on DesignSafe are in your
`$WORK` directory on TACC.  When running large jobs on TACC you probably want
to direct the output to your `$SCRATCH` directory, but then you might want to
copy some output to `$WORK` to make it available for analysis in a Jupyter
notebook running on DesignSafe.

Some files to be shared among collaborators can be found on TACC in

    /work2/04137/rjl/CHTshare

If you plan to run GeoClaw yourself, see [](geoclaw_on_tacc) for more about
these shared files.

Files (such as topofiles or dtopofiles) found in this directory can also be
downloaded to your own computer (if you have an account at TACC) using e.g.
`rsync` or `scp`.

:::{seealso}
- [Managing I/O on TACC resources](https://docs.tacc.utexas.edu/tutorials/managingio/)
- [](jupyter_book) for an explanation of how this book is
  modified and built on DesignSafe.
- [](geoclaw_on_tacc) for those who want to do their own tsunami modeling.
:::
