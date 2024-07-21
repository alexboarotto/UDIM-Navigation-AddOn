import bpy

# Define the Property Group
class UDIMTileAssociation(bpy.types.PropertyGroup):
    object: bpy.props.PointerProperty(name="Object", type=bpy.types.Object)
    udim_tile: bpy.props.IntProperty(name="UDIM Tile")

# Define the UI List
class UDIMTileAssociationUIList(bpy.types.UIList):
    bl_idname = "OBJECT_UL_udim_tile_association"

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(item, "object", text="", icon='OBJECT_DATAMODE')
            layout.prop(item, "udim_tile", text="UDIM Tile")
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon='OBJECT_DATAMODE')

# Define the Panel
class UDIMLinksPanel(bpy.types.Panel):
    bl_idname = "SCENE_PT_csv_rotations"
    bl_label = "UDIM Links"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"
    bl_options = {'DEFAULT_CLOSED'}


    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.row()
        layout.row()


        layout.separator()
        layout.label(text="Object and UDIM Tile Associations:")

        # Draw the UI list
        row = layout.row()
        row.template_list("OBJECT_UL_udim_tile_association", "", scene, "udim_tile_associations", scene, "udim_tile_associations_index")

        # Add/Remove buttons
        col = row.column(align=True)
        col.operator("udim_tile_association_list.add", icon='ADD', text="")
        col.operator("udim_tile_association_list.remove", icon='REMOVE', text="")

# Define the operators for adding/removing items in the list
class UDIMTileAssociationListAdd(bpy.types.Operator):
    bl_idname = "udim_tile_association_list.add"
    bl_label = "Add UDIM Tile Association"

    def execute(self, context):
        context.scene.udim_tile_associations.add()
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

# Register the classes and properties
def register():
    bpy.utils.register_class(UDIMTileAssociation)
    bpy.types.Scene.udim_tile_associations = bpy.props.CollectionProperty(type=UDIMTileAssociation)
    bpy.types.Scene.udim_tile_associations_index = bpy.props.IntProperty()
    bpy.utils.register_class(UDIMTileAssociationUIList)
    bpy.utils.register_class(UDIMLinksPanel)
    bpy.utils.register_class(UDIMTileAssociationListAdd)
    bpy.utils.register_class(UDIMTileAssociationListRemove)
    bpy.types.Scene.skeleton = bpy.props.StringProperty()
    bpy.types.Scene.bone_name = bpy.props.StringProperty()

def unregister():
    bpy.utils.unregister_class(UDIMTileAssociation)
    del bpy.types.Scene.udim_tile_associations
    del bpy.types.Scene.udim_tile_associations_index
    bpy.utils.unregister_class(UDIMTileAssociationUIList)
    bpy.utils.unregister_class(UDIMLinksPanel)
    bpy.utils.unregister_class(UDIMTileAssociationListAdd)
    bpy.utils.unregister_class(UDIMTileAssociationListRemove)
    del bpy.types.Scene.skeleton
    del bpy.types.Scene.bone_name

if __name__ == "__main__":
    register()
