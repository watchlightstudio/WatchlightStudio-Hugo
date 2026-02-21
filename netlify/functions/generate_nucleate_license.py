import uuid
from datetime import datetime, timezone
import tomli_w
import hashlib
from pathlib import Path
import os
import base64
from nacl.signing import SigningKey

BASE_DIR = Path.home() / ".watchlight"
LICENSE_DIR = BASE_DIR / "licenses" / "issued"
LICENSE_DIR.mkdir(parents=True, exist_ok=True)


_PRIVATE_KEY_HEX = os.environ.get("NUCLEATE_LICENSE_PRIVATE_KEY")

if not _PRIVATE_KEY_HEX:
    raise RuntimeError("Missing NUCLEATE_LICENSE_PRIVATE_KEY env variable")

SIGNING_KEY = SigningKey(bytes.fromhex(_PRIVATE_KEY_HEX))

def build_license(email: str, tier: str) -> dict:
    if tier not in {"free", "pro"}:
        raise ValueError("Tier must be 'free' or 'pro'")

    return {
        "license": {
            "schema_version": 1,
            "product": "nucleate",
            "tier": tier,
            "issued_to": email,
            "uuid": str(uuid.uuid4()),
            "issued_at": datetime.now(timezone.utc).isoformat(),
        }
    }


def _sign_license(license_data: dict) -> dict:
    """
    Signs the [license] section and appends [signature].
    """

    # Deterministically serialize ONLY the license section
    payload = tomli_w.dumps({
        "license": license_data["license"]
    }).encode("utf-8")

    signature = SIGNING_KEY.sign(payload).signature
    signature_b64 = base64.b64encode(signature).decode("utf-8")

    license_data["signature"] = {
        "algorithm": "ed25519",
        "value": signature_b64
    }

    return license_data


def generate_license_local(email: str, tier: str = "free") -> Path:
    license_data = build_license(email, tier)
    license_data = _sign_license(license_data)

    safe_email = email.replace("@", "_at_").replace(".", "_")
    filename = f"{safe_email}_{tier}.toml"
    path = LICENSE_DIR / filename

    with open(path, "wb") as f:
        tomli_w.dump(license_data, f)

    print(f"Generated signed license: {path}")
    return path


def generate_license_serverless(email: str, tier: str, source: str) -> tuple[bytes, dict]:
    license_data = build_license(email, tier)
    license_data = _sign_license(license_data)

    license_bytes = tomli_w.dumps(license_data).encode("utf-8")

    email_hash = hashlib.sha256(
        email.lower().strip().encode("utf-8")
    ).hexdigest()

    ledger_entry = {
        "uuid": license_data["license"]["uuid"],
        "tier": tier,
        "issued_at": license_data["license"]["issued_at"],
        "email_hash": f"sha256:{email_hash}",
        "source": source,
    }

    return license_bytes, ledger_entry


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: generate_license.py <email> <tier: free|pro>")
        sys.exit(1)

    email_arg = sys.argv[1]
    tier_arg = sys.argv[2]

    generate_license_local(email_arg, tier_arg)