"""Verify the English notebook archive without importing experiment code.

Run with Python 3.10+: python tools/verify_archive.py
No credentials, network access, model weights, or GPU are required.
"""
import base64
import hashlib
import json
from pathlib import Path
import re
import zlib

ROOT = Path(__file__).resolve().parents[1]
HAN = re.compile(r"[\u3400-\u9fff]")
SECRET = re.compile(r"\b(?:hf_|sk-|ghp_|github_pat_)[A-Za-z0-9_-]{16,}")


def main():
    inventory = json.loads((ROOT / "notebook-inventory.json").read_text())
    outputs = 0
    for item in inventory:
        path = ROOT / item["path"]
        data = path.read_bytes()
        assert hashlib.sha256(data).hexdigest() == item["english_sha256"], item["path"]
        text = data.decode("utf-8")
        assert not HAN.search(text), f"Untranslated text: {item['path']}"
        assert not SECRET.search(text), f"Possible credential: {item['path']}"
        notebook = json.loads(text)
        assert notebook["nbformat"] == 4
        count = sum(len(cell.get("outputs", [])) for cell in notebook["cells"])
        assert count == item["outputs"], item["path"]
        assert len(notebook["cells"]) == item["cells"], item["path"]
        outputs += count
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.ipynb")}
    assert actual == {item["path"] for item in inventory}
    print(json.dumps({"status": "PASS", "notebooks": len(inventory),
                      "saved_output_blocks": outputs, "model_calls": 0}, indent=2))


if __name__ == "__main__":
    main()
