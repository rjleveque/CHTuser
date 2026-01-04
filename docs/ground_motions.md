(ground_motions)=
# Ground motions

As part of the [Cascadia CoPes Hub](https://cascadiacopeshub.org/) project,
a new set of 36 ground motions have been computed using 3D simulations,
archived at [](https://doi.org/10.17603/ds2-dqrm-dh11).


The surface deformation from these ground motions can be used as sources
for tsunami simulations. Several different versions of these have been
computing, including for the full time-dependent kinematic rupture, but also
static displacements for "instantaneous" tsunami generation, as described
elsewhere.   To use these ground motions in simulations on TACC, see
[](run-many-dtopos:share).

## Summary of sources

As shorthand in the tsunami simulations, we use the following set of short
names (and also the event number when setting up job runs for subsets of
these events, as described in [](run-many-dtopos).

See the [dtopo/GroundMotions.ipynb notebook](GroundMotions) for
some additional information and tools for working with these.

|event number | event | long name |
| ---: | :---: | :--- |
|   1  |  BL10D  |  buried-locking-str10-deep |
|   2  |  BL10M  |  buried-locking-str10-middle |
|   3  |  BL10S  |  buried-locking-str10-shallow |
|   4  |  BL13D  |  buried-locking-mur13-deep |
|   5  |  BL13M  |  buried-locking-mur13-middle |
|   6  |  BL13S  |  buried-locking-mur13-shallow |
|   7  |  BL16D  |  buried-locking-skl16-deep |
|   8  |  BL16M  |  buried-locking-skl16-middle |
|   9  |  BL16S  |  buried-locking-skl16-shallow |
|  10  |  BR10D  |  buried-random-str10-deep |
|  11  |  BR10M  |  buried-random-str10-middle |
|  12  |  BR10S  |  buried-random-str10-shallow |
|  13  |  BR13D  |  buried-random-mur13-deep |
|  14  |  BR13M  |  buried-random-mur13-middle |
|  15  |  BR13S  |  buried-random-mur13-shallow |
|  16  |  BR16D  |  buried-random-skl16-deep |
|  17  |  BR16M  |  buried-random-skl16-middle |
|  18  |  BR16S  |  buried-random-skl16-shallow |
|  19  |  FL10D  |  ft-locking-str10-deep |
|  20  |  FL10M  |  ft-locking-str10-middle |
|  21  |  FL10S  |  ft-locking-str10-shallow |
|  22  |  FL13D  |  ft-locking-mur13-deep |
|  23  |  FL13M  |  ft-locking-mur13-middle |
|  24  |  FL13S  |  ft-locking-mur13-shallow |
|  25  |  FL16D  |  ft-locking-skl16-deep |
|  26  |  FL16M  |  ft-locking-skl16-middle |
|  27  |  FL16S  |  ft-locking-skl16-shallow |
|  28  |  FR10D  |  ft-random-str10-deep |
|  29  |  FR10M  |  ft-random-str10-middle |
|  30  |  FR10S  |  ft-random-str10-shallow |
|  31  |  FR13D  |  ft-random-mur13-deep |
|  32  |  FR13M  |  ft-random-mur13-middle |
|  33  |  FR13S  |  ft-random-mur13-shallow |
|  34  |  FR16D  |  ft-random-skl16-deep |
|  35  |  FR16M  |  ft-random-skl16-middle |
|  36  |  FR16S  |  ft-random-skl16-shallow |
