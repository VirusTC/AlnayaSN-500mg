# AlnayaSN-500mg: Electrochemical Lipid & Metabolic Simulator

The U.S. Food and Drug Administration (FDA) allows prescription AlnayaSN (Nicotinic Acid / Niacin) for managing abnormal cholesterol levels (dyslipidemia) and preventing or treating severe niacin deficiency (pellagra). 

This repository contains a Python-based quantitative simulation engine designed to model multi-year tracking of systemic pH, negative charge density, Nernstian potentials, and lipid modifications under progressive high-dose nicotinic acid protocols across varied clinical profiles (healthy, cancer-induced acidosis, and septic crisis).

---

## Key Architectural Models Included

### 1. Unified Electrochemical Engine
Models a continuous 3-year timeline (1095 days) mapping a patient's physical attributes to a deterministic charge-density timeline:
*   **Volumetric Scaling:** Uses the **Watson Formula** to compute baseline total body water volume scaled by customizable build and hydration variables.
*   **Pathological Deficit Scaling:** Automatically degrades daily compound clearance rates and exhausts bicarbonate buffer parameters based on custom initial arterial blood gas (ABG) pH entries.
*   **Electromotive Mapping:** Applies the **Nernst Equation** derivative (-61.5 mV per pH unit shift at 37°C) to track changes in the electrical reduction potential of free proton availability.

### 2. True Mitochondrial Oxidation Simulator
Rejects sweat-loss fallacies and enforces strict thermodynamic laws regarding lipid mass displacement:
*   **Stoichiometric Burning:** Tracks the chemical breakdown of body fat droplets via mitochondrial beta-oxidation (C₅₅H₁₀₄O₆ + 78O₂ → 55CO₂ + 52H₂O), mapping out that **84% of lost fat mass** is exhaled exclusively via the lungs as Carbon Dioxide gas.
*   **Niacin-Induced Thermogenesis:** Models Brown Adipose Tissue (BAT) activation and Uncoupling Protein-1 (UCP1) upregulation to track accelerated cellular lipid burning.

### 3. Hepatic Lipid & Malabsorption Matrix
Simulates circulating blood lipid changes versus gastrointestinal side effects:
*   **Lipid Profiles:** Tracks expected clinical drops in Low-Density Lipoproteins (LDL) and Triglycerides via GPR109A receptor binding and hepatic DGAT2 enzyme inhibition.
*   **Fecal Fat Excretion:** Incorporates a progressive drop in the Coefficient of Fat Absorption (COA) during high-dose mucosal hyper-motility, plotting the clinical onset of severe secondary steatorrhea (oily, lard-like stools).

---

## Getting Started

### Prerequisites
The scripts run on native Python 3 and require standard data-science plotting and analysis libraries:
```bash
pip install numpy pandas matplotlib
```

### Repository Directory Structure
```text
AlnayaSN-500mg/
├── src/
│   ├── unified_simulator.py      # Core biometric, pH, and Nernstian tracking script
│   └── lipid_oxidation_model.py  # True fat oxidation and fecal fat excretion tracker
├── docs/
│   ├── Electrochemistry_pH.md    # Thermodynamic derivations of Nernstian slope equations
│   └── Lipid_Metabolism.md       # Hepatic enzyme blocks and GPR109A pathway data
├── LICENSE                       # BSL-1.0 License
└── README.md                     # Main repository documentation
```

---

## Theoretical Mathematical Equations

### Modified Henderson-Hasselbalch Trajectory
$$\text{pH} = \text{pK}_a + \left(\log_{10}\left(\frac{[\text{A}^-]}{[\text{HA}]}\right) \cdot \frac{1}{\text{Buffer Capacity}}\right)$$

### Fecal Fat Mass Excretion Balance
$$F_{\text{excreted}} = I_{\text{fat}} \times (1.0 - COA)$$

---

## License
This project is licensed under the terms of the **Boost Software License 1.0 (BSL-1.0)** - see the `LICENSE` file for details.

---

## Important Clinical Disclaimer
The software contained within this repository represents a theoretical physics and chemical abstraction modeling un-neutralized molecular dissociation in an isolated system. It does not reflect real-time live human clinical biology or homeostatic respiratory compensation pathways. 

The Food and Nutrition Board establishes the adult Tolerable Upper Intake Level (UL) for niacin at **35 mg per day**. High-dose prescription AlnayaSN (500mg) protocols significantly exceed standard nutritional upper limits, carry strict risks of severe hepatotoxicity, skin flushing, or metabolic shifts, and must strictly be managed under direct clinical oversight from a licensed medical professional.
