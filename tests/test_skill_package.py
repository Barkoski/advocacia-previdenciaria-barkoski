"""Validacao estrutural e de seguranca do pacote da skill."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "advocacia-previdenciaria-barkoski"
SKILL_FILE = SKILL_DIR / "SKILL.md"


def local_markdown_links(path):
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if target and not re.match(r"^(?:https?://|mailto:)", target):
            yield target


class SkillPackageTest(unittest.TestCase):
    def test_frontmatter_has_expected_identity(self):
        text = SKILL_FILE.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(match)
        frontmatter = match.group(1)
        self.assertRegex(frontmatter, r"(?m)^name: advocacia-previdenciaria-barkoski$")
        self.assertRegex(frontmatter, r"(?m)^description: \S.+$")

    def test_every_local_markdown_link_resolves(self):
        missing = []
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts or "graphify-out" in path.parts:
                continue
            for target in local_markdown_links(path):
                if not (path.parent / target).resolve().exists():
                    missing.append(f"{path.relative_to(ROOT)} -> {target}")
        self.assertEqual(missing, [])

    def test_every_reference_is_reachable_from_skill(self):
        pending = [SKILL_FILE.resolve()]
        visited = set()
        while pending:
            current = pending.pop()
            if current in visited:
                continue
            visited.add(current)
            for target in local_markdown_links(current):
                resolved = (current.parent / target).resolve()
                if resolved.suffix.lower() == ".md" and resolved.is_file():
                    pending.append(resolved)

        references = {path.resolve() for path in (SKILL_DIR / "references").glob("*.md")}
        self.assertEqual(references - visited, set())

    def test_codex_metadata_is_present_and_invocable(self):
        metadata = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "Advocacia Previdenciaria Barkoski"', metadata)
        self.assertRegex(metadata, r"(?m)^  short_description: \".{25,64}\"$")
        self.assertIn("$advocacia-previdenciaria-barkoski", metadata)
        self.assertIn("allow_implicit_invocation: true", metadata)

    def test_mandatory_safeguards_precede_case_preferences(self):
        text = SKILL_FILE.read_text(encoding="utf-8")
        order = text.split("## Ordem de controle", 1)[1].split("## Travas obrigatorias", 1)[0]
        items = re.findall(r"(?m)^\d+\. (.+)$", order)
        self.assertGreaterEqual(len(items), 4)
        self.assertIn("Travas obrigatorias", items[0])
        self.assertIn("Instrucao expressa", items[1])
        self.assertIn("Configuracao local", items[2])

    def test_documentation_does_not_claim_cloud_models_are_local_only(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        forbidden = ("os arquivos não saem dela", "os dados não saem da máquina")
        self.assertFalse(any(phrase in readme for phrase in forbidden))
        self.assertIn("pode ser enviado ao provedor configurado", readme)

    def test_plugin_manifest_is_valid_and_versioned(self):
        manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "advocacia-previdenciaria-barkoski")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")


if __name__ == "__main__":
    unittest.main()
