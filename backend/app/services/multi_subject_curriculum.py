"""
Comprehensive Curriculum for Chemistry, Biology, and Mathematics (Class 10 CBSE/ICSE).
Expands Learnix AI from Physics-only into a complete multi-subject STEM platform.
"""

from typing import List, Dict, Any

SUBJECTS = [
    {
        "id": "physics",
        "name": "Physics",
        "icon": "Zap",
        "color": "from-blue-600 to-indigo-600",
        "badgeColor": "bg-blue-50 text-blue-700 border-blue-200",
        "gradient": "bg-gradient-to-tr from-blue-600 to-indigo-600",
        "tagline": "Electricity, Optics, Magnetism & Force",
        "accent": "blue"
    },
    {
        "id": "chemistry",
        "name": "Chemistry",
        "icon": "FlaskConical",
        "color": "from-emerald-600 to-teal-600",
        "badgeColor": "bg-emerald-50 text-emerald-700 border-emerald-200",
        "gradient": "bg-gradient-to-tr from-emerald-600 to-teal-600",
        "tagline": "Reactions, Acids, Metals & Carbon Compounds",
        "accent": "emerald"
    },
    {
        "id": "biology",
        "name": "Biology",
        "icon": "Dna",
        "color": "from-rose-600 to-pink-600",
        "badgeColor": "bg-rose-50 text-rose-700 border-rose-200",
        "gradient": "bg-gradient-to-tr from-rose-600 to-pink-600",
        "tagline": "Life Processes, Control, Genetics & Reproduction",
        "accent": "rose"
    },
    {
        "id": "mathematics",
        "name": "Mathematics",
        "icon": "Sigma",
        "color": "from-amber-500 to-orange-600",
        "badgeColor": "bg-amber-50 text-amber-700 border-amber-200",
        "gradient": "bg-gradient-to-tr from-amber-500 to-orange-600",
        "tagline": "Algebra, Trigonometry, Geometry & Sequences",
        "accent": "amber"
    }
]

# ============================================================================
# CHEMISTRY CHAPTERS & CONCEPTS
# ============================================================================
CHEMISTRY_CHAPTERS = [
    {
        "id": "chemical_reactions_equations",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "title": "Chemical Reactions & Equations",
        "order": 7,
        "description": "Conservation of mass, balancing equations, reaction types (redox, displacement), and rancidity.",
        "icon": "FlaskConical",
        "color": "from-emerald-500 to-teal-600"
    },
    {
        "id": "acids_bases_salts",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "title": "Acids, Bases & Salts",
        "order": 8,
        "description": "pH scale, indicators, neutralization, and manufacturing of baking soda, washing soda & POP.",
        "icon": "Beaker",
        "color": "from-teal-500 to-cyan-600"
    },
    {
        "id": "metals_and_non_metals",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "title": "Metals and Non-Metals",
        "order": 9,
        "description": "Reactivity series, ionic bond crystal structures, metallurgical extraction, and corrosion.",
        "icon": "Layers",
        "color": "from-green-500 to-emerald-600"
    },
    {
        "id": "carbon_and_compounds",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "title": "Carbon and its Compounds",
        "order": 10,
        "description": "Covalent bonding, catenation, homologous series, functional groups, and esterification.",
        "icon": "Atom",
        "color": "from-teal-600 to-indigo-700"
    }
]

