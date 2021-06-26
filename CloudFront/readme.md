## Analyze Amazon CloudFront access logs

[Blog](https://aws.amazon.com/blogs/big-data/analyze-your-amazon-cloudfront-access-logs-at-scale/)

*CloudFront logs*, export web distribution access log. By analysing cloudfront logs:

1. Reduce website latency: By knowing what are the popular objects/web pages that your customers are visiting you can get that from the logs and then base on that you can make sure that those content ate cacged closer to them. In that way they can access them much faster rather than having to experience the latency of going all the way towards your data center.

2. Content optimization: customer uses tablet, phones, laptop , .. you can find out the browser your visitors are using, and improve the performance. 

You can configure Amazon CloudFront to store access logs with detailed information of every request to S3. This lets you gain insight into your cache efficiency and learn how your customers are using your products. A common choice to run standard SQL queries on your data in S3 is [Amazon Athena](https://aws.amazon.com/blogs/big-data/easily-query-aws-service-logs-using-amazon-athena/). 

To extract metadata of your data one can use AWS GLUE. If you have proprietry format you can write your custom crawlers **BUT** for all the other open standards that are there [Glue](https://aws.amazon.com/blogs/big-data/work-with-partitioned-data-in-aws-glue/) will automatically discover the schema. 


### Refrences 
1. [Query the Log Data in Amazon S3](https://docs.aws.amazon.com/kinesis-agent-windows/latest/userguide/kaw-ds2s3-tutorial-step3.html)
2. [Work with partitioned data in AWS Glue](https://aws.amazon.com/blogs/big-data/work-with-partitioned-data-in-aws-glue/)
3. [Extended Log File Format](https://www.w3.org/TR/WD-logfile.html)


### Athena 
[Top 10 Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/)


