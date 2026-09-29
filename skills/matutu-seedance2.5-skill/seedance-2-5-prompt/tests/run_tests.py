#!/usr/bin/env python3
"""Structural smoke test for the Seedance skill.

Checks:
1. Workflows, schemas, templates and tests referenced by SKILL.md exist.
2. Every local schema is valid JSON and fixtures validate against the local
   schema registry (including cross-schema $ref).
3. Every test result keeps the full prompt section order, covers the requested
   duration continuously and ends with a READY QA status.
4. The root-level convenience template stays in sync with references/template.md.
"""

import json
import re
import sys
from pathlib import Path

try:
    import jsonschema
    from referencing import Registry, Resource
    HAS_SCHEMA_LIBS = True
except ImportError:
    HAS_SCHEMA_LIBS = False


SKILL = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL.parent
REQUIRED_WORKFLOWS = [
    "main-pipeline",
    "input-analysis",
    "product-analysis",
    "video-objective",
    "creative-structure",
    "hook-engine",
    "storyboard",
    "shot-feasibility",
    "camera",
    "sound-design",
    "continuity",
    "product-multi-view",
    "reference-video-analysis",
    "human-realism",
    "prompt-compiler",
    "prompt-qa",
    "client-learning",
]
REQUIRED_SCHEMAS = [
    "video-project.schema.json",
    "subject-lock.schema.json",
    "storyboard.schema.json",
    "dialogue.schema.json",
    "human-realism.schema.json",
    "reference-intelligence.schema.json",
    "reference-role.schema.json",
    "reference-lock.schema.json",
    "reference-conflict.schema.json",
]
REQUIRED_TEMPLATES = [
    "product-video",
    "ugc-video",
    "product-demo",
    "story-ad",
    "shot-by-shot",
    "human-realism-template",
    "client-card-template",
]
REQUIRED_TESTS = [
    "product-video",
    "multi-view-product",
    "character-product",
    "dialogue-video",
    "reference-video",
    "prompt-optimization",
    "industrial-product",
]
PROMPT_SECTIONS = [
    "规格",
    "导演意图",
    "参考素材职责",
    "产品锁",
    "人物锁",
    "人物真实感",
    "场景锁",
    "口播台词表｜逐字锁定",
    "时间轴",
    "摄影",
    "光线",
    "声音",
    "连续性",
    "负面约束",
    "结尾状态",
]
OPTIONAL_SECTIONS = {"产品锁", "人物锁", "人物真实感", "口播台词表｜逐字锁定"}
CONDITIONAL_TEMPLATE_SECTIONS = {
    "产品锁",
    "人物锁",
    "人物真实感",
    "口播台词表｜逐字锁定",
}
SECTION_PATTERN = re.compile(r"【([^】]+)】")
FINAL_PROMPT_PATTERN = re.compile(r"## Final Prompt(.*?)## QA", re.DOTALL)


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def schema_registry(schema_dir):
    """Register all local schemas by $id so cross-schema $ref resolves locally."""
    registry = Registry()
    for path in sorted(schema_dir.glob("*.schema.json")):
        resource = Resource.from_contents(load_json(path))
        if resource.id():
            registry = registry.with_resource(resource.id(), resource)
    return registry


def validate_fixture(fixture_path, registry, failures):
    schema_path = SKILL / "schemas" / "video-project.schema.json"
    schema = load_json(schema_path)
    try:
        jsonschema.validate(
            load_json(fixture_path),
            schema,
            registry=registry,
            format_checker=jsonschema.FormatChecker(),
        )
        print(f"[PASS] fixture {fixture_path.name} validates against video-project schema")
    except (jsonschema.SchemaError, jsonschema.ValidationError, jsonschema.RefResolutionError) as exc:
        print(f"[FAIL] fixture {fixture_path.name} validation: {exc.message}")
        failures.append(f"fixture {fixture_path.name} validation")


def ordered_sections(text):
    return SECTION_PATTERN.findall(text)


