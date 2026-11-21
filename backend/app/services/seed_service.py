"""
Curriculum Seed Service for Learnix AI.
Seeds:
- Class 10 Physics chapters
- 26 detailed concepts across all chapters
- 30+ concept graph edges (prerequisites & reinforcements)
- 40+ high quality curriculum questions with distractors and expected reasoning
- Demo Student ("Alex Chen") and Demo Teacher ("Dr. Sarah Jenkins") accounts
- Realistic attempts, learner models, misconceptions, revision schedules, and class analytics
"""

import datetime
from app.utils.security import hash_password
from app.utils.helpers import get_utc_now
from app.ai.misconception_database import PHYSICS_MISCONCEPTIONS
from app.services.multi_subject_curriculum import (
    SUBJECTS,
    CHEMISTRY_CHAPTERS,
    CHEMISTRY_CONCEPTS,
    BIOLOGY_CHAPTERS,
    BIOLOGY_CONCEPTS,
    MATH_CHAPTERS,
    MATH_CONCEPTS,
    MULTI_SUBJECT_RELATIONSHIPS,
    MULTI_SUBJECT_QUESTIONS,
    MULTI_SUBJECT_MISCONCEPTIONS
)
from app.services.grade_curriculum import (
    GRADES,
    CLASS_9_CHAPTERS,
    CLASS_9_CONCEPTS,
    CLASS_11_CHAPTERS,
    CLASS_11_CONCEPTS,
    CLASS_12_CHAPTERS,
    CLASS_12_CONCEPTS,
    CROSS_GRADE_RELATIONSHIPS,
    CROSS_GRADE_QUESTIONS,
    CROSS_GRADE_MISCONCEPTIONS
)

PHYSICS_CHAPTERS = [
    {
        "id": "light_reflection_refraction",
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Light – Reflection and Refraction",
        "order": 1,
        "description": "Spherical mirrors, reflection laws, Snell's law of refraction, and spherical lenses.",
        "icon": "Sun",
        "color": "from-amber-500 to-yellow-600"
    },
    {
        "id": "human_eye_colourful_world",
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Human Eye and Colourful World",
        "order": 2,
        "description": "Structure of eye, defects of vision, prism dispersion, and atmospheric refraction.",
        "icon": "Eye",
        "color": "from-cyan-500 to-blue-600"
    },
    {
        "id": "electricity",
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Electricity",
        "order": 3,
        "description": "Electric charge, potential difference, Ohm's law, series/parallel combinations, and Joule's heating.",
        "icon": "Zap",
        "color": "from-blue-500 to-indigo-600"
    },
    {
        "id": "magnetic_effects_electric_current",
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Magnetic Effects of Electric Current",
        "order": 4,
        "description": "Magnetic fields, field lines, solenoids, Fleming's rules, and electromagnetic induction.",
        "icon": "Compass",
        "color": "from-violet-500 to-purple-600"
    },
    {
        "id": "chemical_effects_electric_current",
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Chemical Effects of Electric Current",
        "order": 5,
        "description": "Conduction in liquids, electrolytes, electrolysis, and industrial electroplating.",
        "icon": "FlaskConical",
        "color": "from-emerald-500 to-teal-600"
    },
    {
        "id": "force_motion_fundamentals",
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Force and Motion Fundamentals",
        "order": 6,
        "description": "Balanced and unbalanced forces, Newton's three laws of motion, and momentum conservation.",
        "icon": "Gauge",
        "color": "from-rose-500 to-orange-600"
    }
]

CLASS_10_CHAPTERS = PHYSICS_CHAPTERS + CHEMISTRY_CHAPTERS + BIOLOGY_CHAPTERS + MATH_CHAPTERS
for ch in CLASS_10_CHAPTERS:
    if "grade" not in ch:
        ch["grade"] = 10

CHAPTERS = CLASS_9_CHAPTERS + CLASS_10_CHAPTERS + CLASS_11_CHAPTERS + CLASS_12_CHAPTERS

