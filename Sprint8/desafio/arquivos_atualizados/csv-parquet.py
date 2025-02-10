import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Lista de filmes escolhidos para a analises
filmes_escolhidos = [
    'tt9683478',
    'tt1893273',
    'tt7798646',
    'tt3581652',
    'tt9100054',
    'tt9620292',
    'tt10293406',
    'tt11847410',
    'tt10366460',
    'tt3108894',
    'tt7983894',
    'tt10362466',
    'tt12676326',
    'tt8847712',
    'tt3661210',
    'tt9827834',
    'tt11161474',
    'tt9354842',
    'tt3907584',
    'tt9866072',
    'tt5726616',
    'tt5580390',
    'tt1517451',
    'tt5164432',
    'tt5776858',
    'tt3281548',
    'tt3104988',
    'tt7125860',
    'tt7653254',
    'tt5462602',
    'tt1289403',
    'tt2226597',
    'tt6472976',
    'tt5977276',
    'tt4799066',
    'tt3799232',
    'tt1667321',
    'tt7942742',
    'tt0385887',
    'tt3846674',
    'tt1160419',
    'tt10872600',
    'tt10272386',
    'tt9100054',
    'tt10539608',
    'tt3581652',
    'tt4244994',
    'tt9376612',
    'tt9032400',
    'tt7395114',
    'tt9620292',
    'tt8847712',
    'tt11161474',
    'tt3108894',
    'tt12676326',
    'tt11847410',
    'tt9354842',
    'tt3907584',
    'tt9866072',
    'tt7983894',
    'tt1825683',
    'tt1727824',
    'tt5726616',
    'tt5580390',
    'tt1517451',
    'tt6105098',
    'tt7131622',
    'tt7653254',
    'tt1213641',
    'tt4154756',
    'tt5308322',
    'tt6644200',
    'tt5164432',
    'tt3104988',
    'tt7125860',
    'tt1856101',
    'tt5462602',
    'tt7286456',
    'tt4633694',
    'tt6751668'
]

# Lendo arquivo .csv
csv_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
).toDF()

# Filtrando filmes escolhidos
csv_filtrado = csv_df.filter(csv_df["id"].isin(filmes_escolhidos))

# Convertendo dataFrame filtrado para parquet e salvando
csv_filtrado.coalesce(1).write \
    .mode("overwrite") \
    .parquet(target_path)

job.commit()
