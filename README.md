<div align="center">
    <h1>ParamPhantom</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-success?logo=githubactions&logoColor=white" alt="Build passing" />
  <img src="https://img.shields.io/badge/Tests-Passing-2ea44f?logo=pytest&logoColor=white" alt="Tests passing" />
  <img src="https://img.shields.io/badge/Stack-Python%20%7C%20JS%20Analysis%20%7C%20HTTP%20Fuzzing-0e7490?logo=python&logoColor=white" alt="Stack: Python, JS analysis, HTTP fuzzing" />
  <img src="https://img.shields.io/badge/Mode-CLI%20Security%20Research-111827?logo=terminal&logoColor=white" alt="CLI security research" />
    
</p>

</div>

<div align="center">
  <p><strong>Client-side parameter discovery for mass-assignment and privilege-escalation testing.</strong></p>
  <p>ParamPhantom bridges static analysis of frontend JavaScript with active API differential fuzzing to expose hidden parameter abuse paths and authorization gaps.</p>
</div>

---

## Why it exists

Many web applications expose sensitive actions through parameter-heavy APIs without exposing those parameters in a single obvious contract. The challenge is not only identifying the route — it is also finding which request fields are accepted, ignored, or abused in ways that create authorization or integrity bypasses.

ParamPhantom addresses that problem by starting from the frontend. It extracts likely state and parameter names from JavaScript bundles and then turns those names into active API probes that test how the backend reacts to hidden or oversupplied fields.

This makes it useful when a developer or researcher wants to move from static observation to actionable evidence without manually enumerating every hidden field or payload variant.

## At a glance

| Area | Focus |
| --- | --- |
| Discovery model | Client-side static analysis of frontend bundles |
| Active testing | Differential API fuzzing against server behavior |
| Target weakness | Mass assignment, hidden parameter abuse, privilege escalation |
| Audience | Security researchers and authorized pentesters |

## Core capabilities

- Extracts object keys and state variables from frontend JavaScript bundles.
- Identifies likely request parameter candidates before active testing begins.
- Uses differential API fuzzing to compare server behavior across payload variants.
- Focuses on hidden mass-assignment paths and privilege-escalation patterns.
- Helps prioritize manual validation for high-risk parameter abuse scenarios.

## How it works

```text
Frontend JS bundle
    ↓
Static key extraction
    ↓
Parameter hypothesis generation
    ↓
Differential API probing
    ↓
Response comparison and privilege / mass-assignment triage
```

The workflow starts with the client-side source of truth. By collecting property names and state objects from frontend code, ParamPhantom builds a high-value parameter set for active API testing. It then evaluates a target endpoint against subtle request variations to reveal when a backend accepts or honors unexpected fields beyond the intended contract.

## Typical usage

This tool is best suited for situations where:

- front-end code reveals internal state or object keys not obvious from public documentation;
- API payloads appear to accept dynamic fields beyond the expected schema;
- mass assignment or privilege escalation is suspected but not yet mapped to a reproducible request;
- researchers want to turn client-side observations into targeted API validation.

## Installation

Install the project in a Python 3.10+ virtual environment and expose the `paramphantom` CLI.

```bash
# Clone the repository
git clone https://github.com/dntaskmehow/paramphantom.git
cd paramphantom

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate
# On Windows PowerShell: .\.venv\Scripts\Activate.ps1

# Upgrade packaging tools and install the project in editable mode
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e .

# Confirm the CLI is available
paramphantom --help
```

## Quick start

The full runtime flow is: prepare the target, harvest candidate keys from JavaScript, run the differential probe, and then review the generated findings.

```bash
# 1) Export the target API endpoint and a JS source to inspect
export TARGET_URL="https://target.example.com/api/profile/update"
export JS_BUNDLE="https://target.example.com/static/app.js"
export API_TOKEN="your-bearer-token"

# 2) Run the ParamPhantom CLI against the endpoint
paramphantom \
  --url "$TARGET_URL" \
  --js "$JS_BUNDLE" \
  --header "Authorization: Bearer $API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{"user":{"name":"alice"}}' \
  --output paramphantom_report.json

# 3) Review the generated findings
cat paramphantom_report.json
```

You can also pass a local JavaScript bundle path instead of a URL, add custom parameters with `--param`, and include additional headers as needed for authentication or CSRF handling.

## Security and responsible use

ParamPhantom is intended for authorized security testing, controlled bug bounty workflows, and lawful research on systems you own or have explicit permission to assess. It should be used for evidence-gathering, confirmation, and responsible disclosure — not as a substitute for formal security control review or unsanctioned probing.

Use it to support responsible disclosure, secure architecture review, and targeted authorization testing — not as a substitute for formal security control review or unsanctioned probing.

## Contributing

Contributions are welcome when they improve the parameter discovery workflow, API differential logic, or testing precision. Keep changes focused and validate them with concrete examples tied to the actual security scenario being addressed.

## Project focus

ParamPhantom is deliberately specialized. It is not a broad application scanner or generic fuzzing framework. Its value lies in connecting client-side observations to active server-side testing in a way that helps prioritize real privilege-escalation and mass-assignment opportunities.

---

<div align="center">
  <p><em>Built for precise, permissioned security testing and evidence-based authorization review.</em></p>
</div>
