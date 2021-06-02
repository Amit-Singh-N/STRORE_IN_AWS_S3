import botocore

import boto3
import logging

from shared.abstract_client.producer import AbstractProducer

logger = logging.getLogger(__name__)

from io import BytesIO


class AmazonS3Uploader(AbstractProducer):
    S3_SERVICE = 's3'

    def __init__(self, **kwargs):
        assert kwargs.get('aws_secret_access_key'), 'aws secret access key missing'
        self.aws_secret_access_key = kwargs.get('aws_secret_access_key')

        assert kwargs.get('aws_access_key_id'), 'aws_access_key_id is missing'
        self.aws_access_key_id = kwargs.get('aws_access_key_id')

        assert kwargs.get('bucket'), 'bucket name missing'
        self.bucket = kwargs.get('bucket')

        self.client = boto3.client(__class__.S3_SERVICE,
                                   aws_access_key_id=self.aws_access_key_id,
                                   aws_secret_access_key=self.aws_secret_access_key)
        try:
            if not self.check_bucket(self.bucket):
                raise Exception('Bucket Not Found')
        except Exception as exc:
            raise exc

    def check_bucket(self, bucket):
        try:
            self.client.head_bucket(Bucket=bucket)
            return True
        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = int(e.response['Error']['Code'])
            if error_code == 403:
                raise Exception("Private Bucket. Forbidden Access!")
            elif error_code == 404:
                raise Exception("Bucket Does Not Exist!")

    def pre_send(self, *args, **kwargs):
        pass

    def send(self, message, **kwargs):
        key = kwargs.get('key')
        encoded_message = message.encode()
        file_like_obj = BytesIO(encoded_message)
        extra_args = dict()
        extra_args['ContentType'] = 'application/json'
        extra_args['ContentEncoding'] = 'gzip'
        response = self.client.upload_fileobj(file_like_obj, self.bucket, key, ExtraArgs=extra_args)
        return response

    def post_send(self, *args, **kwargs):
        pass

    def close(self, *args, **kwargs):
        pass

    def serialize_message(self, message, *args, **kwargs):
        pass

