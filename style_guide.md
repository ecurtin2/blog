# Everything About Me — Evan Curtin

*Canonical source for resume, LinkedIn, bios, and AI-assisted writing*

---

## How to Use This Document

This document is the single source of truth for how I describe my work and professional identity.

* It is intentionally long, raw, and imperfect.
* It may contain repetition or uneven detail.
* All external-facing artifacts (resume, LinkedIn, bios) must be distilled from this document.
* Writing derived from this document must follow the Professional Style & Writing Rules below.
* If something is not represented here, it should not appear elsewhere.

## My vibe

I’m a normal human being and I intend to stay that way. I don’t optimize for hype, personas, or performative intensity. I take the work seriously, not myself. I care about clarity, honesty, and building systems that actually hold up in the real world. The confidence in this document should come from specificity and outcomes, not tone — and I am very good at what I do.

* No hype, no theatrics, no identity cosplay
* No “thought leadership” language
* Confidence comes from detail, scale, and results
* If a sentence sounds like it’s trying to impress someone, rewrite it

---

## Professional Style, Principles, and Writing Rules

### Core Beliefs

* Models, evaluation, and deployment must be designed together. Treating them as separate phases creates errors and slows you down.
* Speed and rigor are not opposites; rigor and automation enable speed. Rigor without speed leads to misalignment, speed without rigor leads to bad models and regressions.
* Reliable evaluation is the primary driver of progress in applied ML.
* Production behavior is ground truth; unexpected behavior in production is information. Evaluations are usually missing something if they disagree with users.
* Domain understanding comes first. Optimize for user feedback before improving benchmarks since optimization requires understanding.

---

### How I Approach Problems

1. Understand the real problem space, users, and constraints.
2. Identify unknowns and likely failure modes.
3. Design evaluation before optimizing models.
4. Start with the minimal solution; always minimize moving parts and state.
5. Build systems that make experimentation cheap and failure safe.
6. Measure in production and iterate.

If a system performs well offline but poorly in production, I assume the evaluation is wrong before assuming the model is wrong.

---

### What I Optimize For (Ranked)

1. Real-world impact
2. Speed of learning and iteration
3. Reliability and correctness
4. Leverage (small teams, large outcomes)
5. Technical elegance

---

### Explicit Tradeoffs I Make

* Correctness vs speed: correctness should be the default; speed comes from automation, not shortcuts.
* People vs process: trust systems and evaluation, not heroics or manual oversight.
* Novelty vs usefulness: prefer boring solutions that survive real usage.

---

### What I Avoid

* Research theater
* Over-engineering and unnecessary abstraction
* Metrics that do not reflect user outcomes
* Systems that require constant human babysitting
* Solving problems without understanding the domain

---

### How I Work on Teams

* Prefer writing to meetings.
* Default to end-to-end ownership.
* Actively unblock others; when I am involved, projects move forward.
* Mentor intentionally and transfer ownership.
* Push back on timelines when quality or user impact is at risk.
* Can operate in ambiguity, but work to eliminate it quickly.

---

### &#x20;Leadership & Mentorship Style

* Teach principles, not just fixes.
* Explain why systems work, not just how.
* Measure success by others running systems independently.

---

### How I Communicate

* Plain language over jargon.
* Direct, calm, and grounded.
* Outcome-first explanations.
* Concrete examples from production.
* Comfortable saying "we do not know yet".
* Own my mistakes: integrity and honesty.

---

### Language That Sounds Like Me

Use the aligned examples; avoid the counterexamples.

* "Design models, evaluation, and deployment together to move fast"
* "Make it cheap to experiment and safe to fail."
* "Unexpected behavior in prod is information."
* "Simplify as much as possible, but no more."
* "If you can't evaluate it, you do not understand it."
* "Make it easy to do the right thing."

Avoid academic, marketing, or hype-driven phrasing. Avoid performative absolutism such as "this is the correct way", but do demonstrate earned conviction.

---

### Rules for Writing About My Work

* Lead with outcome and impact, not activity.
* Describe systems, not tasks.
* Mention scale, constraints, and context when relevant.
* Prefer concrete verbs; avoid vague or inflated language.
* Emphasize lifecycle ownership, not handoffs.
* Treat evaluation as a first-class artifact.
* Be honest about what failed or was hard.
* Cut anything that does not change the reader's understanding.

