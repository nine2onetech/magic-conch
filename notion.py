from notion_client import Client
from notion_client.helpers import is_full_page
from Model.NotionPage import NotionPage
from secret import DATABASE_ID, NOTION_API_TOKEN

def lists():
    notion_token = NOTION_API_TOKEN
    notion = Client(auth=notion_token)

    full_or_partial_pages = notion.databases.query(
        database_id = DATABASE_ID
    )

    results = []

    for page in full_or_partial_pages["results"]:
        if not is_full_page(page):
            continue

        if not page['properties']['이름']['title']:
            continue

        title = page['properties']['이름']['title'][0]['text']['content']
        try:
            category = page['properties']['분류']['select']['name']
        except:
            category = ''
        url = page['url']

        food = NotionPage(title, category, url)

        results.append(food)

    return results
