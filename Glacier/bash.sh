#!/bin/sh

for x in `cat glacier-restore.txt`
  do
    echo "Begin restoring ... $x"
    aws s3api restore-object --restore-request '{"Days":10,"GlacierJobParameters":{"Tier":"Bulk"}}' --bucket degruyter-live-cdnlogging --key "$x"
    echo "Done restoring --->  $x"
  done