from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTraining_pipeline
from cnnClassifier.pipeline.stage_o2_prepare_base_model import PrepareBaseModelTraining_pipeline
from cnnClassifier.pipeline.stage_04_trining import Training_pipeline
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTraining_pipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"############################################")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    preparebasemodel = PrepareBaseModelTraining_pipeline()
    preparebasemodel.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training Model"
try:
    logger.info(f"############################################")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    training= Training_pipeline()
    training.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e