#!/bin/bash
parallel -t -j 1 "python seq_to_json.py {1} -s -o test_output_local/{1/}" ::: test_input_local/*
diff -r test_output_local sample_output_local