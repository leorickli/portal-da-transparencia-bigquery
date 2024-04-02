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
- **Looker Studio:** Used for creating dashboards for our data.

### 1. Choose 5 fundamental concepts of GCP BigQuery and describe them

1. **Serverless Data Warehousing**: BigQuery is a serverless, fully managed data warehousing solution provided by Google Cloud Platform (GCP). Being serverless means that users don't need to provision or manage any infrastructure; instead, Google handles all aspects of scaling, performance optimization, and maintenance behind the scenes. This allows users to focus solely on analyzing their data without worrying about the underlying infrastructure.

2. **Columnar Storage and Execution**: BigQuery utilizes a columnar storage format, where data is stored in columns rather than rows. This format is optimized for analytical queries, as it allows for efficient data compression and retrieval. Additionally, BigQuery's execution engine is designed to operate on columnar data, enabling fast query performance even when dealing with large datasets.

3. **SQL-based Querying**: BigQuery supports standard SQL for querying and analyzing data. Users can write SQL queries to perform a wide range of operations, including filtering, aggregating, joining, and transforming data. The SQL dialect supported by BigQuery is ANSI SQL:2011 compliant, with some extensions and optimizations specific to BigQuery's features and capabilities.

4. **Scalability and Performance**: BigQuery is built to handle petabyte-scale datasets and can execute complex queries across massive datasets with low latency. It achieves this scalability and performance through parallel execution, automatic query optimization, and distributed storage and processing. As query complexity or data volume increases, BigQuery automatically scales resources to ensure consistent performance.

5. **Integration with Google Cloud Ecosystem**: BigQuery seamlessly integrates with other Google Cloud services, allowing users to ingest data from various sources, such as Google Cloud Storage, Google Cloud Pub/Sub, and Google Sheets. Additionally, BigQuery integrates with data visualization tools like Data Studio and BI platforms like Looker. This integration simplifies the process of data ingestion, transformation, analysis, and visualization within the Google Cloud ecosystem, enabling a cohesive and efficient data analytics workflow.

### 2. Describe the architecture of GCP BigQuery

Google Cloud Platform's BigQuery architecture consists of two main components: storage and compute.
The storage layer utilizes Google's distributed storage system, storing data in a columnar format. This format optimizes query performance by enabling efficient data compression and retrieval. 
The compute layer comprises a massively parallel processing engine that executes SQL queries across distributed resources. It dynamically allocates resources based on query complexity and dataset size, ensuring optimal performance and resource utilization. 
BigQuery's architecture is designed for scalability, enabling it to handle large datasets and execute complex queries efficiently. It integrates seamlessly with other Google Cloud services and provides robust security features to protect data integrity.

### 3. Present examples of BigQuery utilization on SQL and NoSQL databases

SQL Database Example:
In a SQL database scenario, such as MySQL or PostgreSQL, where data is structured into tables with rows and columns, you can export your data into BigQuery for analysis. BigQuery allows you to run SQL queries directly on this structured data, enabling you to perform complex analytics and generate insights. For instance, you could analyze sales data to identify top-selling products or track customer behavior over time.

NoSQL Database Example:
In a NoSQL database scenario, such as MongoDB or Firebase Firestore, where data is stored in a more flexible and schema-less format, you can export your data into BigQuery for analysis. BigQuery supports semi-structured data like JSON, allowing you to run SQL-like queries on this data. For example, you could analyze user activity logs to understand user engagement patterns or monitor application performance metrics.

In both cases, BigQuery provides a powerful and scalable platform for analyzing data from SQL and NoSQL databases, helping organizations derive valuable insights and make data-driven decisions.

### 4. Describe the best advantages of using of GCP BigQuery

1. **Scalability**: BigQuery is built to handle massive datasets, scaling seamlessly to accommodate petabytes of data. Its distributed architecture and serverless nature ensure that users can run queries of any size without worrying about provisioning or managing infrastructure. This scalability makes it suitable for organizations of all sizes, from startups to large enterprises.

