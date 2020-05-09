# Pac Man Intelligence

Pacman is one of the most famous arcade games of all time. In this present version, pacman must collect pills, dodge obstacles and escape from ghosts in order to reach the final goal. However, he must do this intelligently and sagaciously.
This work presents five ways to solve the Pacman problem:
- Two blind searches: Breadth First Search (BFS), Depth First Search (DFS);
- Two informed searches: AStar, Best First Search
  - Two Heuristics: Distance from Manhattan and Euclidean
- A local search: Simulated Annealing

The user can choose the algorithm to be executed and the type of map to be generated.
The user is shown the total map, with our hero, ghosts, obstacles, objectives and final path, in addition to the log of use of hardware resources and cost of the solution, leaving the user to draw their conclusions.

Enjoy!

# Requisites
## Download Git

* Download and install Git [link](https://git-scm.com/).

## Clone repository
`````
git https://github.com/MatteusStranger/pac_man_intelligence.git
`````



You can run this project using Anaconda or Docker

---

# How to run
## Install Conda (Summarized)

* Download and install Conda using this [link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages)

* Open ananconda shell and go to project path

* Run jupyter

###  Some recommendation before run jupyter

#### Create an environment
`````
conda create -y --name mo416_project1 python==3.7 
`````

#### Activate environment
`````
conda activate mo416_project1
`````

#### Install requirements
`````
pip install -r requirements.txt
`````

#### Run using python
`````
python3 main.py
`````

#### Open using jupyter notebook

`````
jupyter notebook
`````
Remember: Go to project path before run this command on your Anaconda Terminal


#### Uninstall environment
`````
conda activate base
conda remove --name mo416_project1 --all
`````


## Install Docker

  Download and install Docker using this [link](https://www.docker.com/products/docker-desktop)

#### Create a slim image with python and jupyter

`````
docker build -t "jupyter_slim" .
`````

#### Create container with jupyter notebook

Developement mode (If you modify in jupyter notebook you will see modification on your project)
`````
docker run --name mo416_project1 -p 8888:8888 -v "$(pwd):/app" jupyter_slim
`````

Deploy mode (If you modify in jupyter you won't see modification on your project)
`````
docker run --name mo416_project1 -p 8888:8888  jupyter_slim
`````

Output

`````
##This is example won't work on your computer
##Similar message will appear
## And you will copy this information on your browser e.g  http://127.0.0.1:8888/?token=8edc114e3d542b5df702d213cdcd26ab9316b0cd0d0e36c3

    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
    Or copy and paste one of these URLs:
        http://1121c64889ab:8888/?token=8edc114e3d542b5df702d213cdcd26ab9316b0cd0d0e36c3
     or http://127.0.0.1:8888/?token=8edc114e3d542b5df702d213cdcd26ab9316b0cd0d0e36c3
`````

#### Open your browser and run 

`````
http://127.0.0.1:8888/?
`````

Copy token if necessary



#### Uninstall container and image 
`````
docker stop mo416_project1
docker rm mo416_project1
docker rmi jupyter_slim
`````
