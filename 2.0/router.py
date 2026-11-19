"""Route synthetic service requests. Contains a deliberate training defect."""


def route_request(priority):
    if not isinstance(priority, str):
        raise ValueError("priority must be text")
    priority = priority.strip().lower()
    if priority == "urgent" or priority == "critical":
        return "duty"
    if priority == "standard":
        return "service"
    raise ValueError("unsupported priority")
