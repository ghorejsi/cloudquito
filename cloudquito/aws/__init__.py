""" AWS interactions wrapper for working with resources
"""
__all__ = ['ec2', 'rds']

import boto3


class AWS(object):
    """ Generalized functions for AWS account level actions
    """

    @staticmethod
    def get_account_id():
        return boto3.client('sts').get_caller_identity().get('Account')
