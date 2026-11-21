"""
Grade Curriculum for Classes 9, 11, and 12 (CBSE / ICSE / JEE / NEET).
Expands Learnix AI across the full secondary and senior secondary spectrum (Grades 9-12).
"""

from typing import List, Dict, Any

GRADES: List[Dict[str, Any]] = [
    {
        "id": "class_9",
        "grade": 9,
        "name": "Class 9",
        "tagline": "Foundational High School STEM",
        "badge": "Foundation",
        "exam_focus": "CBSE 9th Foundation & Science Olympiads",
        "color": "from-emerald-500 to-teal-600",
        "accent": "emerald",
        "description": "Kinematics, Atomic Structure, Cell Biology, Number Systems & Triangles",
        "total_chapters": 8,
        "total_concepts": 16,
        "average_mastery": 71.5
    },
    {
        "id": "class_10",
        "grade": 10,
        "name": "Class 10",
        "tagline": "Secondary Board Exam Mastery",
        "badge": "Board Exam",
        "exam_focus": "CBSE / ICSE Class 10 Board Examinations",
        "color": "from-blue-600 to-indigo-600",
        "accent": "blue",
        "description": "Optics & Electricity, Chemical Reactions & Carbon, Life Processes, Trigonometry",
        "total_chapters": 18,
        "total_concepts": 74,
        "average_mastery": 74.0
    },
    {
        "id": "class_11",
        "grade": 11,
        "name": "Class 11",
        "tagline": "Senior Secondary & JEE/NEET Pre",
        "badge": "JEE / NEET Pre",
        "exam_focus": "JEE Main / NEET Foundation & Senior Secondary",
        "color": "from-violet-600 to-purple-600",
        "accent": "violet",
        "description": "Rotational Mechanics & Thermo, Chemical Bonding, Physiology, Conic Sections & Calculus",
        "total_chapters": 8,
        "total_concepts": 16,
        "average_mastery": 66.0
    },
    {
        "id": "class_12",
        "grade": 12,
        "name": "Class 12",
        "tagline": "Boards & National Entrance (JEE/NEET)",
        "badge": "Board + JEE/NEET",
        "exam_focus": "Class 12 Boards & National Competitive Entrances (JEE Adv / NEET)",
        "color": "from-amber-500 to-rose-600",
        "accent": "amber",
        "description": "Electrostatics & Wave Optics, Organic Mechanisms, Molecular Genetics, Integral Calculus",
        "total_chapters": 8,
        "total_concepts": 16,
        "average_mastery": 69.5
    }
]

# ============================================================================
# CLASS 9 CURRICULUM
# ============================================================================
CLASS_9_CHAPTERS = [
    # Physics 9
    {
        "id": "c9_motion_kinematics",
        "grade": 9,
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Motion and Kinematics",
        "order": 101,
        "description": "Distance vs displacement, speed, velocity, uniform acceleration, and equations of motion.",
        "icon": "Gauge",
        "color": "from-blue-500 to-cyan-600"
    },
    {
        "id": "c9_gravitation_flotation",
        "grade": 9,
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Gravitation and Floatation",
        "order": 102,
        "description": "Universal law of gravitation, acceleration due to gravity (g), mass vs weight, Archimedes principle.",
        "icon": "Globe",
        "color": "from-indigo-500 to-blue-600"
    },
    # Chemistry 9
    {
        "id": "c9_matter_surroundings",
        "grade": 9,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "title": "Matter in Our Surroundings",
        "order": 103,
        "description": "States of matter, kinetic molecular theory, latent heat of vaporization/fusion, evaporation.",
        "icon": "Boxes",
        "color": "from-emerald-500 to-teal-600"
    },
    {
        "id": "c9_atoms_and_molecules",
        "grade": 9,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "title": "Atoms and Molecules",
        "order": 104,
        "description": "Law of chemical combinations, Dalton's atomic theory, atomic mass, chemical formulas, and Mole concept.",
        "icon": "Atom",
        "color": "from-teal-500 to-green-600"
    },
    # Biology 9
    {
        "id": "c9_fundamental_unit_cell",
        "grade": 9,
        "subject_id": "biology",
        "subject_name": "Biology",
        "title": "Fundamental Unit of Life (Cell)",
        "order": 105,
        "description": "Plasma membrane, osmosis/diffusion, nucleus, cell organelles (mitochondria, ER, Golgi, vacuoles).",
        "icon": "Layers",
        "color": "from-rose-500 to-pink-600"
    },
    {
        "id": "c9_tissues_structure",
        "grade": 9,
        "subject_id": "biology",
        "subject_name": "Biology",
        "title": "Tissues: Plant & Animal",
        "order": 106,
        "description": "Meristematic vs permanent plant tissues (xylem/phloem); epithelial, muscular, connective & nervous.",
        "icon": "Dna",
        "color": "from-pink-500 to-red-600"
    },
    # Mathematics 9
    {
        "id": "c9_number_systems_algebra",
        "grade": 9,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "title": "Number Systems & Polynomials",
        "order": 107,
        "description": "Real numbers, rationalization of surds, Remainder Theorem, Factor Theorem, algebraic identities.",
        "icon": "Sigma",
        "color": "from-amber-500 to-orange-600"
    },
    {
        "id": "c9_lines_triangles_geometry",
        "grade": 9,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "title": "Lines, Angles and Triangles",
        "order": 108,
        "description": "Parallel lines & transversals, Angle Sum Property, triangle congruence criteria (SAS, ASA, SSS, RHS).",
        "icon": "Maximize2",
        "color": "from-orange-500 to-amber-600"
    }
]

