# Links
* [l1 methods](http://nbviewer.ipython.org/github/gditzler/MG-SubsetSelection/blob/master/notebooks/L1-Regs.ipynb)
* [mim-test](http://nbviewer.ipython.org/github/gditzler/MG-SubsetSelection/blob/master/notebooks/MIM-Test.ipynb)

# Setting up the IPython server

First, `ssh` into the server then run 
```bash
  ipython notebook --no-browser --port=8889
```
to begin an IPython notebook on port `8889`. The open a shell on your local machine and create an `ssh` tunnel to the server that the IPython notebook is running on. This can be achieved with:
```bash
  ssh -N -f -L localhost:8888:localhost:8889 ditzler@myserver.com 
``` 
The open a web browser and go to [http://localhost:8888](http://localhost:8888). You can run `sudo killall ssh` to end all `ssh` sessions once you are done with everything. 
