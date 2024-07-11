# 2 Standard validation using in-situ data

<br>

 
<br>

 

This section describes metrics that can be computed using in-situ drifters.
Several database exists at several depth and with different temporal resolution (from hourly to 6-hourly). Most available drifters are SVP (Surface Velocity Profiler) which are measuring the total currents at 15m depth when droggued and at the surface when the drogue is lost.

<br>

 
## 2.1 Eulerian RMS
 
 
The Eulerian RMS (Root Mean Square) is a metric used to assess the difference between observed and reconstructed currents. It calculates the root of the sum of squared differences between the eastward and northward velocities of the drifter trajectory and the interpolated current at the same position.

Let's call $(u_d(p), v_d(p))$ the eastward and northward velocity derived from the drifter trajectory at the position p. The current to be compared is interpolated in time and space at position p and is called $(u(p), v(p))$.

$$RMS_u = \sqrt{\sum_p{(u(p) -u_d(p))^2}}$$

$$RMS_v = \sqrt{\sum_p{(v(p) -v_d(p))^2}}$$

A lower RMS value indicates better agreement between the observed and model currents.
The RMS in norm and direction can also be computed using:

$$\text{norm}(u, v) = \sqrt{(u^2 + v^2)}$$

$$\text{direction}(u, v) = \text{arctan}(u, v)$$

Note that depending on the temporal resolution of the velocity field you want to validate, you may need to apply a temporal filter to your field.

<br>

 

## 2.2 Lagrangian Cumulative Distance

The Lagrangian Cumulative Distance measures the cumulative separation between real drifters and synthetic drifters over time. For each drifter and each day, an ensemble of particles around the drifter position is released and advected with the velocity field to be validated.

For each drifter, for each day, an ensemble of particles around the drifter position are seeded (1 particle every km in a radius corresponding to the resolution of the velocity field product). These particles are then advected with the velocity field to be validated and compared with the real drifter trajectory.

For each particle $p$, we compute the normalized cumulative separation distance between the real drifter and the synthetic drifter from each product $s_p$ as defined in Liu and Weisberg (2011):

$$s_p[T] = \frac{\sum_{i=t0}^{T} d_p [t]}{\sum_{i=t0}^{T} length[t]} $$

with $d_p[t]$ the Euclidian distance between the virtual particle $p$ and the in situ drifter positions and $length$ the length of the drifter trajectory after a time t of advection from the drifter initial position at time $t0$. $s_p$ are the scores computed for every day T within the period of advection. 

This metric quantifies how well the reconstructed currents can reproduce the drifter's trajectory over time, providing insights into long-term accuracy.