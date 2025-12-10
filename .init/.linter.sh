#!/bin/bash
cd /home/kavia/workspace/code-generation/enterprise-dashboard-project-50168-50284/DashboardBackendAPI
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

