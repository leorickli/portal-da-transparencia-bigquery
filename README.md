# portal-da-transparencia-kafka

![Screenshot 2024-03-05 213908](https://github.com/leorickli/portal-da-transparencia-kafka/assets/106999054/4745b7d7-b864-40c4-855e-14df141507db)

*Google Cloud Pub/Sub is a messaging service provided by Google Cloud Platform (GCP) that enables asynchronous communication between different components of a distributed system.*

### 1. Choose 5 fundamental concepts of GCP Pub/Sub and describe them

1. *Topic:*
  - A topic is a named resource to which messages are sent by publishers and from which messages are pulled by subscribers.
  - Publishers, which are responsible for producing messages, send them to specific topics.
  - Topics serve as the channels through which messages are organized and distributed to interested subscribers.
3. *Subscription:*
  - A subscription represents the stream of messages from a single, specific topic, to be delivered to the subscribing application.
  - Subscribers are the consumers that receive and process messages from subscriptions.
  - Subscriptions are created within the context of a topic, and each subscription has its own acknowledgment state and message backlog.
4. *Message:*
  - A message is the unit of data transmitted between publishers and subscribers via Pub/Sub.
  - Messages contain the payload, which is the actual data being transmitted, and optional metadata like attributes.
  - The payload can be in any format, such as JSON or binary data, and can be up to 10 MB in size.
5. *Acknowledgment:*
  - Acknowledgment is the mechanism by which a subscriber informs Pub/Sub that it has successfully received and processed a message.
  - Once a message is acknowledged, Pub/Sub considers it as delivered and removes it from the subscription's backlog.
  - Subscribers have a configurable acknowledgment deadline, and if a message is not acknowledged within this deadline, Pub/Sub redelivers it to other subscribers.
6. *Push and Pull Delivery:*
  - Pub/Sub supports both push and pull mechanisms for delivering messages to subscribers.
  - Push Delivery: In push mode, Pub/Sub delivers messages directly to an endpoint (e.g., a webhook) specified by the subscriber. This requires the subscriber to expose a public endpoint.
  - Pull Delivery: In pull mode, subscribers explicitly request messages from Pub/Sub at their own pace. The subscriber controls when it pulls messages and acknowledges them.

### 2. Describe the architecture of GCP Pub/Sub

Google Cloud Pub/Sub has a distributed architecture designed for reliable message delivery. Publishers send messages to topics, which are logical channels. The Pub/Sub service manages message storage, retrieval, and distribution. Subscribers, connected to topics through subscriptions, consume messages. Subscribers use pull or push mechanisms for retrieval and acknowledge successful message processing. Messages, the units of data, have payloads and optional metadata. This architecture ensures efficient and scalable asynchronous communication between components in a distributed system.

### 3. Present examples of Pub/Sub utilization on SQL and noSQL databases

*Pub/Sub Utilization with SQL Database (e.g., Cloud SQL):*

Consider a scenario where you have a web application relying on a SQL database, such as Cloud SQL, to store user profiles. Users want real-time updates whenever there's a change to their profile.

In this case, you can implement a change event trigger on the SQL database to detect updates to the user profile table. This trigger acts as a publisher, and whenever a user profile is updated, it publishes a message to a Pub/Sub topic, let's call it "user_profile_updates." On the application side, you can have a subscriber service that listens to this topic. When a message is received, the user interface is updated in real-time, reflecting the changes made to the user profile. This enables users to receive immediate updates without the need for constant manual refreshing.

*Pub/Sub Utilization with NoSQL Database (e.g., Cloud Firestore):*

Now, let's consider a collaborative document editing application using a NoSQL database like Cloud Firestore. In this scenario, users want real-time collaboration updates as they edit a shared document.

The integration involves setting up a NoSQL database to store the collaborative document. For real-time updates, you can create a Pub/Sub topic, say "document_updates." A service acts as a publisher, and whenever a user makes changes to the document, it publishes a message to this topic. On the application side, a subscriber service is implemented to listen to the "document_updates" topic. As messages are received, the collaborative document is updated in real-time. This ensures that all users involved in the collaboration see live changes as they occur, fostering a seamless and responsive collaborative editing experience.

### 4. Describe the best advantages of using of GCP Pub/Sub

1. *Asynchronous Communication:*

Pub/Sub facilitates asynchronous communication between independent components of a system. This enables the decoupling of producers (publishers) and consumers (subscribers), allowing them to operate independently and asynchronously.

2. *Scalability:*

Pub/Sub is designed to scale horizontally, accommodating varying workloads and handling large volumes of messages with ease. This scalability is crucial for applications with unpredictable or fluctuating workloads.

3. *Reliability and Durability:*

Google Cloud Pub/Sub is built on Google's highly reliable and durable infrastructure. It ensures message persistence and delivery, even in the face of system failures or outages. Messages are retained until they are acknowledged by subscribers, providing durability.

4. *Global Availability:*

Pub/Sub is a globally distributed service, allowing you to create topics and subscriptions in multiple regions. This global availability enhances redundancy and fault tolerance, ensuring reliable message delivery across different geographical locations.

5. *Exactly-Once Delivery:*

Pub/Sub supports an "at-least-once" message delivery guarantee, which ensures that a message is delivered to a subscriber at least once. Additionally, its acknowledgment mechanism helps achieve "exactly-once" delivery semantics when subscribers properly acknowledge message processing.

6. *Real-Time Data Processing:*

Pub/Sub supports both push and pull mechanisms, making it suitable for real-time data processing scenarios. Subscribers can receive messages as soon as they are published, enabling quick and responsive systems.

7. *Integration with Other GCP Services:*

Pub/Sub seamlessly integrates with other Google Cloud Platform services, such as Cloud Functions, Dataflow, and BigQuery. This facilitates the building of end-to-end data pipelines and event-driven architectures.

8. *Security and Access Controls:*

Pub/Sub provides robust security features, including identity and access management (IAM) controls. This ensures that only authorized entities can publish or subscribe to topics and receive messages.

9. *Flexible Message Routing:*

Topics allow for flexible message routing, enabling publishers to categorize messages based on topics. Subscribers can then selectively subscribe to specific topics, ensuring that they only receive messages relevant to their needs.

10. *Cost-Efficiency:*

Google Cloud Pub/Sub offers a pay-as-you-go pricing model, allowing you to pay for the resources you consume. It eliminates the need for upfront investments in infrastructure and provides cost efficiency, especially for variable workloads.

### 5. What is a data pipeline?

A data pipeline is a sequence of processes that collect, transform, and move data from one or multiple sources to a destination, typically for analysis, storage, or further processing. It involves the extraction of raw data, its transformation into a usable format, and the loading of the processed data into a target system. Data pipelines play a crucial role in automating and streamlining the flow of information within an organization, enabling efficient data management, analysis, and decision-making.

### 6. Show two examples of data pipelines being applied in the day-to-day life

*Social Media Feeds:*

When you scroll through your social media feed, a data pipeline is at work. The pipeline collects data from various sources, including user posts, images, and interactions. It then processes this data to organize and prioritize content based on relevance, user preferences, and engagement history. The final output is the personalized feed you see, creating a seamless experience of consuming content tailored to your interests.

*Online Shopping Recommendations:*

When you shop online and receive product recommendations, a data pipeline is behind the scenes. This pipeline collects data on your browsing history, purchase behavior, and demographic information. The collected data is then processed to generate personalized recommendations using algorithms. The end result is a curated list of products that align with your preferences and past interactions, enhancing your shopping experience and potentially influencing your purchasing decisions.

### 7. Show the pipeline

#### First steps