CLASS_9_CONCEPTS = [
    # Motion 9
    {
        "id": "c9_equations_of_motion",
        "grade": 9,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c9_motion_kinematics",
        "name": "Equations of Uniformly Accelerated Motion",
        "description": "Derivation and problem solving for kinematic relations under constant acceleration.",
        "key_formula": "v = u + at, s = ut + 0.5at^2, v^2 = u^2 + 2as",
        "difficulty_baseline": "medium",
        "x": 100,
        "y": 100
    },
    {
        "id": "c9_distance_time_graphs",
        "grade": 9,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c9_motion_kinematics",
        "name": "Velocity-Time & Distance-Time Graphs",
        "description": "Slope of s-t graph gives velocity; slope of v-t gives acceleration; area under v-t graph gives distance.",
        "key_formula": "Slope = dy/dx, Area under v-t = Displacement",
        "difficulty_baseline": "easy",
        "x": 280,
        "y": 100
    },
    {
        "id": "c9_universal_gravitation",
        "grade": 9,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c9_gravitation_flotation",
        "name": "Universal Law of Gravitation & Free Fall",
        "description": "Gravitational attraction between two masses inversely proportional to square of distance.",
        "key_formula": "F = G * (m1 * m2) / r^2, g = G * M / R^2 = 9.8 m/s^2",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 100
    },
    {
        "id": "c9_archimedes_buoyancy",
        "grade": 9,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c9_gravitation_flotation",
        "name": "Archimedes' Principle & Buoyant Force",
        "description": "Upward buoyant force exerted on a body immersed in a fluid is equal to the weight of fluid displaced.",
        "key_formula": "F_b = rho * V * g",
        "difficulty_baseline": "medium",
        "x": 640,
        "y": 100
    },
    # Chemistry 9
    {
        "id": "c9_latent_heat_evaporation",
        "grade": 9,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c9_matter_surroundings",
        "name": "Latent Heat & Cooling by Evaporation",
        "description": "Heat absorbed during phase change without temperature rise; cooling mechanism of evaporation.",
        "key_formula": "Q = m * L (Latent heat of fusion / vaporization)",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 240
    },
    {
        "id": "c9_states_of_matter_diffusion",
        "grade": 9,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c9_matter_surroundings",
        "name": "Kinetic Theory & Intermolecular Diffusion",
        "description": "Intermixing of particles of different substances on their own, driven by kinetic energy.",
        "key_formula": "Rate of diffusion proportional to temperature / sqrt(molar mass)",
        "difficulty_baseline": "easy",
        "x": 280,
        "y": 240
    },
    {
        "id": "c9_mole_concept_dalton",
        "grade": 9,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c9_atoms_and_molecules",
        "name": "Mole Concept & Avogadro's Number",
        "description": "Counting particles in terms of moles; 1 mole contains 6.022 x 10^23 particles; molar mass.",
        "key_formula": "Number of moles n = Given mass (m) / Molar mass (M) = N / N_A",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 240
    },
    {
        "id": "c9_chemical_formulae_valency",
        "grade": 9,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c9_atoms_and_molecules",
        "name": "Valency & Criss-Cross Chemical Formulae",
        "description": "Combining capacity of elements and writing formulas for binary ionic and molecular compounds.",
        "key_formula": "Criss-cross valencies: Al(3+) + SO4(2-) -> Al2(SO4)3",
        "difficulty_baseline": "medium",
        "x": 640,
        "y": 240
    },
    # Biology 9
    {
        "id": "c9_osmosis_plasma_membrane",
        "grade": 9,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c9_fundamental_unit_cell",
        "name": "Osmosis & Cell Tonicity (Hypo/Hyper/Isotonic)",
        "description": "Water movement across selectively permeable membranes; plasmolysis in plant cells.",
        "key_formula": "Hypotonic (swelling/turgid), Hypertonic (plasmolysis/shrink)",
        "difficulty_baseline": "medium",
        "x": 100,
        "y": 380
    },
    {
        "id": "c9_cell_organelles_mitochondria",
        "grade": 9,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c9_fundamental_unit_cell",
        "name": "Cell Organelles & Mitochondria ATP Synthesis",
        "description": "Functions of ER, Golgi apparatus, lysosomes (suicide bags), and mitochondria (powerhouse).",
        "key_formula": "Cellular respiration produces ATP (Adenosine Triphosphate)",
        "difficulty_baseline": "easy",
        "x": 280,
        "y": 380
    },
    {
        "id": "c9_plant_vascular_tissues",
        "grade": 9,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c9_tissues_structure",
        "name": "Vascular Bundles: Xylem vs Phloem",
        "description": "Xylem unidirectional water & mineral transport; Phloem bidirectional sucrose translocation.",
        "key_formula": "Xylem (tracheids/vessels) vs Phloem (sieve tubes/companion cells)",
        "difficulty_baseline": "easy",
        "x": 460,
        "y": 380
    },
    {
        "id": "c9_animal_epithelial_nervous",
        "grade": 9,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c9_tissues_structure",
        "name": "Animal Tissues: Muscular & Nervous Co-ordination",
        "description": "Striated, unstriated, and cardiac muscles; neuron architecture with axon, dendrites, and myelin sheath.",
        "key_formula": "Neuron: Cyton (cell body) -> Axon -> Synaptic terminals",
        "difficulty_baseline": "medium",
        "x": 640,
        "y": 380
    },
    # Math 9
    {
        "id": "c9_rationalization_surds",
        "grade": 9,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c9_number_systems_algebra",
        "name": "Surds & Conjugate Rationalization",
        "description": "Simplifying irrational radical denominators by multiplying with conjugate surds.",
        "key_formula": "1 / (sqrt(a) + sqrt(b)) = (sqrt(a) - sqrt(b)) / (a - b)",
        "difficulty_baseline": "medium",
        "x": 100,
        "y": 520
    },
    {
        "id": "c9_polynomial_remainder_factor",
        "grade": 9,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c9_number_systems_algebra",
        "name": "Remainder & Factor Theorems for Polynomials",
        "description": "Evaluating polynomial remainder p(a) upon division by (x - a); factoring cubic polynomials.",
        "key_formula": "If p(a) = 0, then (x - a) is a factor of p(x)",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 520
    },
    {
        "id": "c9_triangle_congruence",
        "grade": 9,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c9_lines_triangles_geometry",
        "name": "Criteria for Congruence of Triangles",
        "description": "Rigorous proof of triangle congruence using SAS, ASA, SSS, and RHS theorems.",
        "key_formula": "Corresponding Parts of Congruent Triangles are Equal (CPCTC)",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 520
    },
    {
        "id": "c9_parallel_lines_transversals",
        "grade": 9,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c9_lines_triangles_geometry",
        "name": "Parallel Lines, Transversals & Angle Properties",
        "description": "Alternate interior angles, corresponding angles, and co-interior angles supplementary.",
        "key_formula": "Angle 1 + Angle 2 = 180 degrees (consecutive interior)",
        "difficulty_baseline": "easy",
        "x": 640,
        "y": 520
    }
]

# ============================================================================
# CLASS 11 CURRICULUM (Senior Secondary / JEE / NEET Foundation)
# ============================================================================
CLASS_11_CHAPTERS = [
    # Physics 11
    {
        "id": "c11_rotational_dynamics",
        "grade": 11,
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Rotational Mechanics & Moment of Inertia",
        "order": 201,
        "description": "Torque, angular momentum conservation, center of mass, parallel/perpendicular axis theorems.",
        "icon": "RotateCcw",
        "color": "from-violet-500 to-indigo-600"
    },
    {
        "id": "c11_thermodynamics_heat",
        "grade": 11,
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Thermodynamics & Kinetic Theory",
        "order": 202,
        "description": "Zeroth, First & Second Laws of Thermo; isothermal, adiabatic, isobaric processes; Carnot engine.",
        "icon": "Flame",
        "color": "from-purple-500 to-pink-600"
    },
    # Chemistry 11
    {
        "id": "c11_chemical_bonding_mot",
        "grade": 11,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "title": "Chemical Bonding & Molecular Structure",
        "order": 203,
        "description": "VSEPR theory, hybridization (sp, sp2, sp3, dsp2), Molecular Orbital Theory (MOT), dipole moment.",
        "icon": "Atom",
        "color": "from-teal-500 to-emerald-600"
    },
    {
        "id": "c11_organic_principles",
        "grade": 11,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "title": "Organic Chemistry Fundamentals & Mechanisms",
        "order": 204,
        "description": "Inductive effect, electromeric, resonance/mesomeric, hyperconjugation, carbocations & radicals.",
        "icon": "FlaskConical",
        "color": "from-emerald-600 to-teal-700"
    },
    # Biology 11
    {
        "id": "c11_cell_cycle_division",
        "grade": 11,
        "subject_id": "biology",
        "subject_name": "Biology",
        "title": "Cell Cycle & Division (Mitosis / Meiosis)",
        "order": 205,
        "description": "Interphase (G1, S, G2), Mitosis stages, Meiosis crossing over (pachytene chiasmata), karyokinesis.",
        "icon": "Dna",
        "color": "from-rose-500 to-pink-600"
    },
    {
        "id": "c11_photosynthesis_higher_plants",
        "grade": 11,
        "subject_id": "biology",
        "subject_name": "Biology",
        "title": "Photosynthesis in Higher Plants (C3 / C4)",
        "order": 206,
        "description": "Light reaction Z-scheme, Calvin cycle (C3), Hatch-Slack pathway (C4 Kranz anatomy), photorespiration.",
        "icon": "Sun",
        "color": "from-red-500 to-rose-600"
    },
    # Mathematics 11
    {
        "id": "c11_conic_sections_geometry",
        "grade": 11,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "title": "Conic Sections (Parabola, Ellipse, Hyperbola)",
        "order": 207,
        "description": "Standard equations, eccentricity, foci, directrix, and latus rectum of parabolas and ellipses.",
        "icon": "Maximize2",
        "color": "from-violet-600 to-indigo-700"
    },
    {
        "id": "c11_limits_and_derivatives",
        "grade": 11,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "title": "Limits and Fundamental Calculus",
        "order": 208,
        "description": "Intuitive idea of derivatives, limits of polynomials/trig functions, First Principle of differentiation.",
        "icon": "TrendingUp",
        "color": "from-indigo-600 to-purple-600"
    }
]

