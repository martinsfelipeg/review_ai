import polars as pl

from env import DATASET_ORDER_ITEMS, DATASET_PRODUCTS, DATASET_REVIEWS


def dataset_reviews_to_silver(dataset):
    df = pl.read_csv(
        f"data/bronze/{dataset}.csv",
        columns=["order_id", "review_comment_message"],
        separator=",",
        dtypes=[str],
        encoding="utf8",
    )

    df = df.drop_nulls()
    df.write_parquet(f"data/silver/{dataset}.parquet")


def dataset_order_items_to_silver(dataset):
    df = pl.read_csv(
        f"data/bronze/{dataset}.csv",
        columns=["order_id", "product_id"],
        separator=",",
        dtypes=[str],
        encoding="utf8",
    )

    df = df.drop_nulls()
    df.write_parquet(f"data/silver/{dataset}.parquet")


def dataset_products_to_silver(dataset):
    df = pl.read_csv(
        f"data/bronze/{dataset}.csv",
        columns=["product_id", "product_category_name"],
        separator=",",
        dtypes=[str],
        encoding="utf8",
    )

    df = df.drop_nulls()
    df.write_parquet(f"data/silver/{dataset}.parquet")


def main():
    dataset_reviews_to_silver(DATASET_REVIEWS)
    dataset_order_items_to_silver(DATASET_ORDER_ITEMS)
    dataset_products_to_silver(DATASET_PRODUCTS)


if __name__ == "__main__":
    main()
