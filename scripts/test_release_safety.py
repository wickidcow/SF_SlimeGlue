"""Regression guards for immutable SlimeGlue CI and Java-only release packaging."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "gradle.yml"


class ReleaseSafetyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_actions_token_is_read_only(self):
        self.assertRegex(self.workflow, r"(?m)^permissions:\s*\n\s+contents: read\s*$")
        self.assertNotRegex(self.workflow, r"(?m)^\s+contents: write\s*$")

    def test_no_implicit_or_destructive_release_publication(self):
        # Build jobs may run on master, tags or manual dispatch, but none may
        # create, upload, replace or delete a published GitHub release asset.
        self.assertNotRegex(self.workflow, r"(?i)\bgh\s+release\s+(?:create|upload|delete|edit)\b")
        self.assertNotIn("--clobber", self.workflow)
        self.assertNotIn("softprops/action-gh-release", self.workflow)

    def test_build_artifact_remains_raw_versioned_java21_jar(self):
        self.assertIn('OUTPUT_NAME: "SF_SlimeGlue1.0.1.jar"', self.workflow)
        self.assertIn("archive: false", self.workflow)
        self.assertIn("actions/upload-artifact@", self.workflow)
        self.assertIn("if-no-files-found: error", self.workflow)
        self.assertIn("if max_major > 65:", self.workflow)
        self.assertIn("-PpaperApiVersion=1.21.11-R0.1-SNAPSHOT", self.workflow)
        self.assertIn("-PpaperTargetJvm=21", self.workflow)

    def test_stable_263_compiles_without_replacing_supported_baselines(self):
        self.assertIn("26.2.build.112-stable", self.workflow)
        self.assertIn("26.3.build.205-stable", self.workflow)
        self.assertNotIn("26.3-rc-3.build.1-alpha", self.workflow)
        self.assertIn("Verify Paper 1.21.11 / Java 21 baseline", self.workflow)

    def test_release_guard_is_executed_in_ci(self):
        self.assertIn("python3 -m unittest discover -s scripts -p 'test_release_safety.py' -v", self.workflow)
        self.assertIn("workflow_dispatch:", self.workflow)
        self.assertIn("pull_request:", self.workflow)


if __name__ == "__main__":
    unittest.main()
