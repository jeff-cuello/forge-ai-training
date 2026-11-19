"""Summarize synthetic check records supplied as JSON on standard input."""
import json
import sys


def summarize(record):
    if not isinstance(record, dict) or not isinstance(record.get("checks"), list):
        raise ValueError("checks must be a list")
    checks = record["checks"]
    for check in checks:
        if not isinstance(check, dict) or not isinstance(check.get("name"), str):
            raise ValueError("each check needs a name")
        if type(check.get("passed")) is not bool:
            raise ValueError("passed must be a JSON boolean")
    return {"total": len(checks), "passed": sum(c["passed"] for c in checks)}


if __name__ == "__main__":
    try:
        print(json.dumps(summarize(json.load(sys.stdin))))
    except (ValueError, TypeError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(2)
