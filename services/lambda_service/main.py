from typing import Any

from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.data_classes import SNSEvent

def parse_input(
    event: Any, context: LambdaContext
) -> Any:
    """Parses any permitted payload for the current lambda."""
    # Step 1: Validate & Parse event
    # Step 2: Validate & Parse LambdaContext (if needed)
    # Step 3: Return new objects from parsed data
    pass



@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: Any, context: LambdaContext):
    """Lambda handler entrypoint"""
    # TODO: ADD FUNCTION (decorator?) TO LOAD .ENV FILE WITH config.py BaseSettings (same as in FastAPI)
    try:
        request_id = context.aws_request_id
        # Set logging context
        logger.set_correlation_id(request_id)

        logger.debug("Event", extra=event.dict())
        return {"status": 200, "message": "Success"}

    except Exception as e:
        logger.exception("Exception Occurred")
        # TODO: How to log full traceback
        return {"statusCode": 500, "body": "Error: " + str(e)}
