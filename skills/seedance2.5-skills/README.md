<p align="center">
  <img src="assets/seedance-25-hero.png" alt="A cinematic Seedance 2.5 direction console combining image, video, audio, camera, and continuity references into one finished shot" width="100%">
</p>

<h1 align="center">Seedance 2.5 Director</h1>

<p align="center">
  <strong>Direct the scene. Bind the references. Preserve the state.</strong><br>
  An English-language agent skill for turning ideas, scripts, and multimodal assets into production-ready Seedance 2.5 prompts.
</p>

<p align="center">
  <img alt="Seedance 2.5" src="https://img.shields.io/badge/Seedance-2.5-7c5cff?style=flat-square">
  <img alt="Agent Skill" src="https://img.shields.io/badge/Agent-Skill-45c8ff?style=flat-square">
  <img alt="Documentation language: English" src="https://img.shields.io/badge/Docs-English-1f9d8a?style=flat-square">
  <img alt="Prompt linter included" src="https://img.shields.io/badge/Prompt_Linter-Included-f2a750?style=flat-square">
</p>

<p align="center">
  <strong>English</strong> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a>
</p>

<p align="center">
  <a href="#why-this-repository-exists">Why</a> ·
  <a href="#what-the-skill-does">Capabilities</a> ·
  <a href="#start-here">Start here</a> ·
  <a href="#installation">Install</a> ·
  <a href="#using-the-skill">Use</a> ·
  <a href="#prompt-linter">Lint</a> ·
  <a href="#official-source-boundary">Sources</a>
</p>

---

## Why this repository exists

Seedance 2.5 can accept text, images, video, and audio, but more input does not automatically produce more control. Complex generations usually fail for structural reasons:

- references compete to control the same dimension;
- characters, props, or dialogue are not bound to named owners;
- a shot contains more events than its duration can support;
- camera language hides the decisive action;
- an edit does not identify one master video and one edit scope;
- an extension follows the planned ending instead of the generated boundary;
- a retry changes too many variables to reveal what fixed the problem.

This repository turns those recurring production problems into one reusable agent skill. It does not merely expand a short idea into a longer adjective list. It first decides what each asset controls, then directs visible action, camera, light, performance, sound, continuity, and the final state.

The result is a prompt that is easier to generate, review, repair, and hand to another collaborator.

## What the skill does

`seedance-25` helps an agent:

- create a new Seedance 2.5 prompt from a brief;
- revise, compress, or translate an existing prompt;
- choose the correct generation path before writing prose;
- map image, video, and audio references to explicit roles;
- plan standard, staged, and multi-clip long-form productions;
- write edit, extension, endpoint, storyboard, blockout, and transition prompts;
- preserve identity, geometry, prop ownership, geography, camera phase, and audio continuity;
- diagnose a failed take and choose between keep, post, edit, re-roll, or rewrite;
- change one variable per retry;
- lint prompt structure before generation.

It deliberately separates two kinds of knowledge:

1. **Verified platform facts** — counts, durations, locked settings, and named workflows from official Dreamina Seedance 2.5 material.
2. **Production method** — reusable directing, reference-contract, continuity, and repair techniques.

That separation prevents old Seedance 2.0 limits or unverified third-party claims from silently becoming “2.5 facts.”

## Seedance 2.5 at a glance