def check_result(name, result, failures):
    text = result.read_text(encoding="utf-8")
    sections = ordered_sections(text)
    present = {section for section in PROMPT_SECTIONS if f"【{section}】" in text}
    required = set(PROMPT_SECTIONS) - OPTIONAL_SECTIONS
    missing = required - present
    if missing:
        print(f"[FAIL] result {name}.md missing sections: {', '.join(sorted(missing))}")
        failures.append(f"result {name}.md sections")

    prompt_order = [s for s in sections if s in PROMPT_SECTIONS]
    expected_order = [s for s in PROMPT_SECTIONS if s in present]
    if prompt_order != expected_order:
        print(f"[FAIL] result {name}.md section order diverges from template")
        failures.append(f"result {name}.md section order")
    else:
        print(f"[PASS] result {name}.md contains {len(prompt_order)} prompt sections in order")

    spec_match = re.search(r"(\d+(?:\.\d+)?)\s*秒", text)
    duration = float(spec_match.group(1)) if spec_match else None
    start_times = [
        float(m.group(1))
        for m in re.finditer(r"^\s*(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)秒", text, re.M)
    ]
    end_times = [
        float(m.group(2))
        for m in re.finditer(r"^\s*(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)秒", text, re.M)
    ]
    if duration is None:
        print(f"[FAIL] result {name}.md has no total duration in spec")
        failures.append(f"result {name}.md duration")
    elif start_times:
        first_start = min(start_times)
        last_end = max(end_times)
        gaps = [
            (end_times[i], start_times[i + 1])
            for i in range(len(start_times) - 1)
            if abs(end_times[i] - start_times[i + 1]) > 0.01
        ]
        if first_start != 0 or last_end < duration - 0.05 or gaps:
            print(
                f"[FAIL] result {name}.md timeline not continuous to {duration}s "
                f"(first={first_start}, last_end={last_end}, gaps={gaps})"
            )
            failures.append(f"result {name}.md timeline")
        else:
            print(f"[PASS] result {name}.md timeline is continuous from 0 to {duration}s")

    final_match = FINAL_PROMPT_PATTERN.search(text)
    if not final_match:
        print(f"[FAIL] result {name}.md has no ## Final Prompt before ## QA")
        failures.append(f"result {name}.md final prompt")
    if not re.search(r"Status:\s*`?READY`?", text):
        print(f"[FAIL] result {name}.md has no explicit READY status in QA")
        failures.append(f"result {name}.md ready")
    else:
        print(f"[PASS] result {name}.md has Final Prompt + READY")


def check(condition, message, failures):
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {message}")
    if not condition:
        failures.append(message)


def check_human_realism_fixture(fixture, failures):
    name = fixture.name
    data = load_json(fixture)
    hr = data.get("human_realism", {})
    enabled = hr.get("enabled")
    character_present = hr.get("character_present")
    if "no-character" in name:
        check(
            enabled is False and character_present is False and hr.get("skip_reason") == "NO_CHARACTER",
            f"human realism {name} skips with NO_CHARACTER",
            failures,
        )
        check(
            data.get("qa", {}).get("checks", {}).get("HUMAN_REALISM") == "SKIP",
            f"human realism {name} QA marks HUMAN_REALISM SKIP",
            failures,
        )
        return

    check(
        enabled is True and character_present is True and bool(hr.get("character_ids")),
        f"human realism {name} is enabled with character ids",
        failures,
    )
    modules = hr.get("routing", {}).get("modules", [])
    if not modules:
        print(f"[FAIL] human realism {name} has empty routing.modules")
        failures.append(f"human realism {name} routing.modules")
    if any(tag in name for tag in ("talking-head", "static-portrait", "close-up", "product-interaction")):
        gait_tokens = [m for m in modules if "gait" in m.lower() or m == "foot_placement" or m == "pelvic_movement"]
        check(
            not gait_tokens,
            f"human realism {name} keeps gait/foot/pelvic out of non-walking modules",
            failures,
        )
    if any(tag in name for tag in ("walking", "full-body", "long-shot")):
        check(
            any("body" in m or "biomechanics" in m for m in modules),
            f"human realism {name} loads body biomechanics for body movement",
            failures,
        )
    score = hr.get("score") or {}
    total = score.get("total")
    if total is not None:
        check(
            0 <= total <= 100 and score.get("level") in {
                "CINEMA REALISM",
                "COMMERCIAL REALISM",
                "ACCEPTABLE",
                "AI ARTIFACT RISK",
                "REGENERATE",
                "SKIPPED",
            },
            f"human realism {name} has bounded risk score and level",
            failures,
        )


