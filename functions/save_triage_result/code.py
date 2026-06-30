#input_type_name: SaveTriageInput
#output_type_name: SaveTriageOutput
#function_name: save_triage_result
from lemma_sdk import Pod
from pydantic import BaseModel
from typing import Optional
import requests

class SaveTriageInput(BaseModel):
    record_id: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    draft_reply: Optional[str] = None
    status: Optional[str] = None

class SaveTriageOutput(BaseModel):
    success: bool
    record_id: str

def save_triage_result(context, input_data=None):
    base_url = str(context.lemma_base_url)
    pod_id   = str(context.pod_id)
    token    = context.lemma_token
    headers  = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    if hasattr(input_data, 'model_dump'):
        fields = input_data.model_dump()
    elif hasattr(input_data, 'dict'):
        fields = input_data.dict()
    else:
        fields = {}

    record_id   = fields.get("record_id")
    subject     = fields.get("subject")
    body        = fields.get("body")
    category    = fields.get("category")
    priority    = fields.get("priority")
    draft_reply = fields.get("draft_reply")
    status      = fields.get("status")

    table_url = f"{base_url}/pods/{pod_id}/datastore/tables/tickets/records"

    if not record_id or record_id == "new":
        data = {}
        if subject     is not None: data["subject"]     = subject
        if body        is not None: data["body"]        = body
        if category    is not None: data["category"]    = category
        if priority    is not None: data["priority"]    = priority
        if draft_reply is not None: data["draft_reply"] = draft_reply
        if status      is not None: data["status"]      = status
        resp = requests.post(table_url, json={"data": data}, headers=headers)
        resp.raise_for_status()
        rec = resp.json()
        new_id = str(rec.get("id") or rec.get("data", {}).get("id", ""))
        return {"success": True, "record_id": new_id}

    data = {}
    if category    is not None: data["category"]    = category
    if priority    is not None: data["priority"]    = priority
    if draft_reply is not None: data["draft_reply"] = draft_reply
    if status      is not None: data["status"]      = status
    resp = requests.patch(f"{table_url}/{record_id}", json={"data": data}, headers=headers)
    resp.raise_for_status()
    return {"success": True, "record_id": record_id}