#!/usr/bin/env sh                                                                        
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/myProject/data
DATA=examples/myProject/data
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/mit_indoor_train_lmdb \
  $DATA/imagenet_mean.binaryproto

echo "Done."

