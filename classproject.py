
def cleaning(spark):
    data = [
        ("Smith", 23, 5.3),
        ("Rashmi", 27, 5.8),
        ("Smith", 23, 5.3),
        ("Payal", 27, 5.8),
        ("Megha", 27, 5.4)
    ]
    columns = ["Name", "Age", "Height"]
    df = spark.createDataFrame(data=data, schema=columns)
    df.printSchema()
    df.show(truncate=False)
    df1 = df.dropDuplicates()
    print("After removing complete duplicates:")
    df1.show()
    df2 = df1.dropDuplicates(["Age", "Height"])
    print("After removing duplicates based on Age and Height:")
    df2.show()