2. **Performance**: BigQuery offers fast query performance, even on large datasets, thanks to its columnar storage format and distributed processing engine. It can execute complex analytical queries in seconds or minutes, enabling users to derive insights from their data quickly. Additionally, BigQuery automatically optimizes query execution and resource allocation to maximize performance and minimize latency.

3. **Ease of Use**: BigQuery is designed to be user-friendly, with a familiar SQL interface that allows users to write and execute queries without the need for specialized skills or training. Its integration with other Google Cloud services, such as Google Cloud Storage and Google Data Studio, further enhances usability, enabling seamless data ingestion, transformation, and visualization workflows.

4. **Cost-effectiveness**: BigQuery offers a pay-as-you-go pricing model, where users only pay for the storage and processing resources they consume. There are no upfront costs or long-term commitments, making it cost-effective for organizations to analyze large volumes of data without incurring unnecessary expenses. Additionally, BigQuery's automatic scaling and resource optimization help minimize costs by ensuring efficient resource utilization.

5. **Security and Compliance**: BigQuery provides robust security features to protect data privacy and ensure compliance with regulatory requirements. It offers fine-grained access controls, encryption at rest and in transit, and audit logging capabilities to safeguard sensitive data. Additionally, BigQuery undergoes regular security audits and certifications to maintain the highest standards of security and compliance.

6. **Integration with Google Ecosystem**: BigQuery seamlessly integrates with other Google Cloud services and tools, enabling organizations to leverage the full power of the Google ecosystem for their data analytics workflows. It integrates with services like Google Cloud Storage, Google Data Studio, Google Cloud Pub/Sub, and more, allowing users to ingest, process, analyze, and visualize data in a cohesive and efficient manner.

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

Dataflow is by far the most complicated part of this project. Before we start creating the Beam pipeline, we have to first create a dataset inside BigQuery, don't worry about defining the table and a schema in the dataset, this will be created inside the Beam script. If you still want to create the table and schema just for quality assertions, here is the [bigquery_schema](https://github.com/leorickli/portal-da-transparencia-streaming/blob/main/bigquery_schema.json) that you can insert as text inside when creating the table.

The [beam_pipeline](https://github.com/leorickli/portal-da-transparencia-streaming/blob/main/beam_pipeline.py) script has a toggle (comment out) so you can test your pipeline on your machine or deploy it to the cloud, this works because one has the DataflowRunner declared and the other does not. With that script, we become a subscriber to our Pub/Sub topic, transform the JSON object by adding fields and changing the its names and then writing it to BigQuery in tabular format. Make sure to test it first on your local machine before deploying it on the cloud, this one can be quite expensive if you leave it testing indefinitely on Dataflow. Once the script has been deployed and it's showing on the "template" folder inside your GCS bucket, you can create your Dataflow job.

Be patient when deploying to Dataflow, the table might take longer to create in BigQuery when compared to your local testing.

<img width="953" alt="Screenshot 2024-03-13 at 23 30 31" src="https://github.com/leorickli/portal-da-transparencia-streaming/assets/106999054/ba5d265a-fce4-4d02-89f4-92951708f3a0">

#### Storage and Serving

Now that the data has been inserted into BigQuery, we can use Looker to build some dashboards on top of it.

<img width="1147" alt="Screenshot 2024-03-14 at 00 08 39" src="https://github.com/leorickli/portal-da-transparencia-streaming/assets/106999054/74234404-e1c7-45df-b8bd-3907c7d2af9e">
<img width="735" alt="Screenshot 2024-03-14 at 12 09 16" src="https://github.com/leorickli/portal-da-transparencia-streaming/assets/106999054/fac9fb4d-e1dc-4cef-8c2c-9af5024fd8a8">

#### Conclusion

The graph answers the business question properly. Indeed there is a high cost in this welfare program throughout the months.
