#!/bin/bash
parallel -t -j 1 "python seq_to_json.py {1} -s -o test_output/{1/}" ::: test_input/*