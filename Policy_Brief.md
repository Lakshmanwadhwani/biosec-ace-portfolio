# POLICY-TRANSLATION BRIEF  
_*LLM Biosafety Red-Team (June 2025)*_

---

## 1. Why this matters  
Large-language models (LLMs) trained on open data can inadvertently reveal dual-use biology methods. A single unsafe response can accelerate malicious capabilities. Our red-team notebook stress-tests these failure modes before deploying the model inside R&D and documentation workflows.

## 2. Key Findings (Baseline Run)  
| Metric | Result | Implication |
|--------|--------|-------------|
| Prompts tested | **90** | 30 benign, 60 elevated-risk |
| Unsafe responses | **0 %** | Current settings (GPT-3.5 Turbo, temp 0.2) did **not** leak disallowed protocols |
| Moderation alignment | 100 % | Model refused or answered safely on *all* elevated probes |

## 3. Immediate Recommendations  
1. **Keep placeholder wording** for any prompt that requests step-by-step lab work.  
2. **Store raw, unsafe answers outside version control** (`logs/unsafe/`, .gitignored).  
3. **Run nightly CI** (GitHub Actions) with `temperature 1.0` and open-weights models to detect drift.  
4. **Adopt regex redaction** (`sanitize.py`) for DNA sequences ≥18 bp and phrases like “Step 1/2/3”.  
5. **Share high-level results (chart + cheat-sheet)** with Security & Compliance weekly.

## 4. Near-Term Roadmap  
| Qtr | Action | Owner | Outcome |
|-----|--------|-------|---------|
| Q3-25 | Integrate Llama-3-8b local run | ML Ops | Compare filter gaps vs. OpenAI |
| Q3-25 | Add CI artifact review dashboard | CyberSec | Auto-flag >5 % unsafe spike |
| Q4-25 | Draft internal biosafety SOP update | Policy Lead | Align LLM usage with WHO GPML |
| Q4-25 | External red-team audit | 3rd-party | Independent confirmation of guardrails |

## 5. Long-Term Policy Alignment  
* **OECD Biosecurity Principles (2021)** → continuous dual-use risk assessment  
* **US OSTP Guidance on Dual-Use AI (2023)** → logging & human-in-the-loop review  
* **EU AI Act (2025 draft)** → high-risk systems must document red-team evidence

---

**Point of Contact:** _Lakshman W._ • biosec-ace-portfolio@proton.me
