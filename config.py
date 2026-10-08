"""Configuration helpers for the Module 11 laboratory."""

from __future__ import annotations

import os


def get_api_key() -> str:
    """Read the API key from the environment instead of source code.

    The default is safe for a local classroom demo only. Real secrets should be
    supplied through the environment or a repository/CI secret store.
    """
    return os.getenv("MEDILINK_API_KEY", "local-demo-key")


def get_request_timeout() -> int:
    """Return a positive integer timeout from the environment."""
    raw = os.getenv("REQUEST_TIMEOUT", "5")
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError("REQUEST_TIMEOUT must be an integer") from exc
    if value <= 0:
        raise ValueError("REQUEST_TIMEOUT must be greater than zero")
    return value
