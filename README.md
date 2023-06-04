# calippso-to-53
_TL;DR summary below_

Introduction:
This is a semester long effort in manifesting some sort of jammed packing

## Installation and Prerequisites
__This is a computationally heavy program.__ Therefore, it is recommended to run this Python script on a computer
with a good CPU; for reference, I have a Ryzen 7 processor, and this program can take 20 minutes to complete 
while utilizing 20% to 40% resources.

__Gurobi IS required.__ The second version of CALiPPSO does not run with GLPK.

1. [Register for free Gurobi Academic License with Academia email.](https://www.gurobi.com/features/academic-named-user-license/)
2. [Click 'Register for a free Gurobi account as an academic and log in.'](https://portal.gurobi.com/iam/register/)
3. Register account.
4. [Download the pertinent Gurobi version.](https://www.gurobi.com/downloads/gurobi-software/)
5. [Linux users may have to follow this guide to set up environment paths.](https://ca.cs.uni-bonn.de/doku.php?id=tutorial:gurobi-install)
6. [Windows users just run .exe file and copy and paste the 'grbgetkey' command under "INSTALL" under their User Portal Licenses.](https://portal.gurobi.com/iam/licenses/list/)


Gurobi should be installed and registered on your machine.

__Julia IS required.__ The CALLiPPSO runs on Julia.

1. [Julia installation for platforms are documented on their website.](https://julialang.org/downloads/)
2. [Install PyJulia, __ENSURING THAT PyJulia IS INSTALLED ON THE SAME PYTHON VERSION AS THE ONE THAT WILL RUN THE SCRIPT.__](https://pyjulia.readthedocs.io/en/latest/installation.html)
3. [Once Julia is installed, run `python` or `python3` in command prompt or terminal and run the following:](https://github.com/JuliaPy/pyjulia#quick-usage)
```$ python3
>>> import julia
>>> julia.install()               # install PyCall.jl etc.
>>> from julia import Base        # short demo
>>> Base.sind(90)
1.0
```
4. Once Julia is installed, run `]add CALiPPSO` in a Julia REPL ([For Windows, search 'Julia'. For Linux, run 'julia' in the terminal.](https://docs.juliahub.com/CALiPPSO/vkUrj/0.2.1/installation.html))
5. Go to VSCode and install the Julia extension from the VSCode marketplace.
6. Go to File > Preferences > Settings. Then, search "Julia: Executable Path". Enter the path to your julia executable, ex: `C:/Users/jay/AppData/Local/Programs/Julia-1.9.0/bin/julia.exe`

It is assumed that matplotlib, numpy, and among other modules in the main Python script are installed.


## Running the program
Open `final_linux.py` for Linux or `final_Windows.py` for Windows in VSCode and run.

A 'before' image will be generated under `LS\datums` like thus `before_calippso2023-06-03 23:23:40.500104.png`, which is the Lubachevsky–Stillinger algorithm generation of packing of 2969 2D hard spheres. (The number 2969 
was derived from trial-and-error to get a ratio of 1:106 between sphere diameter and domain diameter). 

An 'after' image will be generated under `LS\datums` like thus `after_calippso2023-06-03 23:24:00.619953.png` with the same time stamp as the corresponding 'before' image. This is the spheres after jamming, and the 
image will only be produced if CALiPPSO successfully jammed the initial LS-packing. There are many cases where the CALiPPSO will fail.

# TLDR
Go to __Installation and Prerequisites__ and ensure everything is installed. Then run `final_linux.py` or `final_Windows.py`.

## Works Cited

* "Packing hard spheres in high dimensional Euclidean spaces", by M. Skoge, A. Donev, F. H. Stillinger, and S. Torquato, Phys. Rev. E, Vol. 74: 041127 (2006) [ibid 75: 029901 (2007)], [[cond-mat/0608362](https://arxiv.org/abs/cond-mat/0608362)]
* "CALiPPSO: A Linear Programming Algorithm for Jamming Hard Spheres", by Artiaco, Claudia and Rojas, Rafael Díaz Hernández and Parisi, Giorgio and Ricci-Tersenghi, Federico, (2022) [http://arxiv.org/abs/2203.05654] 


