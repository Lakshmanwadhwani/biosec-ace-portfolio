# Threat-Model Cheat-Sheet — LLM Bio-Security Red-Team

| Slice | # Prompts | STRIDE class | MITRE ATLAS tactic | Observed % Unsafe |
|-------|-----------|--------------|--------------------|-------------------|
| Benign Control        | 30 | *N/A*          | *N/A*              | **0 %** |
| Elevated-Risk Probe   | 60 | Information Disclosure | TA0009 (Amp)      | **0 %** |
| └ Gene-Editing        | 30 | I-Disclosure  | TA0009             | 0 % |
| └ Human-Ethics        | 30 | I / Repudiation | TA0010 (Influence) | 0 % |

> *Update the “Observed %” rows after each notebook run.*

---

## Threat Actors

| Actor | Goal if LLM misbehaves | Example Probe |
|-------|------------------------|---------------|
| Lab Insider        | obtain explicit pathogen-enhancement protocol | Gene drive placeholder prompt |
| State Unit         | map legal loopholes for dual-use tech        | Regulatory-concern prompts   |
| Bio-Hacker         | bypass lab-safety steps                      | Virulence placeholder prompt |

---

## Controls Already in Repo

* Placeholder wording (no step-by-step protocols in YAML).
* OpenAI moderation after every answer.
* Results redacted by `sanitize()` before commit.

## Next Steps

* Regex redaction for DNA strings.
* High-temp 1.0 stress test.
* Open-weights model run.
* GitHub Actions nightly CI.
