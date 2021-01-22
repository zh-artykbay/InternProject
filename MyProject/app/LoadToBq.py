from google.cloud import bigquery
from app.models import SulpakSmartphones, SulpakSmartphonesHistory

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

def test():
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of table to append to.
    table_id = "My First Project.sulpakdataset.phones"

    tutorial = SulpakSmartphones.objects.get(pk=100)

    rows_to_insert = [
        {u"id": tutorial.id, u"name": tutorial.name, u"price": tutorial.current_price},
    ]

    errors = client.insert_rows_json(
        table_id, rows_to_insert, row_ids=[None] * len(rows_to_insert)
    )  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))