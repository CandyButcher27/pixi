"""Command-line access to the same contract and verification the MCP server exposes.

For contexts that cannot hold an MCP connection (subagents, CI, a shell).

  design_cli.py contract "<brief>" <build_dir>   freeze a contract into <build_dir>
  design_cli.py verify <page.html>               check a page against its frozen contract
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from designmcp import contract as contract_mod, verify as verify_mod  # noqa: E402


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd = sys.argv[1]

    if cmd == "contract":
        brief, build_dir = sys.argv[2], ROOT / sys.argv[3]
        c, fresh = contract_mod.freeze(brief, build_dir)
        print(contract_mod.as_markdown(c, brief))
        print(f"\n> contract frozen at {c['frozen_at']}"
              f"{'' if fresh else ' (existing freeze reused — selection is fixed)'}")
        print(f"> written to {Path(sys.argv[3])}/DESIGN_CONTRACT.md and contract.json")
    elif cmd == "verify":
        page = Path(sys.argv[2])
        page = page if page.is_absolute() else ROOT / page
        c, source = contract_mod.load_frozen(page.parent)
        if c is None:
            sys.exit(f"no frozen contract beside {page} — run `design_cli.py contract` first")
        print(f"contract: {source}\n")
        print(verify_mod.report(verify_mod.verify(page, c)))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
