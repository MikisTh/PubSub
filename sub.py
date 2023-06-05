import os
from google.cloud import pubsub_v1

subscriber = pubsub_v1.SubscriberClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='MY_TOPIC_NAME'
)

subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    sub='MY_SUBSCRIPTION_NAME'
)

def callback(message):
    print(message.data)
    message.ack()

with pubsub_v1.SubscriberClient() as subscriber:
    subscriber.create_subscription(
        name=subscription_name, topic=topic_name)
    future = subscriber.subscribe(subscription_name, callback)