import kaggle

KAGGLE_DATASET = "olistbr/brazilian-ecommerce"

kaggle.api.dataset_download_files(KAGGLE_DATASET, path="data/bronze/", unzip=True)
