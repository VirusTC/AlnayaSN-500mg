import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ElectrochemicalPhSimulator:
    def __init__(self, weight_kg, height_cm, age, sex, build_modifier, hydration_modifier):
        """
        Initializes the simulator using the user's biometric parameters.
        Build/Hydration modifiers scale the baseline total body water volume.
        """
        self.weight = weight_kg
        self.height = height_cm
        self.age = age
        self.sex = sex
        # Combine build and hydration parameters to scale total distribution volume
        self.volume_scaler = build_modifier * hydration_modifier
        self.total_body_water = self._calculate_total_body_water()
        
        # Physical & Chemical Constants
        self.niacin_mw = 123.11  # Molecular weight of Nicotinic Acid (g/mol)
        self.pka = 4.8           # Dissociation constant (pKa) of the carboxylate group
        self.baseline_ph = 7.40  # Standard homeostatic physiological pH

    def _calculate_total_body_water(self):
        """
        Uses the Watson Formula to compute baseline Liters of fluid,
        adjusted by the user's custom build and hydration modifiers.
        """
        if self.sex.lower() == 'male':
            baseline_tbw = 2.447 - (0.09516 * self.age) + (0.1074 * self.height) + (0.3362 * self.weight)
        else:
            baseline_tbw = -2.097 + (0.1069 * self.height) + (0.2466 * self.weight)
        
        return baseline_tbw * self.volume_scaler

    def calculate_theoretical_ph(self, daily_dose_mg):
        """
        Maps the mass of niacin to a concentration of negative charge [A-]
        and computes the resulting theoretical pH shift using the user's model.
        """
        if daily_dose_mg <= 0:
            return self.baseline_ph
            
        # Convert mg to grams
        dose_g = daily_dose_mg / 1000.0
        
        # Moles of Niacin entering the fluid volume
        moles_niacin = dose_g / self.niacin_mw
        
        # Molar concentration of ionized negative charges [A-] in the body water
        concentration_negative_charge = moles_niacin / self.total_body_water
        
        # Standard un-ionized background acid concentration baseline [HA]
        # Set to physiological equilibrium constant to match baseline resting pH
        ha_baseline = concentration_negative_charge / (10 ** (self.baseline_ph - self.pka))
        
        if ha_baseline == 0:
            return self.baseline_ph
            
        # Calculate resulting pH based on the negative charge density ratio (-H+)
        theoretical_ph = self.pka + np.log10(concentration_negative_charge / ha_baseline)
        
        return theoretical_ph

    def simulate_three_years(self, initial_dose_mg, yearly_increment_mg):
        """
        Generates a 3-year daily dataset (1095 days) mapping out dose progression
        and the corresponding theoretical pH tracking values.
        """
        days = np.arange(1, 1096)
        doses = []
        ph_values = []
        
        for day in days:
            # Simulate a protocol where dose increases each year
            if day <= 365:
                current_dose = initial_dose_mg
            elif day <= 730:
                current_dose = initial_dose_mg + yearly_increment_mg
            else:
                current_dose = initial_dose_mg + (2 * yearly_increment_mg)
                
            theoretical_ph = self.calculate_theoretical_ph(current_dose)
            
            doses.append(current_dose)
            ph_values.append(theoretical_ph)
            
        df = pd.DataFrame({
            'Day': days,
            'Year': np.ceil(days / 365).astype(int),
            'Daily_Dose_mg': doses,
            'Theoretical_pH': ph_values
        })
        return df

# =====================================================================
# EXECUTION & CHARTING ENGINE
# =====================================================================
if __name__ == "__main__":
    # Example Biometric Profile: 75kg, 178cm, 35 years old, Male
    # Build Modifier: 1.0 (Average), Hydration Modifier: 1.0 (Normal)
    user_weight = 75
    user_height = 178
    user_age = 35
    user_sex = 'male'
    build_mod = 1.0       
    hydration_mod = 1.0   

    # Initialize the electrochemical model
    simulator = ElectrochemicalPhSimulator(
        weight_kg=user_weight, 
        height_cm=user_height, 
        age=user_age, 
        sex=user_sex, 
        build_modifier=build_mod, 
        hydration_modifier=hydration_mod
    )
    
    print(f"--- Electrochemical Profile Initialized ---")
    print(f"Calculated Total Distribution Volume: {simulator.total_body_water:.2f} Liters\n")

    # Run 3-Year Simulation: Starting at 100mg, increasing by 150mg each year
    simulation_df = simulator.simulate_three_years(initial_dose_mg=100, yearly_increment_mg=150)
    
    # Generate the dual-axis charting tracking timeline
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot Daily Dosage Progression
    color = 'tab:blue'
    ax1.set_xlabel('Timeline (Days Over 3 Years)')
    ax1.set_ylabel('Daily Niacin Intake (mg)', color=color)
    ax1.plot(simulation_df['Day'], simulation_df['Daily_Dose_mg'], color=color, linewidth=2, label='Dosage Profile')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Instantiate a second axis sharing the same x-axis for theoretical pH
    ax2 = ax1.twinx()  
    color = 'tab:red'
    ax2.set_ylabel('Theoretical Electro-Chemical pH Mapping', color=color)
    ax2.plot(simulation_df['Day'], simulation_df['Theoretical_pH'], color=color, linewidth=2, linestyle=':', label='Theoretical pH')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('3-Year Theoretical Dosage and Negative Charge Concentration Model')
    fig.tight_layout()
    
    print("Simulation complete. Displaying generated charge-density timeline chart...")
    plt.show()
