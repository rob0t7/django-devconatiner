#!/usr/bin/env bash

pdm --pep582 bash >> ~/.bashrc
pdm sync
