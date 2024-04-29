from functools import reduce
import httpx
from itertools import groupby
import json


timeout = httpx.Timeout(10, read=60)
client = httpx.Client(timeout=timeout)

URL = "https://aact.ctti-clinicaltrials.org/definitions.json"


def merger(acc: dict, d: dict):
    acc |= d
    return acc


def create_data_dict(ds):
    out = {}
    for table_name, grouper in ds:
        out[table_name] = reduce(merger, grouper, {})
    return out


def save_json(resp):
    as_dict = groupby(
        ({v["column"]: v["data type"], "table": v["table"]} for v in resp.json()),
        lambda obj: obj["table"],
    )
    data_dict = create_data_dict(as_dict)
    with open("data_dictionary.json", "w") as f:
        json.dump(data_dict, f, indent=4)


if __name__ == "__main__":
    resp = client.get(URL)
    save_json(resp)
