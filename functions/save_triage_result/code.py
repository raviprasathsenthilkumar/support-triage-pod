#input_type_name: SaveTriageInput
#output_type_name: SaveTriageOutput
#function_name: save_triage_result
from lemma_sdk import Pod
from pydantic import BaseModel
from typing import Optional

class SaveTriageInput(BaseModel):
    record_id: str
    category: Optional[str] = None
    priority: Optional[str] = None
    draft_reply: Optional[str] = None

class SaveTriageOutput(BaseModel):
    success: bool
    record_id: str

def run(input_data, context=None):
    pod = Pod.from_env()
    record_id = input_data.get("record_id")
    category = input_data.get("category")
    priority = input_data.get("priority")
    draft_reply = input_data.get("draft_reply")
    pod.records.update("tickets", record_id, {
        "category": category,
        "priority": priority,
        "draft_reply": draft_reply,
        "status": "draft_ready"
    })
    return {"success": True, "record_id": record_id}