# UpdateMediaAds
import tsmapi_v4_functions

# Number of media assets in one batch
LIMIT = 10

# Set category ID to the one where to change the ads
CATEGORY_ID = 9999999

# To clean up ads use this
ADS_CONFIG = []

# To set ads use this
# ADS_CONFIG = [
#     {'url': 'https://1188lv.adocean.pl/ad.xml?id=2wsMiSef7V.pZ8R4M5D2yzr8E2bzbPJacDe5VWHFlB3.e7', 'type': 'PRE',
#      'adsType': 'VAST'},
#     {'url': 'https://1188lv.adocean.pl/ad.xml?id=2wsMiSef7V.pZ8R4M5D2yzr8E2bzbPJacDe5VWHFlB3.e7', 'type': 'MID',
#      'offset': '50%', 'adsType': 'VAST'},
#     {'url': 'https://1188lv.adocean.pl/ad.xml?id=2wsMiSef7V.pZ8R4M5D2yzr8E2bzbPJacDe5VWHFlB3.e7', 'type': 'POST',
#      'adsType': 'VAST'}
# ]


if __name__ == '__main__':
    offset = 0
    while media_list := tsmapi_v4_functions.list_media(offset, LIMIT, cat_id=CATEGORY_ID):
        for media in media_list:
            print(media['id'])
            print(media['ads'])
            tsmapi_v4_functions.update_media_ads(media['id'], ADS_CONFIG)
        offset += LIMIT
