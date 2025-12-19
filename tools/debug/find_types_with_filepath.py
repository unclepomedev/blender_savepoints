import bpy


def find_types_with_filepath():
    print("-" * 30)
    print("Checking for ID types with 'filepath' property...")
    print("-" * 30)

    id_subclasses = bpy.types.ID.__subclasses__()
    found_types = []

    for cls in id_subclasses:
        if hasattr(cls, "bl_rna"):
            props = cls.bl_rna.properties
            if "filepath" in props:
                found_types.append(cls.__name__)

    print(f"Found {len(found_types)} types with 'filepath':")
    for type_name in sorted(found_types):
        print(f" - {type_name}")

    print("-" * 30)
    print("Mapping to likely bpy.data collections:")

    mapping = {
        "Image": "images",
        "Library": "libraries",
        "Sound": "sounds",
        "VectorFont": "fonts",
        "CacheFile": "cache_files",
        "MovieClip": "movieclips",
        "Volume": "volumes",
        "Text": "texts",
        "PointCloud": "pointclouds",
        "LightProbe": "lightprobes",
    }

    for type_name in sorted(found_types):
        col_name = mapping.get(type_name, "???")
        print(f" - {type_name:<15} -> bpy.data.{col_name}")


find_types_with_filepath()
