# portal-da-transparencia-streaming

<img width="706" alt="Screenshot 2024-03-13 at 23 47 15" src="https://github.com/leorickli/portal-da-transparencia-streaming/assets/106999054/9756a9b2-5f8b-485f-8fbd-0af2ace8867f">

This project explores the Google Cloud Platform's resources to create a streaming pipeline to process real-time data from the Portal da Transparência API. Actually, there is no real-time data provided by this API, we have to generate the real-time data through a Python script.

*The Transparency Portal (Portal da Transparência) is a digital platform designed to provide detailed information about public entities' expenditures and financial management. Its primary goal is to promote transparency in public administration, allowing citizens, journalists, researchers, and other interested parties to access and analyze data related to revenues, expenses, contracts, agreements, and salaries of public servants, among other aspects.*

Data is requested via an API from the Portal da Transparência website in JSON format, transformed to rename and add some columns and finally inserted into BigQuery in tabular format for analysis.

The following GCP resources were used:

- **Cloud Functions:** Used to generate the real-time data in a FaaS (Function as a Service) manner. This way we can deploy the script in the cloud, instead of generating the data from your local machine.
- **Pub/Sub:** The main representative of the streaming class in GCP. I could say that pretty much every streaming pipeline will use Pub/Sub as their main motor for real-time messaging solutions on the cloud.
- **Dataflow:** This is the best tool to use when streaming data with Pub/Sub on GCP. Used to transform the data received from Pub/Sub and then writing to BigQuery.
- **BigQuery:** The flagship of GCP; used mainly for warehousing (it can now be a data lake) and anlytics. For this project, it is used for storing the transformed data from Dataflow in tabular format and some analytics.

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

Business question: Given the monthly cost for each city, are we having a higher cost in average for the given city?

#### First steps

Create a new project so it's easier to shut down all the services used when there is no more need. The second step we take is to create a service account for our local machine so it has access to GCP's resources. To do that, we go to IAM & Admin in the Service Accounts section and create a new one. One important steps is defining a role for this service account; In this case we will use the Owner role like in the image below. Be aware that in the cloud, we like to use the least-privilege principle and this Owner role will definitely be unaligned with this principle.

![image](https://github.com/leorickli/portal-da-transparencia-kafka/assets/106999054/56383ba5-1ca3-4b01-94d5-579b0e96ce1f)

After you've created your service account, you can create a JSON key that will be downloaded into your local machine. I like to rename this key into a simpler name and store it in the folder that I'm working with my project, so we don't have to declare the key's absolute path inside our Python scripts, at least on Linux based machines.

Create a GCS bucket for your project and add the folders "temp" (for the temporary files that Dataflow will create) and "template" (for when you deploy your [beam_pipeline](https://github.com/leorickli/portal-da-transparencia-streaming/blob/main/beam_pipeline.py) in the later steps of this project).

Finally, I like to use the Compute Engine default service account as my main service account for my cloud resources. Assign the "BigQuery Data Editor" and the "Pub/Sub Editor" roles on it.

#### Ingestion

First, we have to create an account on [Portal da Transparência's website](https://portaldatransparencia.gov.br/api-de-dados/cadastrar-email) so it give us a key for accessing the API data. This key will be inserted on the Python script. When you request data from an API, it usually comes in JSON format (you can checkout a [sample_data](https://github.com/leorickli/portal-da-transparencia-streaming/blob/main/sample_data.json) in its raw form). The [data_generator](https://github.com/leorickli/portal-da-transparencia-kafka/blob/main/data_generator.py) script was created so we can get data from the Auxílio Brasil's get request of the API and then publish it to a Pub/Sub topic. This script also simulates a streaming process by sending an object of the json file for a given amount of time that you can set; in this case, a message (a JSON object) will be publish every five seconds to a Pub/Sub topic.

When we send this script to Cloud Fucntions, it's advised to comment out the "os.environ" section in the script and add a "def main(request):" along with a return statement on it. When creating the function on Cloud Functions, don't forget to insert "main" as the entry point like in the image below:

![image](https://github.com/leorickli/portal-da-transparencia-kafka/assets/106999054/0889fe4a-4447-4922-9bde-2b0ce995fb5a)

These are the libraries required in the requirements.txt file:

```
google-cloud-pubsub==2.20.1
python-dateutil==2.9.0
```

Now we can deploy our function. After it's been deployed, we can use GCP's CLI to start the function by running the CLI test command given in the "Testing" section.

#### Processing

Pub/Sub will receive these messages and store it in a topic. When you create a topic, it's nice to create a [raw_data_schema](https://github.com/leorickli/portal-da-transparencia-streaming/blob/main/raw_data_schema.json) for the data arriving to that topic, this way you will guarantee order in the data that's being publish to our topic. Don't forget to also create the subscription for the topic.

Dataflow is by far the most complicated part of this project. Before we start creating the Beam pipeline, we have to first create a dataset and a table inside BigQuery, don't worry about defining a schema for the table, this will be declared inside the Beam script. The [beam_pipeline](https://github.com/leorickli/portal-da-transparencia-streaming/blob/main/beam_pipeline.py) script has a toggle (comment out) so you can test your pipeline on your machine or deploy it to the cloud, this works because one has the DataflowRunner declared and the other does not. With that script, we become a subscriber to our Pub/Sub topic, transform the JSON object by adding fields and changing the its names and then writing it to BigQuery in tabular format. Make sure to test it first on your local machine before deploying it on the cloud, this one can be quite expensive if you leave it testing indefinitely on Dataflow. Once the script has been deployed and it's showing on the "template" folder inside your GCS bucket, you can create your Dataflow job.

Be patient when deploying to Dataflow, the table might take longer to create in BigQuery when compared to your local testing.

<img width="953" alt="Screenshot 2024-03-13 at 23 30 31" src="https://github.com/leorickli/portal-da-transparencia-streaming/assets/106999054/ba5d265a-fce4-4d02-89f4-92951708f3a0">

#### Storage and Serving

Now that the data has been inserted into BigQuery, we can use Looker to build some dashboards on top of it.

![image](https://github.com/leorickli/portal-da-transparencia-streaming/assets/106999054/01c22ec1-1bf4-405b-8b3d-037a87dfa5f3)

#### Conclusion

The graph answers the business question properly. Indeed there is a high cost in this welfare program throughout the months.