def check_reference_fixture(fixture, failures):
    """Semantic checks for V3 Reference Intelligence fixtures."""
    name = fixture.name
    data = load_json(fixture)
    ri = data.get("reference_intelligence", {})
    refs = ri.get("references") or []
    roles = {ref.get("role") for ref in refs}
    derived_locks = ri.get("derived_locks") or {}
    check(bool(ri) and refs, f"reference {name} contains a REFERENCE SPEC", failures)

    if "reference-character" in name:
        check(
            "CHARACTER_IDENTITY" in roles
            and bool((derived_locks.get("character_lock") or {}).get("identity")),
            f"reference {name} produces CHARACTER_IDENTITY and identity lock",
            failures,
        )
    if "reference-product" in name:
        check(
            "PRODUCT_IDENTITY" in roles
            and bool((derived_locks.get("product_lock") or {}).get("identity")),
            f"reference {name} produces PRODUCT_IDENTITY and product lock",
            failures,
        )
        check(
            derived_locks.get("product_lock", {}).get("allowed_transformations") is False,
            f"reference {name} keeps product transformations disabled by default",
            failures,
        )
    if "reference-multi-image" in name:
        check(
            {"CHARACTER_IDENTITY", "PRODUCT_IDENTITY", "SCENE"} <= roles,
            f"reference {name} detects character, product and scene roles",
            failures,
        )
        required_locks = ["character_lock", "product_lock", "scene_lock"]
        check(
            all(bool(derived_locks.get(key)) for key in required_locks),
            f"reference {name} produces three derived locks",
            failures,
        )
    if "reference-conflict" in name:
        conflicts = ri.get("conflicts") or []
        check(
            len(conflicts) >= 1 and conflicts[0].get("winner") and conflicts[0].get("resolved") is True,
            f"reference {name} detects and resolves a conflict",
            failures,
        )
    if "reference-video" in name:
        check(
            bool({"MOTION", "ACTION", "CAMERA_MOTION", "TIMING"} & roles)
            and bool((derived_locks.get("motion_lock") or {}).get("subject_motion"))
            and bool((derived_locks.get("camera_lock") or {}).get("camera_motion")),
            f"reference {name} extracts motion, camera motion and timing evidence",
            failures,
        )
    if "reference-no-character" in name:
        hr = data.get("human_realism", {})
        check(
            hr.get("enabled") is False
            and hr.get("character_present") is False
            and hr.get("skip_reason") == "NO_CHARACTER",
            f"reference {name} skips human realism with NO_CHARACTER",
            failures,
        )

    qa = ri.get("reference_qa") or {}
    check(bool(qa), f"reference {name} has Reference QA", failures)
    check(qa.get("status") in {"PASS", "INCOMPLETE", "REPAIR"}, f"reference {name} has valid QA", failures)
    score = ri.get("reference_score") or {}
    check(bool(score), f"reference {name} has Reference Intelligence Score", failures)
    expected_keys = {
        "role_accuracy",
        "feature_extraction",
        "priority_accuracy",
        "conflict_resolution",
        "lock_completeness",
        "prompt_mapping",
    }
    check(expected_keys <= set(score), f"reference {name} has six-part score", failures)
    total = score.get("total")
    check(total == 100, f"reference {name} score totals 100", failures)


