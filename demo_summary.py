"""Small command-line demonstration for the contract used in the lab."""

from __future__ import annotations

import json

from medilink_contract import build_summary


def main() -> None:
    patient = {"patient_id": "P1001", "name": "Ana Reyes", "clinic": "Quezon Clinic"}
    appointments = [
        {"date": "2026-10-05", "service": "General Consultation"},
        {"date": "2026-10-19", "service": "Follow-up"},
    ]
    summary = build_summary(patient, appointments)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
