<div align="center">
  <img src="docs/assets/header.svg" alt="ParamPhantom banner" width="1000" />
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-success?logo=githubactions&logoColor=white" alt="Build passing" />
  <img src="https://img.shields.io/badge/Tests-Passing-2ea44f?logo=pytest&logoColor=white" alt="Tests passing" />
  <img src="https://img.shields.io/badge/Stack-Python%20%7C%20JS%20Analysis%20%7C%20HTTP%20Fuzzing-0e7490?logo=python&logoColor=white" alt="Stack: Python, JS analysis, HTTP fuzzing" />
  <img src="https://img.shields.io/badge/Mode-CLI%20Security%20Research-111827?logo=terminal&logoColor=white" alt="CLI security research" />
</p>

<div align="center">
  <h1>ParamPhantom</h1>
  <p><strong>Client-side parameter discovery for mass-assignment and privilege-escalation testing.</strong></p>
  <p>ParamPhantom bridges static analysis of frontend JavaScript with active API differential fuzzing to expose hidden parameter abuse paths and authorization gaps.</p>
</div>

---

## Why it exists

Many web applications expose sensitive actions through parameter-heavy APIs without exposing those parameters in a single obvious contract. The challenge is not only identifying the route — it is mapping the hidden field names, object state values, and authorization-sensitive inputs that are only visible in client-side logic.

ParamPhantom addresses that problem by starting from the frontend. It extracts likely state and parameter names from JavaScript bundles and then turns those names into active API probes that test how the server behaves under different payload combinations.

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

The workflow starts with the client-side source of truth. By collecting property names and state objects from frontend code, ParamPhantom builds a high-value parameter set for active API testing. It then sends targeted requests with varying payload values to compare baseline and injected responses. Where the server shows a meaningful shift in status, length, or behavior, the result is surfaced as a likely abuse or escalation path worthy of deeper review.

## Typical usage

This tool is best suited for situations where:

- front-end code reveals internal state or object keys not obvious from public documentation;
- API payloads appear to accept dynamic fields beyond the expected schema;
- mass assignment or privilege escalation is suspected but not yet mapped to a reproducible request;
- researchers want to turn client-side observations into targeted API validation.

## Installation

As with the other packaged security tools in this repository set, the project is distributed as an archive payload and is intended to be extracted locally before use.

```bash
# Example workflow
unzip paramphantom.zip -d paramphantom/
cd paramphantom
# run the packaged CLI entrypoint as provided in the release artifacts
```

## Quick start

The practical flow is:

1. extract the packaged project;
2. supply the target application or API context;
3. let ParamPhantom harvest candidate keys from the frontend bundle;
4. run differential fuzzing against the target endpoints;
5. review the resulting findings for likely mass-assignment or escalation paths.

## Security and responsible use

ParamPhantom is intended for authorized security testing, controlled bug bounty workflows, and lawful research on systems you own or have explicit permission to assess. It should be used for evidence-based security review and internal validation in environments where permission to test has been explicitly granted.

Use it to support responsible disclosure, secure architecture review, and targeted authorization testing — not as a substitute for formal security control review or unsanctioned probing.

## Contributing

Contributions are welcome when they improve the parameter discovery workflow, API differential logic, or testing precision. Keep changes focused and validate them with concrete examples tied to the actual security testing workflow and the project’s intended scope.

## Project focus

ParamPhantom is deliberately specialized. It is not a broad application scanner or generic fuzzing framework. Its value lies in connecting client-side observations to active server-side testing in a focused, operationally useful way.

---

<div align="center">
  <p><em>Built for precise, permissioned security testing and evidence-based authorization review.</em></p>
</div>
