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

## Accessing files from TACC

If you have an account/allocation on [TACC](https://tacc.utexas.edu/), e.g.
on `stampede3`, then you can access the `CommunityData/geoclaw` folder
mentioned above as `/corral/projects/NHERI/community/geoclaw`.
This works from a login node or from a job being run via a slurm script
(**True?**).
Note that it does not work from an interactive shell created with the `idev`
command, since that shell does not have access to `/corral`.

Files in the directory `MyProjects/PRJ-6005` on DesignSafe can be accessed
from TACC as
`/corral/projects/NHERI/projects/7f2e74be-d7ca-4e0e-b69a-22c24840b078`

Files in your `Work` directory on DesignSafe are in your
`$WORK` directory on TACC.  When running large jobs on TACC you probably want
to direct the output to your `$SCRATCH` directory, but then you might want to
copy some output to `$WORK` to make it available for analysis in a Jupyter
notebook running on DesignSafe.

:::{seealso}
- [Managing I/O on TACC resources](https://docs.tacc.utexas.edu/tutorials/managingio/)
:::

## Running GeoClaw on TACC

### Creating a conda environment

To use Python modules such as numpy, matplotlib, etc. you will need
to create a Python environment and install this software. 

The set of software listed in
[`$CHT/geoclaw_runs/tacc-test/requirements_geoclaw2.txt`](https://github.com/rjleveque/CopesHubTsunamis/blob/main/geoclaw_runs/tacc-test/requirements_geoclaw2.txt)
can be used to create a new environment named `geoclaw2` via:

    mkdir -p ~/venv
    python -m venv ~/venv/geoclaw2
    source ~/venv/geoclaw2/bin/activate
    pip install -r $CHT/geoclaw_runs/tacc-test/requirements_geoclaw2.txt

In order to activate this environment, you need to do the following
in a bash shell (consider putting this in `~/.bashrc`):

    source ~/venv/geoclaw2/bin/activate


### Using shared Clawpack Python modules and GeoClaw executable:

If you don't need to change any of the Fortran code and/or are only
using the Python tools in GeoClaw, it should be possible to share a single
version of Clawpack.  It should be possible to share the code in

    /work2/04137/rjl/CHTshare/clawpack_src

but this is not yet working.


### Installing your own version of Clawpack/GeoClaw:

You can install your own version of [Clawpack](http://www.clawpack.org) on
TACC.  You might want to install this in a directory `$HOME/clawpack_src` in
case you need multiple versions of the Clawapck in the future.  Here's how
you could install version v5.13.1, for example:

    mkdir -p $HOME/clawpack_src
    cd $HOME/clawpack_src
    git clone https://github.com/clawpack/clawpack.git clawpack-v5.13.1
    cd clawpack-v5.13.1
    git submodule init
    git checkout v5.13.1
    git submodule update
    export CLAW=$HOME/clawpack_src/clawpack-v5.13.1
    export PYTHONPATH=$CLAW

:::{seealso}
- [Installing Clawpack](https://www.clawpack.org/installing.html)
- [Options for installing Clawpack Fortran codes](https://www.clawpack.org/installing_fortcodes.html#installing-fortcodes)
:::

    
## Running GeoClaw for many different events

The sample setup in 
[$CHT/geoclaw_runs/tacc-test](https://github.com/rjleveque/CopesHubTsunamis/tree/main/geoclaw_runs/tacc-test)
shows how the same basic GeoClaw setup (for one particular location of
interest) can be run with many different tsunami sources (dtopo files).
For more discussion of this setup, see [](run-many-dtopos).

In particular, `runclaw_makeplots_dtopos.py` is the main Python
script to run, after making sure all the paths are properly set and the
desired set of events has been selected in the array `events`.

To run this on a laptop or
desktop, this can be done from the command line via e.g.:

    python runclaw_makeplots_dtopos.py 2

which would run two geoclaw jobs at a time to process all of the `events`
(and in this simple example only 2 events are list). Each job would be run
using the environment variable `$OMP_NUM_THREADS` to determine how many
OpenMP threads to use.

On TACC, this job can be submitted for batch processing on one node of
`stampede3` using the SLURM script
[`runm_geoclaw-test.slurm`](https://github.com/rjleveque/CopesHubTsunamis/blob/main/geoclaw_runs/tacc-test/runm_geoclaw-test.slurm)

Note the following before attempting to run this code:

- You will have to change the Allocation name from `DS-portal-rjl` to your
  own allocation on TACC,
- The script is set to submit to the queue `skx-dev`, which is restricted to
  quick jobs. For production runs you will probably want to use `skx`.
- The time limit for this job is set to `00:10:00` (10 minutes) and the
  test code runs even quicker than that (since `tfinal = 120` in 
  `setrun_case.py`, so it runs for only 2 minutes of simulated time.
  For production runs you will need to set this much larger.
- For production runs, make sure the code is producing checkpoint files so
  the runs can be restarted if the job runs out of time. See ??.

To run this quick test on TACC, the command to use at the command line is:

    sbatch runm_geoclaw-test.slurm <nprocs>

where `<nprocs>` represents an integer specifying the number of
jobs to run in parallel.
In this case the slurm script sets `OMP_NUM_THREADS` so that the product of
`<nprocs>` and `OMP_NUM_THREADS` is no larger than 48,
which is the number of threads available on a single node of `stampede3`.

If you have 36 events to run, for example, you could use `<nprocs> = 1` so
they all run in parallel with 1 OpenMP thread each.  But
it might be more efficient to run them in 3 batches of 12 events with
`<nprocs> = 12` so that 4 OpenMP threads are used for each.
Note that the script `runclaw_makeplots_dtopos.py` creates a list
`all_events` of the 36 events corresponding to the CoPes Hub groundmotions,
and so this could be accomplished with the following workflow:

    # edit runclaw_makeplots_dtopos.py to set events = all_events[:12]
    sbatch runm_geoclaw-test.slurm 12
    # edit runclaw_makeplots_dtopos.py to set events = all_events[12:24]
    sbatch runm_geoclaw-test.slurm 12
    # edit runclaw_makeplots_dtopos.py to set events = all_events[24:]
    sbatch runm_geoclaw-test.slurm 12

*More to come on using slurm scripts, etc.*

:::{seealso}
[](jupyter_book) for an explanation of how this book is modified and built.
:::
