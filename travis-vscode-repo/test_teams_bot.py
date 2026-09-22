import json
import requests

# Power Automate / Teams Workflows Webhook URL
WEBHOOK_URL = "https://defaultb945c813dce641f884575a12c2fe15.bf.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/b515a9e1b3344e8793d679483fa37b3b/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=9MCv9xlvMwNnakSWLzxLKApssUxPA-bpClgjRxOya4E"

# Direct Okta-authenticated SVM / SRI Portal Link
SRI_PORTAL_URL = "https://myapps-atl01.secure.fedex.com/svm-gui/trailer-incident-tabs.jsf"

# OTS Daily Briefing Adaptive Card Payload
ots_payload = {
    "type": "message",
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "type": "AdaptiveCard",
                "version": "1.4",
                "body": [
                    {
                        "type": "TextBlock",
                        "size": "Medium",
                        "weight": "Bolder",
                        "color": "Attention",
                        "text": "🚨 OTS DAILY BRIEFING: TOP 3 OPPORTUNITIES"
                    },
                    {
                        "type": "TextBlock",
                        "text": "Automated scan across Linehaul, FTRACK & SRI exemptions.",
                        "isSubtle": True,
                        "spacing": "None"
                    },
                    {
                        "type": "FactSet",
                        "separator": True,
                        "facts": [
                            {"title": "#1 Focus Lane:", "value": "SACR ➔ PORT"},
                            {"title": "Top Root Cause:", "value": "NF11 (Miscellaneous Trailer Issue)"},
                            {"title": "Failed Packages:", "value": "536 packages"},
                            {"title": "Offending Trailer:", "value": "TR-9941 (42 pkgs)"},
                            {"title": "Exemption Status:", "value": "❌ Unexcused (No Exemption Filed)"},
                            {"title": "Action Assigned:", "value": "Advance SACR dispatch to 17:15"}
                        ]
                    },
                    {
                        "type": "TextBlock",
                        "text": "**Key Operational Takeaway:** SACR departed at 18:30 and missed the 9:00 PM gate cutoff at PORT. Requires Linehaul dispatch adjustment.",
                        "wrap": True,
                        "spacing": "Medium"
                    }
                ],
                "actions": [
                    {
                        "type": "Action.OpenUrl",
                        "title": "🔍 View SRI Portal (Trailer Incident Tabs)",
                        "url": SRI_PORTAL_URL
                    }
                ]
            }
        }
    ]
}

def send_ots_card():
    headers = {"Content-Type": "application/json"}
    print("📡 Sending briefing card to Teams channel...")
    
    response = requests.post(WEBHOOK_URL, data=json.dumps(ots_payload), headers=headers)
    
    if response.status_code in [200, 202]:
        print("🎉 Success! Check your Teams channel—the card with your SRI portal button has posted!")
    else:
        print(f"❌ Failed to post ({response.status_code}): {response.text}")

if __name__ == "__main__":
    send_ots_card()
