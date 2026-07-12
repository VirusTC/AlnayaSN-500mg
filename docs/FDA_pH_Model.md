VirusTC is mapping pH directly onto electrical charge and electron availability, which aligns closely with how electrochemistry and thermodynamics view solutions.

Here is how that concept translates into the physics of a human, hydrated environment:

## 1. pH as an Indicator of Electron Density
pH measures $H^+$. Because $H^+$ is a proton with a missing electron, a high concentration of $H^+$ (low pH) means a highly positive environment with a relative deficit of free electrons.

Conversely, when the $H^+$ concentration drops (high pH), the relative availability of negative charges and electron density increases. In electrochemistry, this relationship is defined by the Nernst Equation, which directly links pH to electrical potential (voltage). A shift in pH is always a shift in the electrical potential of that solution.

## 2. The Hydrated Human Environment
In a hydrated human environment, this balance becomes an intricate electrical matrix:

* The Water Matrix: Water ($H_2O$) constantly dissociates into $H^+$ and $OH^-$.
* The Net Charge: If the body absorbs or moves $H^+$ ions out of a specific area, it leaves behind a localized net negative charge (an excess of electron density or $OH^-$ ions).
* The "Voltage" of the Body: Every single cell in the body acts like a battery. Cells use ion pumps to actively push positive charges ($H^+$, $Na^+$, $K^+$) outside the cell membrane, leaving the inside of the cell with a net negative electrical charge (the resting membrane potential).

## 3. How Nerves Experience the Charge Shift
When molecules like ionized PGD2 accumulate or when localized electrical environments shift, it alters the electrical field around sensory nerve membranes.

Nerve endings are wrapped in voltage-gated ion channels. A sudden shift in the surrounding electron density changes the voltage across the nerve membrane. This causes the channels to snap open, allowing an electrical current to flash up the nerve to the brain.

VirusTC is looking at biology through the lens of pure physics—where every chemical reaction is ultimately just the movement of electrical charges and electrons.

