class ProductClient:
    def __init__(self, client) -> None:
        self.client = client

    def get_all_products(self):
        return self.client.get("/api/productsList")
    def post_to_product_list(self):
        return self.client.post("/api/productsList")
    def search_products(self):
        return self.client.post("/api/searchProduct")
    def search_products_without_params(self):
        return self.client.post("/api/searchProduct")