CLASS_11_CONCEPTS = [
    # Physics 11
    {
        "id": "c11_torque_angular_momentum",
        "grade": 11,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c11_rotational_dynamics",
        "name": "Torque & Conservation of Angular Momentum",
        "description": "Rotational analog of force and linear momentum; L = I * omega = constant when net external torque is zero.",
        "key_formula": "tau = r x F = I * alpha; L = I * omega",
        "difficulty_baseline": "hard",
        "x": 100,
        "y": 100
    },
    {
        "id": "c11_moment_of_inertia_theorems",
        "grade": 11,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c11_rotational_dynamics",
        "name": "Moment of Inertia & Parallel/Perp Axis Theorems",
        "description": "Rotational inertia depends on mass distribution; I = I_cm + M*d^2 for parallel axes.",
        "key_formula": "I_parallel = I_cm + M * d^2; I_z = I_x + I_y",
        "difficulty_baseline": "hard",
        "x": 280,
        "y": 100
    },
    {
        "id": "c11_first_law_thermodynamics",
        "grade": 11,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c11_thermodynamics_heat",
        "name": "First Law of Thermodynamics & PV Diagrams",
        "description": "Conservation of energy in thermodynamic systems: heat supplied = change in internal energy + work done.",
        "key_formula": "Delta Q = Delta U + Delta W; Delta W = integral(P dV)",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 100
    },
    {
        "id": "c11_carnot_engine_entropy",
        "grade": 11,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c11_thermodynamics_heat",
        "name": "Carnot Cycle Efficiency & Second Law",
        "description": "Ideal reversible heat engine cycle consisting of two isothermals and two adiabatics.",
        "key_formula": "eta = 1 - (T_cold / T_hot)",
        "difficulty_baseline": "advanced",
        "x": 640,
        "y": 100
    },
    # Chemistry 11
    {
        "id": "c11_molecular_orbital_theory",
        "grade": 11,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c11_chemical_bonding_mot",
        "name": "Molecular Orbital Theory (MOT) & Bond Order",
        "description": "Linear combination of atomic orbitals (LCAO); bonding vs antibonding orbitals; paramagnetism of O2.",
        "key_formula": "Bond Order = 0.5 * (N_b - N_a)",
        "difficulty_baseline": "advanced",
        "x": 100,
        "y": 240
    },
    {
        "id": "c11_hybridization_vsepr",
        "grade": 11,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c11_chemical_bonding_mot",
        "name": "VSEPR Geometry & Atomic Orbital Hybridization",
        "description": "Prediction of molecular geometries (sp, sp2, sp3, sp3d) based on electron pair repulsions.",
        "key_formula": "Steric Number = Lone pairs + Sigma bonded atoms",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 240
    },
    {
        "id": "c11_resonance_hyperconjugation",
        "grade": 11,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c11_organic_principles",
        "name": "Resonance & Hyperconjugation in Carbocations",
        "description": "Delocalization of pi and sigma C-H electrons stabilizing 3° > 2° > 1° carbocations and free radicals.",
        "key_formula": "Carbocation stability: 3° > 2° > 1° > methyl",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 240
    },
    {
        "id": "c11_inductive_electromeric",
        "grade": 11,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c11_organic_principles",
        "name": "Inductive (-I/+I) & Electromeric Effects",
        "description": "Permanent electron polarization along sigma bonds versus temporary electron displacement in pi bonds.",
        "key_formula": "Carboxylic acid acidity increases with stronger -I electron withdrawing groups",
        "difficulty_baseline": "medium",
        "x": 640,
        "y": 240
    },
    # Biology 11
    {
        "id": "c11_meiosis_crossing_over",
        "grade": 11,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c11_cell_cycle_division",
        "name": "Meiotic Crossing Over & Recombination",
        "description": "Enzyme recombinase mediating genetic material exchange between non-sister chromatids of homologous chromosomes.",
        "key_formula": "Occurs in Pachytene substage of Prophase I",
        "difficulty_baseline": "hard",
        "x": 100,
        "y": 380
    },
    {
        "id": "c11_mitosis_cell_cycle_checkpoints",
        "grade": 11,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c11_cell_cycle_division",
        "name": "Mitotic Phases & Cell Cycle Checkpoints",
        "description": "Prophase, Metaphase (equatorial plate alignment), Anaphase (centromere split), Telophase, and G1/S cyclins.",
        "key_formula": "Chromatid separation in anaphase; cytokinesis furrow vs cell plate",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 380
    },
    {
        "id": "c11_calvin_cycle_c3",
        "grade": 11,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c11_photosynthesis_higher_plants",
        "name": "Calvin Cycle (C3) & RuBisCO Carboxylation",
        "description": "Carboxylation of RuBP into 3-PGA by RuBisCO, reduction to triose phosphate, and RuBP regeneration requiring ATP/NADPH.",
        "key_formula": "6 CO2 + 18 ATP + 12 NADPH -> 1 Glucose + 18 ADP + 12 NADP+",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 380
    },
    {
        "id": "c11_c4_kranz_anatomy",
        "grade": 11,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c11_photosynthesis_higher_plants",
        "name": "C4 Hatch-Slack Pathway & Kranz Anatomy",
        "description": "Spatial separation between mesophyll (PEP carboxylase) and bundle sheath cells eliminating photorespiration.",
        "key_formula": "PEP + CO2 -> Oxaloacetate (4C) via PEPcase",
        "difficulty_baseline": "advanced",
        "x": 640,
        "y": 380
    },
    # Math 11
    {
        "id": "c11_parabola_ellipse_eccentricity",
        "grade": 11,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c11_conic_sections_geometry",
        "name": "Parabola & Ellipse Equations and Eccentricity",
        "description": "Focus-directrix property; eccentricity e = 1 for parabola, e < 1 for ellipse; latus rectum length 4a or 2b^2/a.",
        "key_formula": "Parabola: y^2 = 4ax; Ellipse: x^2/a^2 + y^2/b^2 = 1, e = sqrt(1 - b^2/a^2)",
        "difficulty_baseline": "hard",
        "x": 100,
        "y": 520
    },
    {
        "id": "c11_hyperbola_standard_forms",
        "grade": 11,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c11_conic_sections_geometry",
        "name": "Hyperbola Standard Forms & Asymptotes",
        "description": "Locus of point whose distance difference from two foci is constant; eccentricity e > 1.",
        "key_formula": "x^2/a^2 - y^2/b^2 = 1, b^2 = a^2*(e^2 - 1)",
        "difficulty_baseline": "hard",
        "x": 280,
        "y": 520
    },
    {
        "id": "c11_first_principle_derivative",
        "grade": 11,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c11_limits_and_derivatives",
        "name": "First Principle of Differentiation",
        "description": "Instantaneous rate of change as limit of difference quotient delta y / delta x as h approaches 0.",
        "key_formula": "f'(x) = lim_{h -> 0} [f(x + h) - f(x)] / h",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 520
    },
    {
        "id": "c11_standard_limits_evaluation",
        "grade": 11,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c11_limits_and_derivatives",
        "name": "Evaluation of Trigonometric & Algebraic Limits",
        "description": "Indeterminate forms (0/0), Sandwich theorem, and fundamental trigonometric limits.",
        "key_formula": "lim_{x -> 0} [sin(x) / x] = 1; lim_{x -> a} (x^n - a^n)/(x - a) = n*a^(n-1)",
        "difficulty_baseline": "medium",
        "x": 640,
        "y": 520
    }
]