CHEMISTRY_CONCEPTS = [
    # Chemical Reactions
    {
        "id": "c_balancing_equations",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "chemical_reactions_equations",
        "name": "Law of Conservation of Mass & Balancing",
        "description": "Total mass of reactants equals total mass of products; balancing atom coefficients.",
        "key_formula": "Total mass(reactants) = Total mass(products)",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 100
    },
    {
        "id": "c_reaction_types",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "chemical_reactions_equations",
        "name": "Types of Chemical Reactions",
        "description": "Combination, decomposition, displacement, and double displacement precipitation.",
        "key_formula": "A + B -> AB (Combination), AB -> A + B (Decomp)",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 100
    },
    {
        "id": "c_redox_reactions",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "chemical_reactions_equations",
        "name": "Redox Reactions (Oxidation & Reduction)",
        "description": "Simultaneous gain/loss of oxygen and hydrogen; electronic transfer of electrons.",
        "key_formula": "Oxidation: loss of e- / gain of O; Reduction: gain of e- / loss of O",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 100
    },
    {
        "id": "c_corrosion_rancidity",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "chemical_reactions_equations",
        "name": "Corrosion & Rancidity Prevention",
        "description": "Oxidation of metals (rusting) and fats/oils; antioxidants, nitrogen flushing, galvanization.",
        "key_formula": "4Fe + 3O2 + 2xH2O -> 2Fe2O3.xH2O (Hydrated iron oxide)",
        "difficulty_baseline": "easy",
        "x": 640,
        "y": 100
    },

    # Acids, Bases & Salts
    {
        "id": "c_acid_base_indicators",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "acids_bases_salts",
        "name": "Acid-Base Indicators & Olfactory Tests",
        "description": "Litmus, phenolphthalein (pink in base), methyl orange, vanilla essence, and clove oil.",
        "key_formula": "Phenolphthalein: Colorless in Acid, Bright Pink in Base",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 240
    },
    {
        "id": "c_ph_scale",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "acids_bases_salts",
        "name": "pH Scale & Universal Indicators",
        "description": "Logarithmic measure of hydronium ion concentration [H3O+]; neutral at pH 7, acidic < 7, basic > 7.",
        "key_formula": "pH = -log10[H3O+], pH + pOH = 14",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 240
    },
    {
        "id": "c_salts_manufacturing",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "acids_bases_salts",
        "name": "Industrial Salts (Baking Soda & Bleaching Powder)",
        "description": "Chlor-alkali process, CaOCl2 bleaching powder, NaHCO3 baking soda, and CaSO4.1/2H2O POP.",
        "key_formula": "NaCl + H2O + CO2 + NH3 -> NH4Cl + NaHCO3 (Solvay)",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 240
    },
    {
        "id": "c_water_crystallization",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "acids_bases_salts",
        "name": "Water of Crystallization & Efflorescence",
        "description": "Fixed stoichiometric water molecules in crystal lattices (CuSO4.5H2O, Na2CO3.10H2O).",
        "key_formula": "CuSO4.5H2O (Blue) -heat-> CuSO4 (White anhydrous) + 5H2O",
        "difficulty_baseline": "medium",
        "x": 640,
        "y": 240
    },

    # Metals and Non-Metals
    {
        "id": "c_reactivity_series",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "metals_and_non_metals",
        "name": "Reactivity Series of Metals",
        "description": "Hierarchy: K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au.",
        "key_formula": "Zn(s) + CuSO4(aq) -> ZnSO4(aq) + Cu(s) (Displacement)",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 380
    },
    {
        "id": "c_ionic_compounds",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "metals_and_non_metals",
        "name": "Formation & Properties of Ionic Bonds",
        "description": "Complete electron transfer from metal cation to non-metal anion; high MP/BP and molten conductivity.",
        "key_formula": "Na -> Na+ + e-, Cl + e- -> Cl- ==> [Na+][Cl-]",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 380
    },
    {
        "id": "c_metallurgy_extraction",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "metals_and_non_metals",
        "name": "Metallurgy: Roasting & Calcination",
        "description": "Roasting sulphide ores in excess air; calcination of carbonate ores; thermite reaction.",
        "key_formula": "2ZnS + 3O2 -heat-> 2ZnO + 2SO2 (Roasting)",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 380
    },

    # Carbon and its Compounds
    {
        "id": "c_covalent_bonding_carbon",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "carbon_and_compounds",
        "name": "Covalent Bonding & Tetravalency",
        "description": "Electron sharing by carbon (valency 4) avoiding C4+ or C4- ions; catenation capability.",
        "key_formula": "Tetrahedral sp3 geometry in methane (CH4)",
        "difficulty_baseline": "medium",
        "x": 100,
        "y": 520
    },
    {
        "id": "c_homologous_series",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "carbon_and_compounds",
        "name": "Homologous Series & Isomerism",
        "description": "Series of organic compounds with same functional group differing by -CH2- unit (14 u).",
        "key_formula": "Alkanes: CnH2n+2, Alkenes: CnH2n, Alkynes: CnH2n-2",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 520
    },
    {
        "id": "c_functional_groups",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "carbon_and_compounds",
        "name": "Functional Groups & IUPAC Nomenclature",
        "description": "Alcohols (-OH), Aldehydes (-CHO), Ketones (-CO-), Carboxylic Acids (-COOH).",
        "key_formula": "R-OH (ol), R-CHO (al), R-CO-R' (one), R-COOH (oic acid)",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 520
    },
    {
        "id": "c_esterification_saponification",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "carbon_and_compounds",
        "name": "Esterification & Saponification Reactions",
        "description": "Acid + alcohol gives sweet-smelling ester; ester + alkali gives soap (sodium salt of fatty acid).",
        "key_formula": "CH3COOH + C2H5OH -H2SO4-> CH3COOC2H5 + H2O",
        "difficulty_baseline": "hard",
        "x": 640,
        "y": 520
    }
]

# ============================================================================
# BIOLOGY CHAPTERS & CONCEPTS
# ============================================================================
BIOLOGY_CHAPTERS = [
    {
        "id": "life_processes",
        "subject_id": "biology",
        "subject_name": "Biology",
        "title": "Life Processes",
        "order": 11,
        "description": "Autotrophic nutrition, aerobic respiration, double circulation, and renal nephron excretion.",
        "icon": "HeartPulse",
        "color": "from-rose-500 to-pink-600"
    },
    {
        "id": "control_and_coordination",
        "subject_id": "biology",
        "subject_name": "Biology",
        "title": "Control and Coordination",
        "order": 12,
        "description": "Neuron structure, synaptic transmission, reflex arc, phytohormones, and endocrine glands.",
        "icon": "Brain",
        "color": "from-pink-500 to-purple-600"
    },
    {
        "id": "how_do_organisms_reproduce",
        "subject_id": "biology",
        "subject_name": "Biology",
        "title": "How do Organisms Reproduce?",
        "order": 13,
        "description": "Asexual fission/budding, angiosperm double fertilization, and human reproductive anatomy.",
        "icon": "Dna",
        "color": "from-red-500 to-rose-600"
    },
    {
        "id": "heredity_and_evolution",
        "subject_id": "biology",
        "subject_name": "Biology",
        "title": "Heredity and Genetics",
        "order": 14,
        "description": "Mendelian inheritance, monohybrid & dihybrid ratios, sex determination, and ecosystems.",
        "icon": "Share2",
        "color": "from-rose-600 to-amber-600"
    }
]

