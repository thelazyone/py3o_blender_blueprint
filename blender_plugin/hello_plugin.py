import bpy
import os

# Test plugin to use as a blueprint for future compiled code in blender.

bl_info = {
    "name": "Hello Blender Plugin",
    "blender": (4, 0, 0),
    "category": "Object",
    "description": "Rust wrapping in blender test",
    "author": "Your Name",
    "version": (0, 1, 0),
    "location": "View3D > Tool Shelf",
    "warning": "",  # Used for warning icon and text in addons panel
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

class TBRPluginOperator(bpy.types.Operator):
    """TBR Plugin Description"""
    bl_idname = "wm.tbr_plugin"
    bl_label = "TBR Plugin Operator"

    def execute(self, context):
        message = "hi" #hello_blender()
        self.report({'INFO'}, message)
        return {'FINISHED'}

def register():
    print("Registering TBR Plugin...")
    bpy.utils.register_class(TBRPluginOperator)

def unregister():
    bpy.utils.unregister_class(TBRPluginOperator)

if __name__ == "__main__":
    register()
