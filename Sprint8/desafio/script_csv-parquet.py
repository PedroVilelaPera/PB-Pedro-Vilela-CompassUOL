import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext  = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Lista de filmes escolhidos para a analises
filmes_escolhidos = [
    "Avengers: Infinity War",
    "Star Wars: Episode VIII - The Last Jedi",
    "Jurassic World",
    "The Lion King",
    "Black Panther",
    "Incredibles 2",
    "Aquaman",
    "Bohemian Rhapsody",
    "Spider-Man: Into the Spider-Verse",
    "Toy Story 4",
    "Call Me by Your Name",
    "The Shape of Water",
    "The Big Sick",
    "The Greatest Showman",
    "Lady Bird",
    "Black Panther",
    "First Man",
    "A Star Is Born",
    "The Favourite",
    "The Shape of Water",
    "Parasite",
    "The Last Letter from Your Lover",
    "A Hidden Life",
    "The King",
    "Bombshell",
    "Spider-Man: No Way Home",
    "Avengers: Endgame",
    "F9: The Fast Saga",
    "No Time to Die",
    "Dune",
    "Black Widow",
    "Eternals",
    "The Batman",
    "Jurassic World: Dominion",
    "Top Gun: Maverick",
    "Avengers: Infinity War",
    "Star Wars: Episode VIII - The Last Jedi",
    "Jurassic World",
    "The Lion King",
    "Black Panther",
    "Incredibles 2",
    "Aquaman",
    "Bohemian Rhapsody",
    "Spider-Man: Into the Spider-Verse",
    "Toy Story 4"
]

# Lendo arquivo .csv
csv_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
).toDF()

# Filtrando filmes escolhidos
csv_filtrado = csv_df.filter(csv_df["tituloPincipal"].isin(filmes_escolhidos))

# Convertendo dataFrame filtrado para parquet e salvando
csv_filtrado.coalesce(1).write \
    .mode("overwrite") \
    .parquet(target_path)

job.commit()
