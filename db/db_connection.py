from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxDBHandler:
    def __init__(self, url, token, org, bucket):
        self.client = InfluxDBClient(url=url, token=token)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.org = org
        self.bucket = bucket

    def insert_data(self, point):
        self.write_api.write(self.bucket, self.org, point)

    def retrieve_data(self, query):
        query_api = self.client.query_api()
        result = query_api.query(query, org=self.org)
        return result

influxdb_handler = InfluxDBHandler(
    url="http://localhost:8086",
    token="fCnHWK6yPm-SPoz0P_Waq8IBkfxUmBcx3AdD4gxexZVmwyfo8_FRPpTWET4Q5nWBJjEf_KOihgIAk_nrxEx02g==",
    org="d760ec0fc70bb00b",
    bucket="Benchmark"
)