# netlify/functions/issue_license.py

import json
import hashlib
import tomli_w
from pathlib import Path
from generate_nucleate_license import build_license  # your existing function
import uuid
import os

# Optional ledger directory for local testing (won't persist on Netlify)
LEDGER_DIR = Path.home() / ".watchlight" / "licenses" / "ledger"
LEDGER_DIR.mkdir(parents=True, exist_ok=True)
LEDGER_FILE = LEDGER_DIR / "issued.json"

def generate_license_serverless(email: str, tier: str, source: str) -> tuple[bytes, dict, str]:
    """
    Generates a license, returns bytes, ledger entry, and safe filename
    """
    license_data = build_license(email, tier)

    # Serialize license to bytes
    license_bytes = tomli_w.dumps(license_data).encode("utf-8")

    # Minimal ledger entry (no PII)
    email_hash = hashlib.sha256(email.lower().strip().encode("utf-8")).hexdigest()
    ledger_entry = {
        "uuid": license_data["license"]["uuid"],
        "tier": tier,
        "issued_at": license_data["license"]["issued_at"],
        "email_hash": f"sha256:{email_hash}",
        "source": source,
    }

    # Generate safe download filename
    filename = f"license_{ledger_entry['uuid']}.toml"

    # Append to ledger if possible (optional)
    try:
        if LEDGER_FILE.exists():
            with open(LEDGER_FILE, "r", encoding="utf-8") as f:
                existing = json.load(f)
        else:
            existing = []

        existing.append(ledger_entry)
        with open(LEDGER_FILE, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=2)
    except Exception:
        # silently skip ledger write if Netlify ephemeral
        pass

    return license_bytes, ledger_entry, filename


def handler(event, context):
    """
    Netlify function entry point.
    Expects POST JSON payload:
    {
        "email": "user@example.com",
        "tier": "free" | "pro",
        "source": "gumroad" | "itch"
    }
    Returns the license as an in-browser download.
    """
    try:
        if event.get("httpMethod") != "POST":
            return {"statusCode": 405, "body": "Method not allowed"}

        payload = json.loads(event["body"])
        email = payload["email"]
        tier = payload.get("tier", "free")
        source = payload.get("source", "unknown")

        license_bytes, ledger_entry, filename = generate_license_serverless(email, tier, source)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/octet-stream",
                "Content-Disposition": f'attachment; filename="{filename}"'
            },
            "body": license_bytes.decode("utf-8")
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error generating license: {e}"
        }
