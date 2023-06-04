import julia

j = julia.Julia(compiled_modules=False)
ran = j.include("calippso.jl")