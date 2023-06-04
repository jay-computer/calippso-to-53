import julia
import os
#j = julia.Julia(compiled_modules=False)
#ran = j.include("final.jl")
#os.system("del filename.txt")
print(type(os.getcwd()))

new_dirr = os.getcwd() + "//LS"

#os.system(f"cd {new_dirr}")
os.system("cd LS")
os.system("make")