import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class LipidMetabolismSimulator:
    def __init__(self, weight_kg, initial_ldl_mg_dl, initial_triglycerides_mg_dl, baseline_daily_diet_fat_g=90):
        """
        Initializes the lipid metabolism engine to track low-density lipoprotein (LDL),
        triglycerides, and fecal fat excretion over multi-year protocols.
        """
        self.weight = weight_kg
        self.diet_fat_g = baseline_daily_diet_fat_g
        
        # Initial Lipid Baseline Values (mg/dL)
        self.initial_ldl = initial_ldl_mg_dl
        self.initial_tg = initial_triglycerides_mg_dl
        
        # Establish standard physiological limits for maximum therapeutic reduction
        self.max_ldl_reduction_pct = 0.25   # Maximum expected clinical LDL drop (~25%)
        self.max_tg_reduction_pct = 0.40    # Maximum expected clinical Triglyceride drop (~40%)

    def calculate_daily_lipid_metrics(self, daily_dose_mg):
        """
        Calculates lipid profile alterations and gastrointestinal fat absorption
        rates based on the current daily dosage mass.
        """
        # Threshold where niacin begins actively modifying hepatic enzyme pathways (~500mg)
        if daily_dose_mg < 500:
            ldl_modifier = (daily_dose_mg / 500.0) * self.max_ldl_reduction_pct
            tg_modifier = (daily_dose_mg / 500.0) * self.max_tg_reduction_pct
            # Intestinal absorption remains normal (95%)
            coefficient_of_absorption = 0.95
        else:
            # High dose plateau effect for circulating lipids
            ldl_modifier = self.max_ldl_reduction_pct
            tg_modifier = self.max_tg_reduction_pct
            
            # High-dose mucosal irritation model: excess doses track with a drop in 
            # fat absorption efficiency, simulating secondary steatorrhea (oily stools)
            excess_dose = daily_dose_mg - 500.0
            coefficient_of_absorption = max(0.40, 0.95 - (excess_dose / 3000.0))

        # Calculate current circulating values
        current_ldl = self.initial_ldl * (1.0 - ldl_modifier)
        current_tg = self.initial_tg * (1.0 - tg_modifier)
        
        # Calculate Fecal Fat Excretion (g/day) based on absorption failure
        fecal_fat_excreted_g = self.diet_fat_g * (1.0 - coefficient_of_absorption)
        
        return current_ldl, current_tg, fecal_fat_excreted_g, coefficient_of_absorption

    def simulate_three_years(self, start_dose_mg, yearly_increment_mg):
        """
        Executes a daily 1095-day tracking timeline across a 3-year period.
        """
        days = np.arange(1, 1096)
        doses = []
        ldl_history = []
        tg_history = []
        fec_fat_history = []
        coa_history = []
        
        for day in days:
            # Multi-Year Dose Tier Architecture
            if day <= 365:
                current_dose = start_dose_mg
            elif day <= 730:
                current_dose = start_dose_mg + yearly_increment_mg
            else:
                current_dose = start_dose_mg + (2 * yearly_increment_mg)
                
            ldl, tg, fecal_fat, coa = self.calculate_daily_lipid_metrics(current_dose)
            
            doses.append(current_dose)
            ldl_history.append(ldl)
            tg_history.append(tg)
            fec_fat_history.append(fecal_fat)
            coa_history.append(coa * 100.0)  # Convert to percentage
            
        return pd.DataFrame({
            'Day': days,
            'Dose_mg': doses,
            'LDL_mg_dL': ldl_history,
            'Triglycerides_mg_dL': tg_history,
            'Fecal_Fat_Excreted_g': fec_fat_history,
            'Absorption_Efficiency_Pct': coa_history
        })

# =====================================================================
# SIMULATION EXECUTION AND DATA GRAPHING ENGINE
# =====================================================================
if __name__ == "__main__":
    # Baseline Parameters: 80kg Patient, High starting lipids, 90g daily dietary fat intake
    sim = LipidMetabolismSimulator(weight_kg=80, initial_ldl_mg_dl=160, initial_triglycerides_mg_dl=250, baseline_daily_diet_fat_g=90)
    
    # Run 3-Year Simulation: Starting at 250mg, increasing by 500mg each year
    data = sim.simulate_three_years(start_dose_mg=250, yearly_increment_mg=500)
    
    # Plotting the Data
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8), sharex=True)
    
    # Plot 1: Circulating Lipids (LDL and Triglycerides)
    ax1.plot(data['Day'], data['LDL_mg_dL'], label='LDL ("Bad" Cholesterol)', color='crimson', linewidth=2)
    ax1.plot(data['Day'], data['Triglycerides_mg_dL'], label='Triglycerides (Blood Fats)', color='darkorange', linewidth=2)
    ax1.set_ylabel('Circulating Blood Levels (mg/dL)', fontsize=11)
    ax1.set_title('3-Year Simulation: Impact of High Doses on Blood Lipids vs. Fecal Fat Output', fontsize=13, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend(loc='upper right')
    
    # Plot 2: Digestive Fat Malabsorption & Fecal Excretion Output
    ax2.plot(data['Day'], data['Fecal_Fat_Excreted_g'], label='Daily Fecal Fat Excretion (g)', color='saddlebrown', linewidth=2.5)
    ax2.set_xlabel('Timeline (Days Across 3 Years)', fontsize=11)
    ax2.set_ylabel('Undigested Stool Fat (g/day)', fontsize=11)
    ax2.grid(True, linestyle='--', alpha=0.5)
    
    # Share a second axis on subplot 2 to show the drop in absorption efficiency
    ax2_twin = ax2.twinx()
    ax2_twin.plot(data['Day'], data['Absorption_Efficiency_Pct'], color='navy', linestyle=':', linewidth=2, label='Fat Absorption %')
    ax2_twin.set_ylabel('Intestinal Fat Absorption Efficiency (%)', color='navy', fontsize=11)
    ax2_twin.tick_params(axis='y', labelcolor='navy')
    
    # Combine legends for the twin axis plot
    lines, labels = ax2.get_legend_handles_labels()
    lines2, labels2 = ax2_twin.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')
    
    plt.tight_layout()
    print("Lipid alteration simulation complete. Displaying metabolic mapping...")
    plt.show()
