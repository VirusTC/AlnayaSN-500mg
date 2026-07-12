import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class UnifiedElectrochemicalSimulator:
    def __init__(self, weight_kg, height_cm, age, sex, build_modifier, hydration_modifier, entry_blood_ph):
        """
        Unified Electrochemical & Pathological Engine.
        Merges biometric scaling, custom initial pH parameters, multi-year compounding, 
        and dynamic buffer depletion curves into a single deterministic script.
        """
        self.weight = weight_kg
        self.height = height_cm
        self.age = age
        self.sex = sex
        self.volume_scaler = float(build_modifier) * float(hydration_modifier)
        self.total_body_water = self._calculate_total_body_water()
        
        # Foundational Pathological Starting Matrix Input
        self.baseline_ph = float(entry_blood_ph)
        
        # Rigid Chemical and Physical Constants
        self.niacin_mw = 123.11  # Molecular weight of Nicotinic Acid (g/mol)
        self.pka = 4.8           # Dissociation constant (pKa) of carboxylate group
        self.faraday_constant = 96485  # Coulombs per mole of electrons (F)
        
        # Derive Pathological Parameters directly from initial entry blood pH status
        self._calculate_pathological_vulnerability()

    def _calculate_total_body_water(self):
        """
        Calculates the baseline distribution volume (Liters of fluid) using the 
        Watson Formula, scaled explicitly by user build and hydration modifiers.
        """
        if self.sex.lower() == 'male':
            baseline_tbw = 2.447 - (0.09516 * self.age) + (0.1074 * self.height) + (0.3362 * self.weight)
        else:
            baseline_tbw = -2.097 + (0.1069 * self.height) + (0.2466 * self.weight)
        return baseline_tbw * self.volume_scaler

    def _calculate_pathological_vulnerability(self):
        """
        Derives organic clearance degradation and systemic buffer exhaustion directly
        from the absolute distance between the initial pH input and healthy homeostatic baseline (7.40).
        """
        # Calculate the depth of systemic acidosis
        ph_deficit = max(0.0, 7.40 - self.baseline_ph)
        
        # Dynamic Buffer Capacity Model:
        # As pH drops, available bicarbonate reserves are mathematically depleted.
        # Acidosis limits the system's ability to resist local charge accumulations.
        self.buffer_capacity = max(0.02, 1.0 - (ph_deficit * 3.5))
        
        # Dynamic 24-Hour Clearance Rate Model:
        # Acidemia and septic pathologies strain hepatic and renal filtration systems.
        # Healthy status clears 98% daily. Severe acidotic shock states drag clearance down.
        self.clearance_rate = max(0.20, 0.98 - (ph_deficit * 2.8))

    def simulate_three_years(self, initial_dose_mg, yearly_increment_mg, total_days=1095):
        """
        Simulates a continuous 3-year timeline (1095 days). Leftover compound mass balances
        accumulate across 24-hour cycles based on organic clearance performance.
        """
        days = np.arange(1, total_days + 1)
        doses = []
        accumulated_masses_g = []
        charge_densities_c_per_l = []
        nernst_potentials_mv = []
        ph_values = []
        
        current_retained_mass_g = 0.0
        
        for day in days:
            # Multi-Year Dose Tier Setup
            if day <= 365:
                daily_intake_mg = initial_dose_mg
            elif day <= 730:
                daily_intake_mg = initial_dose_mg + yearly_increment_mg
            else:
                daily_intake_mg = initial_dose_mg + (2 * yearly_increment_mg)
            
            # Physics of Accumulation: Residual uncleared mass + new daily intake mass
            daily_intake_g = daily_intake_mg / 1000.0
            total_active_mass_g = current_retained_mass_g + daily_intake_g
            
            # Calculate concentration of negative charges within the total fluid volume
            moles_charge = total_active_mass_g / self.niacin_mw
            concentration_A_minus = moles_charge / self.total_body_water
            
            # Quantify localized charge density in Coulombs/Liter using Faraday's Law
            charge_density = concentration_A_minus * (-1.0) * self.faraday_constant
            
            # Ratio tracking matching Henderson-Hasselbalch equations
            ha_baseline = concentration_A_minus / (10 ** (self.baseline_ph - self.pka))
            
            if ha_baseline > 0:
                # Impaired buffer capacities mathematically amplify the resulting charge-ratio shifts
                raw_ph_shift = np.log10(concentration_A_minus / ha_baseline)
                buffered_ph_shift = raw_ph_shift * (1.0 / self.buffer_capacity)
                
                # Execute trajectory calculation relative to the initial pathological baseline
                modeled_ph = self.pka + buffered_ph_shift
                # Impose physical boundary caps to prevent infinity errors near critical failures
                modeled_ph = max(min(modeled_ph, 7.95), 6.40)
            else:
                modeled_ph = self.baseline_ph
                
            # Electrochemistry: Apply the Nernst Equation derivative (-61.5 mV per pH unit at 37C)
            # Tracks the shifting electrical reduction potential of proton availability
            nernst_mv = -61.5 * modeled_ph
            
            # Save tracked data
            doses.append(daily_intake_mg)
            accumulated_masses_g.append(total_active_mass_g)
            charge_densities_c_per_l.append(charge_density)
            nernst_potentials_mv.append(nernst_mv)
            ph_values.append(modeled_ph)
            
            # Determine leftover mass carried forward into the next daily cycle
            current_retained_mass_g = total_active_mass_g * (1.0 - self.clearance_rate)
            
        return pd.DataFrame({
            'Day': days,
            'Year': np.ceil(days / 365).astype(int),
            'Daily_Dose_mg': doses,
            'Total_Retained_Mass_g': accumulated_masses_g,
            'Charge_Density_C_L': charge_densities_c_per_l,
            'Nernst_Potential_mV': nernst_potentials_mv,
            'Modeled_pH': ph_values
        })

    def print_theoretical_equations_reference(self):
        """Prints a comprehensive breakdown of the physics equations driving this system."""
        equations = """
=========================================================================================
                        THEORETICAL ELECTROCHEMICAL EQUATION GLOSSARY
=========================================================================================
1. FLUID EQUILIBRIUM (Watson Volumetric Metric):
   TBW_Male   = 2.447 - (0.09516 * Age) + (0.1074 * Height_cm) + (0.3362 * Weight_kg)
   TBW_Female = -2.097 + (0.1069 * Height_cm) + (0.2466 * Weight_kg)
   V_Final    = TBW * Build_Modifier * Hydration_Modifier

2. CHARGE DENSITY CONCENTRATION (Faraday's Law):
   [A-] = (Total_Retained_Mass_g / Molecular_Weight) / V_Final
   Q_c  = [A-] * z * F   (where z = -1, F = 96485 Coulombs/mol)

3. PATHOLOGICAL BUFFER TRAJECTORY (Modified Henderson-Hasselbalch):
   pH = pKa + (log10([A-] / [HA]) * (1.0 / Buffer_Capacity))

4. ELECTROCHEMICAL ELECTROMOTIVE CONVERSION (The Nernst Slope at 37°C):
   E = -61.5 * pH mV  (representing a delta of 61.5 mV per 1.0 unit shift in pH)
=========================================================================================
        """
        print(equations)

