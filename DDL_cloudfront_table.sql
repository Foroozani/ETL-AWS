-- Create a table that points to your data in S3, using this query template, with your S3 location sub’d in.
-- This query also shows the fields you’ll have access to in your SQL queries

CREATE EXTERNAL TABLE IF NOT EXISTS `cloudfrontdb.cloudfront_may_october`(
  `date_view` DATE, 
  `time_view` string, 
  `location` string, 
  `bytes` bigint, 
  `request_ip` string, 
  `method` string, 
  `host` string, 
  `uri` string, 
  `status` bigint, 
  `referrer` string, 
  `user_agent` string, 
  `query_string` string, 
  `cookie` string, 
  `result_type` string, 
  `request_id` string, 
  `host_header` string, 
  `request_protocol` string, 
  `request_bytes` bigint, 
  `time_taken` float, 
  `xforwarded_for` string, 
  `ssl_protocol` string, 
  `ssl_cipher` string, 
  `response_result_type` string, 
  `http_version` string, 
  `fle_status` bigint, 
  `fle_encrypted_fields` bigint, 
  `c_port` bigint, 
  `time_to_first_byte` float, 
  `x_edge_detailed_result_type` string, 
  `sc_content_type` bigint, 
  `sc_content_len` bigint, 
  `sc_range_start` bigint, 
  `sc_range_end` bigint)
PARTITIONED BY ( 
  `year` string, 
  `month` string, 
  `day` string, 
  `hour` string)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY '\t' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://degruyter-cdnlogging-live-data/logs/'
TBLPROPERTIES (
  'compressionType'='gzip',
  'skip.header.line.count'='2',
  'classification'='csv',
  'areColumnsQuoted'='false', 
  'columnsOrdered'='true', 
  'commentCharacter'='#',  
  'delimiter'='\t', 
  'typeOfData'='file');

-- Load partitions afterwards
-- Load partitions – Runs the MSCK REPAIR TABLE table_name statement in the Athena Query Editor. This option is available only if the table has partitions.