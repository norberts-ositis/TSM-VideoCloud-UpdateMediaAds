# Functions for TSM API
import tsmapi_v4
from tsmapi_v4_config import *
import time


def list_media(offset=0, limit=1,
               date_from=None,
               date_to=None,
               item_id=None,
               ids=None,
               id_from=None,
               id_to=None,
               item_asset_id=None,
               cat_id=None,
               item_title=None,
               item_status='all',
               only_available=1):

    data = {'object': 'media', 'action': 'list', 'options': {'limit': limit, 'offset': offset}}
    if date_from:
        data['options']['date_from'] = date_from
    if date_to:
        data['options']['date_to'] = date_to
    if item_id:
        data['options']['item_id'] = item_id
    if ids:
        data['options']['id'] = ids
    if id_from:
        data['options']['id_from'] = id_from
    if id_to:
        data['options']['id_to'] = id_to
    if item_asset_id:
        data['options']['item_asset_id'] = item_asset_id
    if cat_id:
        data['options']['cat_id'] = cat_id
    if item_title:
        data['options']['item_title'] = item_title
    data['options']['item_status'] = item_status
    data['options']['only_available'] = only_available

    request = tsmapi_v4.TSMAPI(TSMAPI_URL, TSMAPI_KEY, TSMAPI_SECRET, int(time.time()))
    return request.send_post(data)


def update_media_ads(system_id, ads):
    data = {'object': 'media', 'action': 'update', 'parameters': {'system_id': system_id, 'ads': ads}}
    request = tsmapi_v4.TSMAPI(TSMAPI_URL, TSMAPI_KEY, TSMAPI_SECRET, int(time.time()))
    return request.send_post(data)