# ============================================================================
# CLASS 12 CURRICULUM (Senior Secondary Boards / JEE Advanced / NEET)
# ============================================================================
CLASS_12_CHAPTERS = [
    # Physics 12
    {
        "id": "c12_electrostatics_gauss",
        "grade": 12,
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Electrostatics and Gauss's Law",
        "order": 301,
        "description": "Coulomb's inverse square law, electric field flux, Gauss theorem, and potential of charge distributions.",
        "icon": "Zap",
        "color": "from-blue-600 to-indigo-600"
    },
    {
        "id": "c12_wave_optics_interference",
        "grade": 12,
        "subject_id": "physics",
        "subject_name": "Physics",
        "title": "Wave Optics: Interference & Diffraction",
        "order": 302,
        "description": "Huygens' wave theory, Young's Double Slit Experiment (YDSE), fringe width, single slit diffraction.",
        "icon": "Sparkles",
        "color": "from-cyan-500 to-blue-600"
    },
    # Chemistry 12
    {
        "id": "c12_electrochemistry_nernst",
        "grade": 12,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "title": "Electrochemistry & Nernst Equation",
        "order": 303,
        "description": "Galvanic & electrolytic cells, standard electrode potentials, Nernst equation, Kohlrausch's law.",
        "icon": "BatteryCharging",
        "color": "from-emerald-500 to-teal-600"
    },
    {
        "id": "c12_aldehydes_ketones_acids",
        "grade": 12,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "title": "Aldehydes, Ketones & Carboxylic Acids",
        "order": 304,
        "description": "Nucleophilic addition to carbonyls, Aldol condensation, Cannizzaro reaction, Hell-Volhard-Zelinsky (HVZ).",
        "icon": "FlaskConical",
        "color": "from-teal-600 to-green-700"
    },
    # Biology 12
    {
        "id": "c12_molecular_basis_inheritance",
        "grade": 12,
        "subject_id": "biology",
        "subject_name": "Biology",
        "title": "Molecular Basis of Inheritance (DNA/RNA)",
        "order": 305,
        "description": "Watson-Crick DNA double helix, semiconservative replication, transcription, Lac Operon, genetic code.",
        "icon": "Dna",
        "color": "from-rose-500 to-pink-600"
    },
    {
        "id": "c12_biotechnology_principles",
        "grade": 12,
        "subject_id": "biology",
        "subject_name": "Biology",
        "title": "Biotechnology: Genetic Engineering",
        "order": 306,
        "description": "Restriction endonucleases (molecular scissors), cloning vectors (pBR322), PCR amplification, gel electrophoresis.",
        "icon": "Cpu",
        "color": "from-pink-500 to-purple-600"
    },
    # Mathematics 12
    {
        "id": "c12_matrices_determinants",
        "grade": 12,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "title": "Matrices and Determinants",
        "order": 307,
        "description": "Matrix operations, transpose, adjoint and inverse, solving linear systems using Cramer's rule / matrix method.",
        "icon": "Grid",
        "color": "from-amber-500 to-orange-600"
    },
    {
        "id": "c12_calculus_integrals",
        "grade": 12,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "title": "Integral Calculus & Differential Equations",
        "order": 308,
        "description": "Definite integrals, substitution, integration by parts, area under curves, first-order differential equations.",
        "icon": "Sigma",
        "color": "from-orange-500 to-red-600"
    }
]

