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
`dtopofiles` since the value `case['dtopofiles']` will be used in setting
`dtopo_data.dtopofiles`.  (Also `case['outdir']` is used if doing a
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

The `setrun_case.py` file contains a main program that `setrun` with 
`case={'dtopofiles':[]}` and creates the `*.data` files needed for GeoClaw
so that these can be checked, if desired, before running multiple jobs with
different dtopo files.  

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

The example included in the simple example in `tacc-test`
creates one gauge plot and a text file in the
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

In the script `runclaw_makeplots_dtopos.py`, you can
set `dry_run = True` to just print out info about what will be done   
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

Set events to the list of event names to be run.
Event names like 'BL10D' are now typically expected, and the dtopofile should be
in `f'{dtopo_dir}/{event}.dtt3'`.

The sample code sets `all_events` to a list of 36 events, and then selects only
the first 2 for this test case.

After modifying this file, test it by setting `dry_run = True` and then:

    python runclaw_makeplots_dtopos.py 2

The number 2 indicates that it should do 2 runs at a time using Python
multiprocessing tools.

If the screen output from this looks ok, change to `dry_run = False`
and submit a batch run using Slurm.

## The Slurm script for job submission

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

Once you modified the script appropriately (along with `setrun_case.py`,
`setplot_case.py`, and `runclaw_makeplots_dtopos.py`), you can submit a
batch job that runs `<nprocs>` jobs in parallel via:

    sbatch runm_geoclaw-test.slurm <nprocs>

In this case the Slurm script sets `OMP_NUM_THREADS` so that the product of
`<nprocs>` and `OMP_NUM_THREADS` is no larger than 48,
which is the number of threads available on a single node of `stampede3`.

If you want to run 36 events,
for example, you could use `<nprocs> = 1` so
they all run in parallel with 1 OpenMP thread each.  But
it might be more efficient to run them in 3 batches of 12 events by setting
`<nprocs> = 12`, so that 4 OpenMP threads are used for each.

Note that the script `runclaw_makeplots_dtopos.py` creates a list
`all_events` of the 36 events corresponding to the CoPes Hub [](groundmotions),
and so this could be accomplished with the following workflow:

    # edit runclaw_makeplots_dtopos.py to set events = all_events[:12]
    sbatch runm_geoclaw-test.slurm 12

    # edit runclaw_makeplots_dtopos.py to set events = all_events[12:24]
    sbatch runm_geoclaw-test.slurm 12

    # edit runclaw_makeplots_dtopos.py to set events = all_events[24:]
    sbatch runm_geoclaw-test.slurm 12

:::{seealso}
- [Running Jobs on
  stampede3](https://docs.tacc.utexas.edu/hpc/stampede3/#running)
  in the TACC documentation.
:::
