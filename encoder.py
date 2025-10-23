import urllib.parse
class Encoder:
    def encode(self,data):
        new_data = urllib.parse.urlencode(data)
        return new_data