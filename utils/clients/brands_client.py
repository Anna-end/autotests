class BrandsClient:
    def __init__(self, client) -> None:
        self._client = client

    def get_all_brands(self):
        return self._client.get("/api/brandsList")

    def put_to_brand_list(self):
        return self._client.put("/api/brandsList")