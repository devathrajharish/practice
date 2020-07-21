import findspark
findspark.init()
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
def main():
    # spark = SparkSession.builder \
    #     .master("local") \
    #     .appName("Word Count") \
    #     .config("spark.some.config.option", "some-value") \
    #     .getOrCreate()

    # l = [('Alice', 1)]
    # rdd = spark.createDataFrame(l).collect()
    # print(rdd)
    sc = SparkContext('local')
    rdd = sc.textFile('example')
    print(rdd.first())

    
    sc.stop()

if __name__ == '__main__':
    main()