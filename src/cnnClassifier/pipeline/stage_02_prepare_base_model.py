""""
Prepare Base Model Pipeline Stage 02
"""
from cnnClassifier.config.configuration import ConfiguratonManager
from cnnClassifier.compoents.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelPipeline:
    """
    Prepare Base Model Pipeline Stage 02
    """
    def __init__(self) -> None:
        pass

    def main(self):
        '''
        Main method for Prepare Base Model Pipeline Stage 02
        '''
        config = ConfiguratonManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
    except Exception as ex:
        logger.error(ex, exc_info = True)
        raise ex
