import bpy


class CentreBody_PT_Panel(bpy.types.Panel):
    bl_label = "Central Body"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "physics"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        CentreBody = context.scene.CentreBody

        layout.prop(CentreBody, "centre_name")
        layout.prop(CentreBody, "radius_mantissa")
        layout.prop(CentreBody, "mass_mantissa")
        layout.prop(CentreBody, "axis_tilt")