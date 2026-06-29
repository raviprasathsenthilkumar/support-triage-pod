import json
import requests

def save_triage_result(context, inputs):
    pod_id = "019f1312-d04e-775d-8107-55b24da41e02"
    api_url = f"https://lemma.work{pod_id}/datastore/tables/tickets/records"
    
    headers = {
        "Authorization": f"Bearer {context.token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "data": {
            "subject": inputs.get("subject"),
            "body": inputs.get("body"),
            "category": inputs.get("category", "general"),
            "priority": inputs.get("priority", "medium"),
            "draft_reply": inputs.get("draft_reply", ""),
            "status": "triage_complete"
        }
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    return {"status": response.status_code, "response": response.text}
