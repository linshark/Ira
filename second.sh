#!/bin/bash
BLUE='\033[1;34m'
NC='\033[0m'
cd tests
echo "${BLUE}The result of test 2 is:${NC} "
tclsh test.tcl