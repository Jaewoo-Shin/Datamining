import os
import sys
import subprocess
from itertools import chain

def main():
    # Feel free to use a provided implementation! (AdjMapper/Reducer, TP2Mapper/Reducer, DiffMapper/Reducer)
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

    i = 0
    while True:
        if i == 0:
            if run_with_args("", "/mid0", "Adj", num_reducers=10) != 0: sys.exit(1) #AdjMapper / AdjReducer
        else:
            if run_with_args(f"/iter{i-1}", f"/mid{i}", "PR",
                             {"pagerank_damping_factor": float(sys.argv[2])}, num_reducers=10) != 0: sys.exit(1) # PRMapper / PRReducer

        if run_with_args(f"/mid{i}", f"/stat{i}", "TP1") != 0: sys.exit(1) # TP1Mapper / TP1Reducer

        # read a file to get N and S
        proc_read_stat = subprocess.run(["hadoop", "fs", "-cat", workspace + f"/stat{i}/part-00000"], capture_output=True, text=True)
        if proc_read_stat.returncode != 0: sys.exit(1)
        _, N, _, S = proc_read_stat.stdout.replace('\t', '\n').strip().split('\n')

        if run_with_args(f"/mid{i}", f"/iter{i}", "TP2",
                         {"pagerank_num_nodes": N, "pagerank_sum_scores": S}, num_reducers=10) != 0: sys.exit(1) # TP2Mapper / TP2Reducer

        if i > 0:
            if run_with_args(f"/iter{i}", f"/diff{i}", "Diff") != 0: sys.exit(1) # DiffMapper / DiffReducer

            # read a file to check the loop condition
            proc_read_diff = subprocess.run(["hadoop", "fs", "-cat", workspace + f"/diff{i}/part-00000"], capture_output=True, text=True)
            if proc_read_diff.returncode != 0: sys.exit(1)
            _, Diff = proc_read_diff.stdout.replace('\t', '\n').strip().split('\n')
            if float(Diff) < 1e-4:
                break

        i += 1

    if run_with_args(f"/iter{i}", "/output", "Out") != 0: sys.exit(1) # OutMapper / OutReducer

if __name__ == '__main__':
    main()

