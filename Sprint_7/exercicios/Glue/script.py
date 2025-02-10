import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper, count, desc

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

nomes_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": ","}
).toDF()

print("Schema do DataFrame:")
nomes_df.printSchema()

nomes_df = nomes_df.withColumn("nome", upper(col("nome")))

linha_contagem = nomes_df.count()
print(f"Contagem de linhas presentes no dataframe: {linha_contagem}")

contagem_ano_sexo = nomes_df.groupBy("ano", "sexo").agg(count("nome").alias("contagem_nomes"))
contagem_ano_sexo = contagem_ano_sexo.orderBy(desc("ano"))
print("Contagem de nomes agrupada por ano e sexo:")
contagem_ano_sexo.show()

nome_feminino = nomes_df.filter(col("sexo") == "F").groupBy("nome", "ano").agg(count("nome").alias("contagem"))
nome_feminino = nome_feminino.orderBy(desc("contagem")).limit(1)
print("Nome feminino com mais registros:")
nome_feminino.show()

nome_masculino = nomes_df.filter(col("sexo") == "M").groupBy("nome", "ano").agg(count("nome").alias("contagem"))
nome_masculino = nome_masculino.orderBy(desc("contagem")).limit(1)
print("Nome masculino com mais registros :")
nome_masculino.show()

registros_por_ano = nomes_df.groupBy("ano").agg(count("nome").alias("total_registros"))
registros_por_ano = registros_por_ano.orderBy("ano").limit(10)
print("Total de registros para cada ano (primeiros 10):")
registros_por_ano.show()

output_path = f"{target_path}/frequencia_registro_nomes_eua"
nomes_df.write.partitionBy("sexo", "ano").mode("overwrite").format("json").save(output_path)
print(f"DataFrame salvo em: {output_path}")

job.commit()
