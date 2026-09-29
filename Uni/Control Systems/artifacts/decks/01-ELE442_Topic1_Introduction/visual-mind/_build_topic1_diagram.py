"""One-shot builder: Topic 1 diagram.json for visual-mind reload."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

out_dir = Path(__file__).resolve().parent
shapes: list[dict] = []


def T(id: str, x: float, y: float, text: str, size: str = "m", color: str = "orange"):
    shapes.append(
        {"type": "text", "id": id, "x": x, "y": y, "text": text, "size": size, "color": color}
    )


def G(
    id: str,
    x: float,
    y: float,
    w: float,
    h: float,
    text: str,
    geo: str = "rectangle",
    color: str = "orange",
    fill: str = "semi",
    size: str = "m",
):
    shapes.append(
        {
            "type": "geo",
            "id": id,
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "geo": geo,
            "text": text,
            "color": color,
            "fill": fill,
            "size": size,
        }
    )


def A(fid: str, tid: str, text: str = "", color: str = "orange"):
    shapes.append({"type": "arrow", "fromId": fid, "toId": tid, "text": text, "color": color})


T("title", 80, 40, "ELE442 Topic 1 COMPLETE @ PPT abstraction", "l")
T("src", 80, 100, "Bound to ELE442_Topic1_Introduction.pptx only — no Topic 2 depth yet", "s", "grey")

T("tbl-h", 80, 200, "A. DEFINITIONS TABLE", "l")
G("th1", 80, 280, 280, 70, "Term", color="grey", fill="solid")
G("th2", 360, 280, 900, 70, "Definition (from Topic 1 PPT)", color="grey", fill="solid")
G("th3", 1260, 280, 160, 70, "Slide", color="grey", fill="solid")

rows = [
    ("r1", "Control", "Make a system (process or plant) behave as we desire", "s002", "orange"),
    ("r2", "Plant / Process", "The system being controlled", "s002,s007", "orange"),
    (
        "r3",
        "Open-Loop",
        "Actuator controlled without feedback · no sensors · sensitive to disturbances · needs calibration",
        "s006",
        "orange",
    ),
    (
        "r4",
        "Closed-Loop",
        "Controller acts on error between desired & actual output · actual output via sensors",
        "s009",
        "green",
    ),
    ("r5", "Error", "Desired output − actual (measured) output", "s009", "green"),
    ("r6", "Controller", "Produces the command (Amplifier in DC-motor figs)", "s008–10", "orange"),
    ("r7", "Actuator", "Applies action to the process (DC motor)", "s006,s008", "orange"),
    (
        "r8",
        "Sensor",
        "Measures actual output (Tachometer → voltage). Missing in open-loop.",
        "s006,s010",
        "green",
    ),
    ("r9", "Feedback", "Return path of measured output to the comparison", "s010", "green"),
]
y = 350
for rid, term, defn, slide, col in rows:
    G(f"{rid}a", 80, y, 280, 90, term, color=col)
    G(f"{rid}b", 360, y, 900, 90, defn, color=col)
    G(f"{rid}c", 1260, y, 160, 90, slide, color=col)
    y += 90

T("b-h", 80, 1280, "B. WHAT / WHY / FIELD (s002–s004)", "l")
G(
    "b-ctrl",
    80,
    1380,
    520,
    220,
    "What is controlled? (s002 examples)\n• Airconditioning — room temperature\n• Cars/drones — trajectory/speed\n• CNC machines — position\n• Human body — temperature / blood pressure\nAlmost all systems involve one form of control",
)
G(
    "b-why",
    660,
    1380,
    520,
    220,
    "Why needed? (s004)\n• Convenience (everyday appliances)\n• Dangerous tasks (space, mine clearance)\n• Impossible for humans (nanometer precision)\n• Industrial scale (car-painting, production lines)",
)
G(
    "b-theory",
    1240,
    1380,
    520,
    220,
    "What is Control Theory? (s003)\nPPT shows a big field map (methods,\nplanning, estimation, modeling, analysis).\nAt Topic 1 level: know the field is large.\nThis course walks Modeling → Analysis → Design\n(named on s012–s013) — not the whole map.",
    color="grey",
)

T("c-h", 80, 1720, "C. TWO TYPES (s005) + OPEN-LOOP (s006–s008)", "l")
G("c-types", 80, 1820, 400, 100, "Types (s005): Open-Loop  |  Closed-Loop")

T("ol-gen", 80, 1980, "Generic open-loop (Pearson fig, s006)")
G("ol-in", 80, 2060, 220, 120, "Desired\noutput response")
G("ol-c", 400, 2060, 200, 120, "Controller")
G("ol-a", 700, 2060, 200, 120, "Actuator")
G("ol-p", 1000, 2060, 200, 120, "Process")
G("ol-o", 1300, 2060, 180, 120, "Output")
for a, b in [("ol-in", "ol-c"), ("ol-c", "ol-a"), ("ol-a", "ol-p"), ("ol-p", "ol-o")]:
    A(a, b)

T("ol-lau", 80, 2280, "Laundry example (s007) — PPT labels")
G("lau1", 80, 2360, 280, 120, "Washing Program\n(predetermined settings)")
G("lau2", 460, 2360, 320, 120, "Laundry Machine\n(Plant / Process)")
G("lau3", 880, 2360, 280, 120, "Washed Clothes")
G("lau-n", 1260, 2360, 400, 120, "No measurement of\nclothes cleanliness", geo="cloud", color="red")
A("lau1", "lau2")
A("lau2", "lau3")

T("ol-dc", 80, 2600, "DC motor OPEN (s008 · image6)")
G("od1", 80, 2680, 240, 130, "Desired speed\n(voltage)\n← speed setting pot")
G("od2", 400, 2680, 220, 130, "Controller\nAmplifier")
G("od3", 700, 2680, 220, 130, "Actuator\nDC motor")
G("od4", 1000, 2680, 240, 130, "Process\nRotating disk")
G("od5", 1320, 2680, 200, 130, "Actual speed")
G("od-n", 1600, 2680, 220, 130, "No tachometer\nreturn", geo="cloud", color="red")
for a, b in [("od1", "od2"), ("od2", "od3"), ("od3", "od4"), ("od4", "od5")]:
    A(a, b)

T("d-h", 80, 2960, "D. CLOSED-LOOP (s009–s011)", "l")
T("cl-gen", 80, 3040, "Generic closed-loop (Pearson fig, s009)")
G("cl-in", 80, 3120, 200, 120, "Desired\noutput response")
G("cl-sum", 360, 3120, 140, 120, "Σ\n+ / −", geo="ellipse")
G("cl-err", 580, 3120, 150, 120, "Error")
G("cl-c", 820, 3120, 180, 120, "Controller")
G("cl-a", 1080, 3120, 180, 120, "Actuator")
G("cl-p", 1340, 3120, 180, 120, "Process")
G("cl-o", 1600, 3120, 180, 120, "Actual\noutput")
G("cl-s", 1340, 3360, 240, 120, "Sensor\n→ measurement", color="green")
for a, b in [
    ("cl-in", "cl-sum"),
    ("cl-sum", "cl-err"),
    ("cl-err", "cl-c"),
    ("cl-c", "cl-a"),
    ("cl-a", "cl-p"),
    ("cl-p", "cl-o"),
]:
    A(a, b)
A("cl-o", "cl-s", "feedback", "green")
A("cl-s", "cl-sum", "−", "green")

T("cl-dc", 80, 3620, "DC motor CLOSED (s010 · image7) — same plant, add feedback")
G("cd1", 80, 3700, 200, 120, "Desired speed\n(voltage)")
G("cd-sum", 340, 3700, 120, 120, "Σ\n+ / −", geo="ellipse")
G("cd-err", 520, 3700, 130, 120, "Error")
G("cd2", 720, 3700, 180, 120, "Controller\nAmplifier")
G("cd3", 970, 3700, 180, 120, "Actuator\nDC motor")
G("cd4", 1220, 3700, 200, 120, "Process\nRotating disk")
G("cd5", 1500, 3700, 180, 120, "Actual speed")
G("cd-s", 1220, 3940, 260, 120, "Sensor\nTachometer\n→ measured speed (V)", color="green")
for a, b in [
    ("cd1", "cd-sum"),
    ("cd-sum", "cd-err"),
    ("cd-err", "cd2"),
    ("cd2", "cd3"),
    ("cd3", "cd4"),
    ("cd4", "cd5"),
]:
    A(a, b)
A("cd5", "cd-s", "feedback", "green")
A("cd-s", "cd-sum", "−", "green")

G(
    "micro",
    80,
    4180,
    700,
    140,
    "Closed-loop example — Microsurgical instruments (s011)\nPosition control · Translation accuracy ~ 0.1 mm · Rotation accuracy ~ 0.1°\n(why closed-loop precision matters — PPT level only)",
    color="green",
)

T("e-h", 80, 4440, "E. CONTROLLER DESIGN PROCESS — course menu (s012–s013)", "l")
T("e-note", 80, 4520, "Topic 1 only NAMES these. Do not solve them yet.", "s", "grey")
G(
    "d1",
    80,
    4600,
    380,
    200,
    "1. Modeling\nTransfer Function & Block Diagram\nLaplace Transform\nMechanical, electrical,\nelectromechanical systems",
)
G(
    "d2",
    540,
    4600,
    380,
    200,
    "2. Analysis\nStep / frequency / ramp response\nStability:\nRouth-Hurwitz criterion",
)
G(
    "d3",
    1000,
    4600,
    380,
    200,
    "3. Design\nRoot locus\nFrequency response\nPID control\nLead/lag compensator",
)
G("d4", 1460, 4600, 280, 200, "4. Implementation\n(build / run)")
A("d1", "d2")
A("d2", "d3")
A("d3", "d4")

G(
    "done",
    80,
    4920,
    1660,
    120,
    'TOPIC 1 DONE CRITERIA @ PPT level: you can (1) define the table terms, (2) draw OL vs CL chains, (3) map laundry + DC motor examples to those chains, (4) list why-control + design-process names without deriving them.\nSay "done" if that matches — next is Topic 2 (Mathematical Models / Laplace) at THAT deck\'s abstraction.',
    color="green",
)

G(
    "rule-lock",
    1800,
    40,
    520,
    160,
    "RULE LOCKED 2026-09-20\n\n/visual-mind active →\nDRAW the explanation\nchat = status only (≤ few lines)\n\nNever: long chat walkthroughs",
    color="red",
)

qx = 2100
T("q-title", qx, 200, "TOPIC 1 — mastery question bank (PPT abstraction only)", "l")
T(
    "q-sub",
    qx,
    260,
    "Pass = answer from memory + rebuild the diagrams without looking",
    "s",
    "grey",
)
G("qA-h", qx, 340, 700, 60, "A. KNOW (say it clean)", color="grey", fill="solid")
G(
    "qA",
    qx,
    400,
    700,
    420,
    'A1. What is control? (s002 one-liner)\nA2. What does plant/process mean?\nA3. Define open-loop in PPT words (s006).\nA4. Define closed-loop in PPT words (s009).\nA5. What is error?\nA6. What does "no feedback means no sensors" imply?\nA7. Name controller / actuator / sensor roles.\nA8. What is feedback (one sentence)?',
)
G("qB-h", qx, 860, 700, 60, "B. MEMORIZE (lists exact to PPT)", color="grey", fill="solid")
G(
    "qB",
    qx,
    920,
    700,
    480,
    "B1. Four s002 example domains (AC, cars/drones, CNC, body).\nB2. Four reasons control is needed (s004).\nB3. Four open-loop properties (s006):\n    no feedback · no sensors · disturbances · calibration.\nB4. Two types of control (s005).\nB5. Microsurgery numbers (s011): ~0.1 mm, ~0.1°.\nB6. Design process 4 stages (s012).\nB7. Under Modeling / Analysis / Design —\n    list the method NAMES on s013 (no solving).",
)
G("qC-h", qx, 1440, 700, 60, "C. REBUILD (blank page → draw)", color="grey", fill="solid")
G(
    "qC",
    qx,
    1500,
    700,
    520,
    'C1. Generic open-loop chain (Desired → Controller →\n    Actuator → Process → Output).\nC2. Generic closed-loop chain with Σ, Error,\n    Sensor return (−).\nC3. Laundry open-loop with PPT labels:\n    Washing Program → Laundry Machine (Plant) →\n    Washed Clothes + "no cleanliness measurement".\nC4. DC motor OPEN (s008): Desired speed(V) →\n    Amplifier → DC motor → disk → Actual speed.\nC5. DC motor CLOSED (s010): same + Tachometer\n    feedback + Error path.\nC6. Mark the ONE structural difference between C4 & C5.',
    color="green",
)
G("qD-h", qx, 2060, 700, 60, "D. COMPARE / APPLY", color="grey", fill="solid")
G(
    "qD",
    qx,
    2120,
    700,
    420,
    "D1. Why is laundry open-loop? (no cleanliness sensor)\nD2. Why does a tachometer turn the motor example closed?\nD3. Disturbance hits open-loop vs closed-loop —\n    what changes? (PPT level: sensitive vs corrects via error)\nD4. Pick: toaster timer vs room thermostat —\n    which is OL / CL and why?\nD5. Why does microsurgery need closed-loop? (precision)\nD6. s003 map: what do you claim at Topic 1 depth?\n    (field is large; course follows Modeling→Design names)",
    color="green",
)
G("qE-h", qx, 2580, 700, 60, "E. SELF-CHECK (full comprehension)", color="grey", fill="solid")
G(
    "qE",
    qx,
    2640,
    700,
    320,
    "E1. Close the left canvas. Recite A + B from memory.\nE2. Redraw C1–C5 on paper in <10 min.\nE3. Answer D1–D6 out loud without notes.\nE4. If any fail → that section only (not Topic 2).\nPASS = E1–E3 clean at PPT abstraction.",
    color="red",
)
G(
    "q-link",
    qx,
    3000,
    700,
    100,
    "Sits beside Topic 1 diagram — same deck only,\nno Laplace/PID solving yet",
    geo="cloud",
    color="grey",
)

payload = {"party": "agent", "clearPage": True, "shapes": shapes}
saved_at = datetime.now(timezone.utc).isoformat()

doc = {
    "name": "Topic 1 diagram",
    "kind": "visual_mind_agent_draw",
    "savedAt": saved_at,
    "course": "ELE 442 — Control Systems",
    "topic": 1,
    "deck": "01-ELE442_Topic1_Introduction",
    "source_pptx": "ELE442_Topic1_Introduction.pptx",
    "board": "http://127.0.0.1:5173/",
    "abstraction": "PPT Topic 1 only",
    "contents": [
        "Definitions table",
        "What/Why/Field",
        "Open-loop + laundry + DC open",
        "Closed-loop + DC closed + microsurgery",
        "Design process menu (names only)",
        "Mastery question bank A–E",
    ],
    "reload": {
        "method": "POST",
        "url": "http://127.0.0.1:5173/api/agent-draw",
        "bodyField": "agentDrawPayload",
    },
    "agentDrawPayload": payload,
    "note": "Reloadable Visual Agent payload. For a live tldraw editor dump, use board Export learning snapshot.",
}

path = out_dir / "Topic 1 diagram.json"
path.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
(out_dir / "manifest.yaml").write_text(
    "\n".join(
        [
            'name: "Topic 1 diagram"',
            'file: "Topic 1 diagram.json"',
            f'savedAt: "{saved_at}"',
            f"shapeCount: {len(shapes)}",
            "format: visual_mind_agent_draw",
            "reload: POST http://127.0.0.1:5173/api/agent-draw with .agentDrawPayload",
            "",
        ]
    ),
    encoding="utf-8",
)
print(f"Wrote {path} ({len(shapes)} shapes)")
