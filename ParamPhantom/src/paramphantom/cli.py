import argparse
import sys
import json
from .config import PhantomConfig
from .extractor import JSExtractor
from .engine import PhantomEngine
from .reporter import PhantomReporter

def main():
    parser = argparse.ArgumentParser(description="ParamPhantom: AST JS Taint & Mass Assignment Fuzzer.")
    parser.add_argument("--url", required=True, help="Target API endpoint URL.")
    parser.add_argument("--js", action="append", default=[], help="URL or path to JavaScript bundle.")
    parser.add_argument("--param", action="append", default=[], help="Custom parameter to test.")
    parser.add_argument("--header", action="append", default=[], help="Custom header in 'Key: Value' format.")
    parser.add_argument("--data", default="{}", help="Base JSON request body.")
    parser.add_argument("--output", default="paramphantom_report.json", help="Output JSON report file.")

    args = parser.parse_args()

    headers = {}
    for h in args.header:
        if ":" in h:
            k, v = h.split(":", 1)
            headers[k.strip()] = v.strip()

    try:
        base_body = json.loads(args.data)
    except Exception:
        base_body = {}

    discovered_params = set()
    for js_url in args.js:
        print(f"[*] Harvesting keys from JS source: {js_url}")
        keys = JSExtractor.harvest_from_url(js_url)
        print(f"    [+] Extracted {len(keys)} candidate keys.")
        discovered_params.update(keys)

    config = PhantomConfig(
        target_url=args.url,
        headers=headers,
        base_body=base_body,
        js_sources=args.js,
        custom_params=args.param
    )

    try:
        print(f"[*] Initializing differential mass-assignment engine...")
        engine = PhantomEngine(config, discovered_params)
        findings = engine.run()
        PhantomReporter.print_terminal_report(findings)
        PhantomReporter.save_json_report(findings, args.output)
    except Exception as e:
        print(f"[!] Execution Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
