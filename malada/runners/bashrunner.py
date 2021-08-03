import glob
import os
import ase.io
import subprocess

from .runner import Runner


class BashRunner(Runner):
    """
    Runs a simulation.

    This is a really ugly, system calls based runner, that will soon be changed
    out for a better, ASE based runner.
    """

    def __init__(self):
        super(BashRunner, self).__init__()

    def run_folder(self, folder, calculator_type, qe_input_type="*.pw.scf.in"):
        if calculator_type == "qe":
            filelist = glob.glob(os.path.join(folder, qe_input_type))
            if len(filelist) != 1:
                print(filelist, folder)
                raise Exception("Run folder with ambigous content.")
            filename = os.path.basename(filelist[0])
            outfile = filename.replace("in", "out")
            run_process = subprocess.Popen("pw.x -in "+filename+" > "+outfile, cwd=folder, shell=True)
            run_process.wait()

        elif calculator_type == "vasp":
            raise Exception("VASP currently not implemented.")
        else:
            raise Exception("Calculator type unknown.")


