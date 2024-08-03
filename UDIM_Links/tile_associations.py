import bpy

# Define the operators for adding/removing items in the list
class UDIMTileAssociationListAdd(bpy.types.Operator):
    bl_idname = "udim_tile_association_list.add"
    bl_label = "Add UDIM Tile Association"

    def execute(self, context):
        new_item = context.scene.udim_tile_associations.add()
        return {'FINISHED'}

class UDIMTileAssociationListRemove(bpy.types.Operator):
    bl_idname = "udim_tile_association_list.remove"
    bl_label = "Remove UDIM Tile Association"

    def execute(self, context):
        scene = context.scene
        index = scene.udim_tile_associations_index

        scene.udim_tile_associations.remove(index)
        scene.udim_tile_associations_index = max(0, index - 1)

        return {'FINISHED'}
    

def register():
    bpy.utils.register_class(UDIMTileAssociationListAdd)
    bpy.utils.register_class(UDIMTileAssociationListRemove)

def unregister():
    bpy.utils.unregister_class(UDIMTileAssociationListAdd)
    bpy.utils.unregister_class(UDIMTileAssociationListRemove)