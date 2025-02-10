import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, explode, lit, when

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos
s3_path_csv = "s3://datalake-pedrovilela/Trusted/CSV/PARQUET/Movies/"
s3_path_tmbd = "s3://datalake-pedrovilela/Trusted/TMDB/PARQUET/Movies/2025/01/20/"
s3_path_extras = "s3://datalake-pedrovilela/Trusted/Extras/PARQUET/Movies/2025/01/20/"
s3_output_path = "s3://datalake-pedrovilela/Refined/"

# Lista de IDs de filmes destacados
filmesGerais = [
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
    'tt6751668',
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
    'tt7983894'
]

# Lendo Parquets
csv_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="parquet",
    connection_options={"paths": [s3_path_csv]},
    transformation_ctx="csv_df"
).toDF()

tmdb_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="parquet",
    connection_options={"paths": [s3_path_tmbd]},
    transformation_ctx="tmdb_df"
).toDF()

extras_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="parquet",
    connection_options={"paths": [s3_path_extras]},
    transformation_ctx="extras_df"
).toDF()

# Padronizando coluna chave de junção
csv_df = csv_df.withColumnRenamed("id", "filme_id")
tmdb_df = tmdb_df.withColumnRenamed("ID IMDb", "filme_id")
extras_df = extras_df.withColumnRenamed("ID", "filme_id")
extras_df = extras_df.withColumnRenamed("Título Original", "Título Original Extras")

# Realizando junção
joined_df = csv_df.join(tmdb_df, on="filme_id", how="left") \
                  .join(extras_df, on="filme_id", how="left")

# Função para adicionar a nova coluna "filme_destacado"
joined_df = joined_df.withColumn(
    "filmeGeral", when(col("filme_id").isin(filmesGerais), True).otherwise(False))

# Criando tabelas
fato_filmes = joined_df.select(
    col("filme_id").alias("id"),
    col("Título").alias("tituloPrincipal"),
    col("Título Original").alias("tituloOriginalTMDB"),
    col("tituloPincipal").alias("tituloOriginalCSV"),
    col("Ano de Producao").alias("dataProducao"),
    col("Data de Lançamento").alias("dataLancamento"),
    col("Média das Avaliações").alias("notaMedia"),
    col("Total de Votos").alias("totalVotos"),
    col("Popularidade").alias("popularidade"),
    col("Orçamento Total (USD)").alias("orcamento"),
    col("Receita Total (USD)").alias("receita"),
    col("filmeGeral")
)

dim_streaming = joined_df.select(
    col("filme_id").alias("id"),
    explode(col("Plataformas de Streaming")).alias("plataformasStreaming")
)

dim_generos = joined_df.select(
    col("filme_id").alias("id"),
    explode(col("Gêneros")).alias("generos")
)

# Salvando arquivos parquet
glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(fato_filmes, glueContext, "fato_filmes"),
    connection_type="s3",
    connection_options={"path": s3_output_path + "fato_filmes/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(dim_streaming, glueContext, "dim_streaming"),
    connection_type="s3",
    connection_options={"path": s3_output_path + "dim_streaming/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(dim_generos, glueContext, "dim_generos"),
    connection_type="s3",
    connection_options={"path": s3_output_path + "dim_generos/"},
    format="parquet"
)

job.commit()
