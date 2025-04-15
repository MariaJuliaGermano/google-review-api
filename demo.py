import json
from outscraper import ApiClient
import fastapi


client = ApiClient(api_key='SECRET_API_KEY')
business_with_reviews = api_client.google_maps_business('Memphis Seoul brooklyn usa', limit=)
