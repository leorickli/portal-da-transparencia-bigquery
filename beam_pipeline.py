import apache_beam as beam
import json
import os
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions

pipeline_options = {
    'project': 'lab-project-416114',
    'runner': 'DataflowRunner',
    'region': 'southamerica-east1',
    'job_name': 'leorickli',
    'staging_location': 'gs://pubsub2bq-leo/temp',
    'temp_location': 'gs://pubsub2bq-leo/temp',
    'template_location': 'gs://pubsub2bq-leo/template/streaming_job_template',
    'streaming': True,
    'enable_streaming_engine': True,
    'save_main_session': True
    }
pipeline_options = PipelineOptions.from_dictionary(pipeline_options)
p = beam.Pipeline(options=pipeline_options)

# TOGGLE THAT ON FOR EXECUTING ON PREMISES
# options = PipelineOptions()
# options.view_as(StandardOptions).streaming = True
# p = beam.Pipeline(options=options)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'serviceAccount.json'
subscription = 'projects/lab-project-416114/subscriptions/welfare-programs-topic-sub'
table = 'lab-project-416114.refined.welfare_programs'
table_schema = {
  'fields': [
    {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
    {'name': 'dateReference', 'type': 'DATE', 'mode': 'NULLABLE'},
    {'name': 'cityCode', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'cityName', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'state_name', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'programType', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'cost', 'type': 'FLOAT', 'mode': 'NULLABLE'},
    {'name': 'costMargin', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'numberBeneficiaries', 'type': 'INTEGER', 'mode': 'NULLABLE'},
    {'name': 'numberBeneficiariesMargin', 'type': 'STRING', 'mode': 'NULLABLE'}
  ]
}


def select_fields(element):
    return {
        'id': element['id'],
        'dateReference': element['dataReferencia'],
        'cityCode': element['municipio']['codigoIBGE'],
        'cityName': element['municipio']['nomeIBGE'],
        'state_name': element['municipio']['uf']['nome'],
        'programType': element['tipo']['descricao'],
        'cost': element['valor'],
        'costMargin': element['costMargin'],
        'numberBeneficiaries': element['quantidadeBeneficiados'],
        'numberBeneficiariesMargin': element['numberBeneficiariesMargin']
    }

class AddMarginsDoFn(beam.DoFn):
    def process(self, element):
        if element['valor'] < 80000:
            element['costMargin'] = 'low'
        elif 80000 <= element['valor'] < 250000:
            element['costMargin'] = 'medium'
        else:
            element['costMargin'] = 'high'
            
        if element['quantidadeBeneficiados'] < 400:
            element['numberBeneficiariesMargin'] = 'critical'
        elif 400 <= element['quantidadeBeneficiados'] < 700:
            element['numberBeneficiariesMargin'] = 'average'
        else:
            element['numberBeneficiariesMargin'] = 'ideal'
            
        yield element

(p
  | "Read from PubSub" >> beam.io.ReadFromPubSub(subscription=subscription).with_output_types(bytes)
  | "Decode" >> beam.Map(lambda x: x.decode('utf-8'))
  | "Transform to dict" >> beam.Map(lambda x: json.loads(x))
  | "Add cost margin" >> beam.ParDo(AddMarginsDoFn()) 
  | "Select fields" >> beam.Map(select_fields)
  | "Write to BigQuery" >> beam.io.WriteToBigQuery(
                              table,
                              schema=table_schema,
                              write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                              create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                              custom_gcs_temp_location = 'gs://pubsub2bq-leo/temp'
                              )
)

result = p.run()
result.wait_until_finish()