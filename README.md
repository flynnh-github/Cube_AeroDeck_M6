# Aerodynamic Coefficients of a Cube in Mach 6 Flow

This repository provides correlations for the aerodynamic coefficients of a cube in Mach 6 flow.
The correlations were developed from CFD data calculated using the transient, compressible flow solver Eilmer (https://gdtk.uqcloud.net/docs/eilmer/about/).

## Citing This Work

To be completed once published.

## TLDR

The regression coefficients for the force and moment coefficients are given in **_CFx.csv_**, **_CFy.csv_**, **_CFz.csv_**, **_CMx.csv_**, **_CMy.csv_**, **_CMz.csv_**.
Python files **_example1.py_** and **_example2.py_** show how to use them.

## Force and Moment Coefficients

We model our aerodynamic forces $\mathbf{F}$ and moments $\mathbf{M}$ as force and moment coefficients in body fixed coordinates by

$$ [\mathbf{F}]^{\mathrm{B}} = \frac{1}{2}\rho_{\infty}||v_B||^{2} a_c^2\begin{bmatrix} C_{Fx} (M, \alpha^{\prime}, \phi^{\prime}) \\
C_{Fy} (M, \alpha^{\prime}, \phi^{\prime}) \\
C_{Fz} (M, \alpha^{\prime}, \phi^{\prime}) \end{bmatrix} ^{\mathrm{B}} $$

$$ [\mathbf{M}]^{\mathrm{B}} = \frac{1}{2}\rho_{\infty}||v_B||^{2} a_c^3\begin{bmatrix} C_{Mx} (M, \alpha^{\prime}, \phi^{\prime}) \\
C_{My} (M, \alpha^{\prime}, \phi^{\prime}) \\
C_{Mz} (M, \alpha^{\prime}, \phi^{\prime}) \end{bmatrix} ^{\mathrm{B}} $$

where $a_c$ is the cube side length, $\rho_\infty$ is the freestream flow density and $M$ is the mach number of the freestream flow. 
The aeroballistic flow angles, $\alpha^{\prime}$, $\phi^{\prime}$ and cube velocity relative to the air, $v_B$, are shown below.

<img width="338" alt="image" src="https://github.com/flynnh-github/Cube_AeroDeck_M6/assets/100339411/4ff02893-c743-4ba4-9b12-207e5e0d2581">

## Correlations

The correlations are based on real-valued basis functions defined by spherical harmonics. Spherical harmonics of degree $l$ and order $m$ are described by

$$ \begin{aligned} 
    Y_l^m(\alpha^{\prime}, \phi^{\prime}) = \sqrt{\frac{2l + 1}{4\pi} \frac{(l-m)!}{(l+m)!}} P_l^m(\cos{\alpha^{\prime}})e^{im\phi^{\prime}}
   \end{aligned} $$

where $l$ is a positive integer, $m$ is an integer ($|m| \leq l$) and $P_l^m$ is an associated Legendre Polynomial. The basis function $y_{lm}$ is given by

$$y_{lm} (\alpha^{\prime}_i, \phi^{\prime}_i) = \begin{cases}
            \sqrt{2} \left(-1\right)^{m} \Im{\left[Y_l^{\lvert m \rvert}\left( \alpha_i^{\prime}, \phi_i^{\prime} \right) \right]} & m < 0 \\
            Y_l^0 \left( \alpha_i^{\prime}, \phi_i^{\prime} \right) & m = 0 \\
            \sqrt{2} \left(-1\right)^{m} \Re{\left[Y_l^{m} \left( \alpha_i^{\prime}, \phi_i^{\prime} \right) \right]} & m > 0
        \end{cases} $$

A linear combination of these basis functions form the correlations $C_{Fi}$, $C_{Mi}$, where $i = x^{\mathrm{B}}, y^{\mathrm{B}}$ or $z^{\mathrm{B}}$.
please see _**example1.py**_ and **_example2.py_** for examples of how to use these basis functions to sample our correlations. The correlations are shown below.

<img width="600" alt="image" src="https://github.com/flynnh-github/Cube_AeroDeck_M6/assets/100339411/3bb35584-aa00-4ca8-806a-34f384c9aba5">



