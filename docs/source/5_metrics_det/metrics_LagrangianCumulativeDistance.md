# 6 Lagrangian diagnostics

<br>
 

<br>

Two lagrangian diagnostics used in turbulence to analyze divergence and mixing have been successfully applied in oceanography to better understand the dynamics at stake : the Maximum Extent trajectory and the Lyapunov Exponent. 


<br>

## 6.1 Lon / Lat Maximum Extent Trajectories

In the context of turbulence flow analysis, the Maximum Extent Trajectories (MET) maps can be used to study the spatial and temporal dynamics of velocity fields. These maps help identify the most extensive paths or trajectories that particles or fluid elements follow within a turbulent flow field. Such trajectories can provide insights into the mixing, dispersion, and structure of turbulence.

To compute the MET maps, a lagrangian advection is performed in each grid points during a fixed period (typically 10-20 days depending on the targetted resolution of the studied phenomenon). The distance travelled in each direction (eastward and northward) and the total distance are computed. The Final Maps give insight of the divergence, mixing as well as anisotropic behavior of the flow field.


<br>

## 6.2 Statistics and maps using Lyapunov Exponents (FSLE /FTLE)

Finite-Size Lyapunov Exponents (FSLE) and Finite Time Lypaunov Exponents (FTLE) are powerful tools used in the study of dynamical systems, particularly in the analysis of fluid flows and turbulence. FSLE and FTLE gives a measure of the rate of separation of particles initially close to each other in a flow. High values of FTLE and FSLE
corresponds to barriers of transport and can thus be compared with tracer gradients.

FTLE measures the separation of particles over a finite interval while FSLE measures the time it takes for particles to be separated of a chosen distance.


<br>

## 6.3 FTLE computation

FTLE are computed over a fixed finite time called $T$.
A particle at a given position $x(t_{0})$ at time $t_0$ is advected during the period T to compute the postion at $t_0 + T$ $x(t_0 + T)$
The computation is performed on evry grid points and enables the deformation gradient tensor computation F from the flow maps $F$.
The Eigen values and eigen vectors are derived from the Cauchy Green deformation tensor, the FTLE value is the following:

$$ftle(x(t_0)) = \frac{1}{T} ln(\sqrt{\lambda_{max}})$$

with $\lambda_{max}$The maximum of the previousky computed eigen values.

High FTLE values indicate regions of strong stretching and mixing.


<br>

## 6.4 FSLE computation

To compute FSLE, the initial separation ($\delta_0$) and the final separation ($\delta_f$) of particles are fixed. For a given particle x, a lagrangian advection is performed on a set of particules separated by a distance $\delta_0$ until the distance between two particles has reached $\delta_f$. This time is called $T$ andthe FTLE value is the following:

$$fsle(x) = \frac{1}{T} ln(\frac{\delta_f}{\delta_0})$$

High values of FSLE represents diverging areas when the FSLE are computed forward in time and converging areas when computed backward in time.
in ocenography, computing Backward FSLE is a practical ways to retrieve Lagrangian Coherent Structures (LCS) at a given scale $\delta_f$
with $\lambda_{max}$The maximum of the previousky computed eigen values.
