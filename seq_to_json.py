#!/usr/bin/env python
"""\
This script extracts feature information from GenBank and EMBL files and converts to JSON

Usage: python seq_to_json.py input.gb

Author: Paul Stothard
"""
import argparse
import re
import json
import sys
from pathlib import Path


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def remove_whitespace(string):
    return re.sub(r'\s+', '', string)


def remove_newlines(string):
    return re.sub(r'[\n\r]+', '', string)


def remove_digits(string):
    return re.sub(r'\d', '', string)


# format feature qualifier value by removing newlines if there are no spaces within the value
# otherwise replace newlines with spaces
def format_feature_qualifier_value(feature_qualifier_text):
    if re.search(r'\S\s\S', feature_qualifier_text):
        return re.sub(r'[\s]+', ' ', feature_qualifier_text)
    else:
        return re.sub(r'[\s]+', '', feature_qualifier_text)


def reverse(string):
    return string[::-1]


def complement(dna):
    table = str.maketrans("ACGTURYSWKMBDHVNacgturyswkmbdhvn",
                          "TGCAAYRSWMKVHDBNtgcaayrswmkvhdbn")
    return dna.translate(table)


# return FALSE if sequence record appears to be empty, e.g. just // or blank line
def is_sequence_record(sequence_record_text):
    if re.search(r'^\s*\/\/\s*$', sequence_record_text):
        return False
    elif re.search(r'^\s*$', sequence_record_text):
        return False
    return True


# return FALSE if feature qualifier appears to be empty, e.g. just / or blank line
def is_feature_qualifier(feature_qualifier_text):
    if re.search(r'^\s*\/\s*$', feature_qualifier_text):
        return False
    elif re.search(r'^\s*$', feature_qualifier_text):
        return False
    return True


# return FALSE if feature appears to be empty, e.g. just / or blank line
def is_feature(feature_text):
    if re.search(r'^\s*\/\s*$', feature_text):
        return False
    elif re.search(r'^\s*$', feature_text):
        return False
    return True


# return FALSE if feature range is of a type that cannot be converted to a start and end
# examples of ranges that cannot be converted to start and end:
# 102.110
# 123^124
# J00194.1:100..202
# join(1..100,J00194.1:100..202)
def is_parsable_feature_range(feature_range_text):
    if re.search(r'\d\.\d', feature_range_text):
        return False
    if re.search(r'\^', feature_range_text):
        return False
    if re.search(r':', feature_range_text):
        return False
    elif re.search(r'^\s*$', feature_range_text):
        return False
    return True

# parse text into array of sequence records by splitting on //


def get_seq_records(sequence_file_text):
    records = []
    for record_text in filter(is_sequence_record, re.split(r'^\/\/', sequence_file_text, flags=re.MULTILINE)):
        record = {}
        record['name'] = get_seq_name(record_text)
        record['length'] = get_seq_length(record_text)
        record['sequence'] = get_seq(record_text)
        record['features'] = get_features(record_text)
        records.append(record)
    return records


# get a sequence name from a GenBank or EMBL record
# in GenBank look for e.g.:
# LOCUS       AF177870     3123 bp    DNA             INV       31-OCT-1999
# in EMBL look for e.g.:
# ID   AF177870; SV 1; linear; genomic DNA; STD; INV; 3123 BP.
# name is AF177870
def get_seq_name(sequence_record_text):
    m = re.search(r'^\s*(?:LOCUS|ID)\s*(\S+)', sequence_record_text)
    if m:
        return m.group(1)
    else:
        return ""


# get a sequence length from a GenBank or EMBL record
# in GenBank look for e.g.:
# LOCUS       AF177870     3123 bp    DNA             INV       31-OCT-1999
# in EMBL look for e.g.:
# ID   AF177870; SV 1; linear; genomic DNA; STD; INV; 3123 BP.
# length is 3123
def get_seq_length(sequence_record_text):
    m = re.search(r'^\s*(?:LOCUS|ID).*?(\d+)\s[Bb][Pp]', sequence_record_text)
    if m:
        return m.group(1)
    else:
        return ""


# get the full sequence from a GenBank or EMBL record
# in GenBank look for e.g.:
# ORIGIN
#        1 ttttgccctc agtccgtgac ggcgcaggct ttccgtcacg gtttttactt taaaatggta
# in EMBL look for e.g.:
# SQ   Sequence 3123 BP; 986 A; 605 C; 597 G; 935 T; 0 other;
#     gaacgcgaat gcctctctct ctttcgatgg gtatgccaat tgtccacatt cactcgtgtt        60
def get_seq(sequence_record_text):
    m = re.search(r'^(?:ORIGIN|SQ\s{3}).*?$([^\/]*)(^\s*$|^\s*LOCUS)?',
                  sequence_record_text, flags=re.DOTALL | re.MULTILINE)
    if m:
        return remove_digits(remove_whitespace(m.group(1)))
    else:
        return ""


