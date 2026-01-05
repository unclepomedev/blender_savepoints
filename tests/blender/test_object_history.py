import json
import sys
import unittest
from pathlib import Path

import bmesh
import bpy

# Add project root to path so we can import the addon modules
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.snapshot import create_snapshot, find_snapshot_path
from savepoints.services.object_history import compare_object_history
from savepoints.services.object_data import OBJECT_DATA_SUFFIX
from savepoints_test_case import SavePointsTestCase


class TestObjectHistory(SavePointsTestCase):
    def test_object_history_lifecycle(self):
        # 1. Setup - Create Cube
        bpy.ops.mesh.primitive_cube_add(size=2)
        obj = bpy.context.active_object
        obj.name = "TestCube"
        bpy.ops.object.mode_set(mode='OBJECT')

        # --- VERSION 1: Base State ---
        create_snapshot(bpy.context, "v1", "Base", skip_thumbnail=True)

        with self.subTest("Validate Metadata Format"):
            snap_path = find_snapshot_path("v1")
            meta_path = snap_path.parent / f"v1{OBJECT_DATA_SUFFIX}"
            self.assertTrue(meta_path.exists(), "Metadata file should exist")

            with open(meta_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.assertIn("TestCube", data)
            cube_data = data["TestCube"]

            # Validate Matrix (16 floats)
            self.assertIsInstance(cube_data['matrix'], list)
            self.assertEqual(len(cube_data['matrix']), 16)
            self.assertIsInstance(cube_data['matrix'][0], (float, int))

            # Validate Bbox (2 points * 3 coords)
            self.assertIsInstance(cube_data['bbox'], list)
            self.assertEqual(len(cube_data['bbox']), 2)
            self.assertEqual(len(cube_data['bbox'][0]), 3)

        # --- VERSION 2: Moved (Matrix change) ---
        obj.location.x += 5.0
        bpy.context.view_layer.update()
        create_snapshot(bpy.context, "v2", "Moved", skip_thumbnail=True)

        # --- VERSION 3: Minor (BBox change, same verts) ---
        bpy.ops.object.mode_set(mode='EDIT')
        bm = bmesh.from_edit_mesh(obj.data)
        for v in bm.verts:
            v.co.z += 2.0
        bmesh.update_edit_mesh(obj.data)
        bpy.ops.object.mode_set(mode='OBJECT')
        create_snapshot(bpy.context, "v3", "Stretched", skip_thumbnail=True)

        # --- VERSION 4: Major (Vert count change) ---
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.subdivide()
        bpy.ops.object.mode_set(mode='OBJECT')
        create_snapshot(bpy.context, "v4", "Subdivided", skip_thumbnail=True)

        with self.subTest("Compare History"):
            history = compare_object_history(obj)
            # Implementation is "Static History Log" (Snapshot vs Snapshot).
            # It returns the history of the object name recorded in snapshots.
            # v1: Created
            # v2: Moved (vs v1)
            # v3: Minor (vs v2)
            # v4: Major (vs v3)

            # Returns Newest First (v4, v3, v2, v1)
            self.assertEqual(len(history), 4)

            self.assertEqual(history[0]['version_id'], 'v4')
            self.assertEqual(history[0]['change_type'], 'MAJOR')

            self.assertEqual(history[1]['version_id'], 'v3')
            self.assertEqual(history[1]['change_type'], 'MINOR')

            self.assertEqual(history[2]['version_id'], 'v2')
            self.assertEqual(history[2]['change_type'], 'MOVED')

            self.assertEqual(history[3]['version_id'], 'v1')
            self.assertEqual(history[3]['change_type'], 'CREATED')

    def test_object_history_with_unchanged(self):
        # 1. Setup - Create Cube
        bpy.ops.mesh.primitive_cube_add(size=2)
        obj = bpy.context.active_object
        obj.name = "TestCubeUnchanged"
        bpy.ops.object.mode_set(mode='OBJECT')

        # --- VERSION 1: Base State ---
        create_snapshot(bpy.context, "v1", "Base", skip_thumbnail=True)

        # --- VERSION 2: No Change (Simulate Save without Edit) ---
        create_snapshot(bpy.context, "v2", "Unchanged", skip_thumbnail=True)

        # --- VERSION 3: Moved ---
        obj.location.x += 5.0
        bpy.context.view_layer.update()
        create_snapshot(bpy.context, "v3", "Moved", skip_thumbnail=True)

        with self.subTest("Default behavior (Hidden Unchanged)"):
            history = compare_object_history(obj)
            # Should show v3(MOVED) and v1(CREATED). v2 should be hidden.
            self.assertEqual(len(history), 2)
            self.assertEqual(history[0]['version_id'], 'v3')
            self.assertEqual(history[0]['change_type'], 'MOVED')
            self.assertEqual(history[1]['version_id'], 'v1')
            self.assertEqual(history[1]['change_type'], 'CREATED')

        with self.subTest("Show All (Include Unchanged)"):
            history = compare_object_history(obj, include_change_not_detected=True)
            # Should show v3, v2, v1
            self.assertEqual(len(history), 3)

            self.assertEqual(history[0]['version_id'], 'v3')
            self.assertEqual(history[0]['change_type'], 'MOVED')

            self.assertEqual(history[1]['version_id'], 'v2')
            self.assertEqual(history[1]['change_type'], 'RECORD')
            
            self.assertEqual(history[2]['version_id'], 'v1')
            self.assertEqual(history[2]['change_type'], 'CREATED')


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
