export AWS_ACCESS_KEY_ID=ASIAWVORA2AI76MX7Y7H
export AWS_SECRET_ACCESS_KEY=oJcvVfWmn7XhT8JXuNenWvN/s2q/7UK1EzUlfIvu
export AWS_SESSION_TOKEN=FwoGZXIvYXdzEJn//////////wEaDNHLTbDeL9um0vdwRCK9AfYRqiIZDf2sK1pnL2GN4CetipEXma4/F/r/iub2oIshFGB6bq1u3KwNL00lDeZQh+i4I4l/jeAmi1QNYXJ9B9AIJYngmdUWUsFFdFZ+dfo56C7Z3Dzgj2ZbccHSTe5Qx9jnVnqxVDCOudPhWc315HJDnUW5R0gBfDBPTr51n8hfaWx635YAxuvijtAQ7gd3lV3XenCgcQyeLRrq3UePnf6by9wjcVYPHi4oMA2GGKF1O8ecd3fhfoD36MKqSSifruqUBjItD4FcOn0gsrGM1es6SUtwvBePjpGFhxY5fA5EtPEkX4sKb0zT2QtCjOrk/L3f
export S3_URL="https://s3.amazonaws.com/stack-02-kalil-sptech-bucket-s"
export BLOB_URL="https://fileserverkalil01.blob.core.windows.net/containerkalil01?sv=2020-08-04&ss=bfqt&srt=sco&sp=rwdlacupitfx&se=2022-06-04T07:39:40Z&st=2022-06-03T23:39:40Z&spr=https&sig=l2BOftk2In4Xw055zVqpuY%2BaXLTrP8pOkJMQ4IPFScg%3D"

azcopy copy $S3_URL $BLOB_URL --recursive=true
