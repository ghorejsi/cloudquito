""" EC2 interactions
"""
import boto3
from itertools import chain
from .. import AWS


class Instances(object):
    """EC2 instance Related collection and aggregation functions
    """

    def __init__(self):
        self.__client = boto3.client('ec2')

    def collect(self, filters: list):
        """
        Collect resources matching filter
        :param self:
        :param filters: List of filter items
        """

        response = self.__client.describe_instances(Filters=filters)
        reservations = response['Reservations']

        for instance in chain.from_iterable([instance['Instances'] for instance in reservations]):
            yield instance


class Volumes(object):
    """EC2 ebs volume Related collection and aggregation functions
    """

    def __init__(self):
        self.__client = boto3.client('ec2')

    def collect(self, filters: list):
        """
        Collect resources matching filter
        :param self:
        :param filters: List of filter items
        """

        response = self.__client.describe_volumes(Filters=filters)
        volumes = response['Volumes']

        for volume in volumes:
            yield volume


class Snapshots(object):
    """EC2 EBS Snapshot collection and aggregation functions
    """

    def __init__(self):
        self.__client = boto3.client('ec2')

    def collect(self, filters: list):
        """
        Collect resources matching filter
        :param self:
        :param filters: List of filter items
        """

        response = self.__client.describe_snapshots(Filters=filters)
        snapshots = response['Snapshots']

        for snapshot in snapshots:
            yield snapshot


class AMIs(object):
    """EC2 AMI Related collection and aggregation functions
    """

    def __init__(self):
        self.__client = boto3.client('ec2')

    def collect(self, filters: list):
        """
        Collect resources matching filter
        :param self:
        :param filters: List of filter items
        """

        if 'owner-id' not in [key['Name'] for key in filters if 'Name' in key]:
            filters.append({
                'Name': 'owner-id',
                'Values': [AWS.get_account_id()]
            })

        response = self.__client.describe_images(Filters=filters)
        images = response['Images']

        for image in images:
            yield image