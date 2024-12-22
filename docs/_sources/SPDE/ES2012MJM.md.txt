# An ALE ESFEM for solving PDEs on evolving surfaces

## Main questions:
* which tangentail velocity? by BGN method
* is it stable? or analyzed? Not analyzed. 

## Main feature:
* linear fem
* forced mean curvature flow: \[V=\kappa+\alpha g\], g is a given forcing function

## Other problems:
* eigenvalue problem on surface with holes using homology fem
* 

## Literature
* ESFEM的引入： G. Dziuk and C. M. Elliott, Finite elements on evolving surfaces, IMA Journal Numerical Analysis, 25 (2007), pp. 385–407.
* ESFEM Eulerian: An Eulerian approach to transport and diffusion on evolving implicit surfaces, Computing and Visualization in Science, 13 (2010), pp. 17–28

## Charles M. Elliott and Vanessa Styles
## 主题
* ALE-ESFEM for **parabolic** equation on evolving surfaces
* describing surface by level set function
* influence the quality of the finite element mesh and how this in turn influences the accuracy of the approximate solutions of (1.1)

## Applications
* dealloying metals by surface dissolution [32]
* diffusion in- duced grain boundary motion [44, 39, 16, 18, 41]
* transport of an insoluble surfactant on the interface between two fluids, [1, 63, 46, 36]
* pattern formation on biological surfaces [2] 
* cell migration and chemotaxis, [54, 37].

## Existing works
### stationary surface PDE
* Laplace-Beltrami equation piece-wise linear [22], high order FEM for elliptic [20]
* parabolic on stationary surface [26]
* coupling surface and bulk elliptic [33]
* dG surface FEM [19]
### evolving surface PDE
* conservation law on moving surface [25]

    `The key idea is to use the Leibniz (or transport) formula for the time derivative of integrals over moving surfaces in order to derive weak and variational formulations.`
* Further numerical analysis may be found in [30, 29, 31]
* Applications: [32, 35, 2, 37]
### bulk equations in one space dimension higher
* yielding degenerate bulk PDEs, difficulty: level set approximations to surface quantities such as the mean curvature and normal velocity were required
* [28] using an implicit surface version of the Leibniz formula, use a bulk triangulation, In practice it may be useful to solve in a narrow band and use unfitted bulk finite elements, [3], [15] gave a discretisation error analysis.
* bulk unfitted mesh: 



## Simulations of two applications arising in material science and biology
* solid tumour growth introduced in [12]
* diffusion induced grain boundary motion