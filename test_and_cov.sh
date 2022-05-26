#!/bin/bash

pytest
pytest --cov=base-my_first_sudoku_solver --cov-report=xml
coverage-badge -f -q -o coverage.svg
