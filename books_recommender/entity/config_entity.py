from collections import namedtuple

DataingestionConfig = namedtuple("Datasetconfig",["dataset_download_url",
                                                  "raw_data_dir",
                                                  "ingested_data_dir"])