The following values come from the official Dreamina Seedance 2.5 guides listed in [Official source boundary](#official-source-boundary). They were verified on August 3, 2026 and apply to the documented Dreamina surfaces, not automatically to every API or third-party product.

| Capability | Official Dreamina 2.5 guidance |
|---|---|
| Total reference assets | Up to 50 |
| Images | Up to 30; each no larger than 4K |
| Video references | Up to 10; no more than 30 seconds combined |
| Audio references | Up to 10; no more than 30 seconds combined |
| Standard generation | 4–30 seconds |
| One extension operation | 4–30 seconds |
| Nested extension | Final output up to 60 seconds |
| Listed output resolutions | 480p and 720p |

For a generic or unknown Seedance 2.5 surface, one direct generation must not exceed 30 seconds. Plan longer work as several independently generated clips. A maximum is not a target: the skill removes references that control nothing and selects only the assets required for the current scene.

Current API fields, model IDs, pricing, quotas, regions, accounts, rollout status, and surface availability are intentionally outside the frozen knowledge boundary. They must be checked against current official documentation at the time of use.

## The operating model

<p align="center">
  <img src="assets/skill-workflow.svg" alt="Six-stage Seedance 2.5 workflow: brief, mode gate, reference contracts, direction, compilation, and linting" width="100%">
</p>

Every request moves through the same controlled pipeline:

1. **Brief** — establish the goal, active surface, duration, assets, must-haves, and rights.
2. **Mode gate** — choose generation, edit, extension, endpoint, storyboard, blockout, or transition logic.
3. **Contracts** — assign every reference a role, authority, and exclusions.
4. **Direction** — define the visible event, camera, light, performance, sound, and end state.
5. **Compilation** — produce one copy-ready natural-language prompt with exact reference tokens.
6. **Linting** — detect structural risks before spending a generation.

The skill then delivers a compact production contract: settings, reference role map, final prompt, and only the material risks or next step.

## Start here

Choose the path by production intent, not by how many adjectives appear in the brief.

| Your task | Use this path | Primary protection |
|---|---|---|
| One clear standalone shot | Basic generation | One primary visible event and one primary camera move |
| Image, video, or audio references | Multimodal reference | One defined role and explicit exclusions per asset |
| Several events within 30 seconds | Staged generation | One state change and one visible end state per stage |
| More than 30 seconds | Multi-clip production | Split the work into independently generated clips of no more than 30 seconds |
| Modify existing footage | Video edit | One sole master, one edit scope, and a preservation list |
| Continue accepted footage | Forward or backward extension | The observed boundary frame is continuity truth |
| Two endpoints | First/last-frame generation | Separate endpoint definitions joined by continuous action |
| Several ordered states | Multiple keyframes | Explicit order and arrival state for every anchor |
| Panel grid or sketch | Storyboard reference | Reading order, shot roles, and line-art exclusions |
| 3D gray model | Coarse or fine blockout | Classify motion skeleton versus complete geometry |
| Fast assembly from several images | One-click video | Asset order, motion amount, edit rhythm, packaging, and sound |
| Bridge two clips | Seamless transition | Trigger, coverage process, arrival state, and audio bridge |
| Failed or partly correct take | Diagnose and retry | A verdict first, then exactly one changed variable |

The skill reads only the reference section needed for the selected path. It does not flood every request with every template.

## Reference assets are contracts

<p align="center">
  <img src="assets/reference-role-map.svg" alt="Reference role map connecting image, video, audio, source video, and keyframe assets to distinct output dimensions" width="100%">
</p>

A reference contract answers two questions for every asset:

1. What may this asset control?
2. What must not transfer from it?

Example:

```text
@Image 1 defines Character A's facial features, hairstyle, and wardrobe.
Do not use its background, composition, pose, or lighting.

@Video 1 controls only Character A's motion path, timing, and camera rhythm.
Do not transfer the performer, wardrobe, room, logos, or source audio.

@Audio 1 controls only Character A's voice, delivery, and the quoted line.
Do not add background music.
```

Three rules are non-negotiable:

- preserve platform-inserted reference tokens exactly;
- select one controlling source for every output dimension;
- remove every asset that controls nothing.

When several images show one subject, the prompt says so explicitly and locks the output count. When several sources conflict, the skill selects a winner instead of asking the model to “blend everything.”

## Directorial prompt architecture

The final prompt is compiled in this order:

```text
Reference roles
→ Generation goal
→ Subject and primary event
→ Scene or stage progression
→ Camera
→ Light and visual treatment
→ Audio
→ Continuity and exclusions
```

The architecture favors observable choices:

- “A hard window key from camera left cuts across the face” instead of “beautiful lighting.”
- “The dolly starts waist-high, tracks the runner from the left, then stops on the closed gate” instead of “dynamic camera.”
- “Her gaze drops, jaw tightens, right hand releases the key, and breathing becomes shallow” instead of “very emotional.”
- “The glass fractures from the impact point, fragments catch the desk light, then settle on the floor” instead of “epic destruction.”

Each action should expose an initial state, trigger, change, consequence, and visible end state. Exact seconds are reserved for critical handoffs, entrances, exits, transitions, or beats; ordinary narrative is organized by stages.

## Example: multimodal scene

### Production brief

```text
Goal: a tense 12-second product reveal in a rain-darkened workshop.
References: one product image, one camera-motion clip, one ambience recording.
Must preserve: product geometry, engraved mark, and subject count.
Output: 16:9, 720p, 12 seconds.
```

### Reference role map

```text
@Image 1 — product geometry, material, and engraved mark only;
             do not use its white background or studio reflections.
@Video 1 — camera path and acceleration only;
             do not transfer its room, performer, object, color grade, or audio.
@Audio 1 — rain ambience and distant metal resonance only;
             do not add speech or music.
```

### Final prompt

```text
@Image 1 defines the exact geometry, dark brushed metal, and engraved mark of one product. Do not use its white background, studio composition, or reflections. @Video 1 controls only the camera path and acceleration; do not transfer its room, performer, object, color grade, or sound. @Audio 1 controls only rain ambience and distant metal resonance; do not add dialogue or music.

Generate a 12-second product reveal in a rain-darkened mechanical workshop. The frame begins close on a wet steel workbench with the product mostly hidden beneath a charcoal cloth. A gloved hand enters from frame right and pulls the cloth away in one continuous movement. Water beads remain on the product surface; the engraved mark becomes fully visible as the cloth clears it. End state: exactly one product stands unobstructed at the center of the bench, the hand has exited frame right, and the cloth rests at the far edge.

Camera: inherit only the path and acceleration from @Video 1, beginning at bench height, sliding left around the product, and settling in a centered three-quarter close-up. Light: a cold overhead work lamp creates a narrow rim on the wet metal while one warm furnace reflection moves across the side during the camera slide. Sound: preserve @Audio 1's rain and distant metal resonance, add one soft cloth drag and one restrained metal settle, with no speech and no music.

Maintain exactly one product, its geometry, engraved mark, material, bench position, and screen direction throughout. Do not add text, logos, extra hands, tools crossing the product, or additional products.
```

The generation settings stay outside the prompt when the active surface exposes them as controls.

## Mode-specific protections

### Video editing

An edit prompt must declare:

- one source video as the sole editing master;
- one object, region, time range, or audio category to change;
- the target count and replacement inheritance when relevant;
- everything outside the edit scope that must remain unchanged.

### Forward and backward extension

Accepted footage overrides the original plan. The prompt begins from the observed boundary state: pose, gaze, prop ownership, space, camera position and movement phase, open subject motion, and audio phase. A backward extension also prevents characters, props, or effects from appearing before they exist in the source.

### First/last frames and keyframes

Every endpoint is defined independently. Supplemental references may control identity, wardrobe, or geometry, but they may not override endpoint composition. Multiple keyframes establish ordered states, not frame-by-frame reproduction.

### Storyboards and blockouts

A storyboard controls shot order and approximate composition while excluding line-art style, labels, and placeholder characters. A coarse blockout controls the temporal and spatial skeleton; a fine blockout may control complete geometry before materials, characters, environment, and style are rendered.

### Seamless transitions

A transition needs a physical trigger or morph process, continuous motion through the bridge, a defined arrival composition, and an audio transition. “Make it seamless” is not enough direction.

## Output contract

For a normal request, the skill returns:

1. **Task mode and generation settings** — duration, aspect ratio, resolution, locked values, and disclosed assumptions.
2. **Reference role map** — what to use and what not to use for every asset.
3. **Final prompt** — one directly copyable code block with exact reference tokens.
4. **Risks or next step** — one to three issues that materially affect success.

For a diagnostic request, it returns:

```text
Verdict → Evidence → One changed variable → Repaired prompt
```

If the primary objective already succeeded, the skill can recommend keeping the take, fixing it in post, or editing one layer instead of regenerating the entire shot.

## Prompt linter

The bundled linter performs deterministic structural checks. It does not predict visual quality, call Seedance, or guarantee that a platform will bind references correctly.

Run it on a prompt file:

```bash
python3 seedance-25/scripts/lint_prompt.py prompt.txt --mode auto --duration 30
```

Pipe a draft through standard input:

```bash
printf '%s\n' '@Video 1 is the source. Extend forward from the observed last frame...' \
  | python3 seedance-25/scripts/lint_prompt.py - --mode extend
```

Produce machine-readable output:

```bash
python3 seedance-25/scripts/lint_prompt.py prompt.txt --mode edit --json
```

Supported explicit modes are `base`, `reference`, `long`, `edit`, `extend`, `first-last`, `keyframes`, `storyboard`, `blockout`, and `transition`. `auto` infers the most likely mode.

The linter checks for risks including:

- a planned direct-generation duration above 30 seconds;
- invalid, overlapping, gapped, or out-of-duration time ranges;
- several references without roles or exclusions;
- edits without a sole master, narrow scope, or preservation list;
- extensions without an observed boundary state or continuity locks;
- incomplete first/last-frame definitions;
- unordered keyframes;
- storyboards without a reading order or line-art exclusions;
- unclassified blockouts or missing inheritance rules;
- transitions without two clips, a trigger, or an arrival state;
- long prompts without stages or visible end states;
- generic style-booster overload;
- contradictory audio instructions.

Errors cause a non-zero exit code. Warnings and information notes are review signals.

Run the bundled self-test:

```bash
python3 seedance-25/scripts/lint_prompt.py --self-test
```

## Installation

### Option A — personal Codex skill

```bash
git clone git@github.com:sjinn-ai/seedance2.5-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R seedance2.5-skills/seedance-25 "${CODEX_HOME:-$HOME/.codex}/skills/seedance-25"
```

Restart or refresh the client after installation if it does not detect new skills automatically.

### Option B — project-local skill

From the project that should use the skill:

```bash
mkdir -p .agents/skills
cp -R /path/to/seedance2.5-skills/seedance-25 .agents/skills/seedance-25
```

Use the location required by your agent client if it differs. The runtime skill is self-contained inside `seedance-25/`; the repository-level `assets/` directory is only for this README.

## Using the skill

Invoke it by name and provide the brief plus any available asset descriptions:

```text
$seedance-25 Create a 30-second Seedance 2.5 prompt for a two-character chase.
Use @Image 1 for Character A's identity, @Image 2 for Character B's identity,
@Video 1 only for the motorcycle motion, and @Audio 1 for rain ambience.
Keep the red bag with Character A throughout. End on both characters under the station clock.
```

Diagnostic example:

```text
$seedance-25 Diagnose this failed extension. The new segment duplicates the actor,
repeats the door opening, and reverses the camera direction. Return one changed
variable and a conservative repaired prompt.
```

The skill responds in the user’s requested output language, but all bundled skill instructions and documentation remain in English.

## Repository structure

```text
seedance2.5-skills/
├── README.md
├── README.zh-CN.md
├── README.ja.md
├── assets/
│   ├── reference-role-map.svg
│   ├── seedance-25-hero.png
│   └── skill-workflow.svg
└── seedance-25/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── capabilities-and-limits.md
    │   ├── quality-and-repair.md
    │   └── task-patterns.md
    └── scripts/
        └── lint_prompt.py
```

### Skill map

| File | Responsibility |
|---|---|
| `seedance-25/SKILL.md` | Entry point, truth boundary, mode router, directing workflow, output contract, and safety |
| `capabilities-and-limits.md` | Verified Dreamina 2.5 values, task-specific locked settings, limitations, and factual-claim rules |
| `task-patterns.md` | Mode-specific prompt patterns for generation, references, long video, edit, extension, endpoints, storyboards, blockouts, transitions, audio, performance, and camera |
| `quality-and-repair.md` | Take triage, one-variable retries, symptom diagnosis, continuity repair, and take logs |
| `lint_prompt.py` | English/Chinese-aware heuristic checks for common structural prompt risks |
| `agents/openai.yaml` | Agent-facing display name, description, and default invocation prompt |

## Validation

Validate the skill structure when the Codex `skill-creator` package is installed:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" seedance-25
```

Run the linter regression test:

```bash
python3 seedance-25/scripts/lint_prompt.py --self-test
```

The repository is designed to validate without network access. Live browsing is still required before making time-sensitive claims about APIs, pricing, regions, quotas, or availability.

## Current status and boundaries

| Component | Status | Boundary |
|---|---|---|
| Core skill workflow | Ready | Produces prompts and production plans; it does not call a video-generation service |
| Reference library | Ready | Based on the official guides and production methods described below |
| Prompt linter | Ready, heuristic | Detects structure risks; it does not score aesthetics or model compliance |
| README visuals | Ready | Explanatory artwork only; not generated Seedance output samples |
| API integration | Not included | Surface-specific APIs require separate, current verification |

This repository does not claim access to Seedance 2.5, guarantee a generation result, or treat a client’s uploaded media as proof of rights. Real-person likenesses, voices, brands, music, and protected characters should be used only with appropriate authorization or replaced by an original equivalent.

## Official source boundary

The Seedance 2.5 capability facts in this repository are grounded in:

- [Dreamina Seedance 2.5 User Guide](https://bytedance.larkoffice.com/wiki/NjnWwvf4BiFYFLk2RzrcEgaunGf)
- [Dreamina Seedance 2.5 Prompt Guide](https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh)

The official pages were browser-compared with the user-provided copied text on August 3, 2026. The textual table of contents and body were complete. Embedded images, finished videos, and some visual comparisons were absent from the copied material, so this repository does not describe those example results as visually verified.

The workflow design also learned from the MIT-licensed [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0), especially its mode routing, reference contracts, continuity truth, and one-variable retake method. Only the official 2.5 sources above are used for Seedance 2.5 capability and numeric claims.

## Design standard

A strong prompt produced by this skill should be:

- **Bound** — every important asset, character, product, prop, and line has an owner.
- **Observable** — actions, emotions, light, sound, and endpoints can be seen or heard.
- **Continuous** — identity, geometry, ownership, geography, screen direction, camera phase, and audio state remain coherent.
- **Scoped** — edits change one layer; extensions inherit one real boundary; stages carry one primary state change.
- **Reviewable** — the team can identify what succeeded, what failed, and what single variable to change next.
- **Truthful** — platform facts remain within verified official evidence and the active surface.

The governing idea is simple:

> References define authority. Direction defines change. Accepted footage defines truth.

## Credits

- Official Dreamina Seedance 2.5 documentation for capability and workflow facts.
- [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) for the high-quality open-source reference architecture that informed this repository’s organization and production reasoning.
