"""Domain logic used by the Module 11 Git/CI laboratory.

The module is intentionally deterministic and has no third-party dependencies.
That keeps the laboratory focused on version control and CI rather than package setup.
"""

from __future__ import annotations


def build_summary(patient: dict, appointments: list[dict], clinic_status: str = "ACTIVE") -> dict:
    """Build the public patient-summary contract used by MediLink.

    Raises:
        ValueError: when the inputs do not satisfy the minimum contract.
    """
    if not isinstance(patient, dict):
        raise ValueError("patient must be a dictionary")
    if "patient_id" not in patient or not str(patient["patient_id"]).strip():
        raise ValueError("patient must contain a non-empty patient_id")
    if not isinstance(appointments, list):
        raise ValueError("appointments must be a list")
    if not isinstance(clinic_status, str) or not clinic_status.strip():
        raise ValueError("clinic_status must be a non-empty string")

    # Return a new dictionary instead of mutating the incoming patient object.
    # This reduces surprising side effects for callers of the integration function.
    return {
        "patient": dict(patient),
        "appointments": list(appointments),
        "clinic_status": clinic_status.strip().upper(),
    }
