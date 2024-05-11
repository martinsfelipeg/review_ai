import duckdb

from env import DATASETS

con = duckdb.connect(database=":memory:", read_only=False)

for dataset in DATASETS:
    con.execute(
        f"CREATE TABLE {dataset} AS SELECT * FROM 'data/silver/{dataset}.parquet';"
    )

create_table_product_reviews = """
CREATE TABLE olist_product_reviews_dataset AS

SELECT
    p.product_id,
    p.product_category_name,
    r.review_comment_message

FROM
    olist_order_items_dataset AS o

JOIN
    olist_products_dataset AS p ON o.product_id = p.product_id

JOIN
    olist_order_reviews_dataset AS r ON o.order_id = r.order_id;

"""

load_table_product_reviews = """
COPY olist_product_reviews_dataset
TO 'data/gold/olist_product_reviews_dataset.parquet' (FORMAT PARQUET);
"""

con.execute(create_table_product_reviews)

con.execute(load_table_product_reviews)

con.close()