# get an array of dictionaries containing start and end positions from a feature string
# e.g.
#      gene            complement(<1..>172)
#                      /locus_tag="ECPA2_RS30085"
#                      /old_locus_tag="ECPA2_5227"
#                      /pseudo
def get_feature_locations(feature_text):
    locations = []
    m = re.search(r'^\s{5}\S+\s+([^\/]+)', feature_text, flags=re.DOTALL)
    if m:
        ranges = filter(is_parsable_feature_range,
                        re.split(r'(?=,)', m.group(1)))
        for range in ranges:
            location = {}
            m = re.search(r'(\d+)\D*\.\.\D*(\d+)', range)
            if m:
                location['feature_range_start'] = m.group(1)
                location['feature_range_end'] = m.group(2)
                locations.append(location)
    return locations


# get location text of a feature (1 or -1) from a feature string
# e.g.
#      gene            complement(<1..>172)
#                      /locus_tag="ECPA2_RS30085"
#                      /old_locus_tag="ECPA2_5227"
#                      /pseudo
def get_feature_location_text(feature_text):
    m = re.search(r'^\s{5}\S+\s+([^\/]+)', feature_text, flags=re.DOTALL)
    if m:
        return remove_whitespace(m.group(1))
    else:
        return ""


# get an array of dictionaries containing feature qualifier names and values from a feature string
# e.g.
#      gene            complement(<1..>172)
#                      /locus_tag="ECPA2_RS30085"
#                      /old_locus_tag="ECPA2_5227"
#                      /pseudo
def get_feature_qualifiers(feature_text):
    qualifiers = []
    m = re.search(r'(\/.*)', feature_text, flags=re.DOTALL)
    if m:
        for qualifier_text in filter(is_feature_qualifier, re.split(r'(?=^\s*\/)', m.group(1), flags=re.MULTILINE)):
            qualifier = {}
            m = re.search(
                r'\/(\S+)\s*=\s*\"?([^\"]+)\"?(?=^\s*\/|\s)', qualifier_text, flags=re.DOTALL | re.MULTILINE)
            if m:
                qualifier['feature_name'] = m.group(1)
                qualifier['feature_value'] = format_feature_qualifier_value(
                    m.group(2))
            else:
                qualifier['feature_name'] = remove_whitespace(qualifier_text)
                qualifier['feature_value'] = ""
            qualifiers.append(qualifier)
    return qualifiers


# get strand of a feature (1 or -1) from a feature string
# e.g.
#      gene            complement(<1..>172)
#                      /locus_tag="ECPA2_RS30085"
#                      /old_locus_tag="ECPA2_5227"
#                      /pseudo
def get_feature_strand(feature_text):
    m = re.search(r'^\s{5}\S+\s+complement', feature_text)
    if m:
        return -1
    else:
        return 1


# get name of a feature from a feature string
# e.g.
#      gene            complement(<1..>172)
#                      /locus_tag="ECPA2_RS30085"
#                      /old_locus_tag="ECPA2_5227"
#                      /pseudo
def get_feature_name(feature_text):
    m = re.search(r'^\s{5}(\S+)', feature_text)
    if m:
        return m.group(1)
    else:
        return ""


# add feature sequences to an array of dictionaries containing feature information
def add_feature_sequences(seq_records):
    for seq_record in seq_records:
        for feature in seq_record['features']:
            dna = []
            for locations in feature['feature_locations']:
                try:
                    start = int(locations['feature_range_start'])
                    end = int(locations['feature_range_end'])
                    subseq = seq_record['sequence'][start-1:end]
                    dna.append(subseq)
                except:
                    eprint("Unable to add feature sequence for feature: " +
                           feature['feature_name'] + " in sequence: " + seq_record['name'] + ".")
                    break
            if feature['feature_strand'] == -1:
                feature['feature_sequence'] = reverse(complement("".join(dna)))
            elif feature['feature_strand'] == 1:
                feature['feature_sequence'] = "".join(dna)


# add overall feature start and end positions to an array of dictionaries containing feature information
# the start is the smallest start position of all the feature locations
# the end is the largest end position of all the feature locations
def add_overall_feature_start_and_end(seq_records):
    for seq_record in seq_records:
        for feature in seq_record['features']:
            try:
                feature['feature_start'] = sorted(feature['feature_locations'], key=lambda d: int(
                    d['feature_range_start']))[0]['feature_range_start']
                feature['feature_end'] = sorted(feature['feature_locations'], key=lambda d: int(
                    d['feature_range_end']), reverse=True)[0]['feature_range_end']
            except:
                eprint("Unable to add overall feature start and end for feature: " +
                       feature['feature_name'] + " in sequence: " + seq_record['name'] + ".")


