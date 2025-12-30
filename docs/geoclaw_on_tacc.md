(geoclaw_on_tacc)=
# Running GeoClaw on TACC

These notes are for collaborators who want to do their own tsunami modeling by
running GeoClaw on the TACC computer `stampede3`.

The example used below is from the
[CopesHubTsunamis](https://github.com/rjleveque/CopesHubTsunamis)
repository, where code from many past and current modeling projects is
archived.  If you clone this repository, you may want to set an environment
variable so that `$CHT` points to this repo, as is assumed in some of the
links below.

:::{warning}
The research code repository 
[CopesHubTsunamis](https://github.com/rjleveque/CopesHubTsunamis)
contains much old code that should no longer be used, and lots of work
in progress that is not well documented.
It is not intended for general use, but contains some examples that may be
useful to view.
:::

## Creating a Python environment

To use Python modules such as numpy, matplotlib, etc. on TACC, you will need
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


## Using shared Clawpack Python modules and GeoClaw executable:

If you don't need to change any of the Fortran code and/or are only
using the Python tools in GeoClaw, it should be possible to share a single
version of Clawpack and use the code an executable in

    /work2/04137/rjl/CHTshare/clawpack-share

To use this code, you should set the environment variable `CLAW` to point to
this directory, and also `PYTHONPATH`, e.g.

    export CLAW=/work2/04137/rjl/CHTshare/clawpack-share
    export PYTHONPATH=$CLAW

You cannot compile the Fortran code in this version since that would require
write access, but you can use an executable `xgeoclaw` that is archived in

    /work2/04137/rjl/CHTshare/clawpack-share/tacc

For example, if running a single geoclaw job with a Makefile you could
specify

    EXE=/work2/04137/rjl/CHTshare/clawpack-share/tacc/xgeoclaw_251229

or in the `runclaw_makeplots_dtopos.py` script described below in
[](geoclaw_on_tacc:runclaw) you could set 

    xgeoclaw_path = '/work2/04137/rjl/CHTshare/clawpack-share/tacc/xgeoclaw_251229'


## Installing your own version of Clawpack/GeoClaw:

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

    
(geoclaw_on_tacc:runclaw)=
## Running GeoClaw for many different events

The sample setup in 
[$CHT/geoclaw_runs/tacc-test](https://github.com/rjleveque/CopesHubTsunamis/tree/main/geoclaw_runs/tacc-test)
shows how the same basic GeoClaw setup (for one particular location of
interest) can be run with many different tsunami sources (dtopo files).
For more discussion of this setup, see [](run-many-dtopos).

In particular, `runclaw_makeplots_dtopos.py` is the main Python
script to run, after making sure all the paths are properly set and the
desired set of events has been selected in the array `events`.

You must also first compile the GeoClaw code and make sure that the
variable `xgeoclaw_path` is set properly in `runclaw_makeplots_dtopos.py`
to find the resulting executable.
(On TACC you can use the shared executable described above.)
If you don't plan to change any Fortran code, you can make the executable
once for all GeoClaw runs (updating it only if you want to change versions
of GeoClaw).  For example, the sample `Makefile` found in
[`$CHT/geoclaw_runs/tacc-test/Makefile`](https://github.com/rjleveque/CopesHubTsunamis/tree/main/geoclaw_runs/tacc-test/Makefile)
creates an executable `$CHT/geoclaw_runs/xgeoclaw-v5.13.1`.


To run the script `runclaw_makeplots_dtopos.py` on a laptop or
desktop, this can be done from the command line via e.g.:

    python runclaw_makeplots_dtopos.py 2

which would run two geoclaw jobs at a time to process all of the `events`
(and in this simple example only 2 events are listed). Each job would be run
using the environment variable `$OMP_NUM_THREADS` to determine how many
OpenMP threads to use, and will send the output and plots made to distinct
directories for each run, perhaps on a scratch disk.  If `dry_run = True` in
this script, then it prints information about what will be done without
actually running the code or producing plots, e.g.

    --------------------------
    DRY RUN - settings in runclaw_makeplots_dtopos.py
    Will run GeoClaw for 2 dtopo files
    dtopo files should be in dtopo_dir:
         /work2/04137/rjl/CHTshare//CopesHubTsunamis/dtopo/CSZ_groundmotions/dtopo30sec/dtopofiles
    list of dtopo_files to process:
      BL10D.dtt3
      BL10M.dtt3
    output will go in 
        /scratch/04137/rjl/CopesHubTsunamis/geoclaw_runs/tacc-test/geoclaw_outputs/
    plots will go in 
        /scratch/04137/rjl/CopesHubTsunamis/geoclaw_runs/tacc-test/geoclaw_plots/
    nprocs = 2 jobs will run simultaneously
    OMP_NUM_THREADS =  24
    GeoClaw executable:
         /work2/04137/rjl/CHTshare/clawpack-share/tacc/xgeoclaw_251229
    Set dry_run=False and re-execute to run GeoClaw
    --------------------------


On TACC, this job can be submitted for batch processing on one node of
`stampede3` using the Slurm script
[`runm_geoclaw-test.slurm`](https://github.com/rjleveque/CopesHubTsunamis/blob/main/geoclaw_runs/tacc-test/runm_geoclaw-test.slurm)

:::{note}
- Before running this code, you will have to change the 
  `Allocation name` from `DS-portal-rjl` to your own allocation on TACC.
:::


To run this quick test on TACC, the command to use at the command line is:

    sbatch runm_geoclaw-test.slurm 2

where again the integer 2 implies that the 2 events specified in
`runclaw_makeplots_dtopos.py` should be run in parallel.


(geoclaw_on_tacc:production)=
## Production runs

To adapt this code to doing a "production run" for a realistic simulation
over a longer time span, see the more detailed discussion in 
[](run-many-dtopos).

(geoclaw_on_tacc:rsync)=
## Viewing plots from TACC runs

If you create plots as part of the GeoClaw runs on TACC, you will need to
transfer them elsewhere to view them.

If you want to view them on DesignSafe, you can transfer the plots
directories from your `$SCRATCH` directory to your `$WORK` directory, which
is also accessible from DesignSafe (as your `Work` directory there, see
[](workflow:TACCfiles).

The bash script
[`$CHT/geoclaw_runs/tacc-test/rsync_to_work.sh`](https://github.com/rjleveque/CopesHubTsunamis/blob/main/geoclaw_runs/tacc-test//rsync_to_work.sh)
is an attempt to automate this.

You could also download the plots (and/or the raw GeoClaw output)
to your own computer using ssh tools such as rsync.


