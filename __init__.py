bl_info = {
    'name': 'Orbital Mechanics Simulations',
    'author': 'Jasmeet Singh',
    'version': (1, 0, 0),
    'blender': (2, 82, 0),
    'location': 'Properties > Physics (for objects); Properties > Scene (global settings); 3DView Toolbar',
    'description': 'Create realistic Orbital Simulations for Satellites',
    'category': 'Object',
}


def register():
    print("Orbital Mechanics Add On Enabled")
    pass


def unregister():
    print("Orbital Mechanics Add On Disabled")
    pass
