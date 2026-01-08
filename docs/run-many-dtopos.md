(run-many-dtopos)=
# Running the same GeoClaw setup with many dtopo files

The simple test problem found in 
[`$CHT/geoclaw_runs/tacc-test`](https://github.com/rjleveque/CopesHubTsunamis/tree/main/geoclaw_runs/tacc-test)
shows an example of how the same GeoClaw setup can be applied for two
different tsunami sources (dtopo files) in parallel.

Here we dive into this example in more detail to discuss what needs to
change if to adapt this example to a more realistic case.

:::{note}
This same approach can be used to run multiple jobs on your laptop or other
computer, as a way to automate running one after another and putting the
output and plots in distinct directories created for each run according to
your desired naming scheme.

Depending on how many cores/threads you have
available, you may want to specify that the jobs run one at a time or do
multiple geoclaw runs
in parallel, based on the number of OpenMP threads you want to devote to
each (by setting `OMP_NUM_THREADS` appropriately).
Since OpenMP is used to update the solution on different grid patches
at the same level in parallel, the best value may depend on how large your
problem is, and how many patches you expect.  Values of 4-10 often work
well for many problems.

See [Using OpenMP](https://www.clawpack.org/openmp.html)
in the Clawpack documentation for more information.
:::


## A setrun function for multiple cases

The file `setrun_case.py`
contains the setrun function that will be run for each dtopo
to create the `*.data` files needed by the Fortran code.
This function has the usual form a GeoClaw setrun function, as described for
example in [Setting up the GeoClaw
run](https://rjleveque.github.io/geoclaw_tsunami_tutorial/GTT/CopalisBeach/example1/setrun_description.html)
from the [GeoClaw Tsunami
Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial).

The main difference is that this setrun function has an additional argument
`case` that is not usually in setrun.  This is a dictionary that will be passed
in when creating the `*.data` files for a particular case.
For our situation, the only important entry in the dictionary is
`dtopofile` since the value `case['dtopofile']` will be used in setting
`runclaw.dtopo_data.dtopofiles`.  (Also `case['outdir']` is used if doing a
restart.)

Everything else in `setrun` will be exactly the same for all events being run.

Note that when looping over many dtopo events, you may not want to create
time frame output of the full AMR solution at lots of output times, and
perhaps not at any output times, since this output tends to be huge and may
not be very useful for post-processing the results.  Instead one often only
wants one or more of the following:
 - gauge output: time series at specified synthetic gauge locations,
 - fgmax output: maximum inundation depth, speed, etc. on a fixed grid,
   usually covering a small portion of the computational domain,
 - fgout output: snapshots of the solution on fixed uniform grid, possibly
   at many times, but only over a small portion of the computational domain.

The example included here is set up to produce no time frame output and only
record time series at a single gauge (over a very short run for illustration).

### Testing setrun with no dtopo

The `setrun_case.py` file contains a main program that calls `setrun` with 
`case={}` and creates the `*.data` files needed for GeoClaw
so that these can be checked, if desired, before running multiple jobs with
different dtopo files.  You can do this from the command line via:

    python setrun_case.py

or you can use the usual GeoClaw command:

    make data

since the `Makefile` in this directory is set to use `setrun_case.py`.

This also creates the kml files showing e.g. the domain, topofile extents,
gauge locations, etc. If you do this on TACC you will have to download the
kml files to view them, but this may be particularly valuable if you are
setting up runs on your laptop before transferring the to TACC for
execution.
Note that an error will result if the topofile(s) cannot be found when
making the kml files. 


## A setplot function for multiple cases

The file `setplot_case.py` describes any plotting or other post-processing
to be done after the GeoClaw run completes.

This file is only needed if `make_plots == True` in 
`runclaw_makeplots_dtopos.py` (see below).

This file can then be similar to a standard `setplot.py` that specifies how
the plots should be made for each time frame of output data, as described
for example in  
[Setting up the time frame 
plots](https://rjleveque.github.io/geoclaw_tsunami_tutorial/GTT/CopalisBeach/exercise1/setplot_description.html)
from the [GeoClaw Tsunami
Tutorial](https://rjleveque.github.io/geoclaw_tsunami_tutorial).

However, as noted above, you may not want to save full AMR time frame results.
So alternatively (or in addition), the setplot function can call any other
post-processing scripts that you want to call after performing the geoclaw
runs, for example to make special plots for each gauge, to plot fgmax
results, or to make animations from fgout grid data.

Similar to `setrun_case`, the setplot function in this file has an
additional argument `case` that is used in the post-processing.

The simple example in `tacc-test` creates one gauge plot and a text file in the
`_plots` directory for each event.

## The script to run multiple cases

The script `runclaw_makeplots_dtopos.py` is used to run muliple case
with different dtopo files.

:::{seealso}
This script uses the modules `multip_tools` and `clawmultip_tools` from
`clawpack.clawutil`, designed as wrappers of the [Python `multiprocessing`
module](https://docs.python.org/3/library/multiprocessing.html)
to simplify running parameter sweeps with Clawpack code.

A simple example with some documentation can be found in
[`$CLAW/clawutil/examples/clawmultip_advection_1d_example1`](https://github.com/clawpack/clawutil/tree/master/examples/clawmultip_advection_1d_example1).
:::

On your laptop, 
this script can be run from the command line with a the syntax:

    python runclaw_makeplots_dtopos.py <nprocs> <first_event> <last_event>

where `<procs>` indicates how many geoclaw runs should be done in parallel,
and `<first_event> <last_event>` indicates the range of events that should
be used for the dtopo files, as explained further below.  
In particular, if you just want to run one event, say the `BL13D` event that
is number 4 on [the list of ground
motions](https://depts.washington.edu/ptha/CHTuser/docs/ground-motions/),
then you could use:

    python runclaw_makeplots_dtopos.py 1 4 4


On TACC, if you are logged into a login node you should not run a GeoClaw
job directly from the terminal. Moreover you may not have the required software
installed to run this from a login shell.   The preferred way to run a job
is to submit a batch job using the Slurm script
`runm_geoclaw-test.slurm`, which takes the same arugments as the Python
script when you submit the job:

    sbatch runm_geoclaw-test.slurm <nprocs> <first_event> <last_event>

These arguments are passed to `runclaw_makeplots_dtopos.py` within the
script, and `<procs>` is also used to calculate how many OpenMP threads
to use for each; see [](run-many-dtopos:slurm) for more discussion.

In the script `runclaw_makeplots_dtopos.py`, you can
set `dry_run = True` to just print out info about what will be done,
or to `False` to actually run the code and/or make plots.

Before running the code you should
check that `dtopo_dir` and `topo_dir` will be set properly
based on the location of the data.

Output and plots will be sent to subdirectories of `scratch_dir`,
which is constructed to be the full path relative to `CopesHubTsunamis`, but in
`$SCRATCH` instead of in `$HOME`.

For example, if the directory containing this code is

    /home1/04137/rjl/CopesHubTsunamis/geoclaw_runs/tacc-test

then the output/plots will be sent to

    /scratch/04137/rjl/CopesHubTsunamis/geoclaw_runs/tacc-test/geoclaw_outputs
    /scratch/04137/rjl/CopesHubTsunamis/geoclaw_runs/tacc-test/geoclaw_plots

within these directories, there will be one subdirectory for each event,
with names like `_output_BL10D` or `_plots_BL10D`, referring to event names
as described in [](groundmotions).

Set `run_code = True` to run geoclaw for each event
Set `make_plots = True` to make plots (or other post-processing) for each event

If you have already run geoclaw on each events and only want to redo the
post-processing, make sure you set `run_code = False`.

If `run_code` is True, make sure `xgeoclaw_path` is properly set to the
executable (which must have been previously compiled using an appropriate
Makefile and version of GeoClaw).

This script sets `all_events` to the list of 36 CoPes Hub
groundmotions (see [](groundmotions)),
and this is assumed for the command line arguments
`<first_event>` and `<last_event>` to work properly.
Event names like 'BL10D' are generated, and the dtopofile should be
in `f'{dtopo_dir}/{event}.dtt3'`.
If you want to use static displacement "instant" events, the file names
should be like `BL10D_instant.dtt3` and you should set `instant = True`
in this script to properly generate these file names.


After modifying this file, test it by setting `dry_run = True` and then:

    python runclaw_makeplots_dtopos.py 2 1 4

The number 2 indicates that it should do 2 runs at a time using Python
multiprocessing tools, on events numbered 1 to 4 in the list of 36 events at
[](GroundMotions).

If the screen output from this looks ok, change to `dry_run = False`
and submit a batch run using Slurm.

(run-many-dtopos:slurm)=
## Slurm script for job submission

The script
[`$CHT/geoclaw_runs/tacc-test/runm_geoclaw-test.slurm`](https://github.com/rjleveque/CopesHubTsunamis/tree/main/geoclaw_runs/tacc-test/runm_geoclaw-test.slurm)
can be adapted to run multiple jobs in parallel on TACC.  

:::{note}
Before running the script, note that:
- You will have to change the 
  `Allocation name` from `DS-portal-rjl` to your own allocation on TACC.
- The script is set to submit to the queue `skx-dev`, which is restricted to
  quick jobs. For production runs you will probably want to use `skx`.
- The time limit for this job is set to `00:10:00` (10 minutes) and the
  test code runs even quicker than that (since `tfinal = 120` in 
  `setrun_case.py`, so it runs for only 2 minutes of simulated time.
  For production runs you will need to set this much larger.
- For production runs, make sure the code is producing checkpoint files so
  the runs can be restarted if the job runs out of time. See ??.
:::

Once you have modified the script appropriately (along with `setrun_case.py`,
`setplot_case.py`, and `runclaw_makeplots_dtopos.py`), you can submit a
batch job that runs `<nprocs>` jobs in parallel via:

    sbatch runm_geoclaw-test.slurm <nprocs> <first_event> <last_event>

where `<nprocs>` is some positive integer no greater than 48 (on TACC),
and `<first_event> <last_event>` again specify the range of events from the
36 CHT ground motions.
In this case the Slurm script sets `OMP_NUM_THREADS` so that the product of
`<nprocs>` and `OMP_NUM_THREADS` is no larger than 48,
which is the number of threads available on a single node of `stampede3`.

If you want to run the first 18 CHT events,
for example (the buried rupture events), you could use `<nprocs> = 18` so
they all run in parallel with 2 OpenMP threads for each, or with `<nprocs> = 1`
so that they run sequentially with 48 threads for each run.  But
it might be most efficient to run them in 3 batches of 6 events by setting
`<nprocs> = 6`, so that 8 OpenMP threads are used for each.


Running in 3 batches of 6 could be accomplished one of two ways:

With a single slurm job:

    sbatch runm_geoclaw-test.slurm 6 1 18

which will run 6 at a time until all 18 have been run (automatically
starting a new run whenever a previous run finishes).

or by starting 3 jobs, each one running 6 dtopos in parallel:

    sbatch runm_geoclaw-test.slurm 6 1 6
    sbatch runm_geoclaw-test.slurm 6 7 12
    sbatch runm_geoclaw-test.slurm 6 13 18

This will submit 3 jobs to the queue, each one using one node with 48 cores
(with 8 OpenMP threads for each geoclaw run).


Note that there are limits to how many jobs one user can submit at a time,
and also time limits on individual jobs. The time limit you need to set will
depend on the time for a single geoclaw run and will
also depend on how many jobs are run sequentially, e.g. the first approach
above wil require roughly 3 times as much wall time as the second approach.
The latter approach would also get the work done sooner: provided all three jobs
submitted start running quickly, all 18 of the geoclaw simulations will be
running in parallel. 

Job management could possibly be streamlined using
[PyLauncher](https://docs.tacc.utexas.edu/software/pylauncher/) on
`stampede3`, but this has not yet been investigated.

:::{seealso}
- [Running Jobs on
  stampede3](https://docs.tacc.utexas.edu/hpc/stampede3/#running)
  in the TACC documentation, for more information on the queues and limits.
:::

(run-many-dtopos:share)=
## Shared data files on TACC

The directory `/work2/04137/rjl/CHTshare/CopesHubTsunamis` is accessible on
TACC and contains the dtopofiles needed for these simulations, along with
some topofiles that have been used in the past and may be useful for new
simulations.  (You may also need additional high-resolution coastal
topography if you are setting up runs for a new location.)

In addition to being useful when running jobs on TACC, this can also be used
as a source of data files for setting up or running jobs on your laptop.
If you have an account on TACC, you can download any of the files (or
directories) listed below using `rsync`, for example.

### dtopofiles

The directory
`/work2/04137/rjl/CHTshare/CopesHubTsunamis/dtopo/CSZ_groundmotions`
contains some sets of dtopofiles:

- Subdirectory `dtopo30sec/dtopofiles` contains the original kinematic
  (time-dependent) ground motions as computed by SPECFEM3D, after
  interpolation to a grid with 30 arcsecond resolution in space and 10 second
  resolution in time. The file names are simply `BL13D.dtt3` etc. and each
  one is roughly 180M in size.

  This subdirectory also contains 36 versions with names like
  `BL13D_instant.dtt3`, which contain the final static displacement at the
  end of the earthquake, with the full displacement specified at time 0.
  **(Currently at t=1 second, but we should change this.)**

- Subdirectory `nosubevents_251229/dtopofiles` contains 18 static
  displacements with names like `BL13D_instant.dtt3` that were computed
  using the Okada model from modified slips that do not contain the
  subevents. *(Describe in more detail.)*

### topofiles

The directory `/work2/04137/rjl/CHTshare/CopesHubTsunamis/topo/topofiles`
contains some topfiles. *(Add more details.)*

### GeoClaw executables

The directory `/work2/04137/rjl/CHTshare/clawpack-share/tacc` contains some
geoclaw executables that can be used to run GeoClaw (provided you do not
need to modify any of the Fortran code). See [](geoclaw_on_tacc:share) and
the file `/work2/04137/rjl/CHTshare/clawpack-share/tacc/README.txt`
for more details.
