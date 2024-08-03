import bpy

# Define the Property Group
class UDIMTileAssociation(bpy.types.PropertyGroup):
    def get_udim_items(self, context):
        image = context.scene.selected_image
        if image:
            # Return a list of tuples (identifier, name, description)
            return [(str(tile.number), str(tile.number), '') for tile in image.tiles]
        return []  

    object: bpy.props.PointerProperty(name="Object", type=bpy.types.Object)
    udim_tile: bpy.props.EnumProperty(name="UDIM Tile", items=get_udim_items)

# Define the UI List
class UDIMTileAssociationUIList(bpy.types.UIList):
    bl_idname = "OBJECT_UL_udim_tile_association"

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(item, "object", text="", icon='OBJECT_DATAMODE')
            if context.scene.selected_image:
                layout.prop(item, "udim_tile", text="UDIM Tile")
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon='OBJECT_DATAMODE')

# Define the Panel
class UDIMLinksPanel(bpy.types.Panel):
    bl_idname = "SCENE_PT_udim_links"
    bl_label = "UDIM Links"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene


        layout.prop(scene, "selected_image", text="Image")

        layout.separator()
        layout.label(text="Object and UDIM Tile Associations:")

        # Draw the UI list
        row = layout.row()
        row.template_list("OBJECT_UL_udim_tile_association", "", scene, "udim_tile_associations", scene, "udim_tile_associations_index")

        # Add/Remove buttons
        col = row.column(align=True)
        col.operator("udim_tile_association_list.add", icon='ADD', text="")
        col.operator("udim_tile_association_list.remove", icon='REMOVE', text="")



# Register the classes and properties
def register():
    bpy.utils.register_class(UDIMTileAssociation)
    bpy.types.Scene.udim_tile_associations = bpy.props.CollectionProperty(type=UDIMTileAssociation)
    bpy.types.Scene.udim_tile_associations_index = bpy.props.IntProperty()
    bpy.types.Scene.selected_image = bpy.props.PointerProperty(name="Selected Image", type=bpy.types.Image)
    bpy.utils.register_class(UDIMTileAssociationUIList)
    bpy.utils.register_class(UDIMLinksPanel)

def unregister():
    bpy.utils.unregister_class(UDIMTileAssociation)
    del bpy.types.Scene.udim_tile_associations
    del bpy.types.Scene.udim_tile_associations_index
    del bpy.types.Scene.selected_image
    bpy.utils.unregister_class(UDIMTileAssociationUIList)
    bpy.utils.unregister_class(UDIMLinksPanel)

