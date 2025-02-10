import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Lendo os argumentos do script
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

# Transforma cada um dos arquivos JSON em DataFrame e os adiciona na lista
for arquivo in lista_nomes_arquivos:
    file_path = f"{source_path}/{arquivo}"
    dynamic_frame = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths": [file_path]},
        format="json"
    )

    if dynamic_frame.count() > 0:
        df = dynamic_frame.toDF()
        dataframes.append(df)

# Combina todos os DataFrames em um único DataFrame
if dataframes:
    df_combinado = dataframes[0]
    for df in dataframes[1:]:
        df_combinado = df_combinado.unionByName(df, allowMissingColumns=True)

    # Salva o DataFrame combinado em um único arquivo Parquet
    output_path = f"{target_path}/TMDB/PARQUET/Movies/2025/01/20/"
    df_combinado.coalesce(1).write.mode("overwrite").parquet(output_path)

    print(f"Arquivo Parquet único salvo em: {output_path}")
else:
    print("Nenhum dado válido foi encontrado nos arquivos JSON.")

# Finalizando o job
job.commit()
