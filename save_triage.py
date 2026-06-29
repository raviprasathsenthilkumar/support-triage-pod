from lemma_sdk import Pod
import json

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