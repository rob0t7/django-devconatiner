#!/usr/bin/env bash

# Configure kubectl for running against local docker context
mkdir ~/.kube
docker context export 'default' --kubeconfig
mv default.kubeconfig ~/.kube/config

pdm --pep582 bash >> ~/.bashrc
pdm sync
