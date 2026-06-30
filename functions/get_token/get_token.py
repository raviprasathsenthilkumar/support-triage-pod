#input_type_name: GetTokenInput
#output_type_name: GetTokenOutput
#function_name: get_token
from pydantic import BaseModel

class GetTokenInput(BaseModel):
    ping: str = "ping"

class GetTokenOutput(BaseModel):
    token: str

def get_token(context, input_data=None):
    return {"token": context.lemma_token}