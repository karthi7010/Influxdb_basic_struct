import time

from influxdb_client import Point
from db.db_connection import influxdb_handler


def write(measurement: str, tags: dict, fields: dict):
    # Create a Point object
    point = Point(measurement)

    # Add tags
    for key, value in tags.items():
        point.tag(key, value)

    # Add fields
    for field, value in fields[0].items():
        point.field(field, value)

    # point.time = time.time_ns()
    data = influxdb_handler.insert_data(point=point)
    return point


def retrive(query: str):
    data = influxdb_handler.retrieve_data(query=query)
    return data


def get_datas():
    try:
        # Retrieve all data from the InfluxDB bucket
        query = f'from(bucket:"{influxdb_handler.bucket}") |> range(start: -30d) |> group(columns: ["PatchId"])'
        result = influxdb_handler.client.query_api().query(
            query, org=influxdb_handler.org)

        # Process and return the data
        data = []
        for table in result:
            for row in table.records:
                data.append(row.values)

        return result

    except Exception as e:
        raise RuntimeError(f"Failed to retrieve data from InfluxDB: {str(e)}")
