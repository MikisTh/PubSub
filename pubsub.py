import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()
topic_id = publisher.topic_id(project_id, topic_id)
subscription_id = subscriber.subscription_id(project_id, subscription_id)
response = publisher.list_topic_subscriptions(request={"topic": topic_id})


publisher = pubsub_v1.PublisherClient()
topic_id = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='MY_TOPIC_NAME'
   )
publisher.create_topic(name=topic_id)
future = publisher.publish(topic_id, b'Meu topico!', spam='eggs')
future.result()

 
subscriber = pubsub_v1.SubscriberClient()
topic_id = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='MY_TOPIC_NAME'
)

subscription_id = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    sub='MY_SUBSCRIPTION_NAME'
)

def callback(message):
    print(message.data)
    message.ack()

with pubsub_v1.SubscriberClient() as subscriber:
    subscriber.create_subscription(
        name=subscription_id, topic=topic_id)
    future = subscriber.subscribe(subscription_id, callback)

    response = publisher.list_topic_subscriptions(request={"topic": topic_id})
for subscription in response:
    print(subscription)

