from . import panel

bl_info = {
    "name": "UDIM Links",
    "blender": (4, 1, 0),
    "category": "Object",
    "support": "COMMUNITY",
}

def register():
    panel.register()

def unregister():
    panel.unregister()