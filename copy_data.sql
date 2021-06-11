-- copy data from s3 to redshift via SQL-tool
copy users from 's3://foroozaniboto3demo/tickit/allusers_pipe.txt' 
iam_role 'arn:aws:iam::2945541:role/MyEuRedshiftRole' 
delimiter '|';