def main():
    failures = []

    if not HAS_SCHEMA_LIBS:
        print("[SKIP] jsonschema/referencing not installed; fixture validation skipped")

    for name in REQUIRED_WORKFLOWS:
        check((SKILL / "workflows" / f"{name}.md").exists(), f"workflow {name}.md exists", failures)

    for name in REQUIRED_SCHEMAS:
        path = SKILL / "schemas" / name
        exists = path.exists()
        check(exists, f"schema {name} exists", failures)
        if exists:
            try:
                load_json(path)
                print(f"[PASS] schema {name} is valid JSON")
            except json.JSONDecodeError as exc:
                print(f"[FAIL] schema {name} is invalid JSON: {exc}")
                failures.append(f"schema {name} JSON")

    for name in REQUIRED_TEMPLATES:
        check((SKILL / "templates" / f"{name}.md").exists(), f"template {name}.md exists", failures)

    check((SKILL / "QUICK-START.md").exists(), "QUICK-START.md exists", failures)
    check(
        (SKILL / "references" / "quick-reference.md").exists(),
        "quick-reference.md exists",
        failures,
    )
    check(
        (SKILL / "references" / "learning-path.md").exists(),
        "learning-path.md exists",
        failures,
    )
    template_text = (SKILL / "references" / "template.md").read_text(encoding="utf-8")
    check(
        "REFERENCE DECISION" in template_text and "PROMPT USAGE MAP" in template_text,
        "template requires reference decision and prompt usage map",
        failures,
    )
    compiler_text = (SKILL / "workflows" / "prompt-compiler.md").read_text(encoding="utf-8")
    check(
        "未绑定到实际输出位置的参考素材视为 `Prompt Mapping = MISSING`" in compiler_text,
        "prompt compiler enforces reference-to-shot mapping",
        failures,
    )

    human_modules = sorted((SKILL / "human-realism").glob("*.md"))
    check(bool(human_modules), "human-realism knowledge module directory is populated", failures)
    for module in human_modules:
        check(module.stat().st_size > 0, f"human-realism module {module.name} is non-empty", failures)

    for name in REQUIRED_TESTS:
        check((SKILL / "tests" / f"{name}.md").exists(), f"test {name}.md exists", failures)
        result = SKILL / "tests" / "results" / f"{name}.md"
        if result.exists():
            check_result(name, result, failures)
        else:
            print(f"[FAIL] result {name}.md missing")
            failures.append(f"result {name}.md")

    template = SKILL / "references" / "template.md"
    text = template.read_text(encoding="utf-8")
    template_sections = {s for s in ordered_sections(text) if s in PROMPT_SECTIONS}
    template_required = set(PROMPT_SECTIONS) - CONDITIONAL_TEMPLATE_SECTIONS
    missing_template = template_required - template_sections
    check(
        not missing_template,
        f"template has core sections ({', '.join(sorted(missing_template)) or 'all'})",
        failures,
    )

    root_template = REPO_ROOT / "seedance-2.5-prompt-template.md"
    check(
        root_template.exists() and root_template.read_text(encoding="utf-8") == text,
        "root template stays in sync with references/template.md",
        failures,
    )

    fixture_dir = SKILL / "tests" / "fixtures"
    fixtures = sorted(fixture_dir.glob("video-project.*.json"))
    reference_fixture_dirs = sorted(fixture_dir.glob("reference-*"))
    for reference_dir in reference_fixture_dirs:
        fixtures.extend(sorted(reference_dir.glob("video-project.*.json")))
    fixtures = sorted(fixtures)
    check(bool(fixtures), "tests/fixtures contains video-project fixtures", failures)
    human_fixtures = [f for f in fixtures if "human-realism" in f.name]
    check(len(human_fixtures) >= 11, "tests/fixtures contains 11 human realism fixtures", failures)
    reference_fixtures = [
        f
        for f in fixtures
        if any(d.name.startswith("reference-") for d in f.parents)
        or "reference-" in f.name
    ]
    check(
        len(reference_fixtures) >= 6,
        "tests/fixtures contains V3 reference fixtures",
        failures,
    )
    if HAS_SCHEMA_LIBS and fixtures:
        registry = schema_registry(SKILL / "schemas")
        for fixture in fixtures:
            validate_fixture(fixture, registry, failures)
    for fixture in human_fixtures:
        check_human_realism_fixture(fixture, failures)
    for fixture in reference_fixtures:
        check_reference_fixture(fixture, failures)

    skill_md = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    check(skill_md.startswith("---"), "SKILL.md has frontmatter", failures)
    check("workflows/main-pipeline.md" in skill_md, "SKILL.md routes to main pipeline", failures)
    check("workflows/human-realism.md" in skill_md, "SKILL.md routes to human realism workflow", failures)
    check("human-realism.schema.json" in skill_md, "SKILL.md exposes human realism schema", failures)
    check("QUICK-START.md" in skill_md, "SKILL.md routes to QUICK-START", failures)
    check(
        "references/quick-reference.md" in skill_md,
        "SKILL.md routes to quick-reference",
        failures,
    )
    check("references/learning-path.md" in skill_md, "SKILL.md routes to learning-path", failures)

    quick_md = (SKILL / "QUICK-START.md").read_text(encoding="utf-8")
    check("references/quick-reference.md" in quick_md, "QUICK-START links quick-reference", failures)
    check("references/checklist.md" in quick_md, "QUICK-START links checklist", failures)
    check("../seedance-2.5-prompt-template.md" in quick_md, "QUICK-START links root template", failures)
    check("references/learning-path.md" in quick_md, "QUICK-START routes learning to learning-path", failures)
    check("我已跑满学习轮次表" in quick_md, "QUICK-START keeps learning completion trigger", failures)

    learning_md = (SKILL / "references" / "learning-path.md").read_text(encoding="utf-8")
    check("## 轮次表" in learning_md, "learning-path has round table", failures)
    check(
        "| 1 | 回放诊断 |" in learning_md and "| 8 | QA 门禁 |" in learning_md,
        "learning-path round table covers 1-8",
        failures,
    )
    check("本轮练习" in learning_md, "learning-path accepts round practice trigger", failures)
    check("我已跑满学习轮次表" in learning_md, "learning-path has completion trigger", failures)

    check(
        "workflows/client-learning.md" in skill_md,
        "SKILL.md routes to client learning workflow",
        failures,
    )
    check(
        "templates/client-card-template.md" in skill_md,
        "SKILL.md exposes client card template",
        failures,
    )
    check(
        "workflows/client-learning.md" in quick_md,
        "QUICK-START routes to client learning",
        failures,
    )
    client_md = (SKILL / "workflows" / "client-learning.md").read_text(encoding="utf-8")
    check(
        "templates/client-card-template.md" in client_md,
        "client-learning routes to client card template",
        failures,
    )
    card_md = (SKILL / "templates" / "client-card-template.md").read_text(encoding="utf-8")
    check(
        "CLIENT_ID" in card_md and "## 7. 变更记录" in card_md,
        "client card template keeps bounded card structure",
        failures,
    )

    if failures:
        print(f"\n{len(failures)} check(s) failed")
        return 1
    print("\nAll structural checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
