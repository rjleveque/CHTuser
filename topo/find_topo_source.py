
import re
regexp = re.compile(r"(?P<fname>[^ ]*).nc ")
regexp_tif = re.compile(r"(?P<fname>[^ ]*).tif ")

# Load list of topo file sources found so far:
topo_sources_file = 'topo_sources_cascadia.md'
source_info_lines = open(topo_sources_file).readlines()

print(f'List of catalogs found in {topo_sources_file}:')
print('Warning: This list may not be up to date!')
source_info = {}
for s in source_info_lines:
    if 'Catalog:' in s:
        catalog = s.replace('Catalog: ','').strip()
        print('  Catalog = ',catalog)
    if 'Data URL:' in s:
        url = s.replace('Data URL: ','')
        url = url.replace('/ + filename.nc','').strip()
        url = url.replace('/ + filename.tif','').strip()
        #print(' +++   URL = ',url)
    if 'REMOVED' in s:
        continue  # skip data sets that have been removed
    result = regexp.search(s.replace('\t',' '))
    if result:
        fname = f'{result.group('fname')}.nc'
        file_url = f'{url}/{fname}'
        source_info[fname] = (catalog, file_url)
    result_tif = regexp_tif.search(s.replace('\t',' '))
    if result_tif:
        fname = f'{result_tif.group('fname')}.tif'
        #file_url = s.strip().split(' ')[0]
        file_url = f'{url}/{fname}'
        source_info[fname] = (catalog, file_url)

def tile_coords(x, y, verbose=False):

    tile_catalog = None
    tile_url = None

    q,r = divmod(y,1)
    yint = int(q)
    rbin = int(divmod(r, 0.25)[0])
    if rbin == 3:
        rbin = 0
        yint += 1
    else:
        rbin += 1
    tile_name = f'n{yint}x{rbin*25:02d}'

    if x < 0:
        x = -x
        hemi = 'w'
    else:
        hemi = 'e'

    q,r = divmod(x,1)
    xint = int(q)
    rbin = int(divmod(r, 0.25)[0])
    if rbin == 3:
        rbin = 0
        xint += 1
    else:
        rbin += 1
    tile_name += f'_{hemi}{xint:03d}x{rbin*25:02d}'
    if verbose:
        print(f'Point lies in tile with NW corner: {tile_name}')
    return tile_name

def find_tile_url(tile_name, verbose=True):

    tile_urls = []
    for s in source_info.keys():
        if tile_name in s:
            if verbose:
                print(f'\n  {tile_name} found in:\n    Catalog: ', source_info[s][0])
                print('    URL: ', source_info[s][1])
            tile_catalog, tile_url = source_info[s]
            tile_urls.append(tile_url)
        tile_name_alt = tile_name.replace('_w','_w0')  # since name sometimes has e.g. 'w_0124x'
        if tile_name_alt in s:
            if verbose:
                print(f'\n  {tile_name} found in:\n    Catalog: ', source_info[s][0])
                print('    URL: ', source_info[s][1])
            tile_catalog, tile_url = source_info[s]
            tile_urls.append(tile_url)

    return tile_urls



def make_tile_text(y2, x1):
    from clawpack.geoclaw import kmltools
    import numpy as np
    y1 = y2 - 0.25
    x2 = x1 + 0.25
    extent = [x1,x2,y1,y2]
    y2a = int(np.floor(y2))
    y2b = int(np.mod(y2,1)*100)
    if y2b==0: y2b = '00'
    x1a = int(np.floor(abs(x1)))
    x1b = int(np.mod(abs(x1),1)*100)
    if x1b==0: x1b = '00'
    #print('+++ x1 = %.2f, x1a = %s, x1b = %s' % (x1,x1a,x1b))
    name = 'n%ix%s_w%ix%s' % (y2a,y2b,x1a,x1b)
    #kmltools.box2kml(extent, fname=name+'.kml', name=name,
    #                color='FFFFFF',width=1)

    mapping = {}
    mapping['x1'] = x1
    mapping['x2'] = x2
    mapping['y1'] = y1
    mapping['y2'] = y2
    mapping['elev'] = 0.
    mapping['name'] = name
    mapping['desc'] = "  x1 = %s, x2 = %s\n" \
                            % (kmltools.f2s(x1),kmltools.f2s(x2)) \
                    + "  y1 = %s, y2 = %s" % (kmltools.f2s(y1),kmltools.f2s(y2))
    mapping['color'] = 'w'
    mapping['width'] = 1

    tile_text = kmltools.kml_region(mapping)

    return tile_text

def make_combined_tile_kml(name, xrange, yrange):
    from clawpack.geoclaw import kmltools

    kml_text = kmltools.kml_header(name)

    for y2 in yrange:
        for x1 in xrange:
            tile_text = make_tile_text(y2,x1)
            kml_text = kml_text + tile_text

    kml_text = kml_text + kmltools.kml_footer()
    fname = f'{name.replace(' ','_')}.kml'
    kml_file = open(fname,'w')
    kml_file.write(kml_text)
    print('Created ',fname)
