# Aerodynamic Coefficients of a Cube in Mach 6 Flow

This repository provides correlations for the aerodynamic coefficients of a cube in Mach 6 flow.
The correlations were developed from CFD data calculated using the transient, compressible flow solver Eilmer (https://gdtk.uqcloud.net/docs/eilmer/about/).

## Force and Moment Coefficients

We model our aerodynamic forces $\mathbf{F}$ and moments $\mathbf{M}$ as force and moment coefficients

$$ [\mathbf{F}]^{\mathrm{B}} = \frac{1}{2}\rho_{\infty}||v_B||^{2} a_c^2\begin{bmatrix} C_{Fx} (M, \alpha^{\prime}, \phi^{\prime}) \\
C_{Fy} (M, \alpha^{\prime}, \phi^{\prime}) \\
C_{Fz} (M, \alpha^{\prime}, \phi^{\prime}) \end{bmatrix} ^{\mathrm{B}} $$

$$ [\mathbf{M}]^{\mathrm{B}} = \frac{1}{2}\rho_{\infty}||v_B||^{2} a_c^3\begin{bmatrix} C_{Mx} (M, \alpha^{\prime}, \phi^{\prime}) \\
C_{My} (M, \alpha^{\prime}, \phi^{\prime}) \\
C_{Mz} (M, \alpha^{\prime}, \phi^{\prime}) \end{bmatrix} ^{\mathrm{B}} $$

Where $$