CONCEPTS = [
    # Light
    {
        "id": "c_spherical_mirrors",
        "chapter_id": "light_reflection_refraction",
        "name": "Spherical Mirrors & Ray Tracing",
        "description": "Concave and convex mirrors, focus, center of curvature, and ray formation rules.",
        "key_formula": "R = 2f",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 100
    },
    {
        "id": "c_mirror_formula",
        "chapter_id": "light_reflection_refraction",
        "name": "Mirror Formula & Magnification",
        "description": "Relationship between object distance (u), image distance (v), and focal length (f) with Cartesian sign conventions.",
        "key_formula": "1/f = 1/v + 1/u, m = -v/u",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 100
    },
    {
        "id": "c_refraction_snell",
        "chapter_id": "light_reflection_refraction",
        "name": "Refraction of Light & Snell's Law",
        "description": "Bending of light rays at media boundaries due to phase velocity variation.",
        "key_formula": "n21 = sin(i) / sin(r) = v1 / v2",
        "difficulty_baseline": "medium",
        "x": 100,
        "y": 240
    },
    {
        "id": "c_lenses_refraction",
        "chapter_id": "light_reflection_refraction",
        "name": "Spherical Lenses & Ray Optics",
        "description": "Convex (converging) and concave (diverging) lenses, focal points, and optical center.",
        "key_formula": "1/f = 1/v - 1/u, m = v/u",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 240
    },
    {
        "id": "c_lens_power",
        "chapter_id": "light_reflection_refraction",
        "name": "Lens Power & Optical Combinations",
        "description": "Degree of convergence or divergence of light rays expressed in Dioptres.",
        "key_formula": "P = 1/f (f in meters)",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 240
    },

    # Human Eye
    {
        "id": "c_eye_accommodation",
        "chapter_id": "human_eye_colourful_world",
        "name": "Eye Anatomy & Accommodation",
        "description": "Ciliary muscles modifying crystalline lens curvature for near (25 cm) and distant vision.",
        "key_formula": "Near point = 25 cm, Far point = infinity",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 380
    },
    {
        "id": "c_eye_defects",
        "chapter_id": "human_eye_colourful_world",
        "name": "Defects of Vision & Correction",
        "description": "Myopia (corrected by concave lens), Hypermetropia (convex lens), and Presbyopia.",
        "key_formula": "P = 1/f lens prescription",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 380
    },
    {
        "id": "c_prism_dispersion",
        "chapter_id": "human_eye_colourful_world",
        "name": "Prism Refraction & Dispersion",
        "description": "Splitting of white light into spectrum (VIBGYOR) due to wavelength-dependent refractive indices.",
        "key_formula": "Angle of deviation D = i + e - A",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 380
    },
    {
        "id": "c_light_scattering",
        "chapter_id": "human_eye_colourful_world",
        "name": "Rayleigh Scattering & Tyndall Effect",
        "description": "Wavelength-dependent scattering by atmospheric particles explaining blue sky and red sunsets.",
        "key_formula": "Intensity proportional to 1 / lambda^4",
        "difficulty_baseline": "hard",
        "x": 640,
        "y": 380
    },

    # Electricity
    {
        "id": "c_electric_current",
        "chapter_id": "electricity",
        "name": "Electric Charge & Current",
        "description": "Quantization of charge, definition of electric current, and flow of electrons.",
        "key_formula": "I = Q / t, Q = n * e",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 520
    },
    {
        "id": "c_potential_difference",
        "chapter_id": "electricity",
        "name": "Electric Potential Difference",
        "description": "Work done in moving unit positive charge between two points in an electric field.",
        "key_formula": "V = W / Q",
        "difficulty_baseline": "easy",
        "x": 280,
        "y": 520
    },
    {
        "id": "c_ohms_law",
        "chapter_id": "electricity",
        "name": "Ohm's Law & Characteristic Curves",
        "description": "Linear relationship between current and potential difference at constant temperature.",
        "key_formula": "V = I * R",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 520
    },
    {
        "id": "c_resistance_factors",
        "chapter_id": "electricity",
        "name": "Resistance & Resistivity",
        "description": "Dependence of conductor resistance on material resistivity, length, and cross-sectional area.",
        "key_formula": "R = rho * (L / A)",
        "difficulty_baseline": "medium",
        "x": 640,
        "y": 520
    },
    {
        "id": "c_series_circuits",
        "chapter_id": "electricity",
        "name": "Resistors in Series Combination",
        "description": "Single-loop circuit characteristics: uniform current and additive potential differences.",
        "key_formula": "Rs = R1 + R2 + R3",
        "difficulty_baseline": "medium",
        "x": 820,
        "y": 470
    },
    {
        "id": "c_parallel_circuits",
        "chapter_id": "electricity",
        "name": "Resistors in Parallel Combination",
        "description": "Multi-branch circuits with uniform voltage across branches and divided current.",
        "key_formula": "1 / Rp = 1/R1 + 1/R2 + 1/R3",
        "difficulty_baseline": "hard",
        "x": 820,
        "y": 570
    },
    {
        "id": "c_joule_heating",
        "chapter_id": "electricity",
        "name": "Joule's Law of Heating",
        "description": "Thermal dissipation caused by electron collisions with metal lattice ions.",
        "key_formula": "H = I^2 * R * t",
        "difficulty_baseline": "hard",
        "x": 1000,
        "y": 470
    },
    {
        "id": "c_electric_power",
        "chapter_id": "electricity",
        "name": "Electric Power & Energy Units",
        "description": "Rate of electrical energy conversion and commercial billing calculations.",
        "key_formula": "P = V * I = I^2 * R = V^2 / R",
        "difficulty_baseline": "hard",
        "x": 1000,
        "y": 570
    },

    # Magnetic Effects
    {
        "id": "c_magnetic_fields",
        "chapter_id": "magnetic_effects_electric_current",
        "name": "Magnetic Fields & Field Lines",
        "description": "Continuous closed loops of magnetic flux, direction rules, and non-intersection principle.",
        "key_formula": "B (Tesla), non-intersecting closed curves",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 700
    },
    {
        "id": "c_current_carrying_wire",
        "chapter_id": "magnetic_effects_electric_current",
        "name": "Field Due to Current-Carrying Conductor",
        "description": "Concentric magnetic field lines around straight wires and Right Hand Thumb Rule.",
        "key_formula": "Right Hand Thumb Rule: Thumb=Current, Fingers=Field",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 700
    },
    {
        "id": "c_solenoid_magnetic_field",
        "chapter_id": "magnetic_effects_electric_current",
        "name": "Magnetic Field in a Solenoid",
        "description": "Uniform parallel internal magnetic field inside helical wire coils and electromagnets.",
        "key_formula": "B = mu0 * n * I",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 700
    },
    {
        "id": "c_fleming_left_hand",
        "chapter_id": "magnetic_effects_electric_current",
        "name": "Magnetic Force & Fleming's Left-Hand Rule",
        "description": "Lorentz force on a current-carrying conductor in an external magnetic field (motor principle).",
        "key_formula": "F = B * I * L * sin(theta)",
        "difficulty_baseline": "hard",
        "x": 640,
        "y": 700
    },
    {
        "id": "c_electromagnetic_induction",
        "chapter_id": "magnetic_effects_electric_current",
        "name": "Electromagnetic Induction (EMI)",
        "description": "Inducing potential difference across conductors by changing surrounding magnetic flux.",
        "key_formula": "Fleming's Right-Hand Rule (generator principle)",
        "difficulty_baseline": "advanced",
        "x": 820,
        "y": 700
    },

    # Chemical Effects
    {
        "id": "c_electrolytic_conduction",
        "chapter_id": "chemical_effects_electric_current",
        "name": "Electrolytic Conduction in Liquids",
        "description": "Movement of positively charged cations and negatively charged anions in ionic solutions.",
        "key_formula": "Conduction via dissociated ions",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 840
    },
    {
        "id": "c_electrolysis",
        "chapter_id": "chemical_effects_electric_current",
        "name": "Electrolysis & Chemical Decomposition",
        "description": "Decomposition of chemical compounds (e.g. water into H2 and O2) driven by electric current.",
        "key_formula": "2 H2O -> 2 H2 (cathode) + O2 (anode)",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 840
    },
    {
        "id": "c_electroplating",
        "chapter_id": "chemical_effects_electric_current",
        "name": "Electroplating Mechanism & Uses",
        "description": "Depositing a desired protective or aesthetic metal layer onto another conductor.",
        "key_formula": "Anode: source metal, Cathode: object to plate",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 840
    },

    # Force & Motion
    {
        "id": "c_balanced_forces",
        "chapter_id": "force_motion_fundamentals",
        "name": "Balanced & Unbalanced Forces",
        "description": "Resultant net force concept, equilibrium state, and condition for accelerated motion.",
        "key_formula": "F_net = 0 (equilibrium)",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 980
    },
    {
        "id": "c_newtons_first_law",
        "chapter_id": "force_motion_fundamentals",
        "name": "Newton's First Law & Inertia",
        "description": "Tendency of objects to resist changes in their state of rest or uniform motion.",
        "key_formula": "Inertia is directly proportional to mass",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 980
    },
    {
        "id": "c_newtons_second_law",
        "chapter_id": "force_motion_fundamentals",
        "name": "Newton's Second Law & Momentum",
        "description": "Rate of change of momentum is directly proportional to applied unbalanced force.",
        "key_formula": "F = dp/dt = m * a",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 980
    },
    {
        "id": "c_newtons_third_law",
        "chapter_id": "force_motion_fundamentals",
        "name": "Newton's Third Law (Action-Reaction)",
        "description": "To every action there is an equal and opposite reaction acting on separate bodies.",
        "key_formula": "F_AB = - F_BA",
        "difficulty_baseline": "medium",
        "x": 640,
        "y": 980
    },
    {
        "id": "c_momentum_conservation",
        "chapter_id": "force_motion_fundamentals",
        "name": "Conservation of Linear Momentum",
        "description": "Total momentum of an isolated system remains constant in the absence of external net forces.",
        "key_formula": "m1*u1 + m2*u2 = m1*v1 + m2*v2",
        "difficulty_baseline": "advanced",
        "x": 820,
        "y": 980
    }
]

