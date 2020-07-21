import findspark
findspark.init()
from pyspark.sql import SparkSession
def main():
    spark = SparkSession.builder \
        .master("local") \
        .appName("Word Count") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    print(spark)
    l = [('Alice', 1)]
    rdd = spark.createDataFrame(l).collect()
    print(rdd)

if __name__ == '__main__':
    main()