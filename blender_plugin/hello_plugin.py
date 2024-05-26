import bpy
import os

bl_info = {
    "name": "Hello Blender Plugin",
    "blender": (4, 0, 0),
    "category": "Object",
    "description": "Rust wrapping in blender test",
    "author": "Your Name",
    "version": (0, 1, 0),
    "location": "View3D > Tool Shelf > TBR Panel",
    "warning": "",
    "support": "COMMUNITY"
}

# Adding the dll directory in the path, then trying to import.
dll_directory = os.path.dirname(__file__)
if dll_directory not in os.environ['PATH']:
    os.environ['PATH'] += os.pathsep + dll_directory
try:
    from hello_plugin_lib import hello_blender
except ImportError as e:
    print("DEBUG: Failed to import hello_plugin_lib:", e)
    raise

# Trivial operator, just calling the hello_blender Rust function.
class TBRPluginOperator(bpy.types.Operator):
    """TBR Plugin Description"""
    bl_idname = "wm.tbr_plugin"
    bl_label = "TBR Plugin Operator"

    def execute(self, context):
        message = hello_blender()
        self.report({'INFO'}, message)
        return {'FINISHED'}

# Simple pannel with one button.
class TBR_PT_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "TBR Plugin Panel"
    bl_idname = "TBR_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TBR'

    def draw(self, context):
        layout = self.layout
        layout.operator(TBRPluginOperator.bl_idname, text="Run TBR Plugin")

def register():
    bpy.utils.register_class(TBRPluginOperator)
    bpy.utils.register_class(TBR_PT_Panel)

def unregister():
    bpy.utils.unregister_class(TBRPluginOperator)
    bpy.utils.unregister_class(TBR_PT_Panel)

if __name__ == "__main__":
    register()
