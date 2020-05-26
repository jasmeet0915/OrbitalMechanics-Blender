import bpy

from bpy.props import(
    BoolProperty,
    IntProperty,
    FloatProperty,
    StringProperty,
    EnumProperty)


class CentreBody(bpy.types.PropertyGroup):
    centre_name : StringProperty(
        name="Name",
        description="Name of the object you want to make Central Body",
    )

    radius_mantissa: FloatProperty(
        name="Central Body Radius(km)",
        description="Mantissa of radius of Central Body",
        min=0.01,
        max=1000,
        default=1
    )

    radius_exponent: IntProperty(
        name="Exponent",
        description="The Radius Exponent",
        min=0,
        max=8,
        default=3
    )

    mass_mantissa: FloatProperty(
        name="Mass Mantissa",
        description="Mass Mantissa of the Central body",
        min=0.001,
        max=1000,
        default=1
    )

    mass_exponent: FloatProperty(
        name="Mass Exponent",
        description="Mass Exponent of the Central body",
        min=0,
        max=50,
        default=24
    )

    axis_tilt: FloatProperty(
        name="Tilt of Axis",
        description="Tilt of Axis of Rotation of Central body",
        min=0.0,
        max=90.0,
        default=23.5
    )

    rotation_period: FloatProperty(
        name="Rotation Period(hrs)",
        description="Time taken for one rotation on axis",
        min=10,
    )


class SatelliteData(bpy.types.PropertyGroup):
    sat_name: StringProperty(
        name="Satellite Name",
        description="Name of the object you want to make Satellite",
    )


class OrbitalElements(bpy.types.PropertyGroup):
    Eccentricity: FloatProperty(
        name="Eccentricity of Orbit",
        description="Value that determines shape of orbit, if e=1 then orbit is circle",
        min=0,
        default=1
    )






