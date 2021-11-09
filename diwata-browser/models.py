import json


class Collection(object):
    def __init__(self, response_json):
        self._json = response_json
        self.id = self._json.get('id', None)
        self.stac_version = self._json.get(
            'stac_version', None)
        self.title = self._json.get('title', None)
        self.description = self._json.get(
            'description', None)
        self.license = self._json.get(
            'license', None)


class Extent(object):
    def __init__(self, json):
        self._json = json

    def temporal(self):
        return self._json.get('temporal', None)

    def spatial(self):
        return self._json.get('spatial', None)


class Item(object):
    def __init__(self, response_json):
        self._json = response_json
        self.id = self._json.get('id', None)
        self.stac_version = self._json.get('stac_version', None)
        self.geometry = self._json.get('geometry', None)
        self.bbox = self._json.get('bbox', [])
        self.assets = self._json.get('assets', {})
        self.links = self._json.get('links', [])
        self.properties = self._json.get('properties', {})
        self.start_datetime = self.properties.get('start_datetime', None)
        self.end_datetime = self.properties.get('end_datetime', None)
        self.platform = self.properties.get('platform', None)
        self.payload = self.properties.get('payload', [])
        self.bands = self.properties.get('eo:bands', [])

    def get_assets(self):
        assets = []
        for key, d in self.assets.items():
            assets.append(Asset(key, d, item=self))

        return assets

    def get_links(self):
        links = []
        for link in self.links:
            links.append(Link(link))


class Asset(object):
    def __init__(self, key, d, item=None):
        self.key = key
        self.d = d
        self.item = item
        self.href = self.d.get('href', None)
        self.type = self.d.get('type', None)


class Link:
    def __init__(self, d):
        self.rel = self.d.get('rel', None)
        self.href = self.d.get('href', None)
        self.type = self.d.get('type', None)