import urllib2
from os import mkdir, listdir
import pandas as pd
from lxml import html

URL = 'http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean'
DEST_FOLDER = './data/'
MAX_INDEX = 27
COLS = ['year', 'week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI', 'VHI<15', 'VHI<35']

urls = [URL + '/L1_Mean_UKR.R{0}.txt'.format(str(i).zfill(2)) for i in range(1, MAX_INDEX + 1)]

def get_file_by_url(src_url, dest_file_prefix):
    res = urllib2.urlopen(src_url)
    loaded_date = res.info()['date']
    dest_file = compose_file_name(dest_file_prefix, loaded_date)
    with open(dest_file, 'wb') as f:
        f.write(res.read())

def compose_file_name(prefix, loaded_date):
    return DEST_FOLDER + prefix + '_' + str(loaded_date)

def write_to_files(file_names_prefix):
    mkdir(DEST_FOLDER)
    for index, url in enumerate(urls):
        get_file_by_url(url, file_names_prefix)

def load_all_into_frame(directory):
    data_files =  listdir(directory)
    for file in data_files:
         df = pd.read_csv(directory + file, header=1, names=COLS, index_col=False)
    return df

def load_into_frame(directory):
    data_files =  listdir(directory)
    df = pd.read_csv(directory + data_files[0], header=1, names=COLS, index_col=False)
    return df


def filter_frame(frame, name_col):
    frame = frame[frame[name_col] != -1]
    #print frame.info()
    return frame

def get_border_values_vhi(folder, name_col):
    frame = load_into_frame(folder)
    frame = filter_frame(frame, name_col)
    min = frame[name_col].min()
    max = frame[name_col].max()
    print min, max

def year_of_extreme_vhi(folder, name_col):
    frame = load_into_frame(folder)
    frame = filter_frame(frame, name_col)
    frame = frame[(frame[name_col]<=35)]
    print frame['year'].unique()

def parse_region_from_html():
    res = urllib2.urlopen('http://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/vh_browseByCountry_province.php?country_code=UKR&province_id=1')
    tree = html.fromstring(res.read())
    options = tree.xpath('//select[@id="Province"]/option/text()')
    return options

def get_regions_dict():
    region_list = parse_region_from_html()
    regions = {region.split(':')[0] : region.split(':')[1]
    for region in region_list if ':' in region}
    return regions

def create_region_frame():
    regions = get_regions_dict()
    df = pd.DataFrame(regions.items(), columns=['Region_Index', 'Regions'])
    print df.sort_values(['Regions'], ascending=True)

get_border_values_vhi(DEST_FOLDER, 'VCI')
year_of_extreme_vhi(DEST_FOLDER, 'VCI')
create_region_frame()
