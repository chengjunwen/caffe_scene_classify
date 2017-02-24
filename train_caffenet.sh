#!/usr/bin/env sh                                                                        


./build/tools/caffe train \
    --solver=examples/myProject/scene_solver.prototxt \
	2>&1 | tee scene_lenetbn.output
