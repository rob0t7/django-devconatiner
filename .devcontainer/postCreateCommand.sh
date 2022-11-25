#!/usr/bin/env bash

# Install Tilt for Kubernetes native development
curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash

# Run PDM to manage python packages
pdm --pep582 bash >> ~/.bashrc
pdm sync
