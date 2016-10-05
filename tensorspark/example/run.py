import sys
import tensorspark.example.spark_mnist as mnist
from pyspark import SparkContext

if __name__ == "__main__":
	num_epoch = int(sys.argv[1]) if len(sys.argv) > 1 else 2

	sc = SparkContext()
	mnist.train(sc=sc, user='etri', name='mnist_try', server_host='129.254.164.75', server_port=10080,
                  sync_interval=100, batch_size=100, num_partition=1, num_epoch=num_epoch)
	print('end of run')
