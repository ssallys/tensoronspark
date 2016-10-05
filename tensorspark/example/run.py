import sys
import tensorspark.example.spark_mnist as mnist
from pyspark import SparkContext

if __name__ == "__main__":
	sc = SparkContext()
	num_epoch = int(sys.argv[1]) if len(sys.argv) > 1 else 2

	mnist.train(sc=sc, user='etri', name='mnist_try', server_host='localhost', server_port=10080,
                  sync_interval=100, batch_size=100, num_partition=1, num_epoch=num_epoch)
	spark.stop()
