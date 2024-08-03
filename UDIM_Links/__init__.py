from . import panel
from . import tile_associations
from . import link
import bpy

bl_info = {
    "name": "UDIM Links",
    "blender": (4, 1, 0),
    "category": "Object",
    "support": "COMMUNITY",
}

def start_operator():
    bpy.ops.object.select_checker()

def register():
    tile_associations.register()
    link.register()
    panel.register()
    
    # Start the select checker operator after registration is complete
    bpy.app.timers.register(start_operator)

def unregister():
    panel.unregister()
    tile_associations.unregister()
    link.unregister()
