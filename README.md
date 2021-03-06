# aws_cloudwatch
```
Check_MK AWS Cloudwatch Data Source

USAGE: aws_cloudwatch [OPTIONS] NAMESPACE DIMENSION
       aws_cloudwatch -h

ARGUMENTS:
  NAMESPACE                       AWS Cloudwatch namespace
  DIMENSION                       AWS Cloudwatch dimension to select

OPTIONS:
  -h, --help                      Show this help message and exit
  -p MINUTES, --period MINUTES    Metric period, default is 1 minute
  -i MINUTES, --interval MIUNTES  Metric query time interval, default is 15 minutes
  -a, --agent                     Also retrieve data from the normal Check_MK Agent.
                                  This makes sense if you query a EC2 instance that
                                  you also want to monitor with Check_MK.
  -t, --timeout SECS              Set the network timeout when connecting the agent (option -a).
                                  Default is 60 seconds.
  --debug                         Debug mode: let Python exceptions come through
```
