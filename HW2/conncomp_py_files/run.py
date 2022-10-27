import os
import sys
import subprocess
from itertools import chain

def main():
    workspace = sys.argv[1]

    def run_with_args(_in="", _out="", jobname="Basic", envs={}, num_reducers=1):
        try:
            return subprocess.run(["mapred", "streaming", "-D", f"mapreduce.job.reduces={num_reducers}",
                                   "-file", f"./{jobname}Mapper.py", "-file", f"./{jobname}Reducer.py",
                                   "-input", workspace + _in, "-output", workspace + _out,
                                   "-mapper", f"./{jobname}Mapper.py", "-reducer", f"./{jobname}Reducer.py",
                                   *chain.from_iterable([["-cmdenv", f"{k}={v}"] for k, v in envs.items()])]).returncode
        except:
            return 1

    if run_with_args("", "/iter0", "Adj", num_reducers=10) != 0: sys.exit(1) # AdjMapper / AdjReducer
    
    i = 1
    while True:
        if run_with_args(f"/iter{i-1}", f"/iter{i}", "CC", num_reducers=10) != 0: sys.exit(1) # CCMapper / CCReducer
        if run_with_args(f"/iter{i}", f"/diff{i}", "Diff") != 0: sys.exit(1) # DiffMapper / DiffReducer

        # read a file to check the loop condition
        proc_read_diff = subprocess.run(["hadoop", "fs", "-cat", workspace + f"/diff{i}/part-00000"], capture_output=True, text=True)
        if proc_read_diff.returncode != 0: sys.exit(1)
        _, Diff = proc_read_diff.stdout.replace('\t', '\n').strip().split('\n')
        if int(Diff) == 0:
            break

        i += 1

    if run_with_args(f"/iter{i}", "/cnt", "Cnt", num_reducers=10) != 0: sys.exit(1) # CntMapper / CntReducer
    if run_with_args("/cnt", "/output", "Out") != 0: sys.exit(1) # OutMapper / OutReducer
    

if __name__ == '__main__':
    main()
