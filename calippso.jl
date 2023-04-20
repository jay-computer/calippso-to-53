using CALiPPSO 
using Random
using DelimitedFiles
using Gurobi
Random.seed!(123) 

grb_env = Gurobi.Env()
grb_opt = Gurobi.Optimizer(grb_env)
grb_attributes = Dict("OutputFlag" => 0, "FeasibilityTol" => 1e-9, "OptimalityTol" => 1e-9, "Method" => 3, "Threads" => CALiPPSO.max_threads)
default_tol_optimality = CALiPPSO.default_tol_optimality
tol_Γ_convergence = default_tol_optimality
tol_displacements = 10*default_tol_optimality


L = readdlm("input_Calippso.dat", skipstart=2)[1]
r0 = 1.0 # initial radius of particles
Xs0 = PeriodicVectors(Matrix(readdlm("input_Calippso.dat", skipstart=3)'), L) # initial particles' positions


packing, info, Γ_vs_t, Smax_vs_t, isostatic_vs_t = produce_jammed_configuration!(Xs0, r0; 
        ℓ0=0.2*L, max_iters=500, optimizer=grb_opt, solver_attributes=grb_attributes, tol_Γ_convergence=tol_Γ_convergence, tol_S_convergence=tol_displacements)

file = open("output_Calippso.txt", "w")
for i in getfield.(packing.Particles, :X)
        write(file, string(i[1].value, ", ", i[2].value, "\n"))
end
close(file)