BIOLOGY_CONCEPTS = [
    # Life Processes
    {
        "id": "c_photosynthesis_stomata",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "life_processes",
        "name": "Photosynthesis & Guard Cell Regulation",
        "description": "Light absorption by chlorophyll, photolysis of water, and turgor-driven stomatal pores.",
        "key_formula": "6CO2 + 12H2O -light/chlorophyll-> C6H12O6 + 6O2 + 6H2O",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 100
    },
    {
        "id": "c_cellular_respiration",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "life_processes",
        "name": "Cellular Respiration (Aerobic vs Anaerobic)",
        "description": "Cytoplasmic glycolysis into pyruvate; mitochondrial Krebs cycle (38 ATP) vs lactic acid fermentation.",
        "key_formula": "Glucose -> 2 Pyruvate -> CO2 + H2O + 38 ATP (Mitochondria)",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 100
    },
    {
        "id": "c_human_double_circulation",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "life_processes",
        "name": "Human Heart & Double Circulation",
        "description": "Four chambers preventing mixing of oxygenated/deoxygenated blood; systemic & pulmonary loops.",
        "key_formula": "Blood passes twice through heart per complete bodily circuit",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 100
    },
    {
        "id": "c_nephron_ultrafiltration",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "life_processes",
        "name": "Excretion & Nephron Filtration",
        "description": "Glomerular high-pressure ultrafiltration, selective tubular reabsorption (glucose, amino acids, salts).",
        "key_formula": "Urine = Glomerular Filtrate - Tubular Reabsorption + Tubular Secretion",
        "difficulty_baseline": "hard",
        "x": 640,
        "y": 100
    },

    # Control and Coordination
    {
        "id": "c_neuron_synapse",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "control_and_coordination",
        "name": "Neuron Anatomy & Synaptic Transmission",
        "description": "Dendrite receiving impulse, axon electrical conduction, neurotransmitter chemical diffusion across synapse.",
        "key_formula": "Electrical impulse (Axon) -> Chemical signal (Synapse) -> Electrical impulse (Dendrite)",
        "difficulty_baseline": "medium",
        "x": 100,
        "y": 240
    },
    {
        "id": "c_reflex_arc",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "control_and_coordination",
        "name": "Reflex Arc & Spinal Integration",
        "description": "Involuntary rapid response bypassing brain: Receptor -> Sensory neuron -> Relay neuron -> Motor neuron -> Effector.",
        "key_formula": "Receptor -> Sensory Neuron -> Spinal Relay -> Motor Neuron -> Muscle",
        "difficulty_baseline": "easy",
        "x": 280,
        "y": 240
    },
    {
        "id": "c_plant_hormones_tropisms",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "control_and_coordination",
        "name": "Phytohormones & Tropic Movements",
        "description": "Auxins (phototropism tip elongation), Gibberellins (internode growth), Cytokinins, Abscisic acid (wilting).",
        "key_formula": "Auxin diffuses to shaded side, causing asymmetrical cell elongation",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 240
    },
    {
        "id": "c_human_endocrine_system",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "control_and_coordination",
        "name": "Human Endocrine System & Feedback",
        "description": "Thyroxine (iodine/metabolism), Insulin (pancreatic blood sugar regulation), Adrenaline (fight-or-flight).",
        "key_formula": "Negative feedback loop: High blood glucose -> Pancreas secretes Insulin -> Uptake into cells",
        "difficulty_baseline": "hard",
        "x": 640,
        "y": 240
    },

    # Reproduction
    {
        "id": "c_asexual_reproduction_modes",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "how_do_organisms_reproduce",
        "name": "Modes of Asexual Reproduction",
        "description": "Binary fission (Amoeba), multiple fission (Plasmodium), budding (Hydra), regeneration (Planaria), spore formation.",
        "key_formula": "Single parent produces genetically identical clonal offspring",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 380
    },
    {
        "id": "c_flower_sexual_reproduction",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "how_do_organisms_reproduce",
        "name": "Flowering Plant Sexual Reproduction",
        "description": "Stamen (anther/filament) pollen, Pistil (stigma/style/ovary), pollen tube germination, double fertilization.",
        "key_formula": "Syngamy (Egg + Sperm = Zygote) + Triple Fusion (Polar nuclei + Sperm = Endosperm)",
        "difficulty_baseline": "hard",
        "x": 280,
        "y": 380
    },
    {
        "id": "c_human_reproduction_contraception",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "how_do_organisms_reproduce",
        "name": "Human Reproductive Cycle & Health",
        "description": "Gametogenesis, fertilization in fallopian tube, implantation in uterus, contraception methods (barrier, chemical, surgical).",
        "key_formula": "Sperm (23) + Ovum (23) -> Zygote (46 diploid chromosomes)",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 380
    },

    # Heredity
    {
        "id": "c_mendel_monohybrid_cross",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "heredity_and_evolution",
        "name": "Mendel's Monohybrid Cross & Dominance",
        "description": "Inheritance of single trait (tall vs dwarf); F1 all tall (Tt); F2 phenotypic ratio 3:1, genotypic ratio 1:2:1.",
        "key_formula": "Phenotypic: 3 Tall : 1 Dwarf; Genotypic: 1 TT : 2 Tt : 1 tt",
        "difficulty_baseline": "medium",
        "x": 100,
        "y": 520
    },
    {
        "id": "c_mendel_dihybrid_cross",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "heredity_and_evolution",
        "name": "Dihybrid Cross & Independent Assortment",
        "description": "Inheritance of two independent pairs of traits (round yellow vs wrinkled green seeds); F2 ratio 9:3:3:1.",
        "key_formula": "9 Round Yellow : 3 Round Green : 3 Wrinkled Yellow : 1 Wrinkled Green",
        "difficulty_baseline": "hard",
        "x": 280,
        "y": 520
    },
    {
        "id": "c_human_sex_determination",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "heredity_and_evolution",
        "name": "Sex Determination in Humans",
        "description": "All human eggs carry X chromosome; sperm carries 50% X and 50% Y. Father's sperm determines biological sex.",
        "key_formula": "XX = Female, XY = Male (50% statistical probability)",
        "difficulty_baseline": "easy",
        "x": 460,
        "y": 520
    },
    {
        "id": "c_trophic_levels_biomagnification",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "heredity_and_evolution",
        "name": "10% Energy Law & Biomagnification",
        "description": "Only 10% of energy transfers to next trophic level (Lindeman); progressive pesticide accumulation.",
        "key_formula": "Energy at Level(n+1) = 0.10 * Energy at Level(n)",
        "difficulty_baseline": "medium",
        "x": 640,
        "y": 520
    }
]

