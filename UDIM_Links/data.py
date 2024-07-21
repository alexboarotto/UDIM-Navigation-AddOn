import bpy


# Shared Data Accessor
class Data:
    data = None
    skeleton = None

    @classmethod
    def set_skeleton(self):
        if not bpy.context.scene.skeleton == "":
            self.skeleton = bpy.data.objects[bpy.context.scene.skeleton]
            return self.skeleton

   
        