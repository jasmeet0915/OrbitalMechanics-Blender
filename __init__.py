bl_info = {
    'name': 'Orbital Mechanics Simulations',
    'author': 'Jasmeet Singh',
    'version': (1, 0, 0),
    'blender': (2, 82, 0),
    'location': 'Properties > Physics (for objects); Properties > Scene (global settings); 3DView Toolbar',
    'description': 'Create realistic Orbital Simulations for Satellites',
    'category': 'Object',
}

import bpy

from .properties import CentreBody
from .panels import CentreBody_PT_Panel

from bpy.props import PointerProperty


def register():
    bpy.utils.register_class(CentreBody)
    bpy.utils.register_class(CentreBody_PT_Panel)

    bpy.types.Scene.CentreBody = PointerProperty(type=CentreBody)
    print("Orbital Mechanics Add On Enabled")



def unregister():
    bpy.utils.unregister_class(CentreBody)
    bpy.utils.unregister_class(CentreBody_PT_Panel)

    del bpy.types.Scene.CentreBody
    print("Orbital Mechanics Add On Disabled")


if __name__ == "__main__":
    register()
