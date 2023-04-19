using CALiPPSO 
using Random
Random.seed!(123) # optional, but just for reproducibility sake of this MWE
# Choosing the seed of the Julia's RNG determines the random IC produces below with `generate_random_configuration`

using Gurobi
const grb_env = Gurobi.Env()
const grb_opt = Gurobi.Optimizer(grb_env)
const grb_attributes = Dict("OutputFlag" => 0, "FeasibilityTol" => 1e-9, "OptimalityTol" => 1e-9, "Method" => 3, "Threads" => CALiPPSO.max_threads)

const default_tol_optimality = CALiPPSO.default_tol_optimality
const tol_Γ_convergence = default_tol_optimality
const tol_displacements = 10*default_tol_optimality

#precompile_main_function(grb_opt, grb_attributes) #optional, but highly recommended. This will produce a colorful output that you can safely ignore
const d, N, φ0, L = 2, 500, 0.3, 106.0



r0 = 1.0 # initial radius of particles
Xs0 = PeriodicVectors(Matrix(readdlm("C:/Users/jo/Desktop/dolbow/LS/2969.dat", skipstart=3)'), L) # initial particles' positions


#r0, Xs0 = generate_random_configuration(d, N, φ0, L) # if L is not passed, it's assumed that the systems is in a box of size 1

packing, info, Γ_vs_t, Smax_vs_t, isostatic_vs_t = produce_jammed_configuration!(Xs0, r0; 
        ℓ0=0.2*L, max_iters=500, optimizer=grb_opt, solver_attributes=grb_attributes, tol_Γ_convergence=tol_Γ_convergence, tol_S_convergence=tol_displacements)