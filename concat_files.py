#! /usr/bin/env python

# Import Packages
import sys
import boto3

# Assign arguments
bucket = sys.argv[0]
prefix = sys.argv[1]
filename = sys.argv[2]

# Connect to S3 client
s3_client = boto3.client('s3')

data_holder = []
for key in list(map(lambda x: 
                    x['Key'], s3_client.list_objects(Bucket=bucket,
                                                     Prefix=prefix)['Contents'])):

    # Get data from each file
    data = (s3_client.get_object(Bucket=bucket, Key=key)['Body']
            .read().decode('utf-8'))

    # Collect data
    data_holder += data

# Write data as 1 file
s3_client.put_object(Bucket=bucket, 
                     Key=prefix.replace('landing','gold')+'/'+filename, 
                     Body=bytes('\n'.join(data_holder).encode('UTF-8')))