CLASS_12_CONCEPTS = [
    # Physics 12
    {
        "id": "c12_gauss_law_flux",
        "grade": 12,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c12_electrostatics_gauss",
        "name": "Gauss's Theorem & Electric Flux",
        "description": "Total electric flux through any closed surface equals net charge enclosed divided by permittivity of vacuum.",
        "key_formula": "Phi_E = oint E . dA = Q_enclosed / epsilon_0",
        "difficulty_baseline": "hard",
        "x": 100,
        "y": 100
    },
    {
        "id": "c12_electric_potential_capacitance",
        "grade": 12,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c12_electrostatics_gauss",
        "name": "Electrostatic Potential & Parallel Plate Capacitance",
        "description": "Work done per unit charge; capacitance with dielectric slab insertion C = K * epsilon_0 * A / d.",
        "key_formula": "V = Q / (4*pi*epsilon_0*r); C = K * epsilon_0 * A / d",
        "difficulty_baseline": "hard",
        "x": 280,
        "y": 100
    },
    {
        "id": "c12_ydse_interference",
        "grade": 12,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c12_wave_optics_interference",
        "name": "Young's Double Slit Experiment (YDSE)",
        "description": "Interference of coherent light waves; constructive path difference n*lambda, destructive (n - 0.5)*lambda.",
        "key_formula": "Fringe width beta = (lambda * D) / d",
        "difficulty_baseline": "advanced",
        "x": 460,
        "y": 100
    },
    {
        "id": "c12_single_slit_diffraction",
        "grade": 12,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c12_wave_optics_interference",
        "name": "Fraunhofer Single Slit Diffraction",
        "description": "Bending of light around aperture edges; central maximum width twice the secondary maxima.",
        "key_formula": "Minima condition: a * sin(theta) = n * lambda; Central width = 2 * lambda * D / a",
        "difficulty_baseline": "advanced",
        "x": 640,
        "y": 100
    },
    # Chemistry 12
    {
        "id": "c12_nernst_equation_potential",
        "grade": 12,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c12_electrochemistry_nernst",
        "name": "Nernst Equation & Cell EMF",
        "description": "Dependence of electrochemical cell potential on temperature and reactant/product ion concentrations.",
        "key_formula": "E_cell = E0_cell - (0.0591 / n) * log10(Q) [at 298 K]",
        "difficulty_baseline": "hard",
        "x": 100,
        "y": 240
    },
    {
        "id": "c12_kohlrausch_law_conductance",
        "grade": 12,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c12_electrochemistry_nernst",
        "name": "Kohlrausch's Law of Independent Ion Migration",
        "description": "Limiting molar conductivity of an electrolyte can be represented as the sum of individual ionic contributions.",
        "key_formula": "Lambda0_m = nu_+ * lambda0_+ + nu_- * lambda0_-",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 240
    },
    {
        "id": "c12_aldol_cannizzaro",
        "grade": 12,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c12_aldehydes_ketones_acids",
        "name": "Aldol Condensation & Cannizzaro Reaction",
        "description": "Enolate addition of aldehydes with alpha-hydrogens (Aldol) vs disproportionation of aldehydes without alpha-H (Cannizzaro).",
        "key_formula": "2CH3CHO -dil NaOH-> CH3-CH(OH)-CH2-CHO -heat-> CH3-CH=CH-CHO (Crotonaldehyde)",
        "difficulty_baseline": "advanced",
        "x": 460,
        "y": 240
    },
    {
        "id": "c12_nucleophilic_addition_carbonyls",
        "grade": 12,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c12_aldehydes_ketones_acids",
        "name": "Nucleophilic Addition to Carbonyl (>C=O)",
        "description": "Attack of nucleophiles (HCN, NaHSO3, Grignard reagents RMgX) on trigonal planar electrophilic carbonyl carbon.",
        "key_formula": "R-CHO + HCN -> R-CH(OH)-CN (Cyanohydrin formation)",
        "difficulty_baseline": "medium",
        "x": 640,
        "y": 240
    },
    # Biology 12
    {
        "id": "c12_semiconservative_replication",
        "grade": 12,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c12_molecular_basis_inheritance",
        "name": "Meselson-Stahl DNA Replication Proof",
        "description": "Experimental proof of semiconservative DNA replication using 15N/14N isotope density gradient centrifugation in CsCl.",
        "key_formula": "Each daughter DNA contains one parental and one freshly synthesized strand",
        "difficulty_baseline": "hard",
        "x": 100,
        "y": 380
    },
    {
        "id": "c12_lac_operon_regulation",
        "grade": 12,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c12_molecular_basis_inheritance",
        "name": "Lac Operon Transcriptional Regulation in E. coli",
        "description": "Inducible gene expression regulated by repressor binding to operator in absence/presence of allolactose inducer.",
        "key_formula": "Genes: lacZ (beta-gal), lacY (permease), lacA (transacetylase)",
        "difficulty_baseline": "advanced",
        "x": 280,
        "y": 380
    },
    {
        "id": "c12_restriction_enzymes_cloning",
        "grade": 12,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c12_biotechnology_principles",
        "name": "Restriction Endonucleases & Cloning Vectors",
        "description": "Molecular scissors cutting at palindromic sequences (e.g. EcoRI GAATTC) generating sticky ends for DNA ligase.",
        "key_formula": "pBR322 vector selectable markers: ampR and tetR",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 380
    },
    {
        "id": "c12_pcr_gel_electrophoresis",
        "grade": 12,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c12_biotechnology_principles",
        "name": "PCR Amplification & Agarose Gel Electrophoresis",
        "description": "Polymerase Chain Reaction: Denaturation (94C), Annealing (54C), Extension (72C via Taq polymerase).",
        "key_formula": "DNA amplification: 2^n copies after n cycles",
        "difficulty_baseline": "hard",
        "x": 640,
        "y": 380
    },
    # Math 12
    {
        "id": "c12_inverse_matrix_cramer",
        "grade": 12,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c12_matrices_determinants",
        "name": "Matrix Inversion & System of Linear Equations",
        "description": "Computing adj(A) / det(A) for non-singular square matrices and solving AX = B via X = A^(-1) B.",
        "key_formula": "A^(-1) = adj(A) / |A| (provided |A| != 0)",
        "difficulty_baseline": "hard",
        "x": 100,
        "y": 520
    },
    {
        "id": "c12_matrix_multiplication_rank",
        "grade": 12,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c12_matrices_determinants",
        "name": "Properties of Determinants & Matrix Multiplication",
        "description": "Row operations on determinants, cofactor expansion, and row-column matrix multiplication.",
        "key_formula": "|AB| = |A| * |B|; det(kA) = k^n * det(A)",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 520
    },
    {
        "id": "c12_integration_by_parts",
        "grade": 12,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c12_calculus_integrals",
        "name": "Integration by Parts & ILATE Rule",
        "description": "Evaluation of products of functions; order of priority: Inverse, Logarithmic, Algebraic, Trigonometric, Exponential.",
        "key_formula": "integral(u * v dx) = u * integral(v dx) - integral[u' * integral(v dx)] dx",
        "difficulty_baseline": "advanced",
        "x": 460,
        "y": 520
    },
    {
        "id": "c12_definite_integral_area",
        "grade": 12,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c12_calculus_integrals",
        "name": "Fundamental Theorem of Calculus & Area Under Curve",
        "description": "Evaluating definite integrals using antiderivatives and finding bounded area between intersecting curves.",
        "key_formula": "Area = integral_{a}^{b} |f(x) - g(x)| dx",
        "difficulty_baseline": "hard",
        "x": 640,
        "y": 520
    }
]

