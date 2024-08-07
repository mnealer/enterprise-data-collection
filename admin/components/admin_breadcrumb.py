def admin_breadcrumb(url: str) -> list:
    parts = url.split("/")
    if "model" in parts and "new" in parts:
        model_name = parts[parts.index("model") + 1]
        return [
            {"url": "/admin/", "icon": "home", "title": "Home", "last":False},
            {"url": f"/admin/model/{model_name}", "icon": "home", "title": "Home", "last":False},
            {"url": url, "icon": "new", "title": "Edit", "last":True}
        ]

    if "edit" in parts:
        model_name = parts[parts.index("model") + 1]
        record_id = parts[parts.index("record") + 1]
        return [
            {"url": "/admin/", "icon": "home", "title": "Home", "last":False},
            {"url": f"/admin/model/{model_name}", "icon": "home", "title": "Home", "last":False},
            {"url": url, "icon": "record", "title": record_id, "last":False},
            {"url": url, "icon": "edit", "title": "Edit", "last":True}
        ]

    if "record" in parts:
        model_name = parts[parts.index("model") + 1]
        record_id = parts[parts.index("record") + 1]
        return [
            {"url": "/admin/", "icon": "home", "title": "Home", "last":False},
            {"url": f"/admin/model/{model_name}", "icon": "home", "title": "Home", "last":False},
            {"url": url, "icon": "record", "title": record_id, "last":True},
        ]

    elif "model" in parts:
        model_name = parts[parts.index("model") + 1]
        return [
            {"url": "/admin/", "icon": "home", "title": "Home", "last": False},
            {"url": f"/admin/model/{model_name}", "icon": "home", "title": "Home", "last": True},
        ]
    else:
        return [
            {"url": "/admin/", "icon": "home", "title": "Home", "last": True}]