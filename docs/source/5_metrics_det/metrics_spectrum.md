# 3 Effective resolution computation

<br>
 

<br>

Two tools have been widely used in the oceanography community to assess the effective resolution of a velocity production. The computation of the Eddy Kinetic Energy as a function of the wavelength gives insight of the spatial resolution, while the rotary spectrum as a function of the frequency will provide the temporal scales that are resolved.
Finally, when a reference velocity field is available, the coherence spectrum between the reference and the product to be validated can be analyze to better assess the accuracy as a function of the spatial scale.

<br>
 
## 3.1 EKE spectrum 

The Power Spectrum is used to analyze the energy content of the oceanic current field. Specifically, the EKE (Eddy Kinetic Energy) power spectrum is computed, which describes the distribution of kinetic energy at different spatial scales (k).

$$ E(k) = \sum _k {EKE(k) e^{i2\pi k}}$$

Understanding the EKE power spectrum helps identify the currents energy repartition in space, thus, highlighting dominant features and scales of motion in the ocean.

\subsection{Rotary spectrum}
The rotary spectrum is used to analyse the peak of energy as a function of the frequency. It enables to look at signal with a known temporal repetitivity such as the tides or the inertial response to the wind. The different steps to compute a rotary spectrum are described below.

<br>
 
## 3.2 Compute Fourier Transforms

Complex Time Series: Combine the two orthogonal components into a complex time series:
$$Z(t) = u(t) + i v(t)$$
where $u(t)$ is the eastward velocity component, $v(t)$ is the northward velocity component, and i is the imaginary unit.

Fourier Transform: Compute the discrete Fourier transform (DFT) of the complex time series using the Fast Fourier Transform (FFT) algorithm:

$$\hat{Z} (f)=F{Z(t)}$$
where F denotes the Fourier transform operator and $\hat{Z}(f)$ is the Fourier transform of Z(t).

<br>
 
### 3.2.1 Split into Clockwise and Counterclockwise Components

Rotary Components: Separate the spectrum into clockwise (CW) and counterclockwise (CCW) rotating components. This is done by defining:

$$Z_{+}(f) = \hat{Z}(f)$$

for clockwise components

$$Z_{-}(f) = \hat{Z}^{*}(-f)$$

for counterclockwise components

<br>
 
### 3.2.2 Compute Power Spectral Density (PSD)

Spectral Density: Calculate the power spectral density for each component:

$$S_{+}(f) = \frac{2}{N} |Z_{+}(f)|^{2}$$

$$S_{-}(f) = \frac{2}{N} |Z_{-}(f)|^{2}$$

where N is the number of data points in the time series

<br>
 
### 3.2.3 Interpret the Rotary Spectrum

As described previously, the rotary spectrum
$S(f)$ consists of $S_{+}(f)$ and $S_{-}(f)$, which provide information about the distribution of energy in the clockwise and counterclockwise rotating motions, respectively.
The rotary spectrum is analyzed to understand the directional characteristics and energy distribution of the ocean currents. The peaks in the spectrum indicate dominant frequencies and their rotational direction.


<br>
 
## Coherency spectrum

The spatial coherency spectrum $C_{xy} $ between two fields x and y is computed by normalizing the cross spectral density $S_{xy}$ with the power spectral density of the two signals $S_{x}$ and $S_{y}$ :

$$ C_{xy}(k) = frac{|S_{xy}(k)|^2}{S_{x}(k)S_{y}(k)}$$


 

