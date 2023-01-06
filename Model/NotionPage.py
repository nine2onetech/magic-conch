from dataclasses import dataclass

@dataclass
class NotionPage:
    title: str = ''
    category: str = ''
    url: str = ''