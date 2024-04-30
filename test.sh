#!/usr/bin/env bash
parallel -t -j 1 "python3 seq_to_json.py {1} -s -o test_output/{1/}" ::: test_input/*
diff -r test_output sample_output