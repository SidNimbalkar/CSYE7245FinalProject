from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('sample1', b'Hello, World!')
print ("done")
producer.flush()
