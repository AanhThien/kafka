from kafka import KafkaProducer
import json
import time

# Kafka server và topic
KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME = 'demo-topic'

# Tạo producer
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_SERVER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Gửi dữ liệu
for i in range(20):
    message = {'message': f'Hello vl! {i}'}
    producer.send(TOPIC_NAME, message)
    print(f"Sent: {message}")
    time.sleep(1)

# Đảm bảo gửi hết
producer.flush()

# Đóng kết nối
producer.close()