# get an array of dictionaries containing feature information from a GenBank or EMBL record
# in GenBank look for:
# FEATURES             Location/Qualifiers
# in EMBL look for:
# FH   Key             Location/Qualifiers
# FH
def get_features(sequence_record_text):
    features = []
    m = re.search(
        r'^(?:FEATURES.*?$|FH.*?^FH.*?$)(.*)^(?:ORIGIN|SQ\s{3}).*?$', sequence_record_text, flags=re.DOTALL | re.MULTILINE)
    if m:
        # replace FT from the start of lines
        # e.g.
        # FT   source          1..3123
        # FT                   /organism="Caenorhabditis brenneri"
        feature_text = re.sub(r'^FT', '  ', m.group(1), flags=re.MULTILINE)

        for feature_string in filter(is_feature, re.split(r'(?=^\s{5}\S+)', feature_text, flags=re.MULTILINE)):
            feature = {}
            feature['feature_name'] = get_feature_name(feature_string)
            feature['feature_strand'] = get_feature_strand(feature_string)
            feature['location_text'] = get_feature_location_text(
                feature_string)
            feature['feature_locations'] = get_feature_locations(
                feature_string)
            feature['feature_qualifiers'] = get_feature_qualifiers(
                feature_string)
            features.append(feature)
    return features


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='seq_to_json.py', description='Extracts feature information from GenBank and EMBL files and converts to JSON', epilog='python seq_to_json.py input.gb')
    parser.add_argument('input', help='GenBank or EMBL file to parse')
    parser.add_argument('-o', '--output', type=str,
                        help='JSON file to create, otherwise write to stdout')
    parser.add_argument('-s', '--sequence', action='store_true',
                        help='include the sequence of features in the output', default=False)
    args = parser.parse_args()

    text_string = Path(args.input).read_text()

    seq_records = get_seq_records(text_string)

    if args.sequence:
        add_feature_sequences(seq_records)

    add_overall_feature_start_and_end(seq_records)

    # run sanity checks on the results
    for seq_record in seq_records:
        assert seq_record['length'] or seq_record['sequence'], "Sequence length and sequence are both missing for sequence: " + seq_record['name'] + "."
        if not seq_record['length'] and seq_record['sequence']:
            seq_record['length'] = len(seq_record['sequence'])
        if seq_record['length'] and seq_record['sequence']:
            assert int(seq_record['length']) == len(seq_record['sequence']), "Reported sequence length " + seq_record['length'] + \
                "does not match actual sequence length " + \
                str(len(seq_record['sequence'])) + \
                " for sequence: " + seq_record['name'] + "."
        for feature in seq_record['features']:
            if feature['feature_start'] and feature['feature_end']:
                assert int(feature['feature_end']) >= int(feature['feature_start']), "Feature end " + feature['feature_end'] + " is less than feature start " + \
                    feature['feature_start'] + " for feature: " + \
                    feature['feature_name'] + " in sequence: " + \
                    seq_record['name'] + "."
            if feature['feature_start'] and seq_record['length']:
                assert int(feature['feature_start']) <= int(seq_record['length']), "Feature start " + feature['feature_start'] + " is greater than sequence length " + \
                    seq_record['length'] + " for feature: " + feature['feature_name'] + \
                    " in sequence: " + seq_record['name'] + "."
            if feature['feature_end'] and seq_record['length']:
                assert int(feature['feature_end']) <= int(seq_record['length']), "Feature end " + feature['feature_end'] + " is greater than sequence length " + \
                    seq_record['length'] + " for feature: " + feature['feature_name'] + \
                    " in sequence: " + seq_record['name'] + "."
            if feature['feature_sequence'] and seq_record['length']:
                assert len(feature['feature_sequence']) <= int(seq_record['length']), "Feature sequence " + feature['feature_sequence'] + \
                    " is greater than sequence length " + \
                    seq_record['length'] + " for feature: " + feature['feature_name'] + \
                    " in sequence: " + seq_record['name'] + "."
            if feature['feature_sequence']:
                expected_length = sum(map(lambda dict: int(dict['feature_range_end']) - int(
                    dict['feature_range_start']) + 1, feature['feature_locations']))
                assert len(feature['feature_sequence']) == expected_length, "Feature sequence " + feature['feature_sequence'] + " is not the expected length " + str(
                    expected_length) + " for feature: " + feature['feature_name'] + " in sequence: " + seq_record['name'] + "."
            for locations in feature['feature_locations']:
                if locations['feature_range_start'] and locations['feature_range_end']:
                    assert int(locations['feature_range_end']) >= int(locations['feature_range_start']), "Feature range end " + locations['feature_range_end'] + \
                        " is less than feature range start " + \
                        locations['feature_range_start'] + " for feature: " + \
                        feature['feature_name'] + " in sequence: " + \
                        seq_record['name'] + "."
                if locations['feature_range_start'] and seq_record['length']:
                    assert int(locations['feature_range_start']) <= int(seq_record['length']), "Feature range start " + locations['feature_range_start'] + \
                        " is greater than sequence length " + \
                        seq_record['length'] + " for feature: " + feature['feature_name'] + \
                        " in sequence: " + seq_record['name'] + "."
                if locations['feature_range_end'] and seq_record['length']:
                    assert int(locations['feature_range_end']) <= int(seq_record['length']), "Feature range end " + locations['feature_range_end'] + \
                        " is greater than sequence length " + \
                        seq_record['length'] + " for feature: " + feature['feature_name'] + \
                        " in sequence: " + seq_record['name'] + "."

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(seq_records, f, indent=4)
    else:
        print(json.dumps(seq_records, indent=4))
