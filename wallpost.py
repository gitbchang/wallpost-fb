import facebook 
import requests

"""
change user token

"""


token = 'EAACEdEose0cBAKoZBZAU7xZCe4iLzLUcRYPgZA1mfR2J9xizs0hTeNG5lW9KZCMSc8Kwm9NYXDjG4qsNZAZAgEpI4DBq7rsQQbcMv8mDjaQ6YXTJyqZBPWgaujVrTZB998Xtl6rzp1LVuQupCQJZC8PHxxyta39a99dAp0VZCd8ZCDlbf8lZBkkOgDQFWeJyZCPtGclZAwg5RIymWjYDQZDZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

graph.put_object(parent_object='me', connection_name='feed',
                  message='Hello, world')



print(profile)