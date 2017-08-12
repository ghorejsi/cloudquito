""" RDS interactions
"""
import boto3
from itertools import chain


class DBInstances(object):
    """RDS DB instance Related collection and aggregation functions
    """

    def __init__(self):
        self.__client = boto3.client('rds')

    def collect(self, filters: list):
        """
        Collect resources matching filter
        :param self:
        :param filters: List of filter items
        """

        response = self.__client.describe_db_instances(Filters=filters)
        db_instances = response['DBInstances']

        for db_instance in db_instances:
            yield db_instance