# ============================================================================
# MATHEMATICS CHAPTERS & CONCEPTS
# ============================================================================
MATH_CHAPTERS = [
    {
        "id": "real_numbers_polynomials",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "title": "Real Numbers & Polynomials",
        "order": 15,
        "description": "Fundamental Theorem of Arithmetic, irrationality proofs, zeroes and coefficients of polynomials.",
        "icon": "Sigma",
        "color": "from-amber-500 to-orange-600"
    },
    {
        "id": "quadratic_equations_ap",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "title": "Quadratic Equations & AP",
        "order": 16,
        "description": "Quadratic formula, discriminant nature of roots, nth term and sum of Arithmetic Progressions.",
        "icon": "TrendingUp",
        "color": "from-orange-500 to-red-600"
    },
    {
        "id": "triangles_coordinate_geometry",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "title": "Triangles & Coordinate Geometry",
        "order": 17,
        "description": "Basic Proportionality Theorem, similarity criteria, distance formula, and internal section formula.",
        "icon": "Maximize2",
        "color": "from-yellow-500 to-amber-600"
    },
    {
        "id": "trigonometry_applications",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "title": "Trigonometry & Heights/Distances",
        "order": 18,
        "description": "Trigonometric ratios, identities (sin²θ + cos²θ = 1), and real-world angle of elevation calculations.",
        "icon": "Compass",
        "color": "from-amber-600 to-indigo-700"
    }
]

MATH_CONCEPTS = [
    # Real Numbers & Polynomials
    {
        "id": "c_fundamental_theorem_arithmetic",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "real_numbers_polynomials",
        "name": "Fundamental Theorem of Arithmetic (HCF & LCM)",
        "description": "Every composite number can be uniquely expressed as product of primes; HCF(a,b) * LCM(a,b) = a * b.",
        "key_formula": "HCF(a, b) * LCM(a, b) = a * b",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 100
    },
    {
        "id": "c_irrationality_proof",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "real_numbers_polynomials",
        "name": "Proof of Irrationality by Contradiction",
        "description": "Rigorous proof for irrationality of sqrt(2), sqrt(3), and 5 - sqrt(3) using coprime assumptions.",
        "key_formula": "If p divides a^2, then prime p divides a",
        "difficulty_baseline": "medium",
        "x": 280,
        "y": 100
    },
    {
        "id": "c_polynomial_zeroes_coefficients",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "real_numbers_polynomials",
        "name": "Zeroes & Coefficients of Quadratic Polynomials",
        "description": "For ax^2 + bx + c: sum of zeroes alpha + beta = -b/a, product of zeroes alpha * beta = c/a.",
        "key_formula": "alpha + beta = -b/a, alpha * beta = c/a",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 100
    },

    # Quadratic & AP
    {
        "id": "c_quadratic_discriminant_nature",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "quadratic_equations_ap",
        "name": "Quadratic Formula & Discriminant Analysis",
        "description": "Roots x = (-b +- sqrt(D))/(2a) where D = b^2 - 4ac. Real distinct (D>0), equal (D=0), complex (D<0).",
        "key_formula": "D = b^2 - 4ac; x = (-b +- sqrt(D)) / (2a)",
        "difficulty_baseline": "medium",
        "x": 100,
        "y": 240
    },
    {
        "id": "c_arithmetic_progression_nth_term",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "quadratic_equations_ap",
        "name": "Arithmetic Progression: General nth Term",
        "description": "Sequence where each term differs from previous by constant common difference d.",
        "key_formula": "an = a + (n - 1) * d",
        "difficulty_baseline": "easy",
        "x": 280,
        "y": 240
    },
    {
        "id": "c_arithmetic_progression_sum",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "quadratic_equations_ap",
        "name": "Sum of First n Terms of an AP",
        "description": "Derivation and application of sum formula using first term, common difference, and last term.",
        "key_formula": "Sn = (n/2) * [2a + (n - 1)d] = (n/2) * (a + l)",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 240
    },

    # Geometry & Coordinates
    {
        "id": "c_basic_proportionality_theorem",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "triangles_coordinate_geometry",
        "name": "Basic Proportionality Theorem (Thales' Theorem)",
        "description": "A line parallel to one side of a triangle dividing the other two sides in the same ratio.",
        "key_formula": "AD / DB = AE / EC (when DE || BC)",
        "difficulty_baseline": "medium",
        "x": 100,
        "y": 380
    },
    {
        "id": "c_triangle_similarity_criteria",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "triangles_coordinate_geometry",
        "name": "Criteria for Similarity of Triangles",
        "description": "AA / AAA, SSS, and SAS similarity criteria; ratio of corresponding sides is invariant.",
        "key_formula": "AB/PQ = BC/QR = AC/PR => Triangle ABC ~ Triangle PQR",
        "difficulty_baseline": "hard",
        "x": 280,
        "y": 380
    },
    {
        "id": "c_coordinate_distance_section",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "triangles_coordinate_geometry",
        "name": "Distance & Section Formulae",
        "description": "Distance between two Cartesian points; coordinates of point dividing line segment in ratio m1:m2.",
        "key_formula": "d = sqrt((x2-x1)^2 + (y2-y1)^2), P = ((m1x2 + m2x1)/(m1+m2), (m1y2 + m2y1)/(m1+m2))",
        "difficulty_baseline": "medium",
        "x": 460,
        "y": 380
    },

    # Trigonometry
    {
        "id": "c_trigonometric_ratios",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "trigonometry_applications",
        "name": "Trigonometric Ratios of Acute Angles",
        "description": "Definitions of sin, cos, tan, cosec, sec, and cot in right triangle; values for 0°, 30°, 45°, 60°, 90°.",
        "key_formula": "sin theta = Opp/Hyp, cos theta = Adj/Hyp, tan theta = Opp/Adj",
        "difficulty_baseline": "easy",
        "x": 100,
        "y": 520
    },
    {
        "id": "c_trigonometric_identities",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "trigonometry_applications",
        "name": "Fundamental Trigonometric Identities",
        "description": "Pythagorean trigonometric identities: sin²θ + cos²θ = 1, 1 + tan²θ = sec²θ, 1 + cot²θ = cosec²θ.",
        "key_formula": "sin^2(theta) + cos^2(theta) = 1, 1 + tan^2(theta) = sec^2(theta)",
        "difficulty_baseline": "hard",
        "x": 280,
        "y": 520
    },
    {
        "id": "c_heights_and_distances",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "trigonometry_applications",
        "name": "Heights & Distances (Elevation & Depression)",
        "description": "Solving real-world heights, tower shadows, and multi-observer problems using right triangle trig ratios.",
        "key_formula": "tan(angle_elevation) = Height / Distance",
        "difficulty_baseline": "hard",
        "x": 460,
        "y": 520
    }
]

