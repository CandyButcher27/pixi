import sys

from regenerate_stub_site import call_openrouter
from regenerate_with_review import PROMPT_TEMPLATE, SITES_DIR, parse_files


def generate_with_model(site: str, model_id: str, out_dir_name: str) -> dict[str, str]:
    design_spec = (SITES_DIR / site / "design.md").read_text(encoding="utf-8")
    files = parse_files(call_openrouter(PROMPT_TEMPLATE.format(design_spec=design_spec), model=model_id))

    out_dir = SITES_DIR / out_dir_name
    out_dir.mkdir(exist_ok=True)
    for name, body in files.items():
        (out_dir / name).write_text(body, encoding="utf-8")
    return files


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: python generate_forced_model.py <site> <openrouter_model_id> <out_dir_name>")
        sys.exit(1)

    site, model_id, out_dir_name = sys.argv[1:4]
    print(f"generating {site} with {model_id}...")
    try:
        files = generate_with_model(site, model_id, out_dir_name)
        print(f"  OK  wrote {', '.join(files.keys())} to websites/{out_dir_name}/")
    except Exception as e:
        print(f"  FAIL -> {e}")
