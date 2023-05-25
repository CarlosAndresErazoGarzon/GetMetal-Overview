from data_bands import bands
import functions_metal as mDB

def initialize():

    for band in bands:
        metadata = band.copy()
        band_id     = metadata.pop("id")
        band_name   = metadata.pop("name")

        mDB.index_with_text(band_id, band_name, metadata)

    for i in range(len(bands)):
        for j in range(i+1, len(bands)):
            idA = bands[i]['id']
            idB = bands[j]['id']
            
            label = 1 if bands[i]['genre'] == bands[j]['genre'] else -1
            
            mDB.tune_with_payload(idA, idB, label)
    