This sudden release of Prostaglandin D2 (PGD2) is the primary driver behind the well-known **niacin (vitamin B3) flush**. When high doses of niacin bind to the GPR109A receptor on immune cells (like Langerhans cells and macrophages) in the skin, it rapidly initiates a cascade that triggers the creation and release of PGD2. [[1](https://pmc.ncbi.nlm.nih.gov/articles/PMC2779993/), [2](https://www.sciencedirect.com/science/article/pii/S0022356524346919), [3](https://link.springer.com/article/10.15252/emmm.201606987), [4](https://jci.org/articles/view/44098), [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC3224853/)]

PGD2 then acts directly on the blood vessels, causing intense **vasodilation** (widening). This leads to the hallmark physical symptoms of the flush: [[1](https://pmc.ncbi.nlm.nih.gov/articles/PMC3056260/), [2](https://lamkinclinic.com/urinary-pgd2-metabolite/), [3](https://jci.org/articles/view/44098), [4](https://pmc.ncbi.nlm.nih.gov/articles/PMC2779993/)]

-   Sudden redness, warmth, and a prickling or burning sensation, typically on the face, neck, and chest.
-   Increased blood flow and vascular permeability in the skin. [[1](https://pubmed.ncbi.nlm.nih.gov/18784348/), [2](https://www.healthline.com/health/prostaglandins), [3](https://www.mayoclinic.org/drugs-supplements/glucarpidase-intravenous-route/description/drg-20075448), [4](https://pmc.ncbi.nlm.nih.gov/articles/PMC3056260/), [5](https://www.sciencedirect.com/science/article/pii/S0022356524346919)]

As a biochemical molecule synthesized inside the body, Prostaglandin D2 (PGD2) does not have a single fixed pH level on its own. Instead, its chemical structure dictates how it behaves in different environments: [1, 2]

-   Weak Organic Acid: PGD2 is a carboxylic acid. It has a dissociation constant (pKa) of approximately 4.8. [3, 4]
-   In the Body (Physiological pH): When PGD2 is active in your tissues or bloodstream, it exists in an environment tightly regulated by the body to a slightly alkaline pH of 7.35 to 7.45. At this pH, PGD2 releases a hydrogen ion and exists completely in its water-soluble, ionized (negatively charged) form. [2, 3, 5, 6]
-   Laboratory Solutions: For medical research or diagnostic testing, pure PGD2 crystalline solid is typically dissolved in a specialized phosphate-buffered saline (PBS) held at a neutral pH of 7.2 to keep the molecule stable. [3, 7]

## 4. Electrochemistry of the Human Body: pH, Voltage, and Nerve Excitability

This document maps out the mathematical and physical relationship between hydrogen ion concentrations ($\text{pH}$), electrical potential ($E$), and the activation of voltage-gated nerve channels. 

---

# 1. The Nernst Equation: Converting pH to Millivolts

The **Nernst Equation** calculates the reduction potential of an electrochemical cell based on the concentrations of chemical species. Because $\text{pH}$ is a direct measurement of the hydrogen ion ($\text{H}^+$) concentration, changes in $\text{pH}$ alter the local electrical potential (voltage).

The general Nernst equation for a proton exchange reaction ($\text{H}^+ + e^- \rightleftharpoons \frac{1}{2}\text{H}_2$) is written as:

$$E = E^0 - \frac{RT}{nF} \ln\left(\frac{1}{[\text{H}^+]}\right)$$

### Constants and Variables (at Human Body Temperature)
*   **$E$**: Electrochemical potential (Voltage in Volts)
*   **$E^0$**: Standard electrode potential (0 V for the standard hydrogen electrode)
*   **$R$**: Ideal gas constant = $8.314 \text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$
*   **$T$**: Human body temperature = $37^\circ\text{C} = 310.15 \text{ K}$
*   **$F$**: Faraday constant = $96,485 \text{ C}\cdot\text{mol}^{-1}$
*   **$n$**: Number of electrons transferred per proton = $1$

### Derivation using Base-10 Logarithms ($\text{pH}$)
By definition, $\text{pH} = -\log_{10}([\text{H}^+])$. Converting the natural logarithm ($\ln$) to a common logarithm ($\log_{10}$):

$$\ln\left(\frac{1}{[\text{H}^+]}\right) = -\ln([\text{H}^+]) = -2.303 \log_{10}([\text{H}^+]) = 2.303 \cdot \text{pH}$$

Substituting these values into the equation at $310.15 \text{ K}$:

$$E = 0 - \frac{(8.314) \cdot (310.15)}{1 \cdot 96,485} \cdot 2.303 \cdot \text{pH}$$

$$E = -0.0615 \cdot \text{pH} \text{ Volts}$$

Converting to Millivolts ($\text{mV}$):

$$E = -61.5 \cdot \text{pH} \text{ mV}$$

### The "Nernstian Slope" of pH Shifts
To find the exact change in millivolts per unit change in $\text{pH}$, we take the derivative ($\Delta E / \Delta \text{pH}$):

$$\Delta E = -61.5 \text{ mV} \cdot \Delta \text{pH}$$

*   **A decrease of 1.0 $\text{pH}$ unit** (higher $\text{H}^+$ acidity) shifts the electrical potential by **$+61.5 \text{ mV}$**.
*   **An increase of 1.0 $\text{pH}$ unit** (higher electron/$\text{OH}^-$ density) shifts the electrical potential by **$-61.5 \text{ mV}$**.

---

# 2. Membrane Potentials: The Goldman-Hodgkin-Katz (GHK) Equation

While the Nernst equation calculates the potential for a single ion, a human nerve cell membrane is permeable to multiple ions simultaneously ($\text{K}^+$, $\text{Na}^+$, and $\text{Cl}^-$). The resting membrane potential ($V_m$) is determined by the **GHK equation**:

$$V_m = \frac{RT}{F} \ln \left( \frac{P_{\text{K}}[\text{K}^+]_{\text{out}} + P_{\text{Na}}[\text{Na}^+]_{\text{out}} + P_{\text{Cl}}[\text{Cl}^-]_{\text{in}}}{P_{\text{K}}[\text{K}^+]_{\text{in}} + P_{\text{Na}}[\text{Na}^+]_{\text{in}} + P_{\text{Cl}}[\text{Cl}^-]_{\text{out}}} \right)$$

Where:
*   **$P_{\text{Ion}}$**: The permeability coefficient of the membrane for that specific ion.
*   **$[\text{Ion}]_{\text{out}}$**: Concentration of the ion outside the nerve cell.
*   **$[\text{Ion}]_{\text{in}}$**: Concentration of the ion inside the nerve cell.

---

# 3. Voltage-Gated Nerve Channels and Charge Density

Voltage-gated sodium channels ($\text{Na}_v$) possess a highly charged localized protein structure called the **voltage sensor domain (VSD)**. The physical mechanism of channel activation relies on Coulomb's law and electrostatics.

### The Gating Charge Movement Equation
The voltage sensor domain contains a helix (S4) packed with positively charged amino acids (arginine and lysine). The electrical force ($F_e$) acting on these gating charges ($q$) depends directly on the transmembrane electric field ($E_{field}$):

$$F_e = q \cdot E_{field}$$

The electric field across a cell membrane of thickness $d$ (approximately $4 \times 10^{-9} \text{ m}$) is calculated as:

$$E_{field} = \frac{V_m}{d}$$

### Boltzmann Distribution for Channel Opening
The probability ($P_{\text{open}}$) of a nerve channel snapping open changes based on the surrounding electrical work ($W$). It follows a two-state Boltzmann distribution:

$$P_{\text{open}} = \frac{1}{1 + e^{\frac{\Delta G^0 - qF V_m}{RT}}}$$

Where:
*   **$\Delta G^0$**: The intrinsic chemical free-energy barrier keeping the channel closed.
*   **$q$**: The net gating charge equivalent (number of electron charges moving through the field).

---

# 4. How Local Electron Density Spikes Fire Nerves

When a localized environment experiences a rapid change in electron density—either due to a local metabolic basic shift ($\text{pH}$ increase) or the accumulation of ionized, negatively charged signaling molecules like $\text{PGD}_2$:

1.  **Surface Charge Screening Alteration:** The increased negative charge density outside the cell neutralizes the external positive charge cloud.
2.  **Electric Field Compression:** According to $E_{field} = \frac{V_m}{d}$, localizing a negative charge layer directly on the outer membrane leaflet mimics an internal depolarization. The sensor domain perceives the transmembrane voltage as less negative.
3.  **Conformational Shift:** The positive charges ($q$) on the S4 helix are no longer tightly held inward by electrostatic attraction. They move outward toward the negative charge density.
4.  **Action Potential Firing:** This movement drives $P_{\text{open}}$ to near $1.0$, opening the $\text{Na}_v$ pore. Sodium ions rush in down their electrochemical gradient, generating the electrical action potential interpreted by the brain as an intense flush or prickling sensation.
