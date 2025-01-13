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

source_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

lista_nomes_arquivos = ['pop_pan_drama_romance.json', 'pop_pan_geral.json', 
                        'pop_prepan_drama_romance.json', 'pop_prepan_geral.json']

dataframes = []

# Transforma cada um dos arquivos json em df para a junção
for arquivo in lista_nomes_arquivos:
    file_path = f"{source_path}/{arquivo}"
    dynamic_frame = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths": [file_path]},
        format="json"
    )

    if dynamic_frame.count() > 0:
        df = dynamic_frame.toDF()
        df.write.mode("append").parquet(f"{target_path}/JSON/PARQUET/Movies/2025/01/08/")

# Finalizando o job
job.commit()