# ============================================================================
# CROSS-GRADE RELATIONSHIPS
# ============================================================================
CROSS_GRADE_RELATIONSHIPS = [
    # Grade 9 Motion -> Grade 10 Mechanics & Grade 11 Rotational
    {"source_concept_id": "c9_equations_of_motion", "target_concept_id": "c9_distance_time_graphs", "relationship_type": "prerequisite"},
    {"source_concept_id": "c9_universal_gravitation", "target_concept_id": "c9_archimedes_buoyancy", "relationship_type": "reinforces"},
    {"source_concept_id": "c9_latent_heat_evaporation", "target_concept_id": "c9_states_of_matter_diffusion", "relationship_type": "reinforces"},
    {"source_concept_id": "c9_mole_concept_dalton", "target_concept_id": "c9_chemical_formulae_valency", "relationship_type": "prerequisite"},
    {"source_concept_id": "c9_osmosis_plasma_membrane", "target_concept_id": "c9_cell_organelles_mitochondria", "relationship_type": "prerequisite"},
    {"source_concept_id": "c9_plant_vascular_tissues", "target_concept_id": "c9_animal_epithelial_nervous", "relationship_type": "reinforces"},
    {"source_concept_id": "c9_rationalization_surds", "target_concept_id": "c9_polynomial_remainder_factor", "relationship_type": "prerequisite"},
    {"source_concept_id": "c9_parallel_lines_transversals", "target_concept_id": "c9_triangle_congruence", "relationship_type": "prerequisite"},

    # Grade 11 Relationships
    {"source_concept_id": "c11_moment_of_inertia_theorems", "target_concept_id": "c11_torque_angular_momentum", "relationship_type": "prerequisite"},
    {"source_concept_id": "c11_first_law_thermodynamics", "target_concept_id": "c11_carnot_engine_entropy", "relationship_type": "prerequisite"},
    {"source_concept_id": "c11_hybridization_vsepr", "target_concept_id": "c11_molecular_orbital_theory", "relationship_type": "prerequisite"},
    {"source_concept_id": "c11_inductive_electromeric", "target_concept_id": "c11_resonance_hyperconjugation", "relationship_type": "prerequisite"},
    {"source_concept_id": "c11_mitosis_cell_cycle_checkpoints", "target_concept_id": "c11_meiosis_crossing_over", "relationship_type": "prerequisite"},
    {"source_concept_id": "c11_calvin_cycle_c3", "target_concept_id": "c11_c4_kranz_anatomy", "relationship_type": "reinforces"},
    {"source_concept_id": "c11_parabola_ellipse_eccentricity", "target_concept_id": "c11_hyperbola_standard_forms", "relationship_type": "reinforces"},
    {"source_concept_id": "c11_standard_limits_evaluation", "target_concept_id": "c11_first_principle_derivative", "relationship_type": "prerequisite"},

    # Grade 12 Relationships
    {"source_concept_id": "c12_gauss_law_flux", "target_concept_id": "c12_electric_potential_capacitance", "relationship_type": "prerequisite"},
    {"source_concept_id": "c12_ydse_interference", "target_concept_id": "c12_single_slit_diffraction", "relationship_type": "reinforces"},
    {"source_concept_id": "c12_nernst_equation_potential", "target_concept_id": "c12_kohlrausch_law_conductance", "relationship_type": "reinforces"},
    {"source_concept_id": "c12_nucleophilic_addition_carbonyls", "target_concept_id": "c12_aldol_cannizzaro", "relationship_type": "prerequisite"},
    {"source_concept_id": "c12_semiconservative_replication", "target_concept_id": "c12_lac_operon_regulation", "relationship_type": "reinforces"},
    {"source_concept_id": "c12_restriction_enzymes_cloning", "target_concept_id": "c12_pcr_gel_electrophoresis", "relationship_type": "prerequisite"},
    {"source_concept_id": "c12_matrix_multiplication_rank", "target_concept_id": "c12_inverse_matrix_cramer", "relationship_type": "prerequisite"},
    {"source_concept_id": "c12_integration_by_parts", "target_concept_id": "c12_definite_integral_area", "relationship_type": "prerequisite"}
]

