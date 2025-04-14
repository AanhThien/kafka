from kafka import KafkaConsumer
import json

# Kafka server và topic
KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME = 'demo-topic'

# Tạo consumer
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=[KAFKA_SERVER],
    group_id=TOPIC_NAME,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Lắng nghe các messages và xử lý
print(f"Listening for messages on {TOPIC_NAME}...")
for message in consumer:
    print(f"Received: {message.value}")
