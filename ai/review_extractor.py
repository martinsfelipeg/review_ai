import polars as pl

DF_PATH = "etl/data/gold/olist_product_reviews_dataset.parquet"
REVIEW_PATH = "ai/data/reviews.txt"


class ReviewsExtractor:
    def __init__(self):
        pass

    def read_table(self, product_id):
        df = pl.read_parquet(DF_PATH)
        df = df.filter(pl.col("product_id") == f"{product_id}")
        return df

    def reviews_to_txt(self, df):
        product_reviews = df["review_comment_message"].to_list()

        with open(REVIEW_PATH, "w") as file:
            for line in product_reviews:
                file.write(line + "\n")

    def load_txt(self):
        with open(REVIEW_PATH, "r") as f:
            reviews = f.read()
            return reviews
