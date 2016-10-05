import tensorspark.example.spark_mnist as mnist
from pyspark import SparkContext

sc = SparkContext()
mnist.train(sc=sc, user='etri', name='mnist_try', server_host='localhost', server_port=10080,
                  sync_interval=100, batch_size=100, num_partition=1, num_epoch=2)
