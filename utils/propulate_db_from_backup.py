"""

"""
import json
from datetime import datetime
import os
from importlib import import_module
from pathlib import Path
from collections import namedtuple
from typing import NamedTuple
import logging
from ..order_app.models import OrderSnapshot


CONFIG_MODULE = import_module("config.settings.test_settings")
BACKUP_DIR = CONFIG_MODULE.BACKUP_DIR
raw_response = namedtuple("RawResponse", "lookup_time json_as_bytes json_obj "
                                         "hash_field")
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def load_files_from_dir(backup_dir: Path) -> list[NamedTuple]:
    """
    Walk through backup directory with web cache (raw JSON responses)
    read them and return in a sequence.
    Note that each file (JSON response) were saved with a name at what time
    if was requested.
    Lookup_time is used further as a model field
    """
    #TODO: rewrite with iterator
    loaded_files = []
    for base_path, dirs, files in os.walk(backup_dir):
        for _file in files:
            # FIXME: dot separator was used with outdated version of API
            #  where time format was 13 digits
            timestamp = float(".".join(_file.split(".")[:2]))
            lookup_time = datetime.fromtimestamp(timestamp)
            with open(os.path.join(base_path, _file), "rb") as cm:
                loaded_files.append(
                    raw_response(
                        lookup_time=lookup_time,
                        json_as_bytes=cm.read(),
                        json_obj={},
                        hash_field=""
                    )
                )

    return loaded_files


def filter_out_bad_responses(responses: list) -> list:
    """
    Was needed because previous web caching mechanism was dumb
     and didn't check the response value.
    TODO: no needed actually. Just delete bad responses from backup dir and
     rewrite web caching mechanism to check JSON for being valid
    """
    resp_502 = b"HTTPError: HTTP Error 502: Bad Gateway\n"
    return list(filter(lambda r: r.json_as_bytes not in (resp_502, b""),
                       responses))


def filter_out_bad_json_objects(responses: list) -> list:
    """
    TODO: no needed actually. Just delete bad responses from backup dir and
     rewrite web caching mechanism to check JSON for being valid
    """
    json_at_time_objects = []
    for response in responses:
        try:
            json_obj = json.loads(response.json_as_bytes)
            if json_obj and getattr(json_obj, "result") == "success":
                json_at_time_objects.append(
                    raw_response(
                        lookup_time=response.lookup_time,
                        json_as_bytes=response.json_as_bytes,
                        json_obj=json_obj,
                        hash_field=""
                    )
                )
        except json.JSONDecodeError as err:
            LOGGER.debug(err)
            raise err
        except Exception as err:
            LOGGER.debug(err)
            raise err

    return json_at_time_objects


def get_hash_of_orders(json_at_time_objects: list) -> list:
    """"""
    json_with_hash_objects = []
    for json_with_hash in json_with_hash_objects:
        sorted_lst = []
        json_obj = json_with_hash.json_obj
        orders = json_obj["buyOrders"] + \
                 json_obj["sellOrders"]
        for order in orders:
            row_tuple = (
                order["price"], order["amount"],
                order["total"], order["date"],
                order["orderId"], order["label"],
                order["type"])
            sorted_lst.append(row_tuple)
        sorted_lst.sort(key=lambda x: x[0])
        sorted_tuple = tuple(sorted_lst)
        hash_field = md5(json.dumps(sorted_tuple).encode("UTF-8"))

    return json_with_hash_objects

def create_datebase_row(json_hex_at_time_object: list) -> None:
    """"""
    hash_field = json_hex_at_time_object.hash_field
    hash_field = json_hex_at_time_object.hash_field
    hash_field = json_hex_at_time_object.hash_field
    obj, created = OrderSnapshot.objects.get_or_create(
        hash_field=hash_field.hexdigest())
    if not created:
        # There is a row with given unique hash
        print(
            "Cannot create Snapshot coz already "
            "created"
        )
    else:
        # There is NO row with given unique hash
        obj.lookup_time = lookup_time
        obj.data = data
        obj.save()


if __name__ == '__main__':
    raw_responses = load_files_from_dir(BACKUP_DIR)
    filtered_resps = filter_out_bad_responses(raw_responses)
    json_at_time_seq = filter_out_bad_json_objects(filtered_resps)
    json_objs_at_time_seq = get_hash_of_orders(json_at_time_seq)
