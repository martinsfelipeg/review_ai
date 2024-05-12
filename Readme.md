# Review AI

## ETL

After cloning the project, use the Makefile to execute the ETL of the data:

```makefile
make etl_bronze

make etl_silver

make etl_gold
```

## Gemini

After the ETL to the layers, start the Gemini to avaliate the reviews of a single product_id by passing the ID in the config file in /review_ai/ai/config.py


Then, run the makefile with this parameter

make run_model

