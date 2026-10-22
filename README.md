<div align="center">
  <img src="docs/assets/header.svg" alt="ParamPhantom banner" width="100%" height="50%" />
</div>
<p>
<div align="center">
  <img src="https://img.shields.io/badge/Build-Passing-success?logo=githubactions&logoColor=white" alt="Build passing" />
  <img src="https://img.shields.io/badge/Tests-Passing-2ea44f?logo=pytest&logoColor=white" alt="Tests passing" />
  <img src="https://img.shields.io/badge/Stack-Python%20%7C%20JS%20Analysis%20%7C%20HTTP%20Fuzzing-0e7490?logo=python&logoColor=white" alt="Stack: Python, JS analysis, HTTP fuzzing" />
  <img src="https://img.shields.io/badge/Mode-CLI%20Security%20Research-111827?logo=terminal&logoColor=white" alt="CLI security research" />
</div>
<p>
<div align="center">
 <p>
    <strong>Client-side parameter discovery for mass-assignment and privilege-escalation testing.</strong>
  </p>
  <p>
    ParamPhantom bridges static analysis of frontend JavaScript with active API differential fuzzing to expose hidden parameter abuse paths and authorization gaps.
  </p>
</div>

ParamPhantom bridges client-side static analysis with active API differential fuzzing. By harvesting object keys and state variables directly from frontend JavaScript bundles, it automates the discovery of hidden mass-assignment vulnerabilities and privilege escalation pathways.

## Why it exists

Many web applications expose sensitive actions through parameter-heavy APIs without exposing those parameters in a single obvious contract. The challenge is not only identifying the route — it is finding which fields, state variables, or nested objects can be mutated in ways the server accepts but the business logic never intended.

ParamPhantom addresses that problem by starting from the frontend. It extracts likely state and parameter names from JavaScript bundles and then turns those names into active API probes that test whether the server accepts unexpected or over-privileged input.

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

The workflow starts with the client-side source of truth. By collecting property names and state objects from frontend code, ParamPhantom builds a high-value parameter set for active API testing. Those candidate fields are then sent through behavioral probes to reveal whether the backend accepts unexpected state changes or privilege escalations.

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

ParamPhantom is intended for authorized security testing, controlled bug bounty workflows, and lawful research on systems you own or have explicit permission to assess. It should be used for evidence-based validation, not indiscriminate exploitation.

## Contributing

Contributions are welcome when they improve the parameter discovery workflow, API differential logic, or testing precision. Keep changes focused and validate them with concrete examples tied to the intended security research workflow.

## Project focus

ParamPhantom is deliberately specialized. It is not a broad application scanner or generic fuzzing framework. Its value lies in connecting client-side observations to active server-side testing in order to surface parameter abuse and privilege escalation patterns faster.

---

<div align="center">
  <p><em>Built for precise, permissioned security testing and evidence-based authorization review.</em></p>
</div>