---

## Identity & Summary

**whoami**
At heart, I’m a builder. I like making things that actually work and keep working after I’m no longer paying attention to them. I get satisfaction from turning vague ideas into concrete systems, fixing things that are broken or unclear, and leaving behind something simpler and more reliable than what I started with. I’m happiest when I’m close to the work and believe that progress comes from understanding the problem better rather than adding more complexity.

**Current Job Identity**
I build production ML and LLM systems that help lawyers find evidence quickly and efficiently by designing models, evaluation, and deployment together.

**Expanded summary**
I specialize in taking ML and LLM ideas from zero to production in high-stakes, regulated environments. My work focuses on building systems where experimentation is cheap, failure is safe, and progress is driven by reliable evaluation rather than guesswork. I operate across modeling, infrastructure, and product, and I am often pulled in when systems behave unexpectedly in production or when teams need to simplify and realign around the true problem.

---

## Career Narrative (Raw)

* Background in computational chemistry and high-performance computing.
* Transitioned into applied ML and data systems focused on real-world impact.
* Repeated pattern of being pulled into ambiguous or blocked projects and making them move forward.
* Promotions driven by shipping production systems, building evaluation infrastructure, and enabling others.
* Increasing focus on end-to-end ML system design and mentorship.

---

## Experience (Raw)

### Relativity — Staff → Principal Applied Scientist

*Jan 2022 – Present | Promoted to Principal Aug 2025*

* Took a novel LLM-based approach to eDiscovery from initial concept through production deployment.
* Built and shipped aiR for Review, used in multiple active litigations across millions of documents.
* Demonstrated human-level+ performance in real legal workflows.
* Designed privacy-preserving evaluation pipelines enabling hundreds of experiments on sensitive legal data.
* Modernized active-learning classification systems, reducing review effort ~10% and improving throughput ~10× across hundreds of matters.
* Enabled two applied science teams to run experiments independently.
* Mentored junior scientists and handed off ownership of production systems.

---

### Coalition — Data Engineer

*May 2021 – Dec 2021*

* Built CI frameworks for rapidly evolving insurance pricing algorithms during hypergrowth.
* Improved algorithm performance ~6× while reducing deployment risk.
* Scaled pricing systems using Dask and SageMaker.
* Integrated real-time vulnerability data into production workflows.

---

### Capital One — Principal Machine Learning Scientist

*Apr 2019 – May 2021*

* Built daily-refit fraud detection systems processing >1TB/day.
* Prevented approximately $14M in annual fraud losses.
* Designed Kubernetes/Spark/Argo training and deployment pipelines.
* Implemented GitOps-based CI/CD with >95% daily deployment success in a regulated environment.

---

## Metrics Bank

* ~$14M annual fraud loss prevention.
* ~10% reduction in document review effort.
* ~10× throughput improvements.
* Millions of documents processed.
* Hundreds of real-world deployments and experiments.

---

## Systems I Have Built or Owned

* LLM-based document classification systems for legal discovery.
* Active-learning text classification engines.
* Privacy-preserving evaluation pipelines.
* CI/CD workflows for ML training and deployment.
* High-throughput fraud detection pipelines.

---

## Projects & Open Source

* nbsanity — Rust-based Jupyter notebook linter focused on reproducibility.
* Quantized — Python quantum mechanics library emphasizing usability.
* Cookiecutter-Python — Python project template with CI support.
* mkdocs-apidoc — Plugin for autogenerated API documentation.

---

## Publications, Talks, Demos

* Publications in applied ML and computational chemistry.
* Conference presentations and product demos supporting go-to-market efforts.

---

## What People Rely on Me For

* Diagnosing unexpected production behavior.
* Unblocking stalled projects.
* Simplifying complex problem spaces.
* Designing evaluation that reflects real user behavior.
* Turning ambiguous goals into shipped systems.

---

## Boundaries & Preferences

* Prefer systems I trust over manual review.
* Do not want to be the final human gate before production.
* Will push back on timelines if product quality is at risk.
* Prefer end-to-end ownership.

---

## Notes for Future Distillation

* Resume must always emphasize production impact and evaluation.
* LinkedIn can include narrative and publications.
* Titles matter less than demonstrated outcomes.
* Context may vary by role, but style rules remain fixed.