# =====================================================================
# SYSTEM EXECUTION AND DUAL-AXIS ANALYSIS GRAPHING GRAPH ENGINE
# =====================================================================
if __name__ == "__main__":
    # Fixed Biometric Inputs: 74kg, 176cm, 42-year-old Female
    # Profile parameters set with standard normal build and baseline hydration
    biometrics = {
        "weight_kg": 74, 
        "height_cm": 176, 
        "age": 42, 
        "sex": "female", 
        "build_modifier": 1.0, 
        "hydration_modifier": 1.0
    }
    
    # Run three distinct simulation tracks by feeding raw patient entry pH values directly
    healthy_baseline = UnifiedElectrochemicalSimulator(**biometrics, entry_blood_ph=7.40).simulate_three_years(100, 150)
    cancer_acidosis  = UnifiedElectrochemicalSimulator(**biometrics, entry_blood_ph=7.28).simulate_three_years(100, 150)
    septic_shock     = UnifiedElectrochemicalSimulator(**biometrics, entry_blood_ph=7.10).simulate_three_years(100, 150)
    
    # Print the equation mapping references to the console
    UnifiedElectrochemicalSimulator(**biometrics, entry_blood_ph=7.40).print_theoretical_equations_reference()
    
    # Setup Visual Multi-Patient Timeline Comparison Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    # Subplot 1: Track the shifting Electro-Chemical pH curves over 1095 Days
    ax1.plot(healthy_baseline['Day'], healthy_baseline['Modeled_pH'], label='Healthy Patient Entry (Initial pH: 7.40)', color='seagreen', linewidth=2.5)
    ax1.plot(cancer_acidosis['Day'],  cancer_acidosis['Modeled_pH'],  label='Cancer Acidosis Entry (Initial pH: 7.28, 60% Clear)', color='darkorange', linewidth=2.5, linestyle='--')
    ax1.plot(septic_shock['Day'],     septic_shock['Modeled_pH'],     label='Septic Shock Entry (Initial pH: 7.10, 25% Clear)', color='crimson', linewidth=2.5, linestyle=':')
    
    ax1.set_ylabel('Simulated Electro-Chemical pH Status', fontsize=11)
    ax1.set_title('3-Year Timeline Projections: Pathological Accumulation & Buffer Failure', fontsize=14, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend(loc='best', fontsize=10)
    
    # Subplot 2: Track corresponding Nernst Potential shifts in millivolts (mV)
    ax2.plot(healthy_baseline['Day'], healthy_baseline['Nernst_Potential_mV'], color='seagreen', linewidth=2)\
    ax2.plot(cancer_acidosis['Day'], cancer_acidosis['Nernst_Potential_mV'], color='darkorange', linewidth=2, linestyle='--')\
    ax2.plot(septic_shock['Day'], septic_shock['Nernst_Potential_mV'], color='crimson', linewidth=2, linestyle=':')

    ax2.set_xlabel('Simulation Period (Days Across 3 Years)', fontsize=11)\
    ax2.set_ylabel('Theoretical Nernst Potential (mV)', fontsize=11)\
    ax2.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()\
    print("Multi-year pathological matrices combined. Plotting dual electrochemical timelines...")\
    plt.show()
