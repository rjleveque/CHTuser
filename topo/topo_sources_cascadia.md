
# Topo files for Cascadia

Topography DEMs can be found in various places within the
[NCEI website](https://www.ncei.noaa.gov/),
see [Improving Coastal Resiliency with Digital Elevation
Models](http://ncei.noaa.gov/news/improving-coastal-resiliency-digital-elevation-models)
for an overview.

The "Data URLs" listed below can be used to download a DEM directly. Note
that `.nc` and `.tif` files must be handled differently.

### Downloading netCDF files

For Data URLs that end in '.nc', the data can be downloaded
from a THREDDS server, e.g. using the GeoClaw Python tool

      topo = clawpack.geoclaw.topotools.read_netcdf(data_url)

to download the entire file at full resolution.

See the [topotools documentation](https://www.clawpack.org/topo.html#netcdf-format) and
[read_netcdf documentation](https://www.clawpack.org/topotools_module.html#clawpack.geoclaw.topotools.read_netcdf)
for other arguments to this function, to download a subset, subsample the resolution, etc.
and information on the object returned by this function.

### Downloading GeoTiff files

For Data URLs that end in '.tif', the data can be downloaded by going to the
catalog website and clicking on the file, or in Python using e.g.

    Code to appear

## Global ocean topography

We are mostly using [etopo 2022 15 arcsecond (15") topography](https://data.noaa.gov/metaview/page?xml=NOAA/NESDIS/NGDC/MGG/DEM//iso/xml/etopo_2022.xml&view=getDataView&header=none),
typically by downloading data at the 30" resolution or coarser directly from the THREDDS server,

Data URL: https://www.ngdc.noaa.gov/thredds/dodsC/global/ETOPO2022/30s/30s_bed_elev_netcdf/ETOPO_2022_v1_30s_N90W180_bed.nc



## General NCEI catalog

https://www.ngdc.noaa.gov/thredds/catalog/demCatalog.html

### Coastal Relief Model

Catalog: https://www.ngdc.noaa.gov/thredds/catalog/crm/catalog.html

contains Coastal Relief Model by volume, including vol8 for Pacific Northwest:

Data URL: https://www.ngdc.noaa.gov/thredds/dodsC/crm/crm_vol8.nc

     crm_vol8.nc	 345.8 Mbytes	2010-09-16T18:28:47Z


### thredds/catalog/regional

Catalog: https://www.ngdc.noaa.gov/thredds/catalog/regional/catalog.html

contains e.g.

      la_push_13_mhw_2007.nc
      astoria_13_mhw_2012.nc
      grays_harbor_P280_2018.nc


### thredds/dodsC/pmel

Catalog: https://www.ngdc.noaa.gov/thredds/catalog/pmel/catalog.html

Data URL: https://www.ngdc.noaa.gov/thredds/dodsC/pmel/ + filename.nc

Mostly (all?) referenced to MHW?

Contains various locations, dating from 2016, for A,B,C MOST grids
including:
   (A: 54.5", B: 30", C: 16.522" in x, 9" in y)

      BritishColumbia_A.nc	 385.5 Kbytes	2016-06-01T20:56:44Z
      BritishColumbia_B.nc	 2.797 Mbytes	2016-06-01T20:56:52Z
      BritishColumbia_C.nc	 181.9 Kbytes	2016-06-01T20:57:00Z

and for other locations, some in Cascadia:
    (some have resolutions A: 3 arcmin, B: 18 arcsec, C: 1/5" in x, 1/3" in y)

      CrescentCityCA
      EurekaCA
      LaPushWA
      NeaBayWA
      NewportOR
      etc

## CUDEM tiles

Continuously Updated DEMs (CUDEMs) are provided on 0.25 degree by 0.25 degree
rectangles, typically named based on the latitude and longitude of the
upper left corner along with some information about the date it was released.

Tiles are available some places at both 1/3" and more recently at 1/9"
resolution (the latter is about 2m by 3m horizontal resolution at the latitude
of Cascadia).

These tiles are generally referenced to NAVD88 as the vertical datum, although
some data sets are referenced to MHW (particularly in directories that include
`nthmp` in their name, since these were custom made for tsunami modeling).

These tiles are typically available only for the rectangles that are
intersected by the coastline.

### thredds/dodsC/tiles/tiled_19as

Catalog: https://www.ngdc.noaa.gov/thredds/catalog/tiles/tiled_19as/catalog.html

Data URL: https://www.ngdc.noaa.gov/thredds/dodsC/tiles/tiled_19as/ + filename.nc

Contains the following in Cascadia:

      ncei19_n47x00_w0124x00_2018v1.nc	 166.0 Mbytes	2019-02-07T20:35:13Z
      ncei19_n47x00_w0124x25_2018v1.nc	 156.2 Mbytes	2019-02-07T20:35:45Z
      ncei19_n47x25_w0124x25_2018v1.nc	 158.1 Mbytes	2019-02-07T20:36:19Z
      ncei19_n47x50_w0124x25_2018v1.nc	 155.9 Mbytes	2019-02-07T20:36:52Z
      ncei19_n47x50_w0124x50_2018v1.nc	 139.4 Mbytes	2019-02-07T20:37:24Z
      ncei19_n47x75_w0124x50_2018v1.nc	 146.2 Mbytes	2019-02-07T20:38:04Z
      ncei19_n48x00_w0124x50_2018v1.nc	 150.9 Mbytes	2019-02-07T20:38:49Z
      ncei19_n48x00_w0124x75_2018v1.nc	 138.8 Mbytes	2019-02-07T20:39:32Z
      ncei19_n48x25_w0124x75_2018v1.nc	 156.8 Mbytes	2019-02-07T20:40:16Z
      ncei19_n48x50_w0124x75_2018v1.nc	 140.7 Mbytes	2019-02-07T20:40:59Z
      ncei19_n48x75_w122x50_2017v1.nc	 263.3 Mbytes	2018-05-23T17:49:27Z
      ncei19_n48x75_w122x75_2017v1.nc	 263.3 Mbytes	2018-05-23T17:49:28Z
      ncei19_n48x75_w123x00_2017v1.nc	 263.3 Mbytes	2018-05-23T17:49:29Z
      ncei19_n49x00_w122x50_2017v1.nc	 263.3 Mbytes	2018-05-23T17:49:32Z
      ncei19_n49x00_w122x75_2019v2.nc	 157.8 Mbytes	2019-05-21T17:51:55Z
      ncei19_n49x00_w123x00_2019v2.nc	 147.1 Mbytes	2019-05-21T17:51:27Z

### thredds/dodsC/tiles/tiled_13as

Catalog: https://www.ngdc.noaa.gov/thredds/catalog/tiles/tiled_13as/catalog.html

Data URL: https://www.ngdc.noaa.gov/thredds/dodsC/tiles/tiled_13as/ + filename.nc

Contains the following in Cascadia:

      ncei13_n47x25_w0124x50_2018v1.nc	 15.48 Mbytes	2019-02-07T20:12:10Z
      ncei13_n47x75_w0124x75_2018v1.nc	 14.88 Mbytes	2019-02-07T20:12:13Z
      ncei13_n48x25_w0125x00_2018v1.nc	 15.61 Mbytes	2019-02-07T20:12:16Z
      ncei13_n48x50_w0125x00_2018v1.nc	 15.93 Mbytes	2019-02-07T20:12:19Z

### thredds/dodsC/tiles/nthmp

Catalog: https://www.ngdc.noaa.gov/thredds/catalog/tiles/nthmp/tiled_19as/catalog.html

Data URL: https://www.ngdc.noaa.gov/thredds/dodsC/tiles/nthmp/tiled_19as/ + filename.nc

Some are MHW, others have navd88 in name

Contains the following in Cascadia:

      juan_de_fuca_mhw_g19_n48x25_w123x25_2021v1.nc	 145.5 Mbytes	2021-04-12T00:04:53Z
      juan_de_fuca_mhw_g19_n48x25_w123x50_2021v1.nc	 139.5 Mbytes	2021-04-12T00:06:08Z
      juan_de_fuca_mhw_g19_n48x25_w123x75_2021v1.nc	 136.3 Mbytes	2021-04-12T00:07:29Z
      juan_de_fuca_mhw_g19_n48x25_w124x00_2021v1.nc	 136.2 Mbytes	2021-04-12T00:08:47Z
      juan_de_fuca_mhw_g19_n48x25_w124x25_2021v1.nc	 151.1 Mbytes	2021-04-12T00:10:07Z
      juan_de_fuca_mhw_g19_n48x25_w124x50_2021v1.nc	 154.5 Mbytes	2021-04-12T01:28:02Z
      juan_de_fuca_mhw_g19_n48x50_w124x25_2021v1.nc	 126.6 Mbytes	2021-04-12T00:14:13Z
      juan_de_fuca_mhw_g19_n48x50_w124x50_2021v1.nc	 133.4 Mbytes	2021-04-12T00:15:17Z
      ncei19_n42x00_w124x25_navd88_2021.nc	 148.8 Mbytes	2023-03-24T20:44:59.043Z
      ncei19_n42x00_w124x50_navd88_2021.nc	 123.7 Mbytes	2023-03-24T20:45:00.828Z
      ncei19_n42x25_w124x25_navd88_2021.nc	 149.7 Mbytes	2023-03-24T20:45:02.887Z
      ncei19_n42x25_w124x50_navd88_2021.nc	 132.9 Mbytes	2023-03-24T20:45:04.677Z
      ncei19_n42x50_w124x50_navd88_2021.nc	 146.1 Mbytes	2023-03-24T20:45:07.068Z
      ncei19_n42x50_w124x75_navd88_2021.nc	 121.1 Mbytes	2023-03-24T20:45:08.898Z
      ncei19_n42x75_w124x50_navd88_2021.nc	 147.3 Mbytes	2023-03-24T20:45:10.949Z
      ncei19_n42x75_w124x75_navd88_2021.nc	 123.7 Mbytes	2023-03-24T20:45:12.798Z
      ncei19_n43x00_w124x50_navd88_2021.nc	 152.8 Mbytes	2023-03-24T20:45:15.475Z
      ncei19_n43x00_w124x75_navd88_2021.nc	 130.3 Mbytes	2023-03-24T20:45:17.590Z
      ncei19_n43x25_w124x50_navd88_2021.nc	 155.6 Mbytes	2023-03-24T20:45:19.497Z
      ncei19_n43x25_w124x75_navd88_2021.nc	 120.7 Mbytes	2023-03-24T20:45:21.396Z
      ncei19_n43x50_w124x25_navd88_2021.nc	 166.6 Mbytes	2023-03-24T20:45:23.490Z
      ncei19_n43x50_w124x50_navd88_2021.nc	 140.7 Mbytes	2023-03-24T20:45:25.746Z
      ncei19_n43x75_w124x00_navd88_2021.nc	 159.0 Mbytes	2023-03-24T21:02:55.056Z
      ncei19_n43x75_w124x25_navd88_2021.nc	 167.0 Mbytes	2023-03-24T21:02:58.126Z
      ncei19_n43x75_w124x50_navd88_2021.nc	 107.6 Mbytes	2023-03-24T21:02:58.784Z
      ncei19_n44x00_w124x00_navd88_2021.nc	 161.4 Mbytes	2023-03-24T21:02:59.720Z
      ncei19_n44x00_w124x25_navd88_2021.nc	 156.3 Mbytes	2023-03-24T21:03:00.496Z
      ncei19_n44x00_w124x50_navd88_2021.nc	 104.5 Mbytes	2023-03-24T21:03:01.122Z
      ncei19_n44x25_w124x00_navd88_2021.nc	 161.2 Mbytes	2023-03-24T22:07:34.418Z
      ncei19_n44x25_w124x25_navd88_2021.nc	 145.2 Mbytes	2023-03-24T22:07:35.119Z
      ncei19_n44x50_w124x00_navd88_2021.nc	 157.3 Mbytes	2023-03-24T22:07:35.807Z
      ncei19_n44x50_w124x25_navd88_2021.nc	 140.2 Mbytes	2023-03-24T22:07:36.515Z
      ncei19_n44x75_w124x00_navd88_2021.nc	 160.1 Mbytes	2023-03-24T22:07:39.474Z
      ncei19_n44x75_w124x25_navd88_2021.nc	 142.7 Mbytes	2023-03-24T22:07:40.284Z
      ncei19_n45x00_w124x00_navd88_2021.nc	 156.3 Mbytes	2023-03-24T22:07:41.733Z
      ncei19_n45x00_w124x25_navd88_2021.nc	 133.3 Mbytes	2023-03-24T22:07:42.511Z
      ncei19_n45x25_w124x00_2019v1.nc	 263.3 Mbytes	2023-08-11T15:56:00.012Z
      ncei19_n45x25_w124x25_2019v1.nc	 263.3 Mbytes	2023-08-11T15:56:03.150Z
      ncei19_n45x50_w124x00_2019v1.nc	 263.3 Mbytes	2023-08-11T15:56:05.018Z
      ncei19_n45x50_w124x25_2019v1.nc	 263.3 Mbytes	2023-08-11T15:56:06.759Z
      ncei19_n45x75_w124x00_2019v1.nc	 263.3 Mbytes	2023-08-11T15:56:09.004Z
      ncei19_n45x75_w124x25_2019v1.nc	 263.3 Mbytes	2023-08-11T15:56:10.814Z
      ncei19_n46x00_w124x00_2019v1.nc	 263.3 Mbytes	2023-08-11T15:56:12.671Z
      ncei19_n46x00_w124x25_2019v1.nc	 263.3 Mbytes	2023-08-11T15:56:14.350Z
      ncei19_n46x25_w124x00_2019v1.nc	 263.3 Mbytes	2023-08-11T15:56:16.907Z
      ncei19_n46x25_w124x25_2019v1.nc	 263.3 Mbytes	2023-08-11T15:56:18.871Z
      ncei19_n47x25_w0124x25_2020.nc	 159.1 Mbytes	2020-06-08T21:58:24Z
      ncei19_n47x50_w0124x25_2020.nc	 143.1 Mbytes	2020-06-02T17:20:32Z
      ncei19_n47x50_w0124x50_2020.nc	 136.6 Mbytes	2020-06-08T21:56:54Z
      ncei19_n47x75_w0124x50_2020.nc	 147.1 Mbytes	2020-06-02T17:18:36Z
      ncei19_n48x00_w0124x50_2020.nc	 157.1 Mbytes	2020-06-02T17:17:44Z
      ncei19_n48x00_w0124x75_2020.nc	 136.9 Mbytes	2020-06-02T17:16:40Z
      ncei19_n48x25_w0124x75_2020.nc	 159.1 Mbytes	2020-06-02T17:12:46Z
      ncei19_n48x50_w0124x75_2020.nc	 143.2 Mbytes	2020-06-02T17:10:50Z
      ncei19_n48x75_w122x50_mhw_2020_v3.nc	 131.4 Mbytes	2020-02-25T16:29:26Z
      ncei19_n48x75_w122x75_mhw_2020_v3.nc	 128.8 Mbytes	2020-02-25T16:29:16Z
      ncei19_n48x75_w123x00_mhw_2020_v3.nc	 132.5 Mbytes	2020-02-25T16:29:09Z
      ncei19_n49x00_w122x50_mhw_2020_v3.nc	 125.3 Mbytes	2020-02-25T16:29:02Z
      ncei19_n49x00_w122x75_mhw_2020_v3.nc	 136.5 Mbytes	2020-02-25T16:28:46Z
      ncei19_n49x00_w123x00_mhw_2020_v3.nc	 122.1 Mbytes	2020-02-25T16:28:55Z
      ncei19_n58x50_w135x75_2024v1.nc	 145.9 Mbytes	2025-11-03T17:14:40Z
      ncei19_n58x50_w136x00_2024v1.nc	 145.3 Mbytes	2025-11-03T17:14:59Z
      ncei19_n59x75_w152x00_2022v1.nc	 126.8 Mbytes	2025-10-28T16:11:57.252Z
      ncei19_n60x00_w151x75_2022v1.nc	 136.1 Mbytes	2025-10-28T16:11:57.951Z
      ncei19_n60x00_w152x00_2022v1.nc	 129.6 Mbytes	2025-10-28T16:11:58.618Z
      ncei19_n60x25_w151x50_2022v1.nc	 136.4 Mbytes	2025-10-28T16:11:59.317Z
      ncei19_n60x25_w151x75_2022v1.nc	 130.8 Mbytes	2025-10-28T16:11:59.906Z
      ncei19_n60x25_w152x00_2022v1.nc	 117.6 Mbytes	2025-10-28T16:12:00.719Z
      ncei19_n60x50_w151x25_2022v1.nc	 139.7 Mbytes	2025-10-28T16:12:01.500Z
      ncei19_n60x50_w151x50_2022v1.nc	 137.9 Mbytes	2025-10-28T16:12:02.189Z
      ncei19_n60x75_w151x25_2022v1.nc	 144.4 Mbytes	2025-10-28T16:12:02.877Z
      ncei19_n60x75_w151x50_2022v1.nc	 140.4 Mbytes	2025-10-28T16:12:03.532Z
      ncei19_n64x50_w165x50_2024v1.nc	 124.6 Mbytes	2025-12-08T14:39:39.117Z
      ncei19_n64x50_w165x75_2024v1.nc	 119.5 Mbytes	2025-12-08T14:39:39.813Z
      ncei19_n64x75_w165x50_2024v1.nc	 146.7 Mbytes	2025-12-08T14:39:40.709Z
      ncei19_n64x75_w165x75_2024v1.nc	 145.6 Mbytes	2025-12-08T14:39:41.486Z
      puget_sound_mhw_19_n47x25_w122x25_2024v1.nc	 143.2 Mbytes	2024-01-06T15:11:50Z
      puget_sound_mhw_19_n47x25_w122x50_2024v1.nc	 145.6 Mbytes	2024-01-06T15:11:39Z
      puget_sound_mhw_19_n47x25_w122x75_2024v1.nc	 152.8 Mbytes	2024-01-06T15:11:30Z
      puget_sound_mhw_19_n47x25_w123x00_2024v1.nc	 159.0 Mbytes	2024-01-06T15:11:12Z
      puget_sound_mhw_19_n47x25_w123x25_2024v1.nc	 154.0 Mbytes	2024-01-06T15:10:50Z
      puget_sound_mhw_19_n47x50_w122x25_2023v1.nc	 151.2 Mbytes	2023-06-11T15:14:36Z
      puget_sound_mhw_19_n47x50_w122x50_2023v1.nc	 153.6 Mbytes	2023-06-11T15:10:58Z
      puget_sound_mhw_19_n47x50_w122x75_2023v1.nc	 157.1 Mbytes	2023-04-25T14:08:24Z
      puget_sound_mhw_19_n47x50_w123x00_2023v1.nc	 158.5 Mbytes	2023-04-25T14:06:26Z
      puget_sound_mhw_19_n47x50_w123x25_2023v1.nc	 155.2 Mbytes	2023-04-25T14:03:38Z
      puget_sound_mhw_19_n47x75_w122x25_2023v1.nc	 156.5 Mbytes	2023-06-11T15:12:46Z
      puget_sound_mhw_19_n47x75_w122x50_2023v1.nc	 153.4 Mbytes	2023-06-11T15:09:32Z
      puget_sound_mhw_19_n47x75_w122x75_2023v1.nc	 161.4 Mbytes	2023-06-11T14:59:08Z
      puget_sound_mhw_19_n47x75_w123x00_2023v1.nc	 153.5 Mbytes	2023-04-11T15:13:14Z
      puget_sound_mhw_19_n47x75_w123x25_2023v1.nc	 149.0 Mbytes	2023-04-11T14:00:08Z
      puget_sound_mhw_19_n48x00_w122x25_2023v1.nc	 160.9 Mbytes	2023-06-11T14:56:00Z
      puget_sound_mhw_19_n48x00_w122x50_2023v1.nc	 148.7 Mbytes	2023-06-11T14:53:54Z
      puget_sound_mhw_19_n48x00_w122x75_2023v1.nc	 157.1 Mbytes	2023-04-25T13:45:22Z
      puget_sound_mhw_19_n48x00_w123x00_2023v1.nc	 153.5 Mbytes	2023-04-25T13:43:28Z
      puget_sound_mhw_19_n48x25_w122x25_2024v1.nc	 153.2 Mbytes	2024-04-12T14:41:55Z
      puget_sound_mhw_19_n48x25_w122x50_2024v1.nc	 155.0 Mbytes	2024-04-12T16:55:05Z
      puget_sound_mhw_19_n48x25_w122x75_2024v1.nc	 152.4 Mbytes	2024-04-12T14:42:23Z
      puget_sound_mhw_19_n48x25_w123x00_2024v1.nc	 148.9 Mbytes	2024-04-12T14:42:38Z
      puget_sound_mhw_19_n48x50_w122x50_2024v1.nc	 166.4 Mbytes	2024-03-21T15:30:05Z
      puget_sound_mhw_19_n48x50_w122x75_2024v1.nc	 156.3 Mbytes	2024-04-12T14:42:50Z
      puget_sound_mhw_19_n48x50_w123x00_2024v1.nc	 146.2 Mbytes	2024-04-12T14:43:03Z
      puget_sound_mhw_19_n48x50_w123x25_2024v1.nc	 142.9 Mbytes	2024-03-21T15:29:30Z
      puget_sound_mhw_19_n48x75_w123x25_2024v1.nc	 152.8 Mbytes	2024-03-21T15:29:17Z
      puget_sound_mhw_19_n49x00_w123x25_2024v1.nc	 139.6 Mbytes	2024-03-21T14:45:11Z
      sowa_mhw_19_n46x75_w123x75_2025v1.nc	 163.4 Mbytes	2025-12-11T14:23:35.219Z
      sowa_mhw_19_n46x75_w124x00_2025v1.nc	 167.1 Mbytes	2025-12-11T14:23:36.203Z
      sowa_mhw_19_n46x75_w124x25_2025v1.nc	 142.6 Mbytes	2025-12-11T14:23:37.065Z
      sowa_mhw_19_n47x00_w123x50_2025v1.nc	 159.5 Mbytes	2025-12-11T14:23:37.868Z
      sowa_mhw_19_n47x00_w123x75_2025v1.nc	 166.4 Mbytes	2025-12-11T14:23:38.841Z
      sowa_mhw_19_n47x00_w124x00_2025v1.nc	 170.1 Mbytes	2025-12-11T14:23:39.687Z
      sowa_mhw_19_n47x00_w124x25_2025v1.nc	 152.3 Mbytes	2025-12-11T14:23:40.588Z
      sowa_mhw_19_n47x25_w123x75_2025v1.nc	 158.9 Mbytes	2025-12-11T14:23:41.400Z
      sowa_mhw_19_n47x25_w124x00_2025v1.nc	 163.1 Mbytes	2025-12-11T14:23:42.327Z
      sowa_mhw_19_n47x25_w124x25_2025v1.nc	 156.7 Mbytes	2025-12-11T14:23:43.222Z
      tillamook19_n46x24_w123x99_2021v3.nc	 171.8 Mbytes	2023-08-17T14:09:44.214Z
      tillamook19_n46x24_w124x24_2021v3.nc	 131.2 Mbytes	2023-08-17T14:10:07.987Z

## tif files

### coast.noaa.gov/htdata/raster2

Catalog: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/

Contains the following in Cascadia:

Catalog: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/index.html

Data URL: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/ + filename.tif

      ncei19_n43x75_w124x00_2021v1.tif (152.15 MB)
      ncei19_n43x75_w124x25_2021v1.tif (155.91 MB)
      ncei19_n43x75_w124x50_2021v1.tif (86.61 MB)
      ncei19_n44x00_w124x00_2021v1.tif (154.17 MB)
      ncei19_n44x00_w124x25_2021v1.tif (141.86 MB)
      ncei19_n44x00_w124x50_2021v1.tif (83.32 MB)

      ncei19_n44x25_w124x00_2021v1.tif (155.49 MB) REMOVED
      ncei19_n44x25_w124x25_2021v1.tif (129.38 MB) REMOVED
      ncei19_n44x50_w124x00_2021v1.tif (151.46 MB) REMOVED
      ncei19_n44x50_w124x25_2021v1.tif (122.08 MB) REMOVED
      ncei19_n44x75_w124x00_2021v1.tif (152.83 MB) REMOVED
      ncei19_n44x75_w124x25_2021v1.tif (122.33 MB) REMOVED
      ncei19_n45x00_w124x00_2021v1.tif (149.65 MB) REMOVED
      ncei19_n45x00_w124x25_2021v1.tif (111.79 MB) REMOVED

      ncei19_n44x25_w124x00_2025v2.tif (212.90 MB)
      ncei19_n44x25_w124x25_2025v2.tif (205.21 MB)
      ncei19_n44x25_w124x50_2025v1.tif (175.49 MB)
      ncei19_n44x50_w124x00_2025v2.tif (212.95 MB)
      ncei19_n44x50_w124x25_2025v2.tif (200.10 MB)
      ncei19_n44x50_w124x50_2025v1.tif (175.55 MB)
      ncei19_n44x75_w124x00_2025v2.tif (215.21 MB)
      ncei19_n44x75_w124x25_2025v2.tif (198.42 MB)
      ncei19_n44x75_w124x50_2025v1.tif (182.68 MB)
      ncei19_n45x00_w124x00_2025v2.tif (211.24 MB)
      ncei19_n45x00_w124x25_2025v2.tif (195.45 MB)
      ncei19_n45x00_w124x50_2025v1.tif (176.93 MB)
      ncei19_n45x25_w124x00_2025v1.tif (211.11 MB)
      ncei19_n45x25_w124x25_2025v1.tif (189.41 MB)
      ncei19_n45x50_w124x00_2025v1.tif (211.68 MB)
      ncei19_n45x50_w124x25_2025v1.tif (187.24 MB)
      ncei19_n45x75_w124x00_2025v1.tif (211.99 MB)
      ncei19_n45x75_w124x25_2025v1.tif (184.36 MB)
      ncei19_n46x00_w124x00_2025v1.tif (210.86 MB)
      ncei19_n46x00_w124x25_2025v1.tif (183.79 MB)

Catalog: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/wash_bellingham/index.html

Data URL: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/wash_bellingham/ + filename.tif

      ncei19_n48x50_w122x50_2024v1.tif (209.14 MB)
      ncei19_n48x50_w122x75_2024v1.tif (199.92 MB)
      ncei19_n48x50_w123x00_2024v1.tif (182.50 MB)
      ncei19_n48x50_w123x25_2024v1.tif (177.68 MB)
      ncei19_n48x75_w122x50_2017v1.tif (200.51 MB)
      ncei19_n48x75_w122x75_2017v1.tif (197.42 MB)
      ncei19_n48x75_w123x00_2017v1.tif (197.91 MB)
      ncei19_n48x75_w123x25_2024v1.tif (190.54 MB)
      ncei19_n49x00_w122x50_2017v1.tif (195.16 MB)
      ncei19_n49x00_w122x75_2017v1.tif (203.96 MB)
      ncei19_n49x00_w123x00_2017v1.tif (182.19 MB)
      ncei19_n49x00_w123x25_2024v1.tif (171.20 MB)

Catalog: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/wash_juandefuca/index.html

Data URL: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/wash_juandefuca/ + filename.tif


      ncei19_n48x25_w123x00_2024v2.tif (183.93 MB)
      ncei19_n48x25_w123x25_2021v1.tif (130.02 MB)
      ncei19_n48x25_w123x50_2021v1.tif (121.50 MB)
      ncei19_n48x25_w123x75_2021v1.tif (120.92 MB)
      ncei19_n48x25_w124x00_2021v1.tif (120.47 MB)
      ncei19_n48x25_w124x25_2021v1.tif (140.25 MB)
      ncei19_n48x25_w124x50_2021v1.tif (147.06 MB)
      ncei19_n48x50_w124x25_2021v1.tif (100.65 MB)
      ncei19_n48x50_w124x50_2021v1.tif (109.44 MB)



Catalog: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/wash_outercoast/index.html

Data URL: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/wash_outercoast/ + filename.tif

      ncei19_n47x00_w0124x00_2018v1.tif (207.21 MB) REMOVED
      ncei19_n47x00_w0124x25_2018v1.tif (187.27 MB) REMOVED
      ncei19_n47x25_w0124x25_2018v1.tif (195.08 MB) REMOVED
      ncei19_n47x50_w0124x25_2018v1.tif (200.55 MB) REMOVED
      ncei19_n47x50_w0124x50_2018v1.tif (158.97 MB) REMOVED
      ncei19_n47x75_w0124x50_2018v1.tif (176.32 MB) REMOVED
      ncei19_n48x00_w0124x50_2018v1.tif (189.39 MB) REMOVED
      ncei19_n48x00_w0124x75_2018v1.tif (163.14 MB) REMOVED
      ncei19_n48x25_w0124x75_2018v1.tif (196.46 MB) REMOVED
      ncei19_n48x50_w0124x75_2018v1.tif (165.07 MB) REMOVED

      ncei19_n46x75_w123x75_2025v1.tif (212.87 MB)
      ncei19_n46x75_w124x00_2025v1.tif (206.91 MB)
      ncei19_n46x75_w124x25_2025v1.tif (201.29 MB)
      ncei19_n47x00_w123x50_2025v1.tif (210.47 MB)
      ncei19_n47x00_w123x75_2025v1.tif (213.07 MB)
      ncei19_n47x00_w124x00_2025v2.tif (208.75 MB)
      ncei19_n47x00_w124x25_2025v2.tif (200.00 MB)
      ncei19_n47x25_w123x75_2025v1.tif (209.79 MB)
      ncei19_n47x25_w124x00_2025v1.tif (210.62 MB)
      ncei19_n47x25_w124x25_2025v2.tif (200.38 MB)
      ncei19_n47x25_w124x50_2025v1.tif (185.38 MB)
      ncei19_n47x50_w124x25_2025v2.tif (200.59 MB)
      ncei19_n47x50_w124x50_2025v2.tif (196.98 MB)
      ncei19_n47x75_w124x50_2025v2.tif (202.83 MB)
      ncei19_n47x75_w124x75_2025v1.tif (183.08 MB)
      ncei19_n48x00_w124x50_2025v2.tif (205.70 MB)
      ncei19_n48x00_w124x75_2025v2.tif (196.85 MB)
      ncei19_n48x25_w124x75_2025v2.tif (208.39 MB)
      ncei19_n48x25_w125x00_2025v1.tif (188.22 MB)
      ncei19_n48x50_w124x75_2025v2.tif (196.50 MB)
      ncei19_n48x50_w125x00_2025v1.tif (188.06 MB)

Catalog: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/wash_pugetsound/index.html

Data URL: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/wash_pugetsound/ + filename.tif

      ncei19_n47x25_w122x25_2024v1.tif (180.09 MB)
      ncei19_n47x25_w122x50_2024v1.tif (183.20 MB)
      ncei19_n47x25_w122x75_2024v1.tif (193.70 MB)
      ncei19_n47x25_w123x00_2024v1.tif (201.39 MB)
      ncei19_n47x25_w123x25_2024v1.tif (194.52 MB)
      ncei19_n47x50_w122x25_2023v1.tif (190.66 MB)
      ncei19_n47x50_w122x50_2023v1.tif (191.52 MB)
      ncei19_n47x50_w122x75_2023v1.tif (198.15 MB)
      ncei19_n47x50_w123x00_2023v1.tif (199.95 MB)
      ncei19_n47x50_w123x25_2023v1.tif (194.95 MB)
      ncei19_n47x75_w122x25_2023v1.tif (194.27 MB)
      ncei19_n47x75_w122x50_2023v1.tif (189.51 MB)
      ncei19_n47x75_w122x75_2023v1.tif (204.33 MB)
      ncei19_n47x75_w123x00_2023v1.tif (191.95 MB)
      ncei19_n47x75_w123x25_2023v1.tif (185.66 MB)
      ncei19_n48x00_w122x25_2023v1.tif (202.19 MB)
      ncei19_n48x00_w122x50_2023v1.tif (184.33 MB)
      ncei19_n48x00_w122x75_2023v1.tif (196.52 MB)
      ncei19_n48x00_w123x00_2023v1.tif (194.17 MB)
      ncei19_n48x25_w122x25_2024v1.tif (195.59 MB)
      ncei19_n48x25_w122x50_2024v1.tif (195.53 MB)
      ncei19_n48x25_w122x75_2024v1.tif (190.85 MB)

Catalog: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/columbia_river/index.html

Data URL: https://coast.noaa.gov/htdata/raster2/elevation/NCEI_ninth_Topobathy_2014_8483/columbia_river/ + filename.tif

    ncei19_n45x75_w122x00_2024v1.tif (204.91 MB)
    ncei19_n45x75_w122x25_2024v1.tif (203.95 MB)
    ncei19_n45x75_w122x50_2024v1.tif (200.02 MB)
    ncei19_n45x75_w122x75_2024v1.tif (196.95 MB)
    ncei19_n45x75_w123x00_2024v1.tif (204.90 MB)
    ncei19_n46x00_w122x75_2024v1.tif (201.63 MB)
    ncei19_n46x00_w123x00_2024v1.tif (209.58 MB)
    ncei19_n46x25_w123x00_2024v1.tif (210.19 MB)
    ncei19_n46x25_w123x25_2024v1.tif (209.52 MB)
    ncei19_n46x25_w123x50_2024v1.tif (207.76 MB)
    ncei19_n46x25_w123x75_2024v1.tif (210.24 MB)
    ncei19_n46x25_w124x00_2024v1.tif (213.62 MB)
    ncei19_n46x25_w124x25_2024v1.tif (188.71 MB)
    ncei19_n46x50_w123x50_2024v1.tif (207.65 MB)
    ncei19_n46x50_w123x75_2024v1.tif (212.70 MB)
    ncei19_n46x50_w124x00_2024v1.tif (213.46 MB)
    ncei19_n46x50_w124x25_2024v1.tif (200.29 MB)