# ============================================================================
# CONCEPT RELATIONSHIPS ACROSS SUBJECTS
# ============================================================================
MULTI_SUBJECT_RELATIONSHIPS = [
    # Chemistry
    {"source_concept_id": "c_balancing_equations", "target_concept_id": "c_reaction_types", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_reaction_types", "target_concept_id": "c_redox_reactions", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_redox_reactions", "target_concept_id": "c_corrosion_rancidity", "relationship_type": "application"},
    {"source_concept_id": "c_acid_base_indicators", "target_concept_id": "c_ph_scale", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_ph_scale", "target_concept_id": "c_salts_manufacturing", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_reactivity_series", "target_concept_id": "c_ionic_compounds", "relationship_type": "reinforcement"},
    {"source_concept_id": "c_reactivity_series", "target_concept_id": "c_metallurgy_extraction", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_covalent_bonding_carbon", "target_concept_id": "c_homologous_series", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_homologous_series", "target_concept_id": "c_functional_groups", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_functional_groups", "target_concept_id": "c_esterification_saponification", "relationship_type": "application"},

    # Biology
    {"source_concept_id": "c_photosynthesis_stomata", "target_concept_id": "c_cellular_respiration", "relationship_type": "reinforcement"},
    {"source_concept_id": "c_cellular_respiration", "target_concept_id": "c_human_double_circulation", "relationship_type": "reinforcement"},
    {"source_concept_id": "c_human_double_circulation", "target_concept_id": "c_nephron_ultrafiltration", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_neuron_synapse", "target_concept_id": "c_reflex_arc", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_neuron_synapse", "target_concept_id": "c_human_endocrine_system", "relationship_type": "reinforcement"},
    {"source_concept_id": "c_asexual_reproduction_modes", "target_concept_id": "c_flower_sexual_reproduction", "relationship_type": "progression"},
    {"source_concept_id": "c_flower_sexual_reproduction", "target_concept_id": "c_human_reproduction_contraception", "relationship_type": "reinforcement"},
    {"source_concept_id": "c_mendel_monohybrid_cross", "target_concept_id": "c_mendel_dihybrid_cross", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_mendel_monohybrid_cross", "target_concept_id": "c_human_sex_determination", "relationship_type": "application"},

    # Mathematics
    {"source_concept_id": "c_fundamental_theorem_arithmetic", "target_concept_id": "c_irrationality_proof", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_fundamental_theorem_arithmetic", "target_concept_id": "c_polynomial_zeroes_coefficients", "relationship_type": "reinforcement"},
    {"source_concept_id": "c_polynomial_zeroes_coefficients", "target_concept_id": "c_quadratic_discriminant_nature", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_arithmetic_progression_nth_term", "target_concept_id": "c_arithmetic_progression_sum", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_basic_proportionality_theorem", "target_concept_id": "c_triangle_similarity_criteria", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_trigonometric_ratios", "target_concept_id": "c_trigonometric_identities", "relationship_type": "prerequisite"},
    {"source_concept_id": "c_trigonometric_ratios", "target_concept_id": "c_heights_and_distances", "relationship_type": "application"}
]

# ============================================================================
# HIGH QUALITY CURRICULUM QUESTIONS ACROSS SUBJECTS
# ============================================================================
MULTI_SUBJECT_QUESTIONS = [
    # Chemistry Questions
    {
        "id": "q_chem_01",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "chemical_reactions_equations",
        "concept_id": "c_redox_reactions",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "In the chemical reaction: CuO + H2 -> Cu + H2O, which substance undergoes oxidation and which acts as the reducing agent?",
        "options": [
            {"id": "A", "text": "H2 is oxidized and H2 acts as the reducing agent"},
            {"id": "B", "text": "CuO is oxidized and Cu is the reducing agent"},
            {"id": "C", "text": "CuO is reduced and H2O is the reducing agent"},
            {"id": "D", "text": "Both CuO and H2 undergo oxidation simultaneously"}
        ],
        "correct_answer": "A",
        "explanation": "Hydrogen (H2) gains oxygen to form H2O, so it is oxidized. The substance that undergoes oxidation provides electrons/removes oxygen from the other reactant, making H2 the reducing agent. CuO loses oxygen and is reduced.",
        "expected_reasoning": "Identify the substance gaining oxygen (H2) as the oxidized species, which inherently serves as the reducing agent.",
        "distractor_explanations": {
            "B": "CuO loses oxygen, meaning it undergoes reduction, not oxidation.",
            "C": "H2O is a product, not a starting reducing agent reactant.",
            "D": "In a redox reaction, one species is oxidized while the other is reduced."
        },
        "learning_objective": "Identify oxidized/reduced species and oxidizing/reducing agents in redox equations.",
        "hint": "Remember: The reactant that gains oxygen is oxidized and acts as the reducing agent."
    },
    {
        "id": "q_chem_02",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "acids_bases_salts",
        "concept_id": "c_ph_scale",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "Solution A has a pH of 3 and Solution B has a pH of 6. What is the ratio of [H3O+] ion concentration in Solution A compared to Solution B?",
        "options": [
            {"id": "A", "text": "Solution A has 1,000 times higher [H3O+] concentration than Solution B"},
            {"id": "B", "text": "Solution A has 2 times higher [H3O+] concentration than Solution B"},
            {"id": "C", "text": "Solution A has 3 times higher [H3O+] concentration than Solution B"},
            {"id": "D", "text": "Solution B has 100 times higher [H3O+] concentration than Solution A"}
        ],
        "correct_answer": "A",
        "explanation": "The pH scale is logarithmic: each unit decrease represents a 10-fold increase in hydronium ion concentration. The difference between pH 3 and pH 6 is 3 pH units, which corresponds to 10^3 = 1,000 times higher [H3O+] in Solution A.",
        "expected_reasoning": "Apply the logarithmic definition of pH: Delta pH = 3 corresponds to a 10^3 = 1000x difference in [H+] concentration.",
        "distractor_explanations": {
            "B": "Linear division (6 / 3 = 2) is incorrect because pH is a logarithmic, not linear, scale.",
            "C": "Subtracting 6 - 3 = 3 without exponentiating to base 10 confuses arithmetic difference with concentration ratio.",
            "D": "Lower pH indicates higher acidity (higher [H+]), so Solution A is more concentrated than B."
        },
        "learning_objective": "Interpret the logarithmic nature of the pH scale and calculate hydronium concentration ratios.",
        "hint": "Recall that each step on the pH scale represents a power of 10."
    },
    {
        "id": "q_chem_03",
        "subject_id": "chemistry",
        "subject_name": "Chemistry",
        "chapter_id": "carbon_and_compounds",
        "concept_id": "c_homologous_series",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "An organic compound has the molecular formula C4H8. To which homologous series does it belong, and what is its characteristic reaction with bromine water?",
        "options": [
            {"id": "A", "text": "Alkene series (CnH2n); it decolourises reddish-brown bromine water via addition reaction"},
            {"id": "B", "text": "Alkane series (CnH2n+2); it produces white precipitate with bromine water"},
            {"id": "C", "text": "Alkyne series (CnH2n-2); it reacts with bromine only under strong UV radiation"},
            {"id": "D", "text": "Alcohol series; it undergoes substitution without colour change"}
        ],
        "correct_answer": "A",
        "explanation": "Formula C4H8 matches the general formula for alkenes (CnH2n for n=4). Unsaturated hydrocarbons with double bonds (alkenes) rapidly decolourise reddish-brown bromine water by undergoing electrophilic addition across the double bond to form dibromobutane.",
        "expected_reasoning": "Recognize CnH2n as alkene stoichiometry and recall the bromine water unsaturation addition test.",
        "distractor_explanations": {
            "B": "C4H8 has 2 fewer hydrogens than butane (C4H10), so it is not an alkane.",
            "C": "Alkynes have the formula CnH2n-2 (e.g. C4H6).",
            "D": "Alcohols contain oxygen atoms in their molecular formula."
        },
        "learning_objective": "Identify alkene homologous series and understand unsaturation tests with bromine water.",
        "hint": "Compare C4H8 against CnH2n and remember how unsaturated bonds react with Br2."
    },

    # Biology Questions
    {
        "id": "q_bio_01",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "life_processes",
        "concept_id": "c_cellular_respiration",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "During sudden vigorous sprinting, a student experiences severe muscle cramps. What physiological biochemical process is responsible?",
        "options": [
            {"id": "A", "text": "Anaerobic breakdown of pyruvate into lactic acid due to oxygen deficiency in muscle tissue"},
            {"id": "B", "text": "Excessive accumulation of ethanol and carbon dioxide in muscle fibers"},
            {"id": "C", "text": "Complete aerobic oxidation yielding high ATP and excess carbon dioxide in blood"},
            {"id": "D", "text": "Dehydration causing irreversible breakdown of myofibril actin filaments"}
        ],
        "correct_answer": "A",
        "explanation": "When muscle cells require rapid ATP during intense exertion that outpaces oxygen delivery by blood, pyruvate is converted anaerobically into lactic acid (3-carbon molecule). The accumulation of lactic acid crystals lowers local pH and triggers painful muscle cramps.",
        "expected_reasoning": "Connect insufficient oxygen during vigorous exercise with anaerobic conversion of pyruvate to lactic acid in human myocytes.",
        "distractor_explanations": {
            "B": "Ethanol fermentation occurs in yeast and plant cells, not human skeletal muscle cells.",
            "C": "Aerobic respiration produces CO2 and water without causing acute cramping.",
            "D": "While dehydration can contribute, the direct biochemical cause of sudden exercise cramping is lactic acid buildup."
        },
        "learning_objective": "Distinguish aerobic vs anaerobic pathways of glucose breakdown in human muscles.",
        "hint": "Consider what 3-carbon compound forms in human muscle cells when oxygen is scarce."
    },
    {
        "id": "q_bio_02",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "control_and_coordination",
        "concept_id": "c_plant_hormones_tropisms",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "A potted plant placed horizontally on a windowsill bends its shoot upward toward light and its roots downward. Which hormone and tropism govern the shoot's upward bending?",
        "options": [
            {"id": "A", "text": "Auxin stimulates greater cell elongation on the shaded/lower side, producing positive phototropism"},
            {"id": "B", "text": "Abscisic acid causes rapid leaf shedding on the illuminated surface"},
            {"id": "C", "text": "Cytokinin inhibits shoot growth on the underside, forcing upward curving"},
            {"id": "D", "text": "Gibberellin causes root cells to actively shrink away from gravity"}
        ],
        "correct_answer": "A",
        "explanation": "Auxin synthesized at shoot tips migrates toward the shaded and lower side of the stem. In stems, higher auxin concentration promotes faster cell elongation. The uneven growth between the faster-growing shaded side and slower-growing lit side curves the shoot upward toward light (positive phototropism).",
        "expected_reasoning": "Identify Auxin as the differential elongation hormone responsible for directional phototropism.",
        "distractor_explanations": {
            "B": "Abscisic acid is a growth inhibitor associated with dormancy and stomatal closure.",
            "C": "Cytokinin promotes cell division, not directional curvature.",
            "D": "Roots curve downward due to positive geotropism, where high auxin inhibits root cell elongation."
        },
        "learning_objective": "Explain the role of auxin in differential cell elongation and phototropic curvature.",
        "hint": "Auxin diffuses away from light to cause cells on that side to grow longer."
    },
    {
        "id": "q_bio_03",
        "subject_id": "biology",
        "subject_name": "Biology",
        "chapter_id": "heredity_and_evolution",
        "concept_id": "c_mendel_monohybrid_cross",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "In a cross between pure tall pea plants (TT) and pure dwarf pea plants (tt), all F1 offspring are tall (Tt). If F1 plants self-pollinate, what is the probability of obtaining a dwarf plant in F2 generation?",
        "options": [
            {"id": "A", "text": "25% (1 out of 4 plants will have the homozygous recessive tt genotype)"},
            {"id": "B", "text": "50% (half of the plants will be heterozygous dwarf)"},
            {"id": "C", "text": "0% (tallness completely masks dwarfness across all future generations)"},
            {"id": "D", "text": "75% (dwarf alleles reappear with three times greater frequency)"}
        ],
        "correct_answer": "A",
        "explanation": "Self-crossing F1 hybrids (Tt x Tt) yields a Punnett square of 1 TT : 2 Tt : 1 tt. The dwarf phenotype requires the homozygous recessive 'tt' genotype, which occurs in exactly 1 out of 4 combinations, or 25% (1/4).",
        "expected_reasoning": "Construct the Tt x Tt Punnett square and identify the homozygous recessive fraction as 1/4 (25%).",
        "distractor_explanations": {
            "B": "Heterozygous Tt plants are phenotypically tall due to the dominance of allele T.",
            "C": "Recessive traits segregate cleanly in the F2 generation according to Mendel's Law of Segregation.",
            "D": "75% is the proportion of tall plants (1 TT + 2 Tt), not dwarf plants."
        },
        "learning_objective": "Apply Mendel's Law of Segregation and compute phenotypic/genotypic ratios in F2 generation.",
        "hint": "Draw the 2x2 Punnett square for Tt x Tt and count how many squares have tt."
    },

    # Mathematics Questions
    {
        "id": "q_math_01",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "real_numbers_polynomials",
        "concept_id": "c_polynomial_zeroes_coefficients",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "If alpha and beta are the zeroes of the quadratic polynomial p(x) = 2x^2 - 5x + 7, what is the exact value of (1/alpha + 1/beta)?",
        "options": [
            {"id": "A", "text": "5 / 7"},
            {"id": "B", "text": "-5 / 7"},
            {"id": "C", "text": "7 / 5"},
            {"id": "D", "text": "5 / 2"}
        ],
        "correct_answer": "A",
        "explanation": "For quadratic ax^2 + bx + c: sum of zeroes alpha + beta = -b/a = -(-5)/2 = 5/2. Product of zeroes alpha * beta = c/a = 7/2. Therefore, 1/alpha + 1/beta = (alpha + beta) / (alpha * beta) = (5/2) / (7/2) = 5/7.",
        "expected_reasoning": "Express (1/alpha + 1/beta) as (alpha + beta)/(alpha * beta) and substitute Vieta's formulas.",
        "distractor_explanations": {
            "B": "Forgot the negative sign in Vieta's sum: -(-5) = +5, so the result is positive.",
            "C": "Inverted the numerator and denominator: it is sum/product, not product/sum.",
            "D": "Calculated only the sum of zeroes without dividing by the product."
        },
        "learning_objective": "Apply the relationship between zeroes and coefficients of quadratic polynomials.",
        "hint": "Combine fractions: 1/alpha + 1/beta = (alpha + beta)/(alpha * beta)."
    },
    {
        "id": "q_math_02",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "quadratic_equations_ap",
        "concept_id": "c_arithmetic_progression_sum",
        "difficulty": "medium",
        "question_type": "mcq",
        "question_text": "Find the sum of the first 20 terms of the Arithmetic Progression: 3, 7, 11, 15, ...",
        "options": [
            {"id": "A", "text": "820"},
            {"id": "B", "text": "780"},
            {"id": "C", "text": "860"},
            {"id": "D", "text": "410"}
        ],
        "correct_answer": "A",
        "explanation": "Here first term a = 3, common difference d = 7 - 3 = 4, and n = 20. Using Sn = (n/2) * [2a + (n-1)d]: S20 = (20/2) * [2(3) + (20-1)(4)] = 10 * [6 + 76] = 10 * 82 = 820.",
        "expected_reasoning": "Apply Sn = (n/2)[2a + (n-1)d] with a=3, d=4, n=20 to compute 10*(6 + 76) = 820.",
        "distractor_explanations": {
            "B": "Used (n-1) = 19 with d=3 instead of d=4.",
            "C": "Added 2a + nd instead of 2a + (n-1)d.",
            "D": "Forgot to multiply by 2 or divided sum by 2 again."
        },
        "learning_objective": "Calculate the sum of n terms of an arithmetic progression using the standard formula.",
        "hint": "Check a = 3, d = 4, and calculate Sn = (n/2) * [2a + (n-1)d]."
    },
    {
        "id": "q_math_03",
        "subject_id": "mathematics",
        "subject_name": "Mathematics",
        "chapter_id": "trigonometry_applications",
        "concept_id": "c_heights_and_distances",
        "difficulty": "hard",
        "question_type": "mcq",
        "question_text": "From a point on the ground 30 meters away from the foot of a vertical tower, the angle of elevation of the top of the tower is found to be 30°. What is the height of the tower?",
        "options": [
            {"id": "A", "text": "10 * sqrt(3) meters (approximately 17.32 m)"},
            {"id": "B", "text": "30 * sqrt(3) meters (approximately 51.96 m)"},
            {"id": "C", "text": "15 meters"},
            {"id": "D", "text": "30 / sqrt(2) meters"}
        ],
        "correct_answer": "A",
        "explanation": "Let height of tower be h. In right triangle, tan(30°) = Opposite / Adjacent = h / 30. Since tan(30°) = 1/sqrt(3), we have 1/sqrt(3) = h / 30 => h = 30 / sqrt(3) = (30 * sqrt(3)) / 3 = 10 * sqrt(3) meters.",
        "expected_reasoning": "Set up tan(30) = h/30, substitute tan(30) = 1/sqrt(3), and rationalize 30/sqrt(3) to 10*sqrt(3).",
        "distractor_explanations": {
            "B": "Multiplied by sqrt(3) instead of dividing by sqrt(3) (used tan(60) instead of tan(30)).",
            "C": "Assumed 30-60-90 hypotenuse rule mistakenly for adjacent distance.",
            "D": "Confused tan(30°) with sin(45°)."
        },
        "learning_objective": "Apply tangent ratio to calculate heights using angle of elevation.",
        "hint": "Remember tan(30°) = 1 / sqrt(3) = Height / Distance."
    }
]

# Misconceptions for new subjects
MULTI_SUBJECT_MISCONCEPTIONS = [
    {
        "id": "misc_rusting_is_erosion",
        "subject_id": "chemistry",
        "chapter_id": "chemical_reactions_equations",
        "concept_id": "c_corrosion_rancidity",
        "label": "Rusting is Just Physical Wear or Erosion",
        "keywords": ["erosion", "wearing down", "scratched", "rubbed off"],
        "description": "Student thinks rusting is a mechanical degradation rather than an electrochemical oxidation process.",
        "why_incorrect": "Rusting is a redox reaction where iron atoms transfer electrons to atmospheric oxygen in presence of water, forming hydrated iron(III) oxide (Fe2O3.xH2O).",
        "remediation": "Notice that iron gains mass when it rusts because oxygen atoms chemically bond with the iron metal lattice.",
        "remediation_activity": "Examine mass before and after rusting in a closed sealed test tube."
    },
    {
        "id": "misc_respiration_is_breathing",
        "subject_id": "biology",
        "chapter_id": "life_processes",
        "concept_id": "c_cellular_respiration",
        "label": "Cellular Respiration is the Same as Breathing",
        "keywords": ["inhalation", "lungs breathing", "respiration is breathing", "exhaling air"],
        "description": "Student equates cellular respiration to pulmonary ventilation (inhaling and exhaling).",
        "why_incorrect": "Breathing is physical gas exchange at alveolar membranes; cellular respiration is the intracellular enzymatic biochemical oxidation of glucose in mitochondria to synthesize ATP.",
        "remediation": "Differentiate organ-level gas exchange (lungs) from microscopic chemical energy harvesting inside cells (mitochondria).",
        "remediation_activity": "Compare lung ventilation anatomy vs mitochondrial ATP synthesis diagram."
    },
    {
        "id": "misc_mother_determines_sex",
        "subject_id": "biology",
        "chapter_id": "heredity_and_evolution",
        "concept_id": "c_human_sex_determination",
        "label": "Mother Determines Child's Biological Sex",
        "keywords": ["mother determines", "egg decides gender", "mother chromosome decides boy or girl"],
        "description": "Student incorrectly attributes child sex determination to maternal egg chromosomes.",
        "why_incorrect": "All human eggs contribute an X chromosome. The father's sperm contributes either an X (yielding female XX) or a Y (yielding male XY). Thus paternal gametes determine biological sex.",
        "remediation": "Draw the cross: Female is homogametic (XX, all eggs X); Male is heterogametic (XY, 50% X sperm, 50% Y sperm).",
        "remediation_activity": "Diagram the 50/50 fertilization probability tree with X and Y sperm."
    },
    {
        "id": "misc_trig_distributive",
        "subject_id": "mathematics",
        "chapter_id": "trigonometry_applications",
        "concept_id": "c_trigonometric_identities",
        "label": "Trigonometric Function Distributes Over Addition: sin(A+B) = sin A + sin B",
        "keywords": ["distribute sin", "sin(a+b) is sin a + sin b", "multiplication like brackets"],
        "description": "Student treats 'sin' as an algebraic multiplier rather than a mathematical function.",
        "why_incorrect": "Trigonometric ratios are nonlinear operators. For example, sin(30° + 60°) = sin(90°) = 1, whereas sin(30°) + sin(60°) = 0.5 + 0.866 = 1.366 != 1.",
        "remediation": "Test with numerical values (30° and 60°) to visibly show that the left-hand and right-hand sides do not match.",
        "remediation_activity": "Calculate sin(30+30) = sin(60) = sqrt(3)/2 vs sin(30) + sin(30) = 1."
    }
]
