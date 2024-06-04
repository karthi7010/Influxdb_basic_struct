from connect import influxdb_handler


def write(measurement: str, tags: dict, fields: dict):
    data = influxdb_handler.insert_data(measurement=measurement, tags=tags, fields=fields)
    return data

def retrive(query: str):
    data = influxdb_handler.retrieve_data(query=query)
    return data