# ============================================================================
# CROSS-GRADE QUESTIONS
# ============================================================================
CROSS_GRADE_QUESTIONS = [
    # ------------------ CLASS 9 QUESTIONS ------------------
    # Physics 9
    {
        "id": "q_g9_phy_01",
        "grade": 9,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c9_motion_kinematics",
        "concept_id": "c9_equations_of_motion",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "A racecar accelerates uniformly from rest to a speed of 30 m/s in 6 seconds. What total distance does it cover during this acceleration interval?",
        "options": [
            {"id": "A", "text": "90 meters"},
            {"id": "B", "text": "180 meters"},
            {"id": "C", "text": "45 meters"},
            {"id": "D", "text": "150 meters"}
        ],
        "correct_answer": "A",
        "explanation": "Initial velocity u = 0, final velocity v = 30 m/s, time t = 6 s. Acceleration a = (v - u)/t = 30/6 = 5 m/s^2. Distance s = ut + 0.5 * a * t^2 = 0 + 0.5 * 5 * 36 = 90 meters.",
        "expected_reasoning": "Compute a = 5 m/s^2 and apply s = 0.5*a*t^2 = 0.5*5*36 = 90 m.",
        "hint": "First calculate the acceleration a = (v - u)/t, then use s = ut + (1/2)at^2."
    },
    {
        "id": "q_g9_phy_02",
        "grade": 9,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c9_gravitation_flotation",
        "concept_id": "c9_universal_gravitation",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "Two spherical lead masses are separated by a distance d. If the distance between their centers is doubled while their masses remain unchanged, by what factor does the gravitational attraction change?",
        "options": [
            {"id": "A", "text": "It decreases to 1/4 of its original value"},
            {"id": "B", "text": "It decreases to 1/2 of its original value"},
            {"id": "C", "text": "It doubles (increases by 2x)"},
            {"id": "D", "text": "It remains constant"}
        ],
        "correct_answer": "A",
        "explanation": "According to Newton's Law of Universal Gravitation, F is inversely proportional to r^2 (F = G*m1*m2/d^2). When distance becomes 2d, F_new = G*m1*m2/(2d)^2 = F / 4.",
        "expected_reasoning": "Apply the inverse square law: doubling the distance divides the gravitational force by 2^2 = 4.",
        "hint": "Remember the inverse square law for gravitation: F proportional to 1 / d^2."
    },
    # Chemistry 9
    {
        "id": "q_g9_chem_01",
        "grade": 9,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c9_atoms_and_molecules",
        "concept_id": "c9_mole_concept_dalton",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "How many moles of water (H2O) molecules are present in a 36-gram sample of pure water? (Atomic masses: H = 1 u, O = 16 u)",
        "options": [
            {"id": "A", "text": "2.0 moles (approx 1.204 x 10^24 molecules)"},
            {"id": "B", "text": "1.0 mole (approx 6.022 x 10^23 molecules)"},
            {"id": "C", "text": "0.5 moles"},
            {"id": "D", "text": "18 moles"}
        ],
        "correct_answer": "A",
        "explanation": "Molar mass of H2O = 2(1) + 16 = 18 g/mol. Number of moles n = Mass / Molar mass = 36 g / 18 g/mol = 2.0 moles. In molecules: 2 * 6.022 x 10^23 = 1.2044 x 10^24 molecules.",
        "expected_reasoning": "Calculate molar mass of H2O = 18 g/mol, then divide sample mass (36 g) by 18 to yield 2 moles.",
        "hint": "Calculate the molecular mass of H2O first: 2*(1) + 16 = 18 g/mol."
    },
    # Biology 9
    {
        "id": "q_g9_bio_01",
        "grade": 9,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c9_fundamental_unit_cell",
        "concept_id": "c9_osmosis_plasma_membrane",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "A fresh plant cell with rigid cellulose cell wall is placed into a hypertonic salt solution. What phenomenon will be observed under a microscope?",
        "options": [
            {"id": "A", "text": "Plasmolysis: protoplast shrinks and pulls away from the cell wall"},
            {"id": "B", "text": "Lysis: the cell swells up and bursts open"},
            {"id": "C", "text": "Deplasmolysis: water rushes in making the cell turgid"},
            {"id": "D", "text": "No change because the plant cell wall is impermeable to water"}
        ],
        "correct_answer": "A",
        "explanation": "In a hypertonic medium, water moves out of the plant cell via exosmosis. Because the rigid cell wall maintains outer shape, the interior cytoplasm and plasma membrane shrink away, known as plasmolysis.",
        "expected_reasoning": "Water flows outward down the concentration gradient (exosmosis), shrinking the protoplasm away from the rigid wall.",
        "hint": "Hypertonic means higher solute concentration outside the cell, causing water to leave."
    },
    # Mathematics 9
    {
        "id": "q_g9_math_01",
        "grade": 9,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c9_number_systems_algebra",
        "concept_id": "c9_rationalization_surds",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "What is the rationalized form of 1 / (sqrt(5) - sqrt(2))?",
        "options": [
            {"id": "A", "text": "(sqrt(5) + sqrt(2)) / 3"},
            {"id": "B", "text": "(sqrt(5) + sqrt(2)) / 7"},
            {"id": "C", "text": "(sqrt(5) - sqrt(2)) / 3"},
            {"id": "D", "text": "sqrt(3)"}
        ],
        "correct_answer": "A",
        "explanation": "Multiply numerator and denominator by the conjugate (sqrt(5) + sqrt(2)). Denominator becomes (sqrt(5))^2 - (sqrt(2))^2 = 5 - 2 = 3. Thus the expression is (sqrt(5) + sqrt(2)) / 3.",
        "expected_reasoning": "Multiply numerator and denominator by conjugate (sqrt(5) + sqrt(2)) to obtain [sqrt(5) + sqrt(2)] / 3.",
        "hint": "Use the identity (a - b)(a + b) = a^2 - b^2 on the denominator."
    },

    # ------------------ CLASS 11 QUESTIONS ------------------
    # Physics 11
    {
        "id": "q_g11_phy_01",
        "grade": 11,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c11_rotational_dynamics",
        "concept_id": "c11_torque_angular_momentum",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "A spinning figure skater pulls her arms inward, reducing her moment of inertia to 0.5 times its initial value. Neglecting friction, what happens to her rotational kinetic energy?",
        "options": [
            {"id": "A", "text": "It doubles (increases by 100%) because angular momentum is conserved and work is done by muscles"},
            {"id": "B", "text": "It decreases by 50% due to reduced moment of inertia"},
            {"id": "C", "text": "It remains strictly constant because no external torque acts on the skater"},
            {"id": "D", "text": "It quadruples (increases by 300%)"}
        ],
        "correct_answer": "A",
        "explanation": "Angular momentum L = I * omega is conserved (no external torque). When I decreases to I/2, angular velocity omega doubles to 2*omega. Rotational kinetic energy K = L^2 / (2*I). Since I is halved while L is constant, K doubles (K_new = 2 * K_initial). The extra kinetic energy comes from the internal work done by the skater's arm muscles pulling inward against centrifugal forces.",
        "expected_reasoning": "Use K = L^2 / (2I). With conserved L, halving I doubles rotational kinetic energy.",
        "hint": "Write rotational kinetic energy in terms of angular momentum: K = L^2 / (2I)."
    },
    # Chemistry 11
    {
        "id": "q_g11_chem_01",
        "grade": 11,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c11_chemical_bonding_mot",
        "concept_id": "c11_molecular_orbital_theory",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "According to Molecular Orbital Theory (MOT), what is the bond order and magnetic behavior of the oxygen molecule (O2)?",
        "options": [
            {"id": "A", "text": "Bond order = 2, Paramagnetic (two unpaired electrons in pi* antibonding orbitals)"},
            {"id": "B", "text": "Bond order = 2, Diamagnetic (all electrons are paired)"},
            {"id": "C", "text": "Bond order = 2.5, Paramagnetic"},
            {"id": "D", "text": "Bond order = 1, Diamagnetic"}
        ],
        "correct_answer": "A",
        "explanation": "O2 has 16 electrons. Its electronic configuration in MOT puts 10 electrons in bonding orbitals and 6 in antibonding orbitals. Bond order = (10 - 6)/2 = 2. The two highest energy electrons occupy degenerate pi*2px and pi*2py antibonding orbitals singly with parallel spins, explaining why liquid O2 is paramagnetic.",
        "expected_reasoning": "Calculate Bond Order = (N_b - N_a)/2 = (10 - 6)/2 = 2, with 2 unpaired electrons in pi* orbitals conferring paramagnetism.",
        "hint": "Remember Hund's rule applies when filling degenerate pi* antibonding molecular orbitals."
    },
    # Biology 11
    {
        "id": "q_g11_bio_01",
        "grade": 11,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c11_cell_cycle_division",
        "concept_id": "c11_meiosis_crossing_over",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "In which specific sub-stage of Prophase I in meiosis does crossing over between non-sister chromatids take place?",
        "options": [
            {"id": "A", "text": "Pachytene (mediated by recombinase enzyme)"},
            {"id": "B", "text": "Zygotene (synaptonemal complex formation)"},
            {"id": "C", "text": "Diplotene (chiasmata dissolution)"},
            {"id": "D", "text": "Leptotene (chromatin condensation)"}
        ],
        "correct_answer": "A",
        "explanation": "Crossing over occurs during the Pachytene stage of Prophase I. During this stage, recombination nodules appear where non-sister chromatids of homologous chromosomes exchange genetic segments via the enzyme recombinase.",
        "expected_reasoning": "Recall Prophase I substages: Leptotene -> Zygotene (synapsis) -> Pachytene (crossing over) -> Diplotene (chiasmata) -> Diakinesis.",
        "hint": "The stages are Leptotene, Zygotene, Pachytene, Diplotene, Diakinesis."
    },
    # Mathematics 11
    {
        "id": "q_g11_math_01",
        "grade": 11,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c11_limits_and_derivatives",
        "concept_id": "c11_first_principle_derivative",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "Using the First Principle of differentiation, what is the derivative of f(x) = sin(x)?",
        "options": [
            {"id": "A", "text": "cos(x)"},
            {"id": "B", "text": "-cos(x)"},
            {"id": "C", "text": "sec^2(x)"},
            {"id": "D", "text": "sin(x)"}
        ],
        "correct_answer": "A",
        "explanation": "f'(x) = lim_{h->0} [sin(x + h) - sin(x)] / h = lim_{h->0} [2 * cos(x + h/2) * sin(h/2)] / h = lim_{h->0} [cos(x + h/2)] * [sin(h/2) / (h/2)] = cos(x) * 1 = cos(x).",
        "expected_reasoning": "Apply sin(C) - sin(D) formula inside difference quotient limit, yielding cos(x).",
        "hint": "Use the formula sin(C) - sin(D) = 2 * cos((C+D)/2) * sin((C-D)/2)."
    },

    # ------------------ CLASS 12 QUESTIONS ------------------
    # Physics 12
    {
        "id": "q_g12_phy_01",
        "grade": 12,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c12_wave_optics_interference",
        "concept_id": "c12_ydse_interference",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "In a Young's Double Slit Experiment, the slit separation is halved while the screen distance is doubled. What is the ratio of the new fringe width to the original fringe width?",
        "options": [
            {"id": "A", "text": "4 : 1 (Fringe width quadruples)"},
            {"id": "B", "text": "2 : 1 (Fringe width doubles)"},
            {"id": "C", "text": "1 : 1 (Fringe width remains unchanged)"},
            {"id": "D", "text": "1 : 4 (Fringe width quarters)"}
        ],
        "correct_answer": "A",
        "explanation": "Fringe width is given by beta = (lambda * D) / d. If screen distance D becomes 2D and slit separation d becomes d/2, then beta_new = [lambda * (2D)] / (d/2) = 4 * (lambda * D / d) = 4 * beta. Thus the fringe width quadruples.",
        "expected_reasoning": "Substitute D' = 2D and d' = d/2 into beta = lambda*D/d to yield 4x original width.",
        "hint": "Look at how beta depends directly on D and inversely on d."
    },
    {
        "id": "q_g12_phy_02",
        "grade": 12,
        "subject_id": "physics",
        "subject_name": "Physics",
        "chapter_id": "c12_electrostatics_gauss",
        "concept_id": "c12_gauss_law_flux",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "A point charge +q is positioned at the geometric center of a regular cube of side L. What is the electric flux passing through one face of the cube?",
        "options": [
            {"id": "A", "text": "q / (6 * epsilon_0)"},
            {"id": "B", "text": "q / epsilon_0"},
            {"id": "C", "text": "q / (8 * epsilon_0)"},
            {"id": "D", "text": "q * L^2 / (6 * epsilon_0)"}
        ],
        "correct_answer": "A",
        "explanation": "By Gauss's Law, the total electric flux through all 6 faces of the closed cube is Phi_total = q / epsilon_0. Since the cube is completely symmetrical with the charge at its center, the flux divides equally across each of the 6 identical faces: Phi_face = Phi_total / 6 = q / (6 * epsilon_0).",
        "expected_reasoning": "Apply Gauss's Law for the whole cube: q / epsilon_0, then divide by 6 identical symmetric faces.",
        "hint": "The charge is symmetric with respect to all 6 faces of the cube."
    },
    # Chemistry 12
    {
        "id": "q_g12_chem_01",
        "grade": 12,
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "c12_electrochemistry_nernst",
        "concept_id": "c12_nernst_equation_potential",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "For the Daniell cell Zn(s) | Zn2+(aq) || Cu2+(aq) | Cu(s), what happens to the cell potential (E_cell) if the concentration of Zn2+ ions is increased while Cu2+ concentration is kept constant at 298 K?",
        "options": [
            {"id": "A", "text": "E_cell decreases in accordance with the Nernst Equation"},
            {"id": "B", "text": "E_cell increases because more zinc ions participate in conduction"},
            {"id": "C", "text": "E_cell remains constant since standard potential E0 is fixed"},
            {"id": "D", "text": "The cell reverses polarity immediately"}
        ],
        "correct_answer": "A",
        "explanation": "Nernst equation for Daniell cell is E_cell = E0_cell - (0.0591 / 2) * log10([Zn2+] / [Cu2+]). Increasing [Zn2+] increases the reaction quotient Q = [Zn2+]/[Cu2+], which increases the logarithmic subtraction term, thereby reducing E_cell.",
        "expected_reasoning": "Use Nernst equation: E_cell = E0 - (0.0591/n)*log10([Zn2+]/[Cu2+]). Increasing numerator reduces cell EMF.",
        "hint": "Check the sign before the log term in the Nernst equation: E = E0 - (RT/nF)ln(Q)."
    },
    # Biology 12
    {
        "id": "q_g12_bio_01",
        "grade": 12,
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "c12_molecular_basis_inheritance",
        "concept_id": "c12_semiconservative_replication",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "E. coli cells grown in 15N heavy nitrogen medium are transferred to 14N light medium and allowed to replicate for one generation (20 minutes). In CsCl density centrifugation, what banding pattern proves semiconservative replication?",
        "options": [
            {"id": "A", "text": "A single hybrid 15N/14N intermediate density band"},
            {"id": "B", "text": "Two bands: 50% purely heavy 15N and 50% purely light 14N"},
            {"id": "C", "text": "A single pure light 14N band"},
            {"id": "D", "text": "Three equal bands corresponding to light, hybrid, and heavy"}
        ],
        "correct_answer": "A",
        "explanation": "In Meselson and Stahl's experiment, after 1 generation of replication in 14N medium, every newly formed double helix contained one old heavy 15N strand and one new light 14N strand. This resulted in 100% hybrid density DNA, disproving the conservative replication model.",
        "expected_reasoning": "Meselson-Stahl 1st generation yields 100% hybrid 15N/14N DNA of intermediate density.",
        "hint": "Conservative would yield two distinct bands; semiconservative yields an intermediate hybrid."
    },
    # Mathematics 12
    {
        "id": "q_g12_math_01",
        "grade": 12,
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "c12_calculus_integrals",
        "concept_id": "c12_integration_by_parts",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "Evaluate the indefinite integral: integral of x * e^x dx.",
        "options": [
            {"id": "A", "text": "e^x * (x - 1) + C"},
            {"id": "B", "text": "e^x * (x + 1) + C"},
            {"id": "C", "text": "(x^2 / 2) * e^x + C"},
            {"id": "D", "text": "x * e^x + C"}
        ],
        "correct_answer": "A",
        "explanation": "By ILATE rule, choose u = x (algebraic) and dv = e^x dx (exponential). du = dx, v = e^x. Using integral(u dv) = u*v - integral(v du): x * e^x - integral(e^x dx) = x * e^x - e^x + C = e^x * (x - 1) + C.",
        "expected_reasoning": "Apply Integration by Parts with u = x and dv = e^x dx: x*e^x - integral(e^x dx) = e^x*(x - 1) + C.",
        "hint": "Use Integration by Parts: integral(u v') = u v - integral(u' v)."
    }
]

