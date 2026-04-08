(seismic-and-tsunami-sources)=
# Cascadia CoPes Hub Ground Motions and Tsunami Sources

As part of the [Cascadia CoPes Hub](https://cascadiacopeshub.org/) project,
a new set of 36 ground motions have been computed using 3D simulations,
archived at [](https://doi.org/10.17603/ds2-dqrm-dh11).


The surface deformation from these ground motions can be used as sources
for tsunami simulations. Several different versions of these have been
computed, including for the full time-dependent kinematic rupture, but also
static displacements for "instantaneous" tsunami generation.

Recently a modified set of events has also been generated that we feel
are better to use for tsunami modeling.  These 36 events are
closely related to the original events but without the subevents that were
introduced originally to improve the seismic models at high-frequency,
since these were found to have a significant impact on the low-frequency
and permanent deformation near the coast (which is critical to properly model
in tsunami simulations). For these new events, full 3D seismic simulations
were not performed. Instead the Okada elastic half-space model was used to
approximate the surface deformation
(including a kinematic version, as described below in [](#kinokada).).

To use these ground motions in simulations on TACC, see
[](run-many-dtopos:share).

## Logic Tree

The names of the 36 events are based on a logic tree that follows
the National Seismic Hazard Model logic tree, which weighted buried
events 0.75 and frontal thrust 0.25, and then the following weights
for the downdip limits: Deep: 0.2, Middle: 0.5, Shallow: 0.3. Within
each of these 6 branches there are 6 events that have equal weights,
since both the slip distribution and magnitude-area relationship
branches are equally weighted.


Here's a view of the logic tree in which only the top- and bottom-most
branches are displayed in full (click to view):

:::{dropdown} Logic Tree
:close:
```{mermaid}
graph LR
    CSZ --> |0.75| B{Buried}
    CSZ --> |0.25| F{FrontalThrust}

    B --> |0.5| BL{Locking}
    B --> |0.5| BR{Random}
    BL --> |0.33| BL10{Str10}
    BL --> |0.33| BL13{Mur13}
    BL --> |0.33| BL16{Skl16}
    BL10 --> |0.2| BL10D{Deep - BL10D}
    BL10 --> |0.5| BL10M{Middle - BL10M}
    BL10 --> |0.3| BL10S{Shallow - BL10S}

    F --> |0.5| FL{Locking}
    F --> |0.5| FR{Random}
    FR --> |0.33| FR10{Str10}
    FR --> |0.33| FR13{Mur13}
    FR --> |0.33| FR16{Skl16}
    FR16 --> |0.2| FR16D{Deep - FR16D}
    FR16 --> |0.5| FR16M{Middle - FR16M}
    FR16 --> |0.3| FR16S{Shallow - FR16S}

```
:::

The table below shows a list of all 36 sources from the logic tree,
with their associated short names (e.g. `buried-locking-str10-deep`
is abbreviated `BL10D`) and the weight of each obtained as the product of
the weights from the logic tree branches leading to each leaf.

Note that these weights could potentially be used as conditional
probabilities, i.e. assuming that one of these 36 events happens,
the weight can be viewed as the probability that it was this event.
To compute annual probabilities of occurrence, as needed for PTHA,
one could assign a probability such as $p_0 = 1/525$ for the
occurrence of "some such CSZ event", and then multiply each of the
weights below by this value $p_0$.  This value 1/525 is suggested
by the [National Seismic Hazard
Model](https://www.usgs.gov/programs/earthquake-hazards/national-seismic-hazard-model-project)
that this logic tree is based on [TRUE?].


:::{warning}
These 36 ground motions were not designed to sample the full range of
possible CSZ megathrust events, and are instead realizations of
"more likely" next events.  Hence care should be used in performing
probabilistic tsunami hazard assessment (PTHA) with these events.
:::


:::{dropdown} List of 36 sources - names and weights
:close:

|event number | event | long name | weight |
| ---: | :---: | :--- | :--- |
|   1  |  BL10D  | buried-locking-str10-deep | 0.03750 |
|   2  |  BL10M  | buried-locking-str10-middle | 0.06250 |
|   3  |  BL10S  | buried-locking-str10-shallow | 0.02500 |
|   4  |  BL13D  | buried-locking-mur13-deep | 0.03750 |
|   5  |  BL13M  | buried-locking-mur13-middle | 0.06250 |
|   6  |  BL13S  | buried-locking-mur13-shallow | 0.02500 |
|   7  |  BL16D  | buried-locking-skl16-deep | 0.03750 |
|   8  |  BL16M  | buried-locking-skl16-middle | 0.06250 |
|   9  |  BL16S  | buried-locking-skl16-shallow | 0.02500 |
|  10  |  BR10D  | buried-random-str10-deep | 0.03750 |
|  11  |  BR10M  | buried-random-str10-middle | 0.06250 |
|  12  |  BR10S  | buried-random-str10-shallow | 0.02500 |
|  13  |  BR13D  | buried-random-mur13-deep | 0.03750 |
|  14  |  BR13M  | buried-random-mur13-middle | 0.06250 |
|  15  |  BR13S  | buried-random-mur13-shallow | 0.02500 |
|  16  |  BR16D  | buried-random-skl16-deep | 0.03750 |
|  17  |  BR16M  | buried-random-skl16-middle | 0.06250 |
|  18  |  BR16S  | buried-random-skl16-shallow | 0.02500 |
|  19  |  FL10D  | ft-locking-str10-deep | 0.01250 |
|  20  |  FL10M  | ft-locking-str10-middle | 0.02083 |
|  21  |  FL10S  | ft-locking-str10-shallow | 0.00833 |
|  22  |  FL13D  | ft-locking-mur13-deep | 0.01250 |
|  23  |  FL13M  | ft-locking-mur13-middle | 0.02083 |
|  24  |  FL13S  | ft-locking-mur13-shallow | 0.00833 |
|  25  |  FL16D  | ft-locking-skl16-deep | 0.01250 |
|  26  |  FL16M  | ft-locking-skl16-middle | 0.02083 |
|  27  |  FL16S  | ft-locking-skl16-shallow | 0.00833 |
|  28  |  FR10D  | ft-random-str10-deep | 0.01250 |
|  29  |  FR10M  | ft-random-str10-middle | 0.02083 |
|  30  |  FR10S  | ft-random-str10-shallow | 0.00833 |
|  31  |  FR13D  | ft-random-mur13-deep | 0.01250 |
|  32  |  FR13M  | ft-random-mur13-middle | 0.02083 |
|  33  |  FR13S  | ft-random-mur13-shallow | 0.00833 |
|  34  |  FR16D  | ft-random-skl16-deep | 0.01250 |
|  35  |  FR16M  | ft-random-skl16-middle | 0.02083 |
|  36  |  FR16S  | ft-random-skl16-shallow | 0.00833 |
:::

## Kinematic rupture models

These 36 events were defined by first specifying a fault geometry
for the Cascadia Subduction Zone Megathrust surface (and also for
an additional set of front faults, for the Frontal Thrust events).
This geometry consists of a large number of triangular subfaults.
For each event, several quantities are defined on each of the
subfaults, including:

- **slip**: The magnitude of the slip (relative displacement along subfault),
- **rake**: The direction of the slip along the subfault,
- **rutpure time**: The time the slip of this subfault starts,
- **rise time**: Determines the time history of the slip on this fault.

For each event, the resulting ground motion can then be determined
as described below.  This is called a *kinematic rupture* because
the time-dependent slip is specified *a priori*.  (By contrast a
*dynamic rupture* would attempt to model how the slip evolves using
fracture mechanics based on presumed stresses within the earth.)

[Describe how the slips were defined, or pointer to other discussion of this?]

[Say something here about the subevents added for high frequency shaking?]

## Seismic modeling and earthquake ground motions

The seismic simulation code [SPECFEM3D](https://specfem.org/)
was used to simulate wave propagation in 3-D using a seismic velocity
model for Cascadia.  This produces synthetic waveforms (i.e., time
series) of ground shaking and displacement for each scenario, which
were captured at grid points on the earth surface (both
onshore and on the sea floor).

For the purposes of tsunami modeling, the vertical deformation time series at
each grid point on the earth surface have been subsampled in space and time to
produce a set of vertical deformations every 10 seconds over the duration
of the earthquake (generally less than 500 seconds), to produce tsunami
sources.  For the GeoClaw tsunami model, these are stored as `dtopo files`.

Although initial tsunami simulations were performed using these
deformation files, we observed that for many events the deformation
near the coast was not always consistent with the geologic evidence
of subsidence in past tsunami events.  Investigation revealed that
the subevents that were added to provide realistic high-frequency
shaking in the seismic wave forms resulted in artifacts in the
vertical deformation that were often particularly large near the
coast due to the location of the subevents.

As a result, a new set of `NOSUB` slips were developed that correspond
to similar earthquakes but without the subevents.  Each of these
36 events has the same magnitude Mw as the original event it was
based on, but with slip reassigned from the subevents to the main
rupture [explain better?]. The temporal evolution of the rupture
also matches the original. These new `NOSUB` events do not have the
same high-frequency shaking as the originals, but for tsunami
modeling these high-frequency waves have little effect.  They are
better for tsunami modeling since the final vertical displacement
at the end of the earthquake (which is the primary driver of the
tsunami) behaves more realistically along the coast.

Full seismic simulations of the 36 `NOSUB` events have **not** been
performed, since these would be very expensive and the full seismic
signal is not needed for tsunami modeling (and would not be useful
for seismic hazard assessment either since it would be missing the
high-frequency contributions of the subevents).  Instead the sea
floor motions used as the tsunami model inputs were computed using
the approach described below in [](#kinokada).

## Okada model of an elastic halfspace

For tsunami modeling we are primarily interested in low frequency
components of the vertical deformation of the sea floor, and in
particular the final deformation after all the seismic P-waves and
S-waves have propagated away.  For this reason, tsunami modeling
is often based on a single static deformation that is an estimate
of the eventual permanent deformation, without solving for the
elastic waves.  If we assume the earth is a homogeneous elastic
halfspace with a free surface at the top surface, then it is possible
to compute the static deformation of the surface due to slip on a
single triangular subfault.  This is often called the Okada model
for deformation, since formulas for this deformation due to a point
source or a rectangular subfault were published in widely cited
papers by Y. Okada [citations].  The final static deformation for
one of our events can be approximated by using the final slip (at
large time) on each subfault, applying the Okada model to each in
order to calculate the vertical deformation at each point on a grid
specified on the surface, and then summing these up over all subfaults
(since this model approximates linear elasticity).

In tsunami modeling this deformation is often then applied as an
"instantaneous" rupture happening at the initial time of the
simulation.  This loses all information about the time-dependent
behavior of the kinematic rupture, but since tsunami wave propagation
generally happens on a much slower time scale than the rupture,
this is often a decent approximation.  We have computed a set of
deformations of this nature that we give names like `BL10D_instant`.
However, we suggest instead using the "KinOkada" versions described next.

(kinokada)=
## Kinematic Okada (KinOkada) deformations

Since many Cascadia CoPes Hub researchers are interested in modeling
the combined effect of the earthquake and tsunami, and are interested
in the time scales over which these hazards evolve for different
events, we have also created a set of deformations that are based
on the Okada model but that evolve in time in a manner similar to
the low-frequency components of the deformation obtained from the
original seismic model for each event.  This Kinematic Okada version
is obtained by using the Okada elastic halfspace model to compute
the static deformation that results from the specified slip on each
subfault, but then we accumulate the global deformation on our
surface grid by adding in each such static deformation starting at
the time specified by the rupture time for the subfault, and rising
smoothly from 0 to the final deformation over the time specified
by the rise time of the subfault.  This still ignores the propagation
of seismic waves and assumes that slip on the fault is instantaneously
transferred to static deformation of the surface, but with the time
of this transfer governed by the time-dependent kinematic rupture
properties of the particular event.

### Some animations

This animation shows a comparison of the vertical deformation `dZ` from
the original seismic model of BL10D and from the KinOkada approximation
to the `NOSUB` version of the same event:

:::{dropdown} Animation of BL10D Seismic vs KinOkada vertical deformation
:close:
```{figure} figures/BL10D_seismic_vs_kinokada_dz.mp4
:width: 600px
:align: center
```
:::


The next animation shows (for a different event)
the seismic waves propagating away from the
fault during the rupture, as computed with the original SPECFEM3D simulation
(on the left0), together with the vertical deformation approximated by
the KinOkada version (on the right):

:::{dropdown} Animation of BR13D Seismic waves vs KinOkada deformation
:close:
```{figure} figures/BR13D_with_dZ.mp4
:width: 600px
:align: center
```
:::

The vertical deformation generates the tsunami, as shown in this animation:

:::{dropdown} Animation of BR13D Seismic waves vs KinOkada with tsunami waves
:close:
```{figure} figures/BR13D_with_tsunami.mp4
:width: 600px
:align: center
```
:::

The animation above shows only the first 5 minutes after the earthquake
rupture starts, by which time the seismic waves are propagating out of the
computational domain.  The tsunami evolves over a slower time scale, as
shown in the next animation over 40 minutes.

:::{dropdown} Animation of BR13D tsunami waves over 40 minutes
:close:
```{figure} figures/offshore_BR13D_kinokada_animation.mp4
:width: 600px
:align: center
```
:::

## Combining shake maps with tsunami amplitude maps

The figure below shows the earthquake shake map (PGA) on shore with the
maximum tsunami amplitude offshore for 3 sample events.

```{figure} figures/shaking_tsunami_4ali.png
:width: 600px
:align: center
```
