etl_bronze:
	poetry run python etl/etl_bronze.py

etl_silver:
	poetry run python etl/etl_silver.py

etl_gold:
	poetry run python etl/etl_gold.py

run_model:
	poetry run python ai/model.py