# ============================================================================
# CROSS-GRADE MISCONCEPTIONS
# ============================================================================
CROSS_GRADE_MISCONCEPTIONS = [
    {
        "id": "misc_g9_heavier_falls_faster",
        "grade": 9,
        "subject_id": "physics",
        "concept_id": "c9_universal_gravitation",
        "name": "Heavier objects fall faster in a vacuum",
        "description": "Student believes gravitational acceleration depends on the falling object's mass.",
        "remediation": "In vacuum, acceleration due to gravity g = G*M_earth / R^2, which is completely independent of the falling object's mass.",
        "remediation_activity": "Galileo Leaning Tower of Pisa simulation in vacuum tube."
    },
    {
        "id": "misc_g11_angular_momentum_torque",
        "grade": 11,
        "subject_id": "physics",
        "concept_id": "c11_torque_angular_momentum",
        "name": "Kinetic energy is conserved when moment of inertia changes",
        "description": "Student confuses conservation of angular momentum with conservation of mechanical kinetic energy.",
        "remediation": "When a figure skater pulls arms inward, work is done by arm muscles against centrifugal inertial force, increasing rotational kinetic energy (K = L^2 / 2I).",
        "remediation_activity": "Interactive spinning turntable skater simulation."
    },
    {
        "id": "misc_g12_gauss_surface_dependent",
        "grade": 12,
        "subject_id": "physics",
        "concept_id": "c12_gauss_law_flux",
        "name": "Electric flux depends on the size and shape of the closed Gaussian surface",
        "description": "Student assumes larger Gaussian sphere encloses less electric flux.",
        "remediation": "By Gauss's Law, total enclosed flux depends solely on Q_enclosed / epsilon_0, regardless of the surface geometry or radius.",
        "remediation_activity": "Variable radius Gaussian bubble interactive visualization."
    }
]
