import bpy

class OBJECT_OT_select_checker(bpy.types.Operator):
    bl_idname = "object.select_checker"
    bl_label = "Select Checker"
    
    _timer = None
    last_selected_objects = []

    def modal(self, context, event):
        if event.type == 'TIMER':
            current_selected_objects = bpy.context.selected_objects

            if set(current_selected_objects) != set(self.last_selected_objects):
                self.last_selected_objects = current_selected_objects[:]
                print("Selection changed!")
                print("Selected objects:", [obj.name for obj in current_selected_objects])

        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.5, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        return {'CANCELLED'}

def register():
    # Check if the class is already registered to avoid double registration
    if not hasattr(bpy.types, "OBJECT_OT_select_checker"):
        bpy.utils.register_class(OBJECT_OT_select_checker)

def unregister():
    # Check if the class is registered before trying to unregister it
    if hasattr(bpy.types, "OBJECT_OT_select_checker"):
        bpy.utils.unregister_class(OBJECT_OT_select_checker)