CONCEPT_RELATIONSHIPS = [
    # Light
    {"source_concept_id": "c_spherical_mirrors", "target_concept_id": "c_mirror_formula", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_refraction_snell", "target_concept_id": "c_lenses_refraction", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_lenses_refraction", "target_concept_id": "c_lens_power", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_refraction_snell", "target_concept_id": "c_prism_dispersion", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_lenses_refraction", "target_concept_id": "c_eye_defects", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_eye_accommodation", "target_concept_id": "c_eye_defects", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_prism_dispersion", "target_concept_id": "c_light_scattering", "relationship_type": "reinforces"},

    # Electricity
    {"source_concept_id": "c_electric_current", "target_concept_id": "c_potential_difference", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_potential_difference", "target_concept_id": "c_ohms_law", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_ohms_law", "target_concept_id": "c_resistance_factors", "relationship_type": "reinforces"},
    {"source_concept_id": "c_ohms_law", "target_concept_id": "c_series_circuits", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_ohms_law", "target_concept_id": "c_parallel_circuits", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_series_circuits", "target_concept_id": "c_joule_heating", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_parallel_circuits", "target_concept_id": "c_electric_power", "relationship_type": "prerequisite"},

    # Electromagnetism
    {"source_concept_id": "c_electric_current", "target_concept_id": "c_current_carrying_wire", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_magnetic_fields", "target_concept_id": "c_current_carrying_wire", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_current_carrying_wire", "target_concept_id": "c_solenoid_magnetic_field", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_current_carrying_wire", "target_concept_id": "c_fleming_left_hand", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_fleming_left_hand", "target_concept_id": "c_electromagnetic_induction", "relationship_type": "reinforces"},

    # Chemical
    {"source_concept_id": "c_electric_current", "target_concept_id": "c_electrolytic_conduction", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_electrolytic_conduction", "target_concept_id": "c_electrolysis", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_electrolysis", "target_concept_id": "c_electroplating", "relationship_type": "prerequisite"},

    # Mechanics
    {"source_concept_id": "c_balanced_forces", "target_concept_id": "c_newtons_first_law", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_newtons_first_law", "target_concept_id": "c_newtons_second_law", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_newtons_second_law", "target_concept_id": "c_newtons_third_law", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_newtons_third_law", "target_concept_id": "c_momentum_conservation", "relationship_type": "prerequisite"}
]

SEED_QUESTIONS = [
    # Electricity - Resistance factors
    {
        "id": "q_elec_rf_01",
        "chapter_id": "electricity",
        "concept_id": "c_resistance_factors",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "A cylindrical wire of length L and cross-sectional area A has resistance R. If the wire is stretched uniformly so that its length becomes 2L while its volume remains constant, what is the new resistance?",
        "options": [
            {"id": "A", "text": "2 R"},
            {"id": "B", "text": "4 R"},
            {"id": "C", "text": "R / 2"},
            {"id": "D", "text": "R / 4"}
        ],
        "correct_answer": "B",
        "explanation": "When a wire is stretched, its volume V = A * L remains constant. If length doubles (L' = 2L), its area must halve (A' = A / 2). Since R = rho * L / A, the new resistance is R' = rho * (2L) / (A / 2) = 4 * (rho * L / A) = 4R.",
        "expected_reasoning": "Conservation of volume implies area halves when length doubles; therefore resistance scales quadratically with length.",
        "distractor_explanations": {
            "A": "Considers only length doubling without accounting for area reduction.",
            "C": "Mistakenly assumes stretching wire makes it conduct better.",
            "D": "Inverts the relationship between length and resistance."
        },
        "learning_objective": "Apply R = rho * L / A with constant volume constraint.",
        "hint": "What happens to the thickness (cross-sectional area) of dough or clay when you stretch it to twice its length?"
    },
    {
        "id": "q_elec_rf_02",
        "chapter_id": "electricity",
        "concept_id": "c_resistance_factors",
        "difficulty": "easy",
        "question_type": "mcq",
        "question_text": "Why does the electrical resistance of a metallic conductor increase as its length increases?",
        "options": [
            {"id": "A", "text": "Because electrons encounter more lattice ion collisions over a longer path"},
            {"id": "B", "text": "Because more electrons are created, which absorb electrical energy"},
            {"id": "C", "text": "Because the voltage decreases along the wire automatically"},
            {"id": "D", "text": "Because longer wires lose their electric field"}
        ],
        "correct_answer": "A",
        "explanation": "Current is the drift of electrons through a vibrating crystalline metal lattice. A longer conductor forces charge carriers to travel a greater distance, encountering more frequent scattering collisions with positive metal ions.",
        "expected_reasoning": "Resistance arises from microscopic electron collisions with lattice ions; longer path directly translates to more collisions.",
        "distractor_explanations": {
            "B": "Reflects misconception that charge is absorbed or created.",
            "C": "Confuses potential gradient with intrinsic conductor resistance.",
            "D": "Electric field depends on applied potential difference across conductor length."
        },
        "learning_objective": "Understand microscopic origin of electrical resistance.",
        "hint": "Consider what electrons collide with as they drift through copper."
    },
    # Parallel circuits
    {
        "id": "q_elec_pc_01",
        "chapter_id": "electricity",
        "concept_id": "c_parallel_circuits",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "Two resistors of 6 ohms and 12 ohms are connected in parallel across a 12V battery. What is the equivalent resistance and the total current drawn from the battery?",
        "options": [
            {"id": "A", "text": "18 ohms, 0.67 A"},
            {"id": "B", "text": "4 ohms, 3.0 A"},
            {"id": "C", "text": "4 ohms, 1.5 A"},
            {"id": "D", "text": "8 ohms, 1.5 A"}
        ],
        "correct_answer": "B",
        "explanation": "For parallel resistors: 1/Rp = 1/6 + 1/12 = 2/12 + 1/12 = 3/12 = 1/4, so Rp = 4 ohms. Total current I = V / Rp = 12V / 4 ohms = 3.0 A.",
        "expected_reasoning": "Use reciprocal formula for parallel combination, then apply Ohm's law V = IR.",
        "distractor_explanations": {
            "A": "Calculated series resistance (6 + 12 = 18 ohms) instead of parallel.",
            "C": "Calculated parallel resistance correctly but divided voltage erroneously.",
            "D": "Took simple average of 6 and 12 ohms."
        },
        "learning_objective": "Calculate equivalent resistance and branch currents in parallel circuits.",
        "hint": "Parallel equivalent resistance is always strictly less than the smallest individual resistor."
    },
    # Joule Heating
    {
        "id": "q_elec_jh_01",
        "chapter_id": "electricity",
        "concept_id": "c_joule_heating",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "If the electric current flowing through a fixed resistor of resistance R is tripled, by what factor does the heat produced in a given time interval increase?",
        "options": [
            {"id": "A", "text": "3 times"},
            {"id": "B", "text": "6 times"},
            {"id": "C", "text": "9 times"},
            {"id": "D", "text": "27 times"}
        ],
        "correct_answer": "C",
        "explanation": "According to Joule's Law of Heating, H = I^2 * R * t. If current is tripled (I' = 3I), H' = (3I)^2 * R * t = 9 * (I^2 * R * t) = 9H.",
        "expected_reasoning": "Heat generated is directly proportional to the square of current; tripling current squares to 9.",
        "distractor_explanations": {
            "A": "Assumed linear relationship H proportional to I.",
            "B": "Multiplied 3 by 2 instead of squaring.",
            "D": "Cubed the factor instead of squaring."
        },
        "learning_objective": "Apply Joule's Law quadratic dependency on electric current.",
        "hint": "Check the power of I in Joule's law equation H = I^n * R * t."
    },
    # Light - Refraction Snell
    {
        "id": "q_light_snell_01",
        "chapter_id": "light_reflection_refraction",
        "concept_id": "c_refraction_snell",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "A beam of monochromatic light travels from water (n = 1.33) into crown glass (n = 1.52). How do the speed, frequency, and wavelength of the light change?",
        "options": [
            {"id": "A", "text": "Speed decreases, frequency remains constant, wavelength decreases"},
            {"id": "B", "text": "Speed decreases, frequency decreases, wavelength remains constant"},
            {"id": "C", "text": "Speed increases, frequency remains constant, wavelength increases"},
            {"id": "D", "text": "All three (speed, frequency, wavelength) decrease proportionally"}
        ],
        "correct_answer": "A",
        "explanation": "Optical density is higher in glass (n=1.52) than water (n=1.33). Speed v = c/n decreases. Frequency is determined solely by the emitter source and remains invariant across boundaries. Since v = f * lambda, wavelength lambda = v/f must decrease.",
        "expected_reasoning": "Wave frequency is an invariant invariant of the source; higher refractive index reduces speed and correspondingly compresses wavelength.",
        "distractor_explanations": {
            "B": "Believes frequency changes across optical media.",
            "C": "Inverted refractive index ordering.",
            "D": "Assumes frequency depends on medium."
        },
        "learning_objective": "Distinguish invariant wave frequency from medium-dependent phase velocity and wavelength.",
        "hint": "What physical parameter of a light wave is determined solely by the original source lamp?"
    },
    # Mirrors
    {
        "id": "q_light_mirror_01",
        "chapter_id": "light_reflection_refraction",
        "concept_id": "c_spherical_mirrors",
        "difficulty": "easy",
        "question_type": "mcq",
        "question_text": "An object is placed at the center of curvature (C) of a concave mirror. What are the characteristics of the image formed?",
        "options": [
            {"id": "A", "text": "Real, inverted, same size as object, formed at C"},
            {"id": "B", "text": "Virtual, erect, enlarged, formed behind mirror"},
            {"id": "C", "text": "Real, inverted, diminished, formed between C and F"},
            {"id": "D", "text": "Real, erect, highly enlarged, formed at infinity"}
        ],
        "correct_answer": "A",
        "explanation": "When an object is positioned exactly at C (u = -2f), reflected rays converge back at C (v = -2f). The magnification m = -v/u = -(-2f)/(-2f) = -1, indicating a real, inverted image of identical size.",
        "expected_reasoning": "Object at C forms an image at C with magnification magnitude equal to 1.",
        "distractor_explanations": {
            "B": "Describes an object placed between focus F and pole P.",
            "C": "Describes an object placed beyond C.",
            "D": "Describes an object placed at the principal focus F."
        },
        "learning_objective": "Analyze ray reflection geometry for concave mirrors at the center of curvature.",
        "hint": "Ray directed through center of curvature retraces its path perpendicularly."
    },
    # Human Eye
    {
        "id": "q_eye_defect_01",
        "chapter_id": "human_eye_colourful_world",
        "concept_id": "c_eye_defects",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "A student cannot clearly read the classroom blackboard from the back bench (distance > 3 meters), but reads their textbook at 25 cm with ease. What defect of vision do they have, and what lens corrects it?",
        "options": [
            {"id": "A", "text": "Myopia; corrected with a suitable concave (diverging) lens"},
            {"id": "B", "text": "Hypermetropia; corrected with a convex (converging) lens"},
            {"id": "C", "text": "Presbyopia; corrected with bifocal cylindrical lens"},
            {"id": "D", "text": "Astigmatism; corrected with a plano-convex lens"}
        ],
        "correct_answer": "A",
        "explanation": "The student can see nearby objects distinctly but struggles with distant objects; this is nearsightedness or Myopia. Distant parallel rays converge in front of the retina. A concave lens diverges rays slightly so they focus exactly on the retina.",
        "expected_reasoning": "Inability to focus on distant objects with clear near vision defines myopia; requires diverging (concave) lens.",
        "distractor_explanations": {
            "B": "Hypermetropia is farsightedness (difficulty seeing nearby text).",
            "C": "Presbyopia is age-related loss of accommodation affecting near vision.",
            "D": "Astigmatism is uneven corneal curvature."
        },
        "learning_objective": "Identify vision defects and prescribe corrective optical lenses.",
        "hint": "Does the student need rays to diverge slightly or converge more?"
    },
    # Atmospheric Refraction
    {
        "id": "q_eye_scatter_01",
        "chapter_id": "human_eye_colourful_world",
        "concept_id": "c_light_scattering",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "Why does the clear daytime sky appear blue rather than red or yellow?",
        "options": [
            {"id": "A", "text": "Atmospheric gas molecules scatter shorter wavelengths (blue) much more strongly than longer wavelengths (red)"},
            {"id": "B", "text": "Sunlight contains only blue and violet light when it enters the Earth atmosphere"},
            {"id": "C", "text": "Earth's blue oceans reflect their color upwards onto clouds and air"},
            {"id": "D", "text": "Ozone specifically emits blue photons through chemical fluorescence"}
        ],
        "correct_answer": "A",
        "explanation": "According to Rayleigh's law of scattering, scattering intensity is inversely proportional to the fourth power of wavelength (I ~ 1/lambda^4). Blue light has a significantly shorter wavelength (~450 nm) than red light (~700 nm) and is scattered ~10 times more intensely in all directions by air molecules.",
        "expected_reasoning": "Rayleigh scattering efficiency scales inversely with lambda^4, dispersing shorter blue wavelengths across the sky dome.",
        "distractor_explanations": {
            "B": "Sunlight is continuous polychromatic white light containing all visible spectrum colors.",
            "C": "Common misconception attributing sky color to ocean reflection.",
            "D": "Ozone absorbs UV; it does not fluoresce blue light."
        },
        "learning_objective": "Explain atmospheric optical phenomena via Rayleigh scattering.",
        "hint": "How does scattering intensity depend on the wavelength of light?"
    },
    # Magnetic Effects - Field Lines
    {
        "id": "q_mag_field_01",
        "chapter_id": "magnetic_effects_electric_current",
        "concept_id": "c_magnetic_fields",
        "difficulty": "easy",
        "question_type": "mcq",
        "question_text": "Why is it physically impossible for two magnetic field lines to cross or intersect each other?",
        "options": [
            {"id": "A", "text": "At the point of intersection, a magnetic compass would have to point in two different directions simultaneously"},
            {"id": "B", "text": "Because magnetic field lines carry equal positive charges that repel each other"},
            {"id": "C", "text": "Because the magnetic field completely vanishes wherever lines come close"},
            {"id": "D", "text": "Because magnetic lines only exist in isolated vacuum regions"}
        ],
        "correct_answer": "A",
        "explanation": "The direction of a magnetic field at any point is defined as the tangent to the field line at that point. If two lines intersected, the tangent at that single intersection point would not be unique, implying two distinct directions for the resultant magnetic field—which is physically impossible.",
        "expected_reasoning": "The field vector at any spatial location is unique; an intersection implies two resultant vector directions simultaneously.",
        "distractor_explanations": {
            "B": "Magnetic field lines are mathematical flow representations, not physical charged wires.",
            "C": "Lines being close indicates stronger field, not vanishing field.",
            "D": "Magnetic fields permeate matter and space freely."
        },
        "learning_objective": "Understand uniqueness of resultant vector fields and field line properties.",
        "hint": "What would a magnetic needle placed right on the intersection point do?"
    },
    # Solenoid
    {
        "id": "q_mag_solenoid_01",
        "chapter_id": "magnetic_effects_electric_current",
        "concept_id": "c_solenoid_magnetic_field",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "What is the nature of the magnetic field inside a long, current-carrying cylindrical solenoid?",
        "options": [
            {"id": "A", "text": "Uniform, strong, and parallel to the axis of the solenoid"},
            {"id": "B", "text": "Zero everywhere inside because internal circular fields cancel"},
            {"id": "C", "text": "Circular concentric rings around the central axis"},
            {"id": "D", "text": "Strongest at the exact ends and zero at the center"}
        ],
        "correct_answer": "A",
        "explanation": "Inside a long tightly-wound solenoid, field contributions from individual circular turns sum constructively along the axial direction and cancel radially, producing a remarkably uniform magnetic field represented by equidistant parallel field lines (B = mu0 * n * I).",
        "expected_reasoning": "Parallel equidistant field lines inside a solenoid represent a uniform magnetic field.",
        "distractor_explanations": {
            "B": "Misconception that fields cancel inside coils.",
            "C": "Describes field around an individual straight wire, not inside a solenoid.",
            "D": "The internal field is uniformly strong; fringing occurs at the outer ends."
        },
        "learning_objective": "Describe magnetic field distribution and uniformity inside solenoids.",
        "hint": "Why do engineers insert a soft iron core inside a solenoid to create powerful electromagnets?"
    },
    # Force & Motion - Newton's 1st Law
    {
        "id": "q_motion_n1_01",
        "chapter_id": "force_motion_fundamentals",
        "concept_id": "c_newtons_first_law",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "A hockey puck slides across frictionless horizontal ice at a constant velocity of 12 m/s. What net horizontal force is required to keep it moving at this constant speed?",
        "options": [
            {"id": "A", "text": "Zero Newtons"},
            {"id": "B", "text": "A force proportional to its mass multiplied by 12 m/s"},
            {"id": "C", "text": "A continuous force equal to its kinetic energy"},
            {"id": "D", "text": "9.8 N per kilogram of mass"}
        ],
        "correct_answer": "A",
        "explanation": "According to Newton's First Law (Law of Inertia), an object in motion continues moving with constant velocity in a straight line unless acted upon by a net unbalanced external force. Since ice is frictionless, acceleration a = 0, so F_net = m * a = 0 N.",
        "expected_reasoning": "Constant velocity implies zero acceleration; by Newton's first and second laws, net force must be zero.",
        "distractor_explanations": {
            "B": "Confuses momentum (m*v) with force required to sustain motion (Aristotelian misconception).",
            "C": "Confuses kinetic energy with applied force.",
            "D": "Refers to gravitational acceleration on Earth, which acts vertically, not horizontally."
        },
        "learning_objective": "Differentiate between velocity maintenance and acceleration requirements.",
        "hint": "What is the puck's acceleration if its velocity is perfectly constant?"
    },
    # Newton's 3rd Law
    {
        "id": "q_motion_n3_01",
        "chapter_id": "force_motion_fundamentals",
        "concept_id": "c_newtons_third_law",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "A horse pulls a cart forward. The cart exerts an equal and opposite backward force on the horse. Why does the horse-cart system accelerate forward?",
        "options": [
            {"id": "A", "text": "The horse pushes backward on the ground, and the ground exerts a forward reaction force on the horse greater than backward friction on the cart"},
            {"id": "B", "text": "The horse's pull is slightly greater than the cart's pull for the first second of motion"},
            {"id": "C", "text": "Action force acts before reaction force, creating a momentary unbalanced forward impulse"},
            {"id": "D", "text": "Newton's third law applies only to static objects at rest"}
        ],
        "correct_answer": "A",
        "explanation": "Action-reaction pairs act on different bodies: Force of horse on cart and Force of cart on horse cancel only when considering the horse and cart as an internal system. The external forward force that accelerates the whole system is the friction force that the ground exerts forward on the horse's hooves when the horse pushes backward against Earth.",
        "expected_reasoning": "Identify the external horizontal force from the ground on the horse hooves that produces forward net acceleration.",
        "distractor_explanations": {
            "B": "Violates Newton's 3rd law: action and reaction forces are strictly equal in magnitude at all times.",
            "C": "Action and reaction are simultaneous; there is zero time delay.",
            "D": "Newton's laws apply universally across static and dynamic regimes."
        },
        "learning_objective": "Apply Newton's third law with proper free-body diagram isolation.",
        "hint": "Look at the external horizontal forces exerted by the ground on the hooves."
    }
]

# Mark Class 10 concepts
CLASS_10_CONCEPTS = CONCEPTS + CHEMISTRY_CONCEPTS + BIOLOGY_CONCEPTS + MATH_CONCEPTS
for c in CLASS_10_CONCEPTS:
    if "grade" not in c:
        c["grade"] = 10

# Mark Class 10 questions
for q in SEED_QUESTIONS:
    if "grade" not in q:
        q["grade"] = 10
for q in MULTI_SUBJECT_QUESTIONS:
    if "grade" not in q:
        q["grade"] = 10

# Merge all grades and multi-subject curriculum into core collections
CONCEPTS = CLASS_9_CONCEPTS + CLASS_10_CONCEPTS + CLASS_11_CONCEPTS + CLASS_12_CONCEPTS
CONCEPT_RELATIONSHIPS = CONCEPT_RELATIONSHIPS + MULTI_SUBJECT_RELATIONSHIPS + CROSS_GRADE_RELATIONSHIPS
SEED_QUESTIONS = SEED_QUESTIONS + MULTI_SUBJECT_QUESTIONS + CROSS_GRADE_QUESTIONS
ALL_MISCONCEPTIONS = PHYSICS_MISCONCEPTIONS + MULTI_SUBJECT_MISCONCEPTIONS + CROSS_GRADE_MISCONCEPTIONS

def seed_database(db):
    """Populates collections with syllabus, questions, demo accounts, and initial state."""
    users_col = db.get_collection("users")
    chapters_col = db.get_collection("chapters")
    concepts_col = db.get_collection("concepts")
    relationships_col = db.get_collection("concept_relationships")
    questions_col = db.get_collection("questions")
    learner_models_col = db.get_collection("learner_models")
    misconceptions_col = db.get_collection("misconceptions")
    revision_schedules_col = db.get_collection("revision_schedules")
    assignments_col = db.get_collection("assignments")
    learning_paths_col = db.get_collection("learning_paths")
    grades_col = db.get_collection("grades")
    subjects_col = db.get_collection("subjects")

    # If all 42 chapters across 4 grades and 4 subjects are already seeded and force is not set, skip
    if chapters_col.count_documents({}) >= 42 and subjects_col.count_documents({}) >= 4 and grades_col.count_documents({}) >= 4:
        return

    # Clear previous single-subject data for clean multi-subject upgrade
    for col in [chapters_col, concepts_col, relationships_col, questions_col, 
                learner_models_col, misconceptions_col, revision_schedules_col, 
                assignments_col, learning_paths_col, subjects_col, grades_col]:
        col.docs = []

    print("[Learnix Seed] Seeding Grades (Classes 9, 10, 11, 12)...")
    for g in GRADES:
        grades_col.insert_one(g)

    print("[Learnix Seed] Seeding Subjects (Physics, Chemistry, Biology, Mathematics)...")
    for subj in SUBJECTS:
        subjects_col.insert_one(subj)

    print("[Learnix Seed] Seeding Chapters across all subjects...")
    for ch in CHAPTERS:
        chapters_col.insert_one(ch)

    print("[Learnix Seed] Seeding Concepts...")
    for c in CONCEPTS:
        if "subject_id" not in c:
            c["subject_id"] = "physics"
            c["subject_name"] = "Physics"
        concepts_col.insert_one(c)

    print("[Learnix Seed] Seeding Concept Relationships...")
    for rel in CONCEPT_RELATIONSHIPS:
        relationships_col.insert_one(rel)

    print("[Learnix Seed] Seeding Question Bank...")
    for q in SEED_QUESTIONS:
        if "subject_id" not in q:
            q["subject_id"] = "physics"
            q["subject_name"] = "Physics"
        questions_col.insert_one(q)

    print("[Learnix Seed] Seeding Misconceptions Database...")
    for m in ALL_MISCONCEPTIONS:
        misconceptions_col.insert_one(m)

    # Seed Demo Accounts
    print("[Learnix Seed] Creating Demo Student and Teacher accounts...")
    student_id = "student_alex_chen"
    teacher_id = "teacher_sarah_jenkins"

    hashed_pw = hash_password("password123")

    users_col.insert_one({
        "_id": student_id,
        "email": "student@learnix.ai",
        "password_hash": hashed_pw,
        "name": "Alex Chen",
        "role": "student",
        "grade": "Class 10",
        "target_exam": "CBSE Physics Board Exam",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=Alex",
        "xp": 1420,
        "level": 4,
        "level_title": "Quantum Apprentice",
        "streak_days": 6,
        "daily_goal": 5,
        "daily_completed": 3,
        "total_study_minutes": 240,
        "created_at": get_utc_now()
    })

    users_col.insert_one({
        "_id": teacher_id,
        "email": "teacher@learnix.ai",
        "password_hash": hashed_pw,
        "name": "Dr. Sarah Jenkins",
        "role": "teacher",
        "school": "St. Jude Senior Academy",
        "subject": "Physics",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=Sarah",
        "classes": ["Class 10-A", "Class 10-B"],
        "created_at": get_utc_now()
    })

    # Seed 4 other students for Dr. Jenkins' class analytics
    other_students = [
        {"id": "std_priya", "name": "Priya Sharma", "avatar": "Priya", "overall": 76.5},
        {"id": "std_marcus", "name": "Marcus Vance", "avatar": "Marcus", "overall": 54.0},
        {"id": "std_aanya", "name": "Aanya Patel", "avatar": "Aanya", "overall": 88.0},
        {"id": "std_liam", "name": "Liam Davies", "avatar": "Liam", "overall": 42.5}
    ]
    for s in other_students:
        users_col.insert_one({
            "_id": s["id"],
            "email": f"{s['avatar'].lower()}@learnix.ai",
            "password_hash": hashed_pw,
            "name": s["name"],
            "role": "student",
            "grade": "Class 10",
            "avatar": f"https://api.dicebear.com/7.x/bottts/svg?seed={s['avatar']}",
            "xp": 950,
            "level": 3,
            "level_title": "Circuit Explorer",
            "streak_days": 4,
            "daily_goal": 5,
            "daily_completed": 2,
            "created_at": get_utc_now()
        })

    # Seed Learner Models for Alex Chen
    # Mix of mastered, learning, and weak concepts
    concept_mastery_profiles = {
        "c_spherical_mirrors": (84.0, 0.90, "hard", 12, 10, 2, []),
        "c_mirror_formula": (72.0, 0.80, "hard", 8, 6, 2, []),
        "c_refraction_snell": (65.0, 0.75, "medium", 10, 7, 3, []),
        "c_lenses_refraction": (58.0, 0.65, "medium", 6, 4, 2, []),
        "c_lens_power": (42.0, 0.50, "easy", 5, 2, 3, ["Power unit dioptre reciprocal sign confusion"]),
        "c_eye_accommodation": (91.0, 0.95, "advanced", 9, 9, 0, []),
        "c_eye_defects": (48.0, 0.55, "easy", 7, 3, 4, ["misc_myopia_convex_correction"]),
        "c_prism_dispersion": (78.0, 0.85, "hard", 6, 5, 1, []),
        "c_light_scattering": (38.0, 0.40, "easy", 8, 3, 5, ["misc_sky_blue_because_ocean"]),
        "c_electric_current": (88.0, 0.90, "advanced", 15, 14, 1, []),
        "c_potential_difference": (75.0, 0.80, "hard", 11, 9, 2, []),
        "c_ohms_law": (82.0, 0.85, "hard", 14, 12, 2, []),
        "c_resistance_factors": (36.0, 0.40, "easy", 9, 3, 6, ["misc_longer_wire_less_resistance"]),
        "c_series_circuits": (68.0, 0.70, "medium", 8, 6, 2, []),
        "c_parallel_circuits": (45.0, 0.50, "medium", 10, 4, 6, ["misc_parallel_resistance_additive"]),
        "c_joule_heating": (52.0, 0.60, "medium", 6, 3, 3, []),
        "c_electric_power": (61.0, 0.65, "medium", 7, 5, 2, []),
        "c_magnetic_fields": (76.0, 0.80, "medium", 8, 7, 1, []),
        "c_current_carrying_wire": (64.0, 0.70, "medium", 6, 4, 2, []),
        "c_solenoid_magnetic_field": (34.0, 0.35, "easy", 7, 2, 5, ["misc_solenoid_no_field_inside"]),
        "c_fleming_left_hand": (55.0, 0.60, "medium", 5, 3, 2, []),
        "c_electromagnetic_induction": (28.0, 0.30, "easy", 4, 1, 3, []),
        "c_electrolytic_conduction": (70.0, 0.75, "medium", 6, 5, 1, []),
        "c_electrolysis": (62.0, 0.65, "medium", 5, 3, 2, []),
        "c_electroplating": (50.0, 0.55, "easy", 4, 2, 2, []),
        "c_balanced_forces": (85.0, 0.90, "hard", 10, 9, 1, []),
        "c_newtons_first_law": (40.0, 0.45, "easy", 8, 3, 5, ["misc_constant_force_for_constant_velocity"]),
        "c_newtons_second_law": (60.0, 0.65, "medium", 7, 4, 3, []),
        "c_newtons_third_law": (32.0, 0.35, "easy", 9, 2, 7, ["misc_action_reaction_cancel"]),
        "c_momentum_conservation": (50.0, 0.55, "medium", 5, 2, 3, []),

        # Chemistry Concepts
        "c_balancing_equations": (85.0, 0.90, "hard", 10, 9, 1, []),
        "c_reaction_types": (75.0, 0.80, "medium", 8, 6, 2, []),
        "c_redox_reactions": (70.0, 0.75, "medium", 7, 5, 2, []),
        "c_corrosion_rancidity": (45.0, 0.45, "easy", 6, 2, 4, ["misc_rusting_is_erosion"]),
        "c_acid_base_indicators": (88.0, 0.90, "hard", 10, 9, 1, []),
        "c_ph_scale": (82.0, 0.85, "hard", 9, 8, 1, []),
        "c_salts_manufacturing": (64.0, 0.70, "medium", 7, 5, 2, []),
        "c_water_crystallization": (55.0, 0.60, "medium", 5, 3, 2, []),
        "c_reactivity_series": (72.0, 0.75, "medium", 8, 6, 2, []),
        "c_ionic_compounds": (78.0, 0.80, "medium", 7, 6, 1, []),
        "c_metallurgy_extraction": (48.0, 0.50, "easy", 6, 3, 3, []),
        "c_covalent_bonding_carbon": (76.0, 0.80, "medium", 8, 6, 2, []),
        "c_homologous_series": (80.0, 0.85, "hard", 9, 8, 1, []),
        "c_functional_groups": (52.0, 0.55, "medium", 6, 3, 3, []),
        "c_esterification_saponification": (58.0, 0.60, "medium", 6, 4, 2, []),

        # Biology Concepts
        "c_photosynthesis_stomata": (88.0, 0.90, "hard", 11, 10, 1, []),
        "c_cellular_respiration": (48.0, 0.50, "easy", 7, 3, 4, ["misc_respiration_is_breathing"]),
        "c_human_double_circulation": (82.0, 0.85, "hard", 9, 8, 1, []),
        "c_nephron_ultrafiltration": (60.0, 0.65, "medium", 6, 4, 2, []),
        "c_neuron_synapse": (84.0, 0.85, "hard", 9, 8, 1, []),
        "c_reflex_arc": (90.0, 0.95, "advanced", 8, 8, 0, []),
        "c_plant_hormones_tropisms": (76.0, 0.80, "medium", 7, 6, 1, []),
        "c_human_endocrine_system": (55.0, 0.60, "medium", 6, 3, 3, []),
        "c_asexual_reproduction_modes": (85.0, 0.90, "hard", 8, 7, 1, []),
        "c_flower_sexual_reproduction": (65.0, 0.70, "medium", 7, 5, 2, []),
        "c_human_reproduction_contraception": (72.0, 0.75, "medium", 8, 6, 2, []),
        "c_mendel_monohybrid_cross": (84.0, 0.85, "hard", 10, 9, 1, []),
        "c_mendel_dihybrid_cross": (62.0, 0.65, "medium", 6, 4, 2, []),
        "c_human_sex_determination": (42.0, 0.40, "easy", 7, 2, 5, ["misc_mother_determines_sex"]),
        "c_trophic_levels_biomagnification": (78.0, 0.80, "medium", 7, 6, 1, []),

        # Mathematics Concepts
        "c_fundamental_theorem_arithmetic": (94.0, 0.95, "advanced", 12, 12, 0, []),
        "c_irrationality_proof": (68.0, 0.70, "medium", 7, 5, 2, []),
        "c_polynomial_zeroes_coefficients": (82.0, 0.85, "hard", 9, 8, 1, []),
        "c_quadratic_discriminant_nature": (76.0, 0.80, "medium", 8, 6, 2, []),
        "c_arithmetic_progression_nth_term": (88.0, 0.90, "hard", 10, 9, 1, []),
        "c_arithmetic_progression_sum": (75.0, 0.80, "medium", 8, 6, 2, []),
        "c_basic_proportionality_theorem": (70.0, 0.75, "medium", 7, 5, 2, []),
        "c_triangle_similarity_criteria": (62.0, 0.65, "medium", 6, 4, 2, []),
        "c_coordinate_distance_section": (74.0, 0.75, "medium", 8, 6, 2, []),
        "c_trigonometric_ratios": (82.0, 0.85, "hard", 9, 8, 1, []),
        "c_trigonometric_identities": (42.0, 0.45, "easy", 7, 2, 5, ["misc_trig_distributive"]),
        "c_heights_and_distances": (66.0, 0.70, "medium", 6, 4, 2, [])
    }

    now = datetime.datetime.now(datetime.timezone.utc)
    for c in CONCEPTS:
        cid = c["id"]
        grade_val = c.get("grade", 10)
        default_prof = (
            (76.0, 0.85, "hard", 10, 8, 2, []) if grade_val == 9
            else (64.0, 0.70, "medium", 7, 5, 2, []) if grade_val == 10
            else (58.0, 0.65, "medium", 6, 4, 2, []) if grade_val == 11
            else (54.0, 0.60, "medium", 5, 3, 2, [])
        )
        prof = concept_mastery_profiles.get(cid, default_prof)
        mastery, conf, diff, total, correct, inc, miscs = prof

        # Revision schedule
        rev_due = now + datetime.timedelta(days=1 if mastery < 50 else (4 if mastery < 75 else 9))
        
        learner_models_col.insert_one({
            "student_id": student_id,
            "concept_id": cid,
            "concept_name": c["name"],
            "chapter_id": c["chapter_id"],
            "grade": grade_val,
            "subject_id": c.get("subject_id", "physics"),
            "subject_name": c.get("subject_name", "Physics"),
            "mastery_score": mastery,
            "confidence_level": conf,
            "total_questions_answered": total,
            "correct_answers": correct,
            "incorrect_answers": inc,
            "last_studied": (now - datetime.timedelta(hours=6)).isoformat(),
            "current_difficulty": diff,
            "misconceptions_detected": miscs,
            "revision_due_date": rev_due.isoformat(),
            "review_interval_days": 1 if mastery < 50 else (3 if mastery < 75 else 7),
            "ease_factor": 2.2 if mastery < 50 else 2.6
        })

        # Revision record
        revision_schedules_col.insert_one({
            "student_id": student_id,
            "concept_id": cid,
            "concept_name": c["name"],
            "chapter_id": c["chapter_id"],
            "grade": grade_val,
            "subject_id": c.get("subject_id", "physics"),
            "subject_name": c.get("subject_name", "Physics"),
            "due_date": rev_due.isoformat(),
            "interval_days": 1 if mastery < 50 else 5,
            "ease_factor": 2.5,
            "repetition_count": 2 if mastery > 60 else 0,
            "last_reviewed": (now - datetime.timedelta(days=2)).isoformat(),
            "status": "due_today" if mastery < 45 else ("overdue" if mastery < 35 else "upcoming")
        })

        # Also populate learner models for other mock students with slight variations
        for s in other_students:
            mod_factor = s["overall"] / 60.0
            s_mastery = min(98.0, max(15.0, round(mastery * mod_factor, 1)))
            learner_models_col.insert_one({
                "student_id": s["id"],
                "concept_id": cid,
                "concept_name": c["name"],
                "chapter_id": c["chapter_id"],
                "grade": grade_val,
                "subject_id": c.get("subject_id", "physics"),
                "subject_name": c.get("subject_name", "Physics"),
                "mastery_score": s_mastery,
                "confidence_level": min(0.95, max(0.2, conf * mod_factor)),
                "total_questions_answered": max(2, int(total * mod_factor)),
                "correct_answers": max(1, int(correct * mod_factor)),
                "incorrect_answers": max(0, int(inc * (1.2 / mod_factor))),
                "last_studied": (now - datetime.timedelta(days=1)).isoformat(),
                "current_difficulty": "easy" if s_mastery < 35 else ("medium" if s_mastery < 65 else "hard"),
                "misconceptions_detected": miscs if s_mastery < 45 else [],
                "revision_due_date": (now + datetime.timedelta(days=2)).isoformat()
            })

    # Seed Sample Teacher Assignments
    assignments_col.insert_one({
        "id": "asg_elec_mastery",
        "teacher_id": teacher_id,
        "title": "Mastering Resistance & Circuit Combinations",
        "chapter_id": "electricity",
        "target_concepts": ["c_resistance_factors", "c_parallel_circuits", "c_joule_heating"],
        "assigned_class": "Class 10-A",
        "due_date": (now + datetime.timedelta(days=4)).isoformat(),
        "created_at": (now - datetime.timedelta(days=1)).isoformat(),
        "total_assigned": 5,
        "completed_count": 3,
        "average_score": 68.4
    })
    assignments_col.insert_one({
        "id": "asg_optics_lens",
        "teacher_id": teacher_id,
        "title": "Snell's Law & Lens Power Diagnostic",
        "chapter_id": "light_reflection_refraction",
        "target_concepts": ["c_refraction_snell", "c_lenses_refraction", "c_lens_power"],
        "assigned_class": "Class 10-A",
        "due_date": (now + datetime.timedelta(days=7)).isoformat(),
        "created_at": (now - datetime.timedelta(days=2)).isoformat(),
        "total_assigned": 5,
        "completed_count": 2,
        "average_score": 58.2
    })

    # Seed Personalized Learning Path for Alex Chen
    learning_path_items = [
        {
            "id": "lp_01",
            "concept_id": "c_resistance_factors",
            "concept_name": "Resistance & Resistivity",
            "chapter_id": "electricity",
            "priority": "Critical",
            "estimated_minutes": 15,
            "status": "in_progress",
            "mastery_target": 75,
            "reason": "Active misconception detected: longer wire decreases resistance.",
            "recommended_activity": "Interactive wire stretching simulation + 3 practice problems."
        },
        {
            "id": "lp_02",
            "concept_id": "c_parallel_circuits",
            "concept_name": "Parallel Circuits & Conductance",
            "chapter_id": "electricity",
            "priority": "High",
            "estimated_minutes": 20,
            "status": "locked",
            "mastery_target": 75,
            "reason": "Prerequisite for Joule's law & electrical power.",
            "recommended_activity": "Multi-branch current calculation practice."
        },
        {
            "id": "lp_03",
            "concept_id": "c_solenoid_magnetic_field",
            "concept_name": "Magnetic Field in a Solenoid",
            "chapter_id": "magnetic_effects_electric_current",
            "priority": "High",
            "estimated_minutes": 15,
            "status": "locked",
            "mastery_target": 70,
            "reason": "Weak foundational conceptual model (34% mastery).",
            "recommended_activity": "Field lines comparison: bar magnet vs long solenoid."
        },
        {
            "id": "lp_04",
            "concept_id": "c_newtons_third_law",
            "concept_name": "Newton's Third Law Pairs",
            "chapter_id": "force_motion_fundamentals",
            "priority": "Medium",
            "estimated_minutes": 25,
            "status": "locked",
            "mastery_target": 80,
            "reason": "Active misconception: action-reaction cancel out.",
            "recommended_activity": "Free-body diagrams for interacting multi-body systems."
        },
        {
            "id": "lp_05",
            "concept_id": "c_electromagnetic_induction",
            "concept_name": "Electromagnetic Induction (EMI)",
            "chapter_id": "magnetic_effects_electric_current",
            "priority": "Medium",
            "estimated_minutes": 30,
            "status": "locked",
            "mastery_target": 75,
            "reason": "Advanced CBSE board high-weightage topic.",
            "recommended_activity": "Faraday coil flux simulation and Fleming's Right Hand Rule."
        }
    ]

    for item in learning_path_items:
        learning_paths_col.insert_one({
            "student_id": student_id,
            **item
        })

    print("[Learnix Seed] Database seeding successfully completed!")
