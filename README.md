# seq_to_json
Converts a raw, FASTA, GenBank, or EMBL file to an easy-to-parse JSON file. Feature information is included in the output from GenBank and EMBL files.

## Usage

```
usage: seq_to_json.py [-h] [-o OUTPUT] [-s] input

Converts a raw, FASTA, GenBank, or EMBL file to an easy-to-parse JSON file.

positional arguments:
  input                 Raw, FASTA, GenBank, or EMBL file to parse

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        JSON file to create, otherwise write to stdout
  -s, --sequence        include the sequence of features in the output

python seq_to_json.py input
```

## Example usage

To write JSON to stdout:

```bash
python seq_to_json.py sequence.gbk
```

To write JSON to a file provided as an argument:

```bash
python seq_to_json.py sequence.gbk -o sequence.json
```

To include the sequence of each feature in the JSON:

```bash
python seq_to_json.py sequence.gbk -s
```

## Notes

* Supplied FASTA, GenBank, and EMBL files can contain multiple sequence records.
* For GenBank and EMBL files the `-s` option computes the sequence of each feature, using the supplied feature locations and the overall sequence.
* The script exits with a non-zero exit code if the sequence length for a record cannot be determined or if other anomalies are detected.

## Sample raw input

```text
gacgtcattcaatgggaattactcatcagcttccaatgaaatcctcgggtgtggtcaaaa
gtgtcgcacctcggttgtaccagtagaagaagacgggaccgaccttgggcgactaacgtc
tcctatctgccgcgacacataggactccacgaaggcggtctaaataagcctcaccctcca
tggaactcctaaagggtcttgcacgggcccagtgaactgagaagtgcgtccgggagaacg
ctcgtattggccactgtccgactctaggccggaacccatgtacccgcttagcgttggcaa
agggcatggctacactaaaagcggtaaagggggaacacttctccagctattcccttttcc
aggaagccacgggcgaaacaagaataacgaacgattatcactcaaacttgacaaactggg
atggttatcgtgggtttctatcgctccatggaatcacacttatactttcctgagccttgt
caccaagatcgctgcttgacccacgtgcgcatccatagctggaatcgtttataatgaaca
aagtcaaatggcacatctctggccggccgtgtgaagagatccgttactaatcttggcctc
gtgctgttcaattggcacacttacggtatgatgatctgcagctcgagcccactacacgat
tcctccttattgtcatctaggtcatgattctggtaatgcttcggcagcgacctactacaa
agagcatagcgaacgggtacaaacgccccgttccgtcctctagtaatagttataatcagt
cgtatgatcctacggtactctcaccctcgggttggcaatgcgtattatggacgtctgatt
gagtggatgacggcatatgcccctaaagggtagcgtaataatcttgttaggaaaacgcct
gttgatacgtaagcttgcccgagtggaaccatgttagcgtcttttgagggcgaagtggtc
cgacggtcggggtagtcctctgtcgagcatgcacggtcct
```

## Sample raw output

```text
[
    {
        "name": "",
        "sequence": "gacgtcattcaatgggaattactcatcagcttccaatgaaatcctcgggtgtggtcaaaagtgtcgcacctcggttgtaccagtagaagaagacgggaccgaccttgggcgactaacgtctcctatctgccgcgacacataggactccacgaaggcggtctaaataagcctcaccctccatggaactcctaaagggtcttgcacgggcccagtgaactgagaagtgcgtccgggagaacgctcgtattggccactgtccgactctaggccggaacccatgtacccgcttagcgttggcaaagggcatggctacactaaaagcggtaaagggggaacacttctccagctattcccttttccaggaagccacgggcgaaacaagaataacgaacgattatcactcaaacttgacaaactgggatggttatcgtgggtttctatcgctccatggaatcacacttatactttcctgagccttgtcaccaagatcgctgcttgacccacgtgcgcatccatagctggaatcgtttataatgaacaaagtcaaatggcacatctctggccggccgtgtgaagagatccgttactaatcttggcctcgtgctgttcaattggcacacttacggtatgatgatctgcagctcgagcccactacacgattcctccttattgtcatctaggtcatgattctggtaatgcttcggcagcgacctactacaaagagcatagcgaacgggtacaaacgccccgttccgtcctctagtaatagttataatcagtcgtatgatcctacggtactctcaccctcgggttggcaatgcgtattatggacgtctgattgagtggatgacggcatatgcccctaaagggtagcgtaataatcttgttaggaaaacgcctgttgatacgtaagcttgcccgagtggaaccatgttagcgtcttttgagggcgaagtggtccgacggtcggggtagtcctctgtcgagcatgcacggtcct",
        "length": 1000,
        "features": [],
        "type": "dna"
    }
]
```

## Sample FASTA input

```text
>random sequence 1 consisting of 100 bases.
caggaaagactaacgttctggtcatagatctatggtgtagatgtcaccgtgtccaccatg
cggcaaacaacgattttcgtagcaatgaacaaccgcaagc

>random sequence 2 consisting of 100 bases.
ggtaaagtgctcgttagtttctataggccctggcattactgatagacctcgtcctcccta
tctgttcctaggaacggcccatctctcagccactggtgcc

>random sequence 3 consisting of 100 bases.
ccgtttacgtcgttcggaagttctcagctcatcatacaaggtggctacatgctctctatg
tcgtaatccgacgcaaatgcagaccatggaagtacgaatg
```

## Sample FASTA output

```text
[
    {
        "name": "random sequence 1 consisting of 100 bases.",
        "sequence": "caggaaagactaacgttctggtcatagatctatggtgtagatgtcaccgtgtccaccatgcggcaaacaacgattttcgtagcaatgaacaaccgcaagc",
        "length": 100,
        "features": [],
        "type": "dna"
    },
    {
        "name": "random sequence 2 consisting of 100 bases.",
        "sequence": "ggtaaagtgctcgttagtttctataggccctggcattactgatagacctcgtcctccctatctgttcctaggaacggcccatctctcagccactggtgcc",
        "length": 100,
        "features": [],
        "type": "dna"
    },
    {
        "name": "random sequence 3 consisting of 100 bases.",
        "sequence": "ccgtttacgtcgttcggaagttctcagctcatcatacaaggtggctacatgctctctatgtcgtaatccgacgcaaatgcagaccatggaagtacgaatg",
        "length": 100,
        "features": [],
        "type": "dna"
    }
]
```

## Sample GenBank input

```text
LOCUS       AF177870                3123 bp    DNA     linear   INV 30-MAR-2006
DEFINITION  Caenorhabditis sp. CB5161 putative PP2C protein phosphatase FEM-2
            (fem-2) gene, complete cds.
ACCESSION   AF177870
VERSION     AF177870.1
KEYWORDS    .
SOURCE      Caenorhabditis brenneri
  ORGANISM  Caenorhabditis brenneri
            Eukaryota; Metazoa; Ecdysozoa; Nematoda; Chromadorea; Rhabditida;
            Rhabditina; Rhabditomorpha; Rhabditoidea; Rhabditidae; Peloderinae;
            Caenorhabditis.
REFERENCE   1  (bases 1 to 3123)
  AUTHORS   Stothard,P., Hansen,D. and Pilgrim,D.
  TITLE     Evolution of the PP2C family in Caenorhabditis: rapid divergence of
            the sex-determining protein FEM-2
  JOURNAL   J. Mol. Evol. 54 (2), 267-282 (2002)
   PUBMED   11821919
REFERENCE   2  (bases 1 to 3123)
  AUTHORS   Stothard,P. and Pilgrim,D.
  TITLE     Conspecific and interspecific interactions between the FEM-2 and
            the FEM-3 sex-determining proteins despite rapid sequence
            divergence
  JOURNAL   J. Mol. Evol. 62 (3), 281-291 (2006)
   PUBMED   16477523
REFERENCE   3  (bases 1 to 3123)
  AUTHORS   Stothard,P.M., Hansen,D. and Pilgrim,D.
  TITLE     Direct Submission
  JOURNAL   Submitted (17-AUG-1999) Biological Sciences, University of Alberta,
            Edmonton, AB T6G-2E9, Canada
FEATURES             Location/Qualifiers
     source          1..3123
                     /organism="Caenorhabditis brenneri"
                     /mol_type="genomic DNA"
                     /strain="CB5161"
                     /db_xref="taxon:135651"
     gene            <265..>2855
                     /gene="fem-2"
     mRNA            join(<265..402,673..781,911..1007,1088..1215,1377..1573,
                     1866..2146,2306..2634,2683..>2855)
                     /gene="fem-2"
                     /product="putative FEM-2 protein phosphatase type 2C"
     CDS             join(265..402,673..781,911..1007,1088..1215,1377..1573,
                     1866..2146,2306..2634,2683..2855)
                     /gene="fem-2"
                     /note="possible sex-determining protein"
                     /codon_start=1
                     /product="putative PP2C protein phosphatase FEM-2"
                     /protein_id="AAF04557.1"
                     /translation="MSDSLNHPSSSTVHADDGFEPPTSPEDNNKKPSLEQIKQEREAL
                     FTDLFADRRRSARSVIEEAFQNELMSAEPVQPNVPNPHSIPIRFRHQPVAGPAHDVFG
                     DAVHSIFQKIMSRGVNADYSHWMSYWIALGIDKKTQMNYHMKPFCKDTYATEGSLEAK
                     QTFTDKIRSAVEEIIWKSAEYCDILSEKWTGIHVSADQLKGQRNKQEDRFVAYPNGQY
                     MNRGQSDISLLAVFDGHGGHECSQYAAAHFWEAWSDAQHHHSQDMKLDELLEKALETL
                     DERMTVRSVRESWKGGTTAVCCAVDLNTNQIAFAWLGDSPGYIMSNLEFRKFTTEHSP
                     SDPEECRRVEEVGGQIFVIGGELRVNGVLNLTRALGDVPGRPMISNKPDTLLKTIEPA
                     DYLVLLACDGISDVFNTSDLYNLVQAFVNEYDVEDYHELARYICNQAVSAGSADNVTV
                     VIGFLRPPEDVWRVMKTDSDDEESELEEEDDNE"
ORIGIN      
        1 gaacgcgaat gcctctctct ctttcgatgg gtatgccaat tgtccacatt cactcgtgtt
       61 gcctcctctt tgccaacacg caagacacca gaaacgcgtc aaccaaagag aaaaagacgc
      121 cgacaacggg cagcactcgc gagagacaaa ggttatcgcg ttgtgttatt atacattcgc
      181 atccgggtca actttagtcc gttgaacatg cttcttgaaa acctagttct cttaaaataa
      241 cgttttagaa gttttggtct tcagatgtct gattcgctaa atcatccatc gagttctacg
      301 gtgcatgcag atgatggatt cgagccacca acatctccgg aagacaacaa caaaaaaccg
      361 tctttagaac aaattaaaca ggaaagagaa gcgttgttta cggttagtta cctattagct
      421 gcaagttttg aaaaagcgga atctgtaaaa agcggaatct gtaaaaaaaa catctaagga
      481 ataattctga aaagaaaaag tttctaaatg ttaatcggaa tccaattttt atgaaattat
      541 ttaaaaaaaa actaaaatta gtttctaaaa aatttttcta aagtaattgg accatgtgaa
      601 ggtacaccca cttgttccaa tatgccatat ctaactgtaa aataatttga ttctcatgag
      661 aatatttttc aggatctatt cgcagatcgt cgacgaagcg ctcgttctgt gattgaagaa
      721 gctttccaaa acgaactcat gagtgctgaa ccagtccagc caaacgtgcc gaatccacat
      781 tgtgagttgg aaatttttat ttgataacca agagaaaaaa agttctacct ttttttcaaa
      841 aacctttcca aaaatgattc catctgatat aggattaaga aaaatatttt ccgaaatctc
      901 tgcttttcag cgattcccat tcgtttccgt catcaaccag ttgctggacc tgctcatgat
      961 gttttcggag acgcggtgca ttcaattttt caaaaaataa tgtccaggta tacactattt
     1021 ttgcatattt ttcttgccaa atttggtcaa aaaccgtagt acaacccaaa aagtttcttc
     1081 atttcagagg agtgaacgcg gattatagtc attggatgtc atattggatc gcgttgggaa
     1141 tcgacaaaaa aacacaaatg aactatcata tgaaaccgtt ttgcaaagat acttatgcaa
     1201 ctgaaggctc cttaggtagg ttagtctttt ctaggcacag aagagtgaga aaattctaaa
     1261 tttctgagca gtctgctttt tgttttcctt gagtttttac ttaaagctct taaaagaaat
     1321 ctaggcgtga agttcgagcc ttgtaccata ccacaacagc attccaaatg ttacagaagc
     1381 gaaacaaaca tttactgata aaatcaggtc agctgttgag gaaattatct ggaagtccgc
     1441 tgaatattgt gatattctta gcgagaagtg gacaggaatt catgtgtcgg ccgaccaact
     1501 gaaaggtcaa agaaataagc aagaagatcg ttttgtggct tatccaaatg gacaatacat
     1561 gaatcgtgga caggttagtg cgaatcgggg actcaagatt tactgaaata gtgaagagaa
     1621 aacaaaagaa aactatattt tcaaaaaaaa tgagaactct aataaacaga atgaaaaaca
     1681 ttcaaagcta cagtagtatt tccagctgga gtttccagag ccaaaaaaat gcgagtatta
     1741 ctgtagtttt gaaattggtt tctcacttta cgtacgattt tttgattttt ttttcagact
     1801 cttcatatga aaaaaaatca tgttttctcc tttacaagat ttttttgatc tcaaaacatt
     1861 tccagagtga catttcactt cttgcggtgt tcgatgggca tggcggacac gagtgctctc
     1921 aatatgcagc tgctcatttc tgggaagcat ggtccgatgc tcaacatcat cattcacaag
     1981 atatgaaact tgacgaactc ctagaaaagg ctctagaaac attggacgaa agaatgacag
     2041 tcagaagtgt tcgagaatct tggaaaggtg gaaccactgc tgtctgctgt gctgttgatt
     2101 tgaacactaa tcaaatcgca tttgcctggc ttggagattc accagggtaa tcaatttttt
     2161 tttagttttt ggaactttac gtcccgaaaa attattcctt tatcacctaa ttcctacagt
     2221 aacccaagct ccgaattaaa taaagttaaa gcgtggtata cacataaaaa taagaaaaaa
     2281 ttgttcatga aatccatttt tccagttaca tcatgtcaaa cttggagttc cgcaaattca
     2341 ctactgaaca ctccccgtct gacccggagg aatgtcgacg agtcgaagaa gtcggtggcc
     2401 agatttttgt gatcggtggt gagctccgtg tgaatggagt actcaacctg acgcgagcac
     2461 taggagacgt acctggaaga ccaatgatat ccaacaaacc tgatacctta ctgaagacga
     2521 tcgaacctgc ggattatctt gttttgttgg cctgtgacgg gatttctgac gtcttcaaca
     2581 ctagtgattt gtacaatttg gttcaggctt ttgtcaatga atatgacgta gaaggtatca
     2641 aactgatcgt ttttcacatc acaaaattct tgaattttcc agattatcac gaacttgcac
     2701 gctacatttg caatcaagca gtttcagctg gaagtgctga caatgtgaca gtagttatag
     2761 gtttcctccg tccaccagaa gacgtttggc gtgtaatgaa aacagactcg gatgatgaag
     2821 agagcgagct cgaggaagaa gatgacaatg aatagtttat tgcaagtttt ccaaaacttt
     2881 tccaatttcc ctgggtattg attagcatcc atatcttacg gcgattatat caattgtaac
     2941 attatttctg tttctccccc cacctctcaa attttcaaat gacccttttt cttttcgtct
     3001 acctgtatcg ttttccattc atctcccccc ctccactgtg gtatatcatt ttgtcattag
     3061 aaagtattat tttgattttc attggcagta gaagacaaca ggatacagaa gaggttttca
     3121 cag
//
LOCUS       AF054982                3766 bp    DNA     linear   INV 30-MAR-2006
DEFINITION  Caenorhabditis briggsae putative PP2C protein phosphatase FEM-2
            (fem-2) gene, complete cds.
ACCESSION   AF054982
VERSION     AF054982.1
KEYWORDS    .
SOURCE      Caenorhabditis briggsae
  ORGANISM  Caenorhabditis briggsae
            Eukaryota; Metazoa; Ecdysozoa; Nematoda; Chromadorea; Rhabditida;
            Rhabditina; Rhabditomorpha; Rhabditoidea; Rhabditidae; Peloderinae;
            Caenorhabditis.
REFERENCE   1  (bases 1 to 3766)
  AUTHORS   Hansen,D. and Pilgrim,D.
  TITLE     Molecular evolution of a sex determination protein. FEM-2 (pp2c) in
            Caenorhabditis
  JOURNAL   Genetics 149 (3), 1353-1362 (1998)
   PUBMED   9649525
REFERENCE   2  (bases 1 to 3766)
  AUTHORS   Stothard,P. and Pilgrim,D.
  TITLE     Conspecific and interspecific interactions between the FEM-2 and
            the FEM-3 sex-determining proteins despite rapid sequence
            divergence
  JOURNAL   J. Mol. Evol. 62 (3), 281-291 (2006)
   PUBMED   16477523
REFERENCE   3  (bases 1 to 3766)
  AUTHORS   Hansen,D. and Pilgrim,D.
  TITLE     Direct Submission
  JOURNAL   Submitted (20-MAR-1998) Department of Biological Sciences,
            University of Alberta, Edmonton, AB T6G-2E9, Canada
FEATURES             Location/Qualifiers
     source          1..3766
                     /organism="Caenorhabditis briggsae"
                     /mol_type="genomic DNA"
                     /strain="AF16"
                     /db_xref="taxon:6238"
                     /note="obtained from genomic mini-library screened with
                     Caenorhabditis elegans fem-2 sequence"
     gene            <415..>3405
                     /gene="fem-2"
     mRNA            join(<415..609,1482..1693,1749..1876,1946..2423,
                     2471..2799,3239..>3405)
                     /gene="fem-2"
                     /product="putative PP2C protein phosphatase FEM-2"
     CDS             join(415..609,1482..1693,1749..1876,1946..2423,2471..2799,
                     3239..3405)
                     /gene="fem-2"
                     /note="possible sex determination protein"
                     /codon_start=1
                     /product="putative PP2C protein phosphatase FEM-2"
                     /protein_id="AAC08602.1"
                     /translation="MSGPPPPKTNEKSSQPVTGRSQEPTRKGQLGPNYLRIIEEDEEY
                     GHALLEPSEEQIKFEREALFEDLHLDRQRSARSFIEETFEEEMLGPQNGIPPTTESPQ
                     SYIPIRYRNPPAAAPVHDVFGDAVHAIFQKLMTRGPPVEYCHWMSYWIAKQIDKDSPV
                     KYHECRFTPDQYVTENTAEAKKTYMDNMWKAAEKNLWMYTYNSPLLRTKWTGIHVSAE
                     QIKGQRHKQEDRFVAYPNSLYMDTSRSDHIALLGVFDGHGGHECSQYAAGHMWETWIE
                     TRASHFEEPLEKQLKTSLDLLDERMTVRSTKECWKGGTTAVCCAIDMNKKELAFAWLG
                     DSPGYIMDNLEVRKVTRDHSPSDPEEGRRVEEAGGQLFVIGGELRVNGVLNLTRALGD
                     VPGRPMISNQAETCQRDIEVGDYLVILACDGISDVFNTSDLYNLVQAYVNENPVEEYN
                     DLAHYICHEAIAHGSTDNVTVVIGFLRPPQDLWRMMKIDEESDEEEDEVDDE"
ORIGIN      
        1 tctagagatg ctagcgatca ttttcatacc gagaaatcaa aattttgttc agataatccc
       61 actaaattca cataaataaa tttgttatct acagtatccg ttttgctccg tcccctcgta
      121 aatcgacacg agcgctgtct ccgagatttc aggtgtcact attttaatcc gacaatattt
      181 ttggctccct gaacattttt tatgtgtaaa taaaaaattt tgtttttttg aatctacaat
      241 agaagaattt ggagagaaaa atcgaaattt ttagtgaaac tgatggtttc aaatattcag
      301 aaaaagagaa tctgcattag aaattttctt tttttcattt ttgttttttg ctattcttca
      361 ttccatcctt gcaatacttt gtaaatcacc tttttcgaaa tctcaccttt tcagatgtcc
      421 ggcccaccac cacccaaaac taacgagaaa tcatcacaac cggtcaccgg acgatcacaa
      481 gagcctacgc gtaaaggtca acttggaccc aattacttgc gtataattga agaggacgaa
      541 gaatatgggc atgctctttt ggagccaagt gaggagcaga tcaaattcga aagagaagca
      601 ctttttgagg tatacaaata attatggatt aagcataatc actaaaagtt tcgcaaacct
      661 tatcgtctga gtgacccagt tttatcactg tttctgtgga agatatgcga taaaaactac
      721 cgtaaacact actagaacgc caccagaacc gtccactttg agcctatata tctcactttt
      781 ttcaaaagat atcaaaaaat tgtcaactaa caaaatgttt gctcatgtgt cgcaacttta
      841 attagttgac cacttgttga tatcttttac aggaaatgag atacatgggc tcgaatatat
      901 gattccgatg gtgttctttt agagtgttta cggcatactg cgaccgcgta tttgccgggc
      961 cccttcgtca tagtttcttt ttgaatcaat atttttagat taactaaatt agatatgata
     1021 aaactcggcg agtactacaa aatgatacta tttggaaaac agtgtcttgt ctataacaaa
     1081 gtaacaagtc ataaagtggc cagacgaggc ctctgttttt ttgtctgtaa ctttgttcat
     1141 agacaagaca cagtcctcca aataatatca ttatgtagca ctcgtcgagt tctttcatat
     1201 ctaagtgagt tggtctgaaa attttgattc taaaagaaac tatggcagat gaaggcttgt
     1261 ttcgaagtat ggtttacggt attgaaaaat tataactcct gtgtttcaag ataaattcaa
     1321 cggtctaaaa atcctaattg tgatgaaatt aaacttcgaa agaaaaatgt ttacaatttt
     1381 cgaaaaactg aaaattagag caaaattaac tgaaattttc ttcctgtctg aaaattaaaa
     1441 ctccaagttt tttgttgctc ttttcaaata caagtttcca ggatctccac ttggaccgtc
     1501 aacgaagtgc ccgttcattc attgaagaga ctttcgagga ggagatgctt ggaccccaaa
     1561 atggcattcc acccactaca gaatctccac agtcatacat tcccatccga taccgtaatc
     1621 caccagcagc tgcaccggtt catgacgttt tcggagatgc tgtacatgca atttttcaaa
     1681 agttgatgac tcggtaaaag tttgaaatta gagaggaaaa agtttaggat tttacaaaat
     1741 gttttcagag gtccacctgt cgagtactgt cactggatgt cctattggat tgccaagcag
     1801 attgataagg atagtccagt gaagtatcat gagtgtcgtt ttactcctga ccaatacgtg
     1861 acggagaata ctgcaggtat gcttgtatca tccagataac cacggggatc cttggaacat
     1921 ggaatctaat gtttcgtttt cacagaagcc aagaagactt acatggacaa tatgtggaag
     1981 gcagcagaaa agaatttatg gatgtacacc tacaactctc cactccttcg cacaaaatgg
     2041 actggaattc acgtgtctgc tgaacaaata aaaggacaac gtcacaaaca ggaggatcga
     2101 tttgtcgcct atccgaatag cttgtacatg gatacgtctc gttcggacca tattgctctt
     2161 ttgggtgttt tcgatggtca tggaggccac gagtgctccc aatacgctgc tgggcatatg
     2221 tgggagacgt ggattgagac acgagcctcg cacttcgagg agccacttga gaagcaactg
     2281 aagacttcgt tggatcttct ggatgagcgt atgactgtaa gaagtacgaa ggaatgctgg
     2341 aagggaggta ccacggctgt ctgttgtgca attgatatga ataagaagga gttggcattt
     2401 gcttggttgg gagattcacc agggtatgaa aataggagtt ttatattttt taaaaactgg
     2461 aaaatctcag ctacattatg gataatctgg aagttcgcaa agtgacacgc gatcactctc
     2521 catcagatcc cgaagaaggt cgtcgcgtcg aagaggctgg tggtcaactg tttgtgattg
     2581 gtggagagct tcgagtgaat ggtgtgctca atctgacacg tgcactagga gatgtccctg
     2641 gccgaccgat gatctcgaat caagcggaaa cgtgtcagcg agatattgaa gtaggcgact
     2701 atctggtaat tcttgcttgc gatggaatat cggatgtctt caacacaagt gatttgtaca
     2761 atttagtgca ggcctatgtc aatgaaaatc ctgtagaagg tgagagctca ttttagaaaa
     2821 aaagtacgaa atcttaaagg attttatgaa ttctaaaaat gcttaaaatt gcttactaga
     2881 aggaattcta cagaaaactt gaacgtgaga aaatttgtaa tcagtttttg tgttcgatct
     2941 gaaaattgga aacttgttca actaagcgag agctgttata tttatgcttg aactctgttt
     3001 tttttgtata ttactgaaag tgttggagca gtcaaacaac tgtaacttac atccttagtg
     3061 ctagactttt gtcaaagaaa atcaaatttt tcaattttaa ttgaaaagtt ttgaaacact
     3121 taccattaga gaagttctta taacttttga ccgaaaaagt caaaaagagt attttcaact
     3181 agagccaata gtgataaagt caagactgat taaaacctca aaatttattt atttccagaa
     3241 tataacgact tggctcatta catctgccac gaagcgattg ctcatggaag tacggacaat
     3301 gtgacagtcg tcattggatt cctccgtcca ccacaagatc tctggcgcat gatgaaaatc
     3361 gacgaagagt cagacgaaga agaagacgag gttgatgatg aatagaattc cactgctttc
     3421 ttgtttccaa actgtatata ttttttcttt gactcttctt ataactttat ttgaaaatcc
     3481 tttcttttct cccgtctaga tttgttttgt ataggcgttg gtatcaattt tctatcaatc
     3541 atccacacca tatctatttg aactttatta cagtaacttc agagctcgaa aacatttcga
     3601 agtttttttt tgtgttccta tcttttacgt atagcatttc cttatcttcc gaattttggc
     3661 ttaagtacag gcttaggaaa atccttaata actttgttca aataagagat ttgggcctga
     3721 aacttttgga cgtaacttga aattgaatgt agaacgttcc tatgac
//
LOCUS       AF507019                1796 bp    mRNA    linear   INV 30-MAR-2006
DEFINITION  Caenorhabditis remanei putative protein phosphatase FEM-2 (fem-2)
            mRNA, complete cds.
ACCESSION   AF507019
VERSION     AF507019.1
KEYWORDS    .
SOURCE      Caenorhabditis remanei
  ORGANISM  Caenorhabditis remanei
            Eukaryota; Metazoa; Ecdysozoa; Nematoda; Chromadorea; Rhabditida;
            Rhabditina; Rhabditomorpha; Rhabditoidea; Rhabditidae; Peloderinae;
            Caenorhabditis.
REFERENCE   1  (bases 1 to 1796)
  AUTHORS   Stothard,P. and Pilgrim,D.
  TITLE     Conspecific and interspecific interactions between the FEM-2 and
            the FEM-3 sex-determining proteins despite rapid sequence
            divergence
  JOURNAL   J. Mol. Evol. 62 (3), 281-291 (2006)
   PUBMED   16477523
REFERENCE   2  (bases 1 to 1796)
  AUTHORS   Stothard,P.M. and Pilgrim,D.
  TITLE     Isolation of protein phosphatase type 2C (PP2C) sequences from
            nematodes
  JOURNAL   Unpublished
REFERENCE   3  (bases 1 to 1796)
  AUTHORS   Stothard,P.M. and Pilgrim,D.
  TITLE     Direct Submission
  JOURNAL   Submitted (29-APR-2002) Biological Sciences, University of Alberta,
            Edmonton, AB T6G-2E9, Canada
FEATURES             Location/Qualifiers
     source          1..1796
                     /organism="Caenorhabditis remanei"
                     /mol_type="mRNA"
                     /strain="SB146"
                     /db_xref="taxon:31234"
     gene            1..1796
                     /gene="fem-2"
     CDS             1..1467
                     /gene="fem-2"
                     /note="type 2C phosphatase; possible sex-determining
                     protein"
                     /codon_start=1
                     /product="putative protein phosphatase FEM-2"
                     /protein_id="AAM33404.1"
                     /translation="MSDPPVEKTSPEKTEGSSSGSFRVPLESDKLGDPDFKPCVAQIT
                     MERNAVFEDNFLDRRQSARAVIEYCFEDEMQNLVEGRPAVSEEPVVPIRFRRPPPSGP
                     AHDVFGDAMNEIFQKLMMKGQCADFCHWMAYWLTKEQDDANDGFFGNIRYNPDVYVTE
                     GTTETKKAFVDSMWPTAQRILLKSVRNSTILRTKWTGIHVSADQLKGQRPKQEDRFVA
                     YPNSQYMNRTQDPVALLGVFDGHGGHECSQYAASHFWEAWLETRQTSDGDELQNQLKK
                     SLELLDQRLTVRSVKEYWKGGTTAACCAIDKENKTMAFAWLGDSPGYVMNNMEFRKVT
                     REHSPSDPEEARRVEEAGGQLFVIGGELRVNGVLNLTRALGDVPGRPMISNEPEICER
                     PIEQGDYMVFLACDGVSDVLNTADLYNLVGEFVRTFPVEDYSEMARWFCHKSITAGSA
                     DNVTVVIGFLRPPQDIWNLMSRSSDDESDEEEEDEDDD"
     misc_feature    1
                     /gene="fem-2"
                     /note="SL1 splice site"
ORIGIN      
        1 atgtccgacc caccggtcga aaaaacaagt ccagagaaga cagagggctc ttcatccggc
       61 agttttcgcg tcccactcga atccgacaag cttggtgacc cggatttcaa gccatgcgtt
      121 gcacaaatca caatggagag aaacgcagtg ttcgaggaca acttcctcga tcggagacag
      181 agtgctcgcg ccgtaatcga gtattgcttt gaggacgaaa tgcaaaactt ggttgaaggg
      241 cgacctgctg tttcagaaga accagttgtt cccatacgat tccgacgccc accaccgtcc
      301 ggacctgctc acgacgtctt tggcgacgcc atgaacgaaa ttttccagaa attaatgatg
      361 aaaggtcaat gcgcagactt ctgccactgg atggcttatt ggctaacaaa ggaacaagat
      421 gatgcgaatg atggattttt tggcaatatt cgctataatc cagatgtcta tgtcacggaa
      481 ggcacaacag aaaccaaaaa ggcgttcgtc gacagcatgt ggccgactgc tcagcgaatt
      541 cttctgaaat ccgtccggaa cagcacgatt ttacgcacaa agtggactgg aatccacgtg
      601 tcagcggatc agttgaaggg gcaacgcccg aagcaagaag atagattcgt agcttatccg
      661 aatagtcagt atatgaatcg gacgcaggat cccgtcgccc ttctcggtgt gttcgatggt
      721 catggcggac acgagtgctc acaatacgcg gcctctcact tctgggaggc atggctggag
      781 actcgacaaa ctagcgacgg tgatgagctc cagaatcagc tgaagaagtc acttgagttg
      841 ttggatcaac gattgacagt cagaagtgtg aaggaatact ggaagggtgg cactacggcg
      901 gcgtgttgcg ctatcgataa ggagaacaaa acgatggcgt tcgcgtggtt gggcgattca
      961 ccaggatacg tcatgaacaa catggaattc cgcaaagtga cacgcgagca ctcgccgtcc
     1021 gatccagaag aagcgcgtcg agtcgaagaa gccggcggac aactattcgt gatcggtggc
     1081 gagttgcgag tcaacggagt gctcaacctg acgcgtgctc tcggcgacgt tcccggacga
     1141 ccgatgatat caaatgagcc ggagatatgc gagagaccga ttgagcaagg cgactatatg
     1201 gtgtttttgg cgtgtgatgg tgtatcggac gtgttgaaca ctgccgattt atacaatttg
     1261 gttggcgagt ttgtcagaac atttcctgtt gaagactact cggaaatggc tcgctggttt
     1321 tgtcacaaat cgatcaccgc tggaagtgcc gacaacgtga cagtcgtcat tggattcctt
     1381 cgtccaccac aagacatctg gaatctcatg agtcgtagct cggatgatga gtctgatgaa
     1441 gaagaagagg atgaggacga cgattgaacg acgacgcctc ttccctgtac attaatatat
     1501 tttctcgttt tccaaacccc tcgtatagct ttttctcgtt ttctcccctc cctatctctt
     1561 atacaatttt gggtaaacct cctttcccat atctatcaaa ttgtttcttt tttccccttt
     1621 cggataacac ctcacccacg aaatgtatca ttgtttctca cctccctaac ttccggatgt
     1681 ccctattccc tcggtttctt gtagcatttc atttcatctc cccgtattat ttttcaatta
     1741 tatatatata gacatgtatg aactgttaaa tttaaaaaaa aaaaaaaaaa aaaaaa
//
```

## Sample GenBank output

The following was generated using the `-s` option, which causes the sequences of features to be included:

```json
[
    {
        "name": "AF177870",
        "length": "3123",
        "sequence": "gaacgcgaatgcctctctctctttcgatgggtatgccaattgtccacattcactcgtgttgcctcctctttgccaacacgcaagacaccagaaacgcgtcaaccaaagagaaaaagacgccgacaacgggcagcactcgcgagagacaaaggttatcgcgttgtgttattatacattcgcatccgggtcaactttagtccgttgaacatgcttcttgaaaacctagttctcttaaaataacgttttagaagttttggtcttcagatgtctgattcgctaaatcatccatcgagttctacggtgcatgcagatgatggattcgagccaccaacatctccggaagacaacaacaaaaaaccgtctttagaacaaattaaacaggaaagagaagcgttgtttacggttagttacctattagctgcaagttttgaaaaagcggaatctgtaaaaagcggaatctgtaaaaaaaacatctaaggaataattctgaaaagaaaaagtttctaaatgttaatcggaatccaatttttatgaaattatttaaaaaaaaactaaaattagtttctaaaaaatttttctaaagtaattggaccatgtgaaggtacacccacttgttccaatatgccatatctaactgtaaaataatttgattctcatgagaatatttttcaggatctattcgcagatcgtcgacgaagcgctcgttctgtgattgaagaagctttccaaaacgaactcatgagtgctgaaccagtccagccaaacgtgccgaatccacattgtgagttggaaatttttatttgataaccaagagaaaaaaagttctacctttttttcaaaaacctttccaaaaatgattccatctgatataggattaagaaaaatattttccgaaatctctgcttttcagcgattcccattcgtttccgtcatcaaccagttgctggacctgctcatgatgttttcggagacgcggtgcattcaatttttcaaaaaataatgtccaggtatacactatttttgcatatttttcttgccaaatttggtcaaaaaccgtagtacaacccaaaaagtttcttcatttcagaggagtgaacgcggattatagtcattggatgtcatattggatcgcgttgggaatcgacaaaaaaacacaaatgaactatcatatgaaaccgttttgcaaagatacttatgcaactgaaggctccttaggtaggttagtcttttctaggcacagaagagtgagaaaattctaaatttctgagcagtctgctttttgttttccttgagtttttacttaaagctcttaaaagaaatctaggcgtgaagttcgagccttgtaccataccacaacagcattccaaatgttacagaagcgaaacaaacatttactgataaaatcaggtcagctgttgaggaaattatctggaagtccgctgaatattgtgatattcttagcgagaagtggacaggaattcatgtgtcggccgaccaactgaaaggtcaaagaaataagcaagaagatcgttttgtggcttatccaaatggacaatacatgaatcgtggacaggttagtgcgaatcggggactcaagatttactgaaatagtgaagagaaaacaaaagaaaactatattttcaaaaaaaatgagaactctaataaacagaatgaaaaacattcaaagctacagtagtatttccagctggagtttccagagccaaaaaaatgcgagtattactgtagttttgaaattggtttctcactttacgtacgattttttgatttttttttcagactcttcatatgaaaaaaaatcatgttttctcctttacaagatttttttgatctcaaaacatttccagagtgacatttcacttcttgcggtgttcgatgggcatggcggacacgagtgctctcaatatgcagctgctcatttctgggaagcatggtccgatgctcaacatcatcattcacaagatatgaaacttgacgaactcctagaaaaggctctagaaacattggacgaaagaatgacagtcagaagtgttcgagaatcttggaaaggtggaaccactgctgtctgctgtgctgttgatttgaacactaatcaaatcgcatttgcctggcttggagattcaccagggtaatcaatttttttttagtttttggaactttacgtcccgaaaaattattcctttatcacctaattcctacagtaacccaagctccgaattaaataaagttaaagcgtggtatacacataaaaataagaaaaaattgttcatgaaatccatttttccagttacatcatgtcaaacttggagttccgcaaattcactactgaacactccccgtctgacccggaggaatgtcgacgagtcgaagaagtcggtggccagatttttgtgatcggtggtgagctccgtgtgaatggagtactcaacctgacgcgagcactaggagacgtacctggaagaccaatgatatccaacaaacctgataccttactgaagacgatcgaacctgcggattatcttgttttgttggcctgtgacgggatttctgacgtcttcaacactagtgatttgtacaatttggttcaggcttttgtcaatgaatatgacgtagaaggtatcaaactgatcgtttttcacatcacaaaattcttgaattttccagattatcacgaacttgcacgctacatttgcaatcaagcagtttcagctggaagtgctgacaatgtgacagtagttataggtttcctccgtccaccagaagacgtttggcgtgtaatgaaaacagactcggatgatgaagagagcgagctcgaggaagaagatgacaatgaatagtttattgcaagttttccaaaacttttccaatttccctgggtattgattagcatccatatcttacggcgattatatcaattgtaacattatttctgtttctccccccacctctcaaattttcaaatgaccctttttcttttcgtctacctgtatcgttttccattcatctccccccctccactgtggtatatcattttgtcattagaaagtattattttgattttcattggcagtagaagacaacaggatacagaagaggttttcacag",
        "features": [
            {
                "feature_name": "source",
                "feature_strand": 1,
                "location_text": "1..3123",
                "feature_locations": [
                    {
                        "feature_range_start": "1",
                        "feature_range_end": "3123"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "organism",
                        "feature_value": "Caenorhabditis brenneri"
                    },
                    {
                        "feature_name": "mol_type",
                        "feature_value": "genomic DNA"
                    },
                    {
                        "feature_name": "strain",
                        "feature_value": "CB5161"
                    },
                    {
                        "feature_name": "db_xref",
                        "feature_value": "taxon:135651"
                    }
                ],
                "feature_sequence": "gaacgcgaatgcctctctctctttcgatgggtatgccaattgtccacattcactcgtgttgcctcctctttgccaacacgcaagacaccagaaacgcgtcaaccaaagagaaaaagacgccgacaacgggcagcactcgcgagagacaaaggttatcgcgttgtgttattatacattcgcatccgggtcaactttagtccgttgaacatgcttcttgaaaacctagttctcttaaaataacgttttagaagttttggtcttcagatgtctgattcgctaaatcatccatcgagttctacggtgcatgcagatgatggattcgagccaccaacatctccggaagacaacaacaaaaaaccgtctttagaacaaattaaacaggaaagagaagcgttgtttacggttagttacctattagctgcaagttttgaaaaagcggaatctgtaaaaagcggaatctgtaaaaaaaacatctaaggaataattctgaaaagaaaaagtttctaaatgttaatcggaatccaatttttatgaaattatttaaaaaaaaactaaaattagtttctaaaaaatttttctaaagtaattggaccatgtgaaggtacacccacttgttccaatatgccatatctaactgtaaaataatttgattctcatgagaatatttttcaggatctattcgcagatcgtcgacgaagcgctcgttctgtgattgaagaagctttccaaaacgaactcatgagtgctgaaccagtccagccaaacgtgccgaatccacattgtgagttggaaatttttatttgataaccaagagaaaaaaagttctacctttttttcaaaaacctttccaaaaatgattccatctgatataggattaagaaaaatattttccgaaatctctgcttttcagcgattcccattcgtttccgtcatcaaccagttgctggacctgctcatgatgttttcggagacgcggtgcattcaatttttcaaaaaataatgtccaggtatacactatttttgcatatttttcttgccaaatttggtcaaaaaccgtagtacaacccaaaaagtttcttcatttcagaggagtgaacgcggattatagtcattggatgtcatattggatcgcgttgggaatcgacaaaaaaacacaaatgaactatcatatgaaaccgttttgcaaagatacttatgcaactgaaggctccttaggtaggttagtcttttctaggcacagaagagtgagaaaattctaaatttctgagcagtctgctttttgttttccttgagtttttacttaaagctcttaaaagaaatctaggcgtgaagttcgagccttgtaccataccacaacagcattccaaatgttacagaagcgaaacaaacatttactgataaaatcaggtcagctgttgaggaaattatctggaagtccgctgaatattgtgatattcttagcgagaagtggacaggaattcatgtgtcggccgaccaactgaaaggtcaaagaaataagcaagaagatcgttttgtggcttatccaaatggacaatacatgaatcgtggacaggttagtgcgaatcggggactcaagatttactgaaatagtgaagagaaaacaaaagaaaactatattttcaaaaaaaatgagaactctaataaacagaatgaaaaacattcaaagctacagtagtatttccagctggagtttccagagccaaaaaaatgcgagtattactgtagttttgaaattggtttctcactttacgtacgattttttgatttttttttcagactcttcatatgaaaaaaaatcatgttttctcctttacaagatttttttgatctcaaaacatttccagagtgacatttcacttcttgcggtgttcgatgggcatggcggacacgagtgctctcaatatgcagctgctcatttctgggaagcatggtccgatgctcaacatcatcattcacaagatatgaaacttgacgaactcctagaaaaggctctagaaacattggacgaaagaatgacagtcagaagtgttcgagaatcttggaaaggtggaaccactgctgtctgctgtgctgttgatttgaacactaatcaaatcgcatttgcctggcttggagattcaccagggtaatcaatttttttttagtttttggaactttacgtcccgaaaaattattcctttatcacctaattcctacagtaacccaagctccgaattaaataaagttaaagcgtggtatacacataaaaataagaaaaaattgttcatgaaatccatttttccagttacatcatgtcaaacttggagttccgcaaattcactactgaacactccccgtctgacccggaggaatgtcgacgagtcgaagaagtcggtggccagatttttgtgatcggtggtgagctccgtgtgaatggagtactcaacctgacgcgagcactaggagacgtacctggaagaccaatgatatccaacaaacctgataccttactgaagacgatcgaacctgcggattatcttgttttgttggcctgtgacgggatttctgacgtcttcaacactagtgatttgtacaatttggttcaggcttttgtcaatgaatatgacgtagaaggtatcaaactgatcgtttttcacatcacaaaattcttgaattttccagattatcacgaacttgcacgctacatttgcaatcaagcagtttcagctggaagtgctgacaatgtgacagtagttataggtttcctccgtccaccagaagacgtttggcgtgtaatgaaaacagactcggatgatgaagagagcgagctcgaggaagaagatgacaatgaatagtttattgcaagttttccaaaacttttccaatttccctgggtattgattagcatccatatcttacggcgattatatcaattgtaacattatttctgtttctccccccacctctcaaattttcaaatgaccctttttcttttcgtctacctgtatcgttttccattcatctccccccctccactgtggtatatcattttgtcattagaaagtattattttgattttcattggcagtagaagacaacaggatacagaagaggttttcacag"
            },
            {
                "feature_name": "gene",
                "feature_strand": 1,
                "location_text": "<265..>2855",
                "feature_locations": [
                    {
                        "feature_range_start": "265",
                        "feature_range_end": "2855"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    }
                ],
                "feature_sequence": "atgtctgattcgctaaatcatccatcgagttctacggtgcatgcagatgatggattcgagccaccaacatctccggaagacaacaacaaaaaaccgtctttagaacaaattaaacaggaaagagaagcgttgtttacggttagttacctattagctgcaagttttgaaaaagcggaatctgtaaaaagcggaatctgtaaaaaaaacatctaaggaataattctgaaaagaaaaagtttctaaatgttaatcggaatccaatttttatgaaattatttaaaaaaaaactaaaattagtttctaaaaaatttttctaaagtaattggaccatgtgaaggtacacccacttgttccaatatgccatatctaactgtaaaataatttgattctcatgagaatatttttcaggatctattcgcagatcgtcgacgaagcgctcgttctgtgattgaagaagctttccaaaacgaactcatgagtgctgaaccagtccagccaaacgtgccgaatccacattgtgagttggaaatttttatttgataaccaagagaaaaaaagttctacctttttttcaaaaacctttccaaaaatgattccatctgatataggattaagaaaaatattttccgaaatctctgcttttcagcgattcccattcgtttccgtcatcaaccagttgctggacctgctcatgatgttttcggagacgcggtgcattcaatttttcaaaaaataatgtccaggtatacactatttttgcatatttttcttgccaaatttggtcaaaaaccgtagtacaacccaaaaagtttcttcatttcagaggagtgaacgcggattatagtcattggatgtcatattggatcgcgttgggaatcgacaaaaaaacacaaatgaactatcatatgaaaccgttttgcaaagatacttatgcaactgaaggctccttaggtaggttagtcttttctaggcacagaagagtgagaaaattctaaatttctgagcagtctgctttttgttttccttgagtttttacttaaagctcttaaaagaaatctaggcgtgaagttcgagccttgtaccataccacaacagcattccaaatgttacagaagcgaaacaaacatttactgataaaatcaggtcagctgttgaggaaattatctggaagtccgctgaatattgtgatattcttagcgagaagtggacaggaattcatgtgtcggccgaccaactgaaaggtcaaagaaataagcaagaagatcgttttgtggcttatccaaatggacaatacatgaatcgtggacaggttagtgcgaatcggggactcaagatttactgaaatagtgaagagaaaacaaaagaaaactatattttcaaaaaaaatgagaactctaataaacagaatgaaaaacattcaaagctacagtagtatttccagctggagtttccagagccaaaaaaatgcgagtattactgtagttttgaaattggtttctcactttacgtacgattttttgatttttttttcagactcttcatatgaaaaaaaatcatgttttctcctttacaagatttttttgatctcaaaacatttccagagtgacatttcacttcttgcggtgttcgatgggcatggcggacacgagtgctctcaatatgcagctgctcatttctgggaagcatggtccgatgctcaacatcatcattcacaagatatgaaacttgacgaactcctagaaaaggctctagaaacattggacgaaagaatgacagtcagaagtgttcgagaatcttggaaaggtggaaccactgctgtctgctgtgctgttgatttgaacactaatcaaatcgcatttgcctggcttggagattcaccagggtaatcaatttttttttagtttttggaactttacgtcccgaaaaattattcctttatcacctaattcctacagtaacccaagctccgaattaaataaagttaaagcgtggtatacacataaaaataagaaaaaattgttcatgaaatccatttttccagttacatcatgtcaaacttggagttccgcaaattcactactgaacactccccgtctgacccggaggaatgtcgacgagtcgaagaagtcggtggccagatttttgtgatcggtggtgagctccgtgtgaatggagtactcaacctgacgcgagcactaggagacgtacctggaagaccaatgatatccaacaaacctgataccttactgaagacgatcgaacctgcggattatcttgttttgttggcctgtgacgggatttctgacgtcttcaacactagtgatttgtacaatttggttcaggcttttgtcaatgaatatgacgtagaaggtatcaaactgatcgtttttcacatcacaaaattcttgaattttccagattatcacgaacttgcacgctacatttgcaatcaagcagtttcagctggaagtgctgacaatgtgacagtagttataggtttcctccgtccaccagaagacgtttggcgtgtaatgaaaacagactcggatgatgaagagagcgagctcgaggaagaagatgacaatgaatag"
            },
            {
                "feature_name": "mRNA",
                "feature_strand": 1,
                "location_text": "join(<265..402,673..781,911..1007,1088..1215,1377..1573,1866..2146,2306..2634,2683..>2855)",
                "feature_locations": [
                    {
                        "feature_range_start": "265",
                        "feature_range_end": "402"
                    },
                    {
                        "feature_range_start": "673",
                        "feature_range_end": "781"
                    },
                    {
                        "feature_range_start": "911",
                        "feature_range_end": "1007"
                    },
                    {
                        "feature_range_start": "1088",
                        "feature_range_end": "1215"
                    },
                    {
                        "feature_range_start": "1377",
                        "feature_range_end": "1573"
                    },
                    {
                        "feature_range_start": "1866",
                        "feature_range_end": "2146"
                    },
                    {
                        "feature_range_start": "2306",
                        "feature_range_end": "2634"
                    },
                    {
                        "feature_range_start": "2683",
                        "feature_range_end": "2855"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    },
                    {
                        "feature_name": "product",
                        "feature_value": "putative FEM-2 protein phosphatase type 2C"
                    }
                ],
                "feature_sequence": "atgtctgattcgctaaatcatccatcgagttctacggtgcatgcagatgatggattcgagccaccaacatctccggaagacaacaacaaaaaaccgtctttagaacaaattaaacaggaaagagaagcgttgtttacggatctattcgcagatcgtcgacgaagcgctcgttctgtgattgaagaagctttccaaaacgaactcatgagtgctgaaccagtccagccaaacgtgccgaatccacattcgattcccattcgtttccgtcatcaaccagttgctggacctgctcatgatgttttcggagacgcggtgcattcaatttttcaaaaaataatgtccagaggagtgaacgcggattatagtcattggatgtcatattggatcgcgttgggaatcgacaaaaaaacacaaatgaactatcatatgaaaccgttttgcaaagatacttatgcaactgaaggctccttagaagcgaaacaaacatttactgataaaatcaggtcagctgttgaggaaattatctggaagtccgctgaatattgtgatattcttagcgagaagtggacaggaattcatgtgtcggccgaccaactgaaaggtcaaagaaataagcaagaagatcgttttgtggcttatccaaatggacaatacatgaatcgtggacagagtgacatttcacttcttgcggtgttcgatgggcatggcggacacgagtgctctcaatatgcagctgctcatttctgggaagcatggtccgatgctcaacatcatcattcacaagatatgaaacttgacgaactcctagaaaaggctctagaaacattggacgaaagaatgacagtcagaagtgttcgagaatcttggaaaggtggaaccactgctgtctgctgtgctgttgatttgaacactaatcaaatcgcatttgcctggcttggagattcaccaggttacatcatgtcaaacttggagttccgcaaattcactactgaacactccccgtctgacccggaggaatgtcgacgagtcgaagaagtcggtggccagatttttgtgatcggtggtgagctccgtgtgaatggagtactcaacctgacgcgagcactaggagacgtacctggaagaccaatgatatccaacaaacctgataccttactgaagacgatcgaacctgcggattatcttgttttgttggcctgtgacgggatttctgacgtcttcaacactagtgatttgtacaatttggttcaggcttttgtcaatgaatatgacgtagaagattatcacgaacttgcacgctacatttgcaatcaagcagtttcagctggaagtgctgacaatgtgacagtagttataggtttcctccgtccaccagaagacgtttggcgtgtaatgaaaacagactcggatgatgaagagagcgagctcgaggaagaagatgacaatgaatag"
            },
            {
                "feature_name": "CDS",
                "feature_strand": 1,
                "location_text": "join(265..402,673..781,911..1007,1088..1215,1377..1573,1866..2146,2306..2634,2683..2855)",
                "feature_locations": [
                    {
                        "feature_range_start": "265",
                        "feature_range_end": "402"
                    },
                    {
                        "feature_range_start": "673",
                        "feature_range_end": "781"
                    },
                    {
                        "feature_range_start": "911",
                        "feature_range_end": "1007"
                    },
                    {
                        "feature_range_start": "1088",
                        "feature_range_end": "1215"
                    },
                    {
                        "feature_range_start": "1377",
                        "feature_range_end": "1573"
                    },
                    {
                        "feature_range_start": "1866",
                        "feature_range_end": "2146"
                    },
                    {
                        "feature_range_start": "2306",
                        "feature_range_end": "2634"
                    },
                    {
                        "feature_range_start": "2683",
                        "feature_range_end": "2855"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    },
                    {
                        "feature_name": "note",
                        "feature_value": "possible sex-determining protein"
                    },
                    {
                        "feature_name": "codon_start",
                        "feature_value": "1"
                    },
                    {
                        "feature_name": "product",
                        "feature_value": "putative PP2C protein phosphatase FEM-2"
                    },
                    {
                        "feature_name": "protein_id",
                        "feature_value": "AAF04557.1"
                    },
                    {
                        "feature_name": "translation",
                        "feature_value": "MSDSLNHPSSSTVHADDGFEPPTSPEDNNKKPSLEQIKQEREALFTDLFADRRRSARSVIEEAFQNELMSAEPVQPNVPNPHSIPIRFRHQPVAGPAHDVFGDAVHSIFQKIMSRGVNADYSHWMSYWIALGIDKKTQMNYHMKPFCKDTYATEGSLEAKQTFTDKIRSAVEEIIWKSAEYCDILSEKWTGIHVSADQLKGQRNKQEDRFVAYPNGQYMNRGQSDISLLAVFDGHGGHECSQYAAAHFWEAWSDAQHHHSQDMKLDELLEKALETLDERMTVRSVRESWKGGTTAVCCAVDLNTNQIAFAWLGDSPGYIMSNLEFRKFTTEHSPSDPEECRRVEEVGGQIFVIGGELRVNGVLNLTRALGDVPGRPMISNKPDTLLKTIEPADYLVLLACDGISDVFNTSDLYNLVQAFVNEYDVEDYHELARYICNQAVSAGSADNVTVVIGFLRPPEDVWRVMKTDSDDEESELEEEDDNE"
                    }
                ],
                "feature_sequence": "atgtctgattcgctaaatcatccatcgagttctacggtgcatgcagatgatggattcgagccaccaacatctccggaagacaacaacaaaaaaccgtctttagaacaaattaaacaggaaagagaagcgttgtttacggatctattcgcagatcgtcgacgaagcgctcgttctgtgattgaagaagctttccaaaacgaactcatgagtgctgaaccagtccagccaaacgtgccgaatccacattcgattcccattcgtttccgtcatcaaccagttgctggacctgctcatgatgttttcggagacgcggtgcattcaatttttcaaaaaataatgtccagaggagtgaacgcggattatagtcattggatgtcatattggatcgcgttgggaatcgacaaaaaaacacaaatgaactatcatatgaaaccgttttgcaaagatacttatgcaactgaaggctccttagaagcgaaacaaacatttactgataaaatcaggtcagctgttgaggaaattatctggaagtccgctgaatattgtgatattcttagcgagaagtggacaggaattcatgtgtcggccgaccaactgaaaggtcaaagaaataagcaagaagatcgttttgtggcttatccaaatggacaatacatgaatcgtggacagagtgacatttcacttcttgcggtgttcgatgggcatggcggacacgagtgctctcaatatgcagctgctcatttctgggaagcatggtccgatgctcaacatcatcattcacaagatatgaaacttgacgaactcctagaaaaggctctagaaacattggacgaaagaatgacagtcagaagtgttcgagaatcttggaaaggtggaaccactgctgtctgctgtgctgttgatttgaacactaatcaaatcgcatttgcctggcttggagattcaccaggttacatcatgtcaaacttggagttccgcaaattcactactgaacactccccgtctgacccggaggaatgtcgacgagtcgaagaagtcggtggccagatttttgtgatcggtggtgagctccgtgtgaatggagtactcaacctgacgcgagcactaggagacgtacctggaagaccaatgatatccaacaaacctgataccttactgaagacgatcgaacctgcggattatcttgttttgttggcctgtgacgggatttctgacgtcttcaacactagtgatttgtacaatttggttcaggcttttgtcaatgaatatgacgtagaagattatcacgaacttgcacgctacatttgcaatcaagcagtttcagctggaagtgctgacaatgtgacagtagttataggtttcctccgtccaccagaagacgtttggcgtgtaatgaaaacagactcggatgatgaagagagcgagctcgaggaagaagatgacaatgaatag"
            }
        ]
    },
    {
        "name": "AF054982",
        "length": "3766",
        "sequence": "tctagagatgctagcgatcattttcataccgagaaatcaaaattttgttcagataatcccactaaattcacataaataaatttgttatctacagtatccgttttgctccgtcccctcgtaaatcgacacgagcgctgtctccgagatttcaggtgtcactattttaatccgacaatatttttggctccctgaacattttttatgtgtaaataaaaaattttgtttttttgaatctacaatagaagaatttggagagaaaaatcgaaatttttagtgaaactgatggtttcaaatattcagaaaaagagaatctgcattagaaattttctttttttcatttttgttttttgctattcttcattccatccttgcaatactttgtaaatcacctttttcgaaatctcaccttttcagatgtccggcccaccaccacccaaaactaacgagaaatcatcacaaccggtcaccggacgatcacaagagcctacgcgtaaaggtcaacttggacccaattacttgcgtataattgaagaggacgaagaatatgggcatgctcttttggagccaagtgaggagcagatcaaattcgaaagagaagcactttttgaggtatacaaataattatggattaagcataatcactaaaagtttcgcaaaccttatcgtctgagtgacccagttttatcactgtttctgtggaagatatgcgataaaaactaccgtaaacactactagaacgccaccagaaccgtccactttgagcctatatatctcacttttttcaaaagatatcaaaaaattgtcaactaacaaaatgtttgctcatgtgtcgcaactttaattagttgaccacttgttgatatcttttacaggaaatgagatacatgggctcgaatatatgattccgatggtgttcttttagagtgtttacggcatactgcgaccgcgtatttgccgggccccttcgtcatagtttctttttgaatcaatatttttagattaactaaattagatatgataaaactcggcgagtactacaaaatgatactatttggaaaacagtgtcttgtctataacaaagtaacaagtcataaagtggccagacgaggcctctgtttttttgtctgtaactttgttcatagacaagacacagtcctccaaataatatcattatgtagcactcgtcgagttctttcatatctaagtgagttggtctgaaaattttgattctaaaagaaactatggcagatgaaggcttgtttcgaagtatggtttacggtattgaaaaattataactcctgtgtttcaagataaattcaacggtctaaaaatcctaattgtgatgaaattaaacttcgaaagaaaaatgtttacaattttcgaaaaactgaaaattagagcaaaattaactgaaattttcttcctgtctgaaaattaaaactccaagttttttgttgctcttttcaaatacaagtttccaggatctccacttggaccgtcaacgaagtgcccgttcattcattgaagagactttcgaggaggagatgcttggaccccaaaatggcattccacccactacagaatctccacagtcatacattcccatccgataccgtaatccaccagcagctgcaccggttcatgacgttttcggagatgctgtacatgcaatttttcaaaagttgatgactcggtaaaagtttgaaattagagaggaaaaagtttaggattttacaaaatgttttcagaggtccacctgtcgagtactgtcactggatgtcctattggattgccaagcagattgataaggatagtccagtgaagtatcatgagtgtcgttttactcctgaccaatacgtgacggagaatactgcaggtatgcttgtatcatccagataaccacggggatccttggaacatggaatctaatgtttcgttttcacagaagccaagaagacttacatggacaatatgtggaaggcagcagaaaagaatttatggatgtacacctacaactctccactccttcgcacaaaatggactggaattcacgtgtctgctgaacaaataaaaggacaacgtcacaaacaggaggatcgatttgtcgcctatccgaatagcttgtacatggatacgtctcgttcggaccatattgctcttttgggtgttttcgatggtcatggaggccacgagtgctcccaatacgctgctgggcatatgtgggagacgtggattgagacacgagcctcgcacttcgaggagccacttgagaagcaactgaagacttcgttggatcttctggatgagcgtatgactgtaagaagtacgaaggaatgctggaagggaggtaccacggctgtctgttgtgcaattgatatgaataagaaggagttggcatttgcttggttgggagattcaccagggtatgaaaataggagttttatattttttaaaaactggaaaatctcagctacattatggataatctggaagttcgcaaagtgacacgcgatcactctccatcagatcccgaagaaggtcgtcgcgtcgaagaggctggtggtcaactgtttgtgattggtggagagcttcgagtgaatggtgtgctcaatctgacacgtgcactaggagatgtccctggccgaccgatgatctcgaatcaagcggaaacgtgtcagcgagatattgaagtaggcgactatctggtaattcttgcttgcgatggaatatcggatgtcttcaacacaagtgatttgtacaatttagtgcaggcctatgtcaatgaaaatcctgtagaaggtgagagctcattttagaaaaaaagtacgaaatcttaaaggattttatgaattctaaaaatgcttaaaattgcttactagaaggaattctacagaaaacttgaacgtgagaaaatttgtaatcagtttttgtgttcgatctgaaaattggaaacttgttcaactaagcgagagctgttatatttatgcttgaactctgttttttttgtatattactgaaagtgttggagcagtcaaacaactgtaacttacatccttagtgctagacttttgtcaaagaaaatcaaatttttcaattttaattgaaaagttttgaaacacttaccattagagaagttcttataacttttgaccgaaaaagtcaaaaagagtattttcaactagagccaatagtgataaagtcaagactgattaaaacctcaaaatttatttatttccagaatataacgacttggctcattacatctgccacgaagcgattgctcatggaagtacggacaatgtgacagtcgtcattggattcctccgtccaccacaagatctctggcgcatgatgaaaatcgacgaagagtcagacgaagaagaagacgaggttgatgatgaatagaattccactgctttcttgtttccaaactgtatatattttttctttgactcttcttataactttatttgaaaatcctttcttttctcccgtctagatttgttttgtataggcgttggtatcaattttctatcaatcatccacaccatatctatttgaactttattacagtaacttcagagctcgaaaacatttcgaagtttttttttgtgttcctatcttttacgtatagcatttccttatcttccgaattttggcttaagtacaggcttaggaaaatccttaataactttgttcaaataagagatttgggcctgaaacttttggacgtaacttgaaattgaatgtagaacgttcctatgac",
        "features": [
            {
                "feature_name": "source",
                "feature_strand": 1,
                "location_text": "1..3766",
                "feature_locations": [
                    {
                        "feature_range_start": "1",
                        "feature_range_end": "3766"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "organism",
                        "feature_value": "Caenorhabditis briggsae"
                    },
                    {
                        "feature_name": "mol_type",
                        "feature_value": "genomic DNA"
                    },
                    {
                        "feature_name": "strain",
                        "feature_value": "AF16"
                    },
                    {
                        "feature_name": "db_xref",
                        "feature_value": "taxon:6238"
                    },
                    {
                        "feature_name": "note",
                        "feature_value": "obtained from genomic mini-library screened with Caenorhabditis elegans fem-2 sequence"
                    }
                ],
                "feature_sequence": "tctagagatgctagcgatcattttcataccgagaaatcaaaattttgttcagataatcccactaaattcacataaataaatttgttatctacagtatccgttttgctccgtcccctcgtaaatcgacacgagcgctgtctccgagatttcaggtgtcactattttaatccgacaatatttttggctccctgaacattttttatgtgtaaataaaaaattttgtttttttgaatctacaatagaagaatttggagagaaaaatcgaaatttttagtgaaactgatggtttcaaatattcagaaaaagagaatctgcattagaaattttctttttttcatttttgttttttgctattcttcattccatccttgcaatactttgtaaatcacctttttcgaaatctcaccttttcagatgtccggcccaccaccacccaaaactaacgagaaatcatcacaaccggtcaccggacgatcacaagagcctacgcgtaaaggtcaacttggacccaattacttgcgtataattgaagaggacgaagaatatgggcatgctcttttggagccaagtgaggagcagatcaaattcgaaagagaagcactttttgaggtatacaaataattatggattaagcataatcactaaaagtttcgcaaaccttatcgtctgagtgacccagttttatcactgtttctgtggaagatatgcgataaaaactaccgtaaacactactagaacgccaccagaaccgtccactttgagcctatatatctcacttttttcaaaagatatcaaaaaattgtcaactaacaaaatgtttgctcatgtgtcgcaactttaattagttgaccacttgttgatatcttttacaggaaatgagatacatgggctcgaatatatgattccgatggtgttcttttagagtgtttacggcatactgcgaccgcgtatttgccgggccccttcgtcatagtttctttttgaatcaatatttttagattaactaaattagatatgataaaactcggcgagtactacaaaatgatactatttggaaaacagtgtcttgtctataacaaagtaacaagtcataaagtggccagacgaggcctctgtttttttgtctgtaactttgttcatagacaagacacagtcctccaaataatatcattatgtagcactcgtcgagttctttcatatctaagtgagttggtctgaaaattttgattctaaaagaaactatggcagatgaaggcttgtttcgaagtatggtttacggtattgaaaaattataactcctgtgtttcaagataaattcaacggtctaaaaatcctaattgtgatgaaattaaacttcgaaagaaaaatgtttacaattttcgaaaaactgaaaattagagcaaaattaactgaaattttcttcctgtctgaaaattaaaactccaagttttttgttgctcttttcaaatacaagtttccaggatctccacttggaccgtcaacgaagtgcccgttcattcattgaagagactttcgaggaggagatgcttggaccccaaaatggcattccacccactacagaatctccacagtcatacattcccatccgataccgtaatccaccagcagctgcaccggttcatgacgttttcggagatgctgtacatgcaatttttcaaaagttgatgactcggtaaaagtttgaaattagagaggaaaaagtttaggattttacaaaatgttttcagaggtccacctgtcgagtactgtcactggatgtcctattggattgccaagcagattgataaggatagtccagtgaagtatcatgagtgtcgttttactcctgaccaatacgtgacggagaatactgcaggtatgcttgtatcatccagataaccacggggatccttggaacatggaatctaatgtttcgttttcacagaagccaagaagacttacatggacaatatgtggaaggcagcagaaaagaatttatggatgtacacctacaactctccactccttcgcacaaaatggactggaattcacgtgtctgctgaacaaataaaaggacaacgtcacaaacaggaggatcgatttgtcgcctatccgaatagcttgtacatggatacgtctcgttcggaccatattgctcttttgggtgttttcgatggtcatggaggccacgagtgctcccaatacgctgctgggcatatgtgggagacgtggattgagacacgagcctcgcacttcgaggagccacttgagaagcaactgaagacttcgttggatcttctggatgagcgtatgactgtaagaagtacgaaggaatgctggaagggaggtaccacggctgtctgttgtgcaattgatatgaataagaaggagttggcatttgcttggttgggagattcaccagggtatgaaaataggagttttatattttttaaaaactggaaaatctcagctacattatggataatctggaagttcgcaaagtgacacgcgatcactctccatcagatcccgaagaaggtcgtcgcgtcgaagaggctggtggtcaactgtttgtgattggtggagagcttcgagtgaatggtgtgctcaatctgacacgtgcactaggagatgtccctggccgaccgatgatctcgaatcaagcggaaacgtgtcagcgagatattgaagtaggcgactatctggtaattcttgcttgcgatggaatatcggatgtcttcaacacaagtgatttgtacaatttagtgcaggcctatgtcaatgaaaatcctgtagaaggtgagagctcattttagaaaaaaagtacgaaatcttaaaggattttatgaattctaaaaatgcttaaaattgcttactagaaggaattctacagaaaacttgaacgtgagaaaatttgtaatcagtttttgtgttcgatctgaaaattggaaacttgttcaactaagcgagagctgttatatttatgcttgaactctgttttttttgtatattactgaaagtgttggagcagtcaaacaactgtaacttacatccttagtgctagacttttgtcaaagaaaatcaaatttttcaattttaattgaaaagttttgaaacacttaccattagagaagttcttataacttttgaccgaaaaagtcaaaaagagtattttcaactagagccaatagtgataaagtcaagactgattaaaacctcaaaatttatttatttccagaatataacgacttggctcattacatctgccacgaagcgattgctcatggaagtacggacaatgtgacagtcgtcattggattcctccgtccaccacaagatctctggcgcatgatgaaaatcgacgaagagtcagacgaagaagaagacgaggttgatgatgaatagaattccactgctttcttgtttccaaactgtatatattttttctttgactcttcttataactttatttgaaaatcctttcttttctcccgtctagatttgttttgtataggcgttggtatcaattttctatcaatcatccacaccatatctatttgaactttattacagtaacttcagagctcgaaaacatttcgaagtttttttttgtgttcctatcttttacgtatagcatttccttatcttccgaattttggcttaagtacaggcttaggaaaatccttaataactttgttcaaataagagatttgggcctgaaacttttggacgtaacttgaaattgaatgtagaacgttcctatgac"
            },
            {
                "feature_name": "gene",
                "feature_strand": 1,
                "location_text": "<415..>3405",
                "feature_locations": [
                    {
                        "feature_range_start": "415",
                        "feature_range_end": "3405"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    }
                ],
                "feature_sequence": "atgtccggcccaccaccacccaaaactaacgagaaatcatcacaaccggtcaccggacgatcacaagagcctacgcgtaaaggtcaacttggacccaattacttgcgtataattgaagaggacgaagaatatgggcatgctcttttggagccaagtgaggagcagatcaaattcgaaagagaagcactttttgaggtatacaaataattatggattaagcataatcactaaaagtttcgcaaaccttatcgtctgagtgacccagttttatcactgtttctgtggaagatatgcgataaaaactaccgtaaacactactagaacgccaccagaaccgtccactttgagcctatatatctcacttttttcaaaagatatcaaaaaattgtcaactaacaaaatgtttgctcatgtgtcgcaactttaattagttgaccacttgttgatatcttttacaggaaatgagatacatgggctcgaatatatgattccgatggtgttcttttagagtgtttacggcatactgcgaccgcgtatttgccgggccccttcgtcatagtttctttttgaatcaatatttttagattaactaaattagatatgataaaactcggcgagtactacaaaatgatactatttggaaaacagtgtcttgtctataacaaagtaacaagtcataaagtggccagacgaggcctctgtttttttgtctgtaactttgttcatagacaagacacagtcctccaaataatatcattatgtagcactcgtcgagttctttcatatctaagtgagttggtctgaaaattttgattctaaaagaaactatggcagatgaaggcttgtttcgaagtatggtttacggtattgaaaaattataactcctgtgtttcaagataaattcaacggtctaaaaatcctaattgtgatgaaattaaacttcgaaagaaaaatgtttacaattttcgaaaaactgaaaattagagcaaaattaactgaaattttcttcctgtctgaaaattaaaactccaagttttttgttgctcttttcaaatacaagtttccaggatctccacttggaccgtcaacgaagtgcccgttcattcattgaagagactttcgaggaggagatgcttggaccccaaaatggcattccacccactacagaatctccacagtcatacattcccatccgataccgtaatccaccagcagctgcaccggttcatgacgttttcggagatgctgtacatgcaatttttcaaaagttgatgactcggtaaaagtttgaaattagagaggaaaaagtttaggattttacaaaatgttttcagaggtccacctgtcgagtactgtcactggatgtcctattggattgccaagcagattgataaggatagtccagtgaagtatcatgagtgtcgttttactcctgaccaatacgtgacggagaatactgcaggtatgcttgtatcatccagataaccacggggatccttggaacatggaatctaatgtttcgttttcacagaagccaagaagacttacatggacaatatgtggaaggcagcagaaaagaatttatggatgtacacctacaactctccactccttcgcacaaaatggactggaattcacgtgtctgctgaacaaataaaaggacaacgtcacaaacaggaggatcgatttgtcgcctatccgaatagcttgtacatggatacgtctcgttcggaccatattgctcttttgggtgttttcgatggtcatggaggccacgagtgctcccaatacgctgctgggcatatgtgggagacgtggattgagacacgagcctcgcacttcgaggagccacttgagaagcaactgaagacttcgttggatcttctggatgagcgtatgactgtaagaagtacgaaggaatgctggaagggaggtaccacggctgtctgttgtgcaattgatatgaataagaaggagttggcatttgcttggttgggagattcaccagggtatgaaaataggagttttatattttttaaaaactggaaaatctcagctacattatggataatctggaagttcgcaaagtgacacgcgatcactctccatcagatcccgaagaaggtcgtcgcgtcgaagaggctggtggtcaactgtttgtgattggtggagagcttcgagtgaatggtgtgctcaatctgacacgtgcactaggagatgtccctggccgaccgatgatctcgaatcaagcggaaacgtgtcagcgagatattgaagtaggcgactatctggtaattcttgcttgcgatggaatatcggatgtcttcaacacaagtgatttgtacaatttagtgcaggcctatgtcaatgaaaatcctgtagaaggtgagagctcattttagaaaaaaagtacgaaatcttaaaggattttatgaattctaaaaatgcttaaaattgcttactagaaggaattctacagaaaacttgaacgtgagaaaatttgtaatcagtttttgtgttcgatctgaaaattggaaacttgttcaactaagcgagagctgttatatttatgcttgaactctgttttttttgtatattactgaaagtgttggagcagtcaaacaactgtaacttacatccttagtgctagacttttgtcaaagaaaatcaaatttttcaattttaattgaaaagttttgaaacacttaccattagagaagttcttataacttttgaccgaaaaagtcaaaaagagtattttcaactagagccaatagtgataaagtcaagactgattaaaacctcaaaatttatttatttccagaatataacgacttggctcattacatctgccacgaagcgattgctcatggaagtacggacaatgtgacagtcgtcattggattcctccgtccaccacaagatctctggcgcatgatgaaaatcgacgaagagtcagacgaagaagaagacgaggttgatgatgaatag"
            },
            {
                "feature_name": "mRNA",
                "feature_strand": 1,
                "location_text": "join(<415..609,1482..1693,1749..1876,1946..2423,2471..2799,3239..>3405)",
                "feature_locations": [
                    {
                        "feature_range_start": "415",
                        "feature_range_end": "609"
                    },
                    {
                        "feature_range_start": "1482",
                        "feature_range_end": "1693"
                    },
                    {
                        "feature_range_start": "1749",
                        "feature_range_end": "1876"
                    },
                    {
                        "feature_range_start": "1946",
                        "feature_range_end": "2423"
                    },
                    {
                        "feature_range_start": "2471",
                        "feature_range_end": "2799"
                    },
                    {
                        "feature_range_start": "3239",
                        "feature_range_end": "3405"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    },
                    {
                        "feature_name": "product",
                        "feature_value": "putative PP2C protein phosphatase FEM-2"
                    }
                ],
                "feature_sequence": "atgtccggcccaccaccacccaaaactaacgagaaatcatcacaaccggtcaccggacgatcacaagagcctacgcgtaaaggtcaacttggacccaattacttgcgtataattgaagaggacgaagaatatgggcatgctcttttggagccaagtgaggagcagatcaaattcgaaagagaagcactttttgaggatctccacttggaccgtcaacgaagtgcccgttcattcattgaagagactttcgaggaggagatgcttggaccccaaaatggcattccacccactacagaatctccacagtcatacattcccatccgataccgtaatccaccagcagctgcaccggttcatgacgttttcggagatgctgtacatgcaatttttcaaaagttgatgactcgaggtccacctgtcgagtactgtcactggatgtcctattggattgccaagcagattgataaggatagtccagtgaagtatcatgagtgtcgttttactcctgaccaatacgtgacggagaatactgcagaagccaagaagacttacatggacaatatgtggaaggcagcagaaaagaatttatggatgtacacctacaactctccactccttcgcacaaaatggactggaattcacgtgtctgctgaacaaataaaaggacaacgtcacaaacaggaggatcgatttgtcgcctatccgaatagcttgtacatggatacgtctcgttcggaccatattgctcttttgggtgttttcgatggtcatggaggccacgagtgctcccaatacgctgctgggcatatgtgggagacgtggattgagacacgagcctcgcacttcgaggagccacttgagaagcaactgaagacttcgttggatcttctggatgagcgtatgactgtaagaagtacgaaggaatgctggaagggaggtaccacggctgtctgttgtgcaattgatatgaataagaaggagttggcatttgcttggttgggagattcaccaggctacattatggataatctggaagttcgcaaagtgacacgcgatcactctccatcagatcccgaagaaggtcgtcgcgtcgaagaggctggtggtcaactgtttgtgattggtggagagcttcgagtgaatggtgtgctcaatctgacacgtgcactaggagatgtccctggccgaccgatgatctcgaatcaagcggaaacgtgtcagcgagatattgaagtaggcgactatctggtaattcttgcttgcgatggaatatcggatgtcttcaacacaagtgatttgtacaatttagtgcaggcctatgtcaatgaaaatcctgtagaagaatataacgacttggctcattacatctgccacgaagcgattgctcatggaagtacggacaatgtgacagtcgtcattggattcctccgtccaccacaagatctctggcgcatgatgaaaatcgacgaagagtcagacgaagaagaagacgaggttgatgatgaatag"
            },
            {
                "feature_name": "CDS",
                "feature_strand": 1,
                "location_text": "join(415..609,1482..1693,1749..1876,1946..2423,2471..2799,3239..3405)",
                "feature_locations": [
                    {
                        "feature_range_start": "415",
                        "feature_range_end": "609"
                    },
                    {
                        "feature_range_start": "1482",
                        "feature_range_end": "1693"
                    },
                    {
                        "feature_range_start": "1749",
                        "feature_range_end": "1876"
                    },
                    {
                        "feature_range_start": "1946",
                        "feature_range_end": "2423"
                    },
                    {
                        "feature_range_start": "2471",
                        "feature_range_end": "2799"
                    },
                    {
                        "feature_range_start": "3239",
                        "feature_range_end": "3405"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    },
                    {
                        "feature_name": "note",
                        "feature_value": "possible sex determination protein"
                    },
                    {
                        "feature_name": "codon_start",
                        "feature_value": "1"
                    },
                    {
                        "feature_name": "product",
                        "feature_value": "putative PP2C protein phosphatase FEM-2"
                    },
                    {
                        "feature_name": "protein_id",
                        "feature_value": "AAC08602.1"
                    },
                    {
                        "feature_name": "translation",
                        "feature_value": "MSGPPPPKTNEKSSQPVTGRSQEPTRKGQLGPNYLRIIEEDEEYGHALLEPSEEQIKFEREALFEDLHLDRQRSARSFIEETFEEEMLGPQNGIPPTTESPQSYIPIRYRNPPAAAPVHDVFGDAVHAIFQKLMTRGPPVEYCHWMSYWIAKQIDKDSPVKYHECRFTPDQYVTENTAEAKKTYMDNMWKAAEKNLWMYTYNSPLLRTKWTGIHVSAEQIKGQRHKQEDRFVAYPNSLYMDTSRSDHIALLGVFDGHGGHECSQYAAGHMWETWIETRASHFEEPLEKQLKTSLDLLDERMTVRSTKECWKGGTTAVCCAIDMNKKELAFAWLGDSPGYIMDNLEVRKVTRDHSPSDPEEGRRVEEAGGQLFVIGGELRVNGVLNLTRALGDVPGRPMISNQAETCQRDIEVGDYLVILACDGISDVFNTSDLYNLVQAYVNENPVEEYNDLAHYICHEAIAHGSTDNVTVVIGFLRPPQDLWRMMKIDEESDEEEDEVDDE"
                    }
                ],
                "feature_sequence": "atgtccggcccaccaccacccaaaactaacgagaaatcatcacaaccggtcaccggacgatcacaagagcctacgcgtaaaggtcaacttggacccaattacttgcgtataattgaagaggacgaagaatatgggcatgctcttttggagccaagtgaggagcagatcaaattcgaaagagaagcactttttgaggatctccacttggaccgtcaacgaagtgcccgttcattcattgaagagactttcgaggaggagatgcttggaccccaaaatggcattccacccactacagaatctccacagtcatacattcccatccgataccgtaatccaccagcagctgcaccggttcatgacgttttcggagatgctgtacatgcaatttttcaaaagttgatgactcgaggtccacctgtcgagtactgtcactggatgtcctattggattgccaagcagattgataaggatagtccagtgaagtatcatgagtgtcgttttactcctgaccaatacgtgacggagaatactgcagaagccaagaagacttacatggacaatatgtggaaggcagcagaaaagaatttatggatgtacacctacaactctccactccttcgcacaaaatggactggaattcacgtgtctgctgaacaaataaaaggacaacgtcacaaacaggaggatcgatttgtcgcctatccgaatagcttgtacatggatacgtctcgttcggaccatattgctcttttgggtgttttcgatggtcatggaggccacgagtgctcccaatacgctgctgggcatatgtgggagacgtggattgagacacgagcctcgcacttcgaggagccacttgagaagcaactgaagacttcgttggatcttctggatgagcgtatgactgtaagaagtacgaaggaatgctggaagggaggtaccacggctgtctgttgtgcaattgatatgaataagaaggagttggcatttgcttggttgggagattcaccaggctacattatggataatctggaagttcgcaaagtgacacgcgatcactctccatcagatcccgaagaaggtcgtcgcgtcgaagaggctggtggtcaactgtttgtgattggtggagagcttcgagtgaatggtgtgctcaatctgacacgtgcactaggagatgtccctggccgaccgatgatctcgaatcaagcggaaacgtgtcagcgagatattgaagtaggcgactatctggtaattcttgcttgcgatggaatatcggatgtcttcaacacaagtgatttgtacaatttagtgcaggcctatgtcaatgaaaatcctgtagaagaatataacgacttggctcattacatctgccacgaagcgattgctcatggaagtacggacaatgtgacagtcgtcattggattcctccgtccaccacaagatctctggcgcatgatgaaaatcgacgaagagtcagacgaagaagaagacgaggttgatgatgaatag"
            }
        ]
    },
    {
        "name": "AF507019",
        "length": "1796",
        "sequence": "atgtccgacccaccggtcgaaaaaacaagtccagagaagacagagggctcttcatccggcagttttcgcgtcccactcgaatccgacaagcttggtgacccggatttcaagccatgcgttgcacaaatcacaatggagagaaacgcagtgttcgaggacaacttcctcgatcggagacagagtgctcgcgccgtaatcgagtattgctttgaggacgaaatgcaaaacttggttgaagggcgacctgctgtttcagaagaaccagttgttcccatacgattccgacgcccaccaccgtccggacctgctcacgacgtctttggcgacgccatgaacgaaattttccagaaattaatgatgaaaggtcaatgcgcagacttctgccactggatggcttattggctaacaaaggaacaagatgatgcgaatgatggattttttggcaatattcgctataatccagatgtctatgtcacggaaggcacaacagaaaccaaaaaggcgttcgtcgacagcatgtggccgactgctcagcgaattcttctgaaatccgtccggaacagcacgattttacgcacaaagtggactggaatccacgtgtcagcggatcagttgaaggggcaacgcccgaagcaagaagatagattcgtagcttatccgaatagtcagtatatgaatcggacgcaggatcccgtcgcccttctcggtgtgttcgatggtcatggcggacacgagtgctcacaatacgcggcctctcacttctgggaggcatggctggagactcgacaaactagcgacggtgatgagctccagaatcagctgaagaagtcacttgagttgttggatcaacgattgacagtcagaagtgtgaaggaatactggaagggtggcactacggcggcgtgttgcgctatcgataaggagaacaaaacgatggcgttcgcgtggttgggcgattcaccaggatacgtcatgaacaacatggaattccgcaaagtgacacgcgagcactcgccgtccgatccagaagaagcgcgtcgagtcgaagaagccggcggacaactattcgtgatcggtggcgagttgcgagtcaacggagtgctcaacctgacgcgtgctctcggcgacgttcccggacgaccgatgatatcaaatgagccggagatatgcgagagaccgattgagcaaggcgactatatggtgtttttggcgtgtgatggtgtatcggacgtgttgaacactgccgatttatacaatttggttggcgagtttgtcagaacatttcctgttgaagactactcggaaatggctcgctggttttgtcacaaatcgatcaccgctggaagtgccgacaacgtgacagtcgtcattggattccttcgtccaccacaagacatctggaatctcatgagtcgtagctcggatgatgagtctgatgaagaagaagaggatgaggacgacgattgaacgacgacgcctcttccctgtacattaatatattttctcgttttccaaacccctcgtatagctttttctcgttttctcccctccctatctcttatacaattttgggtaaacctcctttcccatatctatcaaattgtttcttttttcccctttcggataacacctcacccacgaaatgtatcattgtttctcacctccctaacttccggatgtccctattccctcggtttcttgtagcatttcatttcatctccccgtattatttttcaattatatatatatagacatgtatgaactgttaaatttaaaaaaaaaaaaaaaaaaaaaaa",
        "features": [
            {
                "feature_name": "source",
                "feature_strand": 1,
                "location_text": "1..1796",
                "feature_locations": [
                    {
                        "feature_range_start": "1",
                        "feature_range_end": "1796"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "organism",
                        "feature_value": "Caenorhabditis remanei"
                    },
                    {
                        "feature_name": "mol_type",
                        "feature_value": "mRNA"
                    },
                    {
                        "feature_name": "strain",
                        "feature_value": "SB146"
                    },
                    {
                        "feature_name": "db_xref",
                        "feature_value": "taxon:31234"
                    }
                ],
                "feature_sequence": "atgtccgacccaccggtcgaaaaaacaagtccagagaagacagagggctcttcatccggcagttttcgcgtcccactcgaatccgacaagcttggtgacccggatttcaagccatgcgttgcacaaatcacaatggagagaaacgcagtgttcgaggacaacttcctcgatcggagacagagtgctcgcgccgtaatcgagtattgctttgaggacgaaatgcaaaacttggttgaagggcgacctgctgtttcagaagaaccagttgttcccatacgattccgacgcccaccaccgtccggacctgctcacgacgtctttggcgacgccatgaacgaaattttccagaaattaatgatgaaaggtcaatgcgcagacttctgccactggatggcttattggctaacaaaggaacaagatgatgcgaatgatggattttttggcaatattcgctataatccagatgtctatgtcacggaaggcacaacagaaaccaaaaaggcgttcgtcgacagcatgtggccgactgctcagcgaattcttctgaaatccgtccggaacagcacgattttacgcacaaagtggactggaatccacgtgtcagcggatcagttgaaggggcaacgcccgaagcaagaagatagattcgtagcttatccgaatagtcagtatatgaatcggacgcaggatcccgtcgcccttctcggtgtgttcgatggtcatggcggacacgagtgctcacaatacgcggcctctcacttctgggaggcatggctggagactcgacaaactagcgacggtgatgagctccagaatcagctgaagaagtcacttgagttgttggatcaacgattgacagtcagaagtgtgaaggaatactggaagggtggcactacggcggcgtgttgcgctatcgataaggagaacaaaacgatggcgttcgcgtggttgggcgattcaccaggatacgtcatgaacaacatggaattccgcaaagtgacacgcgagcactcgccgtccgatccagaagaagcgcgtcgagtcgaagaagccggcggacaactattcgtgatcggtggcgagttgcgagtcaacggagtgctcaacctgacgcgtgctctcggcgacgttcccggacgaccgatgatatcaaatgagccggagatatgcgagagaccgattgagcaaggcgactatatggtgtttttggcgtgtgatggtgtatcggacgtgttgaacactgccgatttatacaatttggttggcgagtttgtcagaacatttcctgttgaagactactcggaaatggctcgctggttttgtcacaaatcgatcaccgctggaagtgccgacaacgtgacagtcgtcattggattccttcgtccaccacaagacatctggaatctcatgagtcgtagctcggatgatgagtctgatgaagaagaagaggatgaggacgacgattgaacgacgacgcctcttccctgtacattaatatattttctcgttttccaaacccctcgtatagctttttctcgttttctcccctccctatctcttatacaattttgggtaaacctcctttcccatatctatcaaattgtttcttttttcccctttcggataacacctcacccacgaaatgtatcattgtttctcacctccctaacttccggatgtccctattccctcggtttcttgtagcatttcatttcatctccccgtattatttttcaattatatatatatagacatgtatgaactgttaaatttaaaaaaaaaaaaaaaaaaaaaaa"
            },
            {
                "feature_name": "gene",
                "feature_strand": 1,
                "location_text": "1..1796",
                "feature_locations": [
                    {
                        "feature_range_start": "1",
                        "feature_range_end": "1796"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    }
                ],
                "feature_sequence": "atgtccgacccaccggtcgaaaaaacaagtccagagaagacagagggctcttcatccggcagttttcgcgtcccactcgaatccgacaagcttggtgacccggatttcaagccatgcgttgcacaaatcacaatggagagaaacgcagtgttcgaggacaacttcctcgatcggagacagagtgctcgcgccgtaatcgagtattgctttgaggacgaaatgcaaaacttggttgaagggcgacctgctgtttcagaagaaccagttgttcccatacgattccgacgcccaccaccgtccggacctgctcacgacgtctttggcgacgccatgaacgaaattttccagaaattaatgatgaaaggtcaatgcgcagacttctgccactggatggcttattggctaacaaaggaacaagatgatgcgaatgatggattttttggcaatattcgctataatccagatgtctatgtcacggaaggcacaacagaaaccaaaaaggcgttcgtcgacagcatgtggccgactgctcagcgaattcttctgaaatccgtccggaacagcacgattttacgcacaaagtggactggaatccacgtgtcagcggatcagttgaaggggcaacgcccgaagcaagaagatagattcgtagcttatccgaatagtcagtatatgaatcggacgcaggatcccgtcgcccttctcggtgtgttcgatggtcatggcggacacgagtgctcacaatacgcggcctctcacttctgggaggcatggctggagactcgacaaactagcgacggtgatgagctccagaatcagctgaagaagtcacttgagttgttggatcaacgattgacagtcagaagtgtgaaggaatactggaagggtggcactacggcggcgtgttgcgctatcgataaggagaacaaaacgatggcgttcgcgtggttgggcgattcaccaggatacgtcatgaacaacatggaattccgcaaagtgacacgcgagcactcgccgtccgatccagaagaagcgcgtcgagtcgaagaagccggcggacaactattcgtgatcggtggcgagttgcgagtcaacggagtgctcaacctgacgcgtgctctcggcgacgttcccggacgaccgatgatatcaaatgagccggagatatgcgagagaccgattgagcaaggcgactatatggtgtttttggcgtgtgatggtgtatcggacgtgttgaacactgccgatttatacaatttggttggcgagtttgtcagaacatttcctgttgaagactactcggaaatggctcgctggttttgtcacaaatcgatcaccgctggaagtgccgacaacgtgacagtcgtcattggattccttcgtccaccacaagacatctggaatctcatgagtcgtagctcggatgatgagtctgatgaagaagaagaggatgaggacgacgattgaacgacgacgcctcttccctgtacattaatatattttctcgttttccaaacccctcgtatagctttttctcgttttctcccctccctatctcttatacaattttgggtaaacctcctttcccatatctatcaaattgtttcttttttcccctttcggataacacctcacccacgaaatgtatcattgtttctcacctccctaacttccggatgtccctattccctcggtttcttgtagcatttcatttcatctccccgtattatttttcaattatatatatatagacatgtatgaactgttaaatttaaaaaaaaaaaaaaaaaaaaaaa"
            },
            {
                "feature_name": "CDS",
                "feature_strand": 1,
                "location_text": "1..1467",
                "feature_locations": [
                    {
                        "feature_range_start": "1",
                        "feature_range_end": "1467"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    },
                    {
                        "feature_name": "note",
                        "feature_value": "type 2C phosphatase; possible sex-determining protein"
                    },
                    {
                        "feature_name": "codon_start",
                        "feature_value": "1"
                    },
                    {
                        "feature_name": "product",
                        "feature_value": "putative protein phosphatase FEM-2"
                    },
                    {
                        "feature_name": "protein_id",
                        "feature_value": "AAM33404.1"
                    },
                    {
                        "feature_name": "translation",
                        "feature_value": "MSDPPVEKTSPEKTEGSSSGSFRVPLESDKLGDPDFKPCVAQITMERNAVFEDNFLDRRQSARAVIEYCFEDEMQNLVEGRPAVSEEPVVPIRFRRPPPSGPAHDVFGDAMNEIFQKLMMKGQCADFCHWMAYWLTKEQDDANDGFFGNIRYNPDVYVTEGTTETKKAFVDSMWPTAQRILLKSVRNSTILRTKWTGIHVSADQLKGQRPKQEDRFVAYPNSQYMNRTQDPVALLGVFDGHGGHECSQYAASHFWEAWLETRQTSDGDELQNQLKKSLELLDQRLTVRSVKEYWKGGTTAACCAIDKENKTMAFAWLGDSPGYVMNNMEFRKVTREHSPSDPEEARRVEEAGGQLFVIGGELRVNGVLNLTRALGDVPGRPMISNEPEICERPIEQGDYMVFLACDGVSDVLNTADLYNLVGEFVRTFPVEDYSEMARWFCHKSITAGSADNVTVVIGFLRPPQDIWNLMSRSSDDESDEEEEDEDDD"
                    }
                ],
                "feature_sequence": "atgtccgacccaccggtcgaaaaaacaagtccagagaagacagagggctcttcatccggcagttttcgcgtcccactcgaatccgacaagcttggtgacccggatttcaagccatgcgttgcacaaatcacaatggagagaaacgcagtgttcgaggacaacttcctcgatcggagacagagtgctcgcgccgtaatcgagtattgctttgaggacgaaatgcaaaacttggttgaagggcgacctgctgtttcagaagaaccagttgttcccatacgattccgacgcccaccaccgtccggacctgctcacgacgtctttggcgacgccatgaacgaaattttccagaaattaatgatgaaaggtcaatgcgcagacttctgccactggatggcttattggctaacaaaggaacaagatgatgcgaatgatggattttttggcaatattcgctataatccagatgtctatgtcacggaaggcacaacagaaaccaaaaaggcgttcgtcgacagcatgtggccgactgctcagcgaattcttctgaaatccgtccggaacagcacgattttacgcacaaagtggactggaatccacgtgtcagcggatcagttgaaggggcaacgcccgaagcaagaagatagattcgtagcttatccgaatagtcagtatatgaatcggacgcaggatcccgtcgcccttctcggtgtgttcgatggtcatggcggacacgagtgctcacaatacgcggcctctcacttctgggaggcatggctggagactcgacaaactagcgacggtgatgagctccagaatcagctgaagaagtcacttgagttgttggatcaacgattgacagtcagaagtgtgaaggaatactggaagggtggcactacggcggcgtgttgcgctatcgataaggagaacaaaacgatggcgttcgcgtggttgggcgattcaccaggatacgtcatgaacaacatggaattccgcaaagtgacacgcgagcactcgccgtccgatccagaagaagcgcgtcgagtcgaagaagccggcggacaactattcgtgatcggtggcgagttgcgagtcaacggagtgctcaacctgacgcgtgctctcggcgacgttcccggacgaccgatgatatcaaatgagccggagatatgcgagagaccgattgagcaaggcgactatatggtgtttttggcgtgtgatggtgtatcggacgtgttgaacactgccgatttatacaatttggttggcgagtttgtcagaacatttcctgttgaagactactcggaaatggctcgctggttttgtcacaaatcgatcaccgctggaagtgccgacaacgtgacagtcgtcattggattccttcgtccaccacaagacatctggaatctcatgagtcgtagctcggatgatgagtctgatgaagaagaagaggatgaggacgacgattga"
            },
            {
                "feature_name": "misc_feature",
                "feature_strand": 1,
                "location_text": "1",
                "feature_locations": [
                    {
                        "feature_range_start": "1",
                        "feature_range_end": "1"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    },
                    {
                        "feature_name": "note",
                        "feature_value": "SL1 splice site"
                    }
                ],
                "feature_sequence": "a"
            }
        ]
    }
]
```

## Sample EMBL input

The following was generated using the `-s` option, which causes the sequences of features to be included:

```text
ID   AF177870; SV 1; linear; genomic DNA; STD; INV; 3123 BP.
XX
AC   AF177870;
XX
DT   02-NOV-1999 (Rel. 61, Created)
DT   31-MAR-2006 (Rel. 87, Last updated, Version 4)
XX
DE   Caenorhabditis sp. CB5161 putative PP2C protein phosphatase FEM-2 (fem-2)
DE   gene, complete cds.
XX
KW   .
XX
OS   Caenorhabditis brenneri
OC   Eukaryota; Metazoa; Ecdysozoa; Nematoda; Chromadorea; Rhabditida;
OC   Rhabditina; Rhabditomorpha; Rhabditoidea; Rhabditidae; Peloderinae;
OC   Caenorhabditis.
XX
RN   [1]
RP   1-3123
RX   DOI; 10.1007/s0023901-0008-y.
RX   PUBMED; 11821919.
RA   Stothard P., Hansen D., Pilgrim D.;
RT   "Evolution of the PP2C family in Caenorhabditis: rapid divergence of the
RT   sex-determining protein FEM-2";
RL   J. Mol. Evol. 54(2):267-282(2002).
XX
RN   [2]
RP   1-3123
RX   DOI; 10.1007/s00239-005-0084-5.
RX   PUBMED; 16477523.
RA   Stothard P., Pilgrim D.;
RT   "Conspecific and interspecific interactions between the FEM-2 and the FEM-3
RT   sex-determining proteins despite rapid sequence divergence";
RL   J. Mol. Evol. 62(3):281-291(2006).
XX
RN   [3]
RP   1-3123
RA   Stothard P.M., Hansen D., Pilgrim D.;
RT   ;
RL   Submitted (17-AUG-1999) to the INSDC.
RL   Biological Sciences, University of Alberta, Edmonton, AB T6G-2E9, Canada
XX
DR   MD5; e3c61da8990212eb27e2a1414a24795b.
XX
FH   Key             Location/Qualifiers
FH
FT   source          1..3123
FT                   /organism="Caenorhabditis brenneri"
FT                   /strain="CB5161"
FT                   /mol_type="genomic DNA"
FT                   /db_xref="taxon:135651"
FT   gene            <265..>2855
FT                   /gene="fem-2"
FT   mRNA            join(<265..402,673..781,911..1007,1088..1215,1377..1573,
FT                   1866..2146,2306..2634,2683..>2855)
FT                   /gene="fem-2"
FT                   /product="putative FEM-2 protein phosphatase type 2C"
FT   CDS             join(265..402,673..781,911..1007,1088..1215,1377..1573,
FT                   1866..2146,2306..2634,2683..2855)
FT                   /codon_start=1
FT                   /gene="fem-2"
FT                   /product="putative PP2C protein phosphatase FEM-2"
FT                   /note="possible sex-determining protein"
FT                   /db_xref="GOA:Q9U6S2"
FT                   /db_xref="InterPro:IPR000222"
FT                   /db_xref="InterPro:IPR001932"
FT                   /db_xref="InterPro:IPR015655"
FT                   /db_xref="InterPro:IPR036457"
FT                   /db_xref="UniProtKB/TrEMBL:Q9U6S2"
FT                   /protein_id="AAF04557.1"
FT                   /translation="MSDSLNHPSSSTVHADDGFEPPTSPEDNNKKPSLEQIKQEREALF
FT                   TDLFADRRRSARSVIEEAFQNELMSAEPVQPNVPNPHSIPIRFRHQPVAGPAHDVFGDA
FT                   VHSIFQKIMSRGVNADYSHWMSYWIALGIDKKTQMNYHMKPFCKDTYATEGSLEAKQTF
FT                   TDKIRSAVEEIIWKSAEYCDILSEKWTGIHVSADQLKGQRNKQEDRFVAYPNGQYMNRG
FT                   QSDISLLAVFDGHGGHECSQYAAAHFWEAWSDAQHHHSQDMKLDELLEKALETLDERMT
FT                   VRSVRESWKGGTTAVCCAVDLNTNQIAFAWLGDSPGYIMSNLEFRKFTTEHSPSDPEEC
FT                   RRVEEVGGQIFVIGGELRVNGVLNLTRALGDVPGRPMISNKPDTLLKTIEPADYLVLLA
FT                   CDGISDVFNTSDLYNLVQAFVNEYDVEDYHELARYICNQAVSAGSADNVTVVIGFLRPP
FT                   EDVWRVMKTDSDDEESELEEEDDNE"
XX
SQ   Sequence 3123 BP; 986 A; 605 C; 597 G; 935 T; 0 other;
     gaacgcgaat gcctctctct ctttcgatgg gtatgccaat tgtccacatt cactcgtgtt        60
     gcctcctctt tgccaacacg caagacacca gaaacgcgtc aaccaaagag aaaaagacgc       120
     cgacaacggg cagcactcgc gagagacaaa ggttatcgcg ttgtgttatt atacattcgc       180
     atccgggtca actttagtcc gttgaacatg cttcttgaaa acctagttct cttaaaataa       240
     cgttttagaa gttttggtct tcagatgtct gattcgctaa atcatccatc gagttctacg       300
     gtgcatgcag atgatggatt cgagccacca acatctccgg aagacaacaa caaaaaaccg       360
     tctttagaac aaattaaaca ggaaagagaa gcgttgttta cggttagtta cctattagct       420
     gcaagttttg aaaaagcgga atctgtaaaa agcggaatct gtaaaaaaaa catctaagga       480
     ataattctga aaagaaaaag tttctaaatg ttaatcggaa tccaattttt atgaaattat       540
     ttaaaaaaaa actaaaatta gtttctaaaa aatttttcta aagtaattgg accatgtgaa       600
     ggtacaccca cttgttccaa tatgccatat ctaactgtaa aataatttga ttctcatgag       660
     aatatttttc aggatctatt cgcagatcgt cgacgaagcg ctcgttctgt gattgaagaa       720
     gctttccaaa acgaactcat gagtgctgaa ccagtccagc caaacgtgcc gaatccacat       780
     tgtgagttgg aaatttttat ttgataacca agagaaaaaa agttctacct ttttttcaaa       840
     aacctttcca aaaatgattc catctgatat aggattaaga aaaatatttt ccgaaatctc       900
     tgcttttcag cgattcccat tcgtttccgt catcaaccag ttgctggacc tgctcatgat       960
     gttttcggag acgcggtgca ttcaattttt caaaaaataa tgtccaggta tacactattt      1020
     ttgcatattt ttcttgccaa atttggtcaa aaaccgtagt acaacccaaa aagtttcttc      1080
     atttcagagg agtgaacgcg gattatagtc attggatgtc atattggatc gcgttgggaa      1140
     tcgacaaaaa aacacaaatg aactatcata tgaaaccgtt ttgcaaagat acttatgcaa      1200
     ctgaaggctc cttaggtagg ttagtctttt ctaggcacag aagagtgaga aaattctaaa      1260
     tttctgagca gtctgctttt tgttttcctt gagtttttac ttaaagctct taaaagaaat      1320
     ctaggcgtga agttcgagcc ttgtaccata ccacaacagc attccaaatg ttacagaagc      1380
     gaaacaaaca tttactgata aaatcaggtc agctgttgag gaaattatct ggaagtccgc      1440
     tgaatattgt gatattctta gcgagaagtg gacaggaatt catgtgtcgg ccgaccaact      1500
     gaaaggtcaa agaaataagc aagaagatcg ttttgtggct tatccaaatg gacaatacat      1560
     gaatcgtgga caggttagtg cgaatcgggg actcaagatt tactgaaata gtgaagagaa      1620
     aacaaaagaa aactatattt tcaaaaaaaa tgagaactct aataaacaga atgaaaaaca      1680
     ttcaaagcta cagtagtatt tccagctgga gtttccagag ccaaaaaaat gcgagtatta      1740
     ctgtagtttt gaaattggtt tctcacttta cgtacgattt tttgattttt ttttcagact      1800
     cttcatatga aaaaaaatca tgttttctcc tttacaagat ttttttgatc tcaaaacatt      1860
     tccagagtga catttcactt cttgcggtgt tcgatgggca tggcggacac gagtgctctc      1920
     aatatgcagc tgctcatttc tgggaagcat ggtccgatgc tcaacatcat cattcacaag      1980
     atatgaaact tgacgaactc ctagaaaagg ctctagaaac attggacgaa agaatgacag      2040
     tcagaagtgt tcgagaatct tggaaaggtg gaaccactgc tgtctgctgt gctgttgatt      2100
     tgaacactaa tcaaatcgca tttgcctggc ttggagattc accagggtaa tcaatttttt      2160
     tttagttttt ggaactttac gtcccgaaaa attattcctt tatcacctaa ttcctacagt      2220
     aacccaagct ccgaattaaa taaagttaaa gcgtggtata cacataaaaa taagaaaaaa      2280
     ttgttcatga aatccatttt tccagttaca tcatgtcaaa cttggagttc cgcaaattca      2340
     ctactgaaca ctccccgtct gacccggagg aatgtcgacg agtcgaagaa gtcggtggcc      2400
     agatttttgt gatcggtggt gagctccgtg tgaatggagt actcaacctg acgcgagcac      2460
     taggagacgt acctggaaga ccaatgatat ccaacaaacc tgatacctta ctgaagacga      2520
     tcgaacctgc ggattatctt gttttgttgg cctgtgacgg gatttctgac gtcttcaaca      2580
     ctagtgattt gtacaatttg gttcaggctt ttgtcaatga atatgacgta gaaggtatca      2640
     aactgatcgt ttttcacatc acaaaattct tgaattttcc agattatcac gaacttgcac      2700
     gctacatttg caatcaagca gtttcagctg gaagtgctga caatgtgaca gtagttatag      2760
     gtttcctccg tccaccagaa gacgtttggc gtgtaatgaa aacagactcg gatgatgaag      2820
     agagcgagct cgaggaagaa gatgacaatg aatagtttat tgcaagtttt ccaaaacttt      2880
     tccaatttcc ctgggtattg attagcatcc atatcttacg gcgattatat caattgtaac      2940
     attatttctg tttctccccc cacctctcaa attttcaaat gacccttttt cttttcgtct      3000
     acctgtatcg ttttccattc atctcccccc ctccactgtg gtatatcatt ttgtcattag      3060
     aaagtattat tttgattttc attggcagta gaagacaaca ggatacagaa gaggttttca      3120
     cag                                                                    3123
//
```

## Sample EMBL output

```text
[
    {
        "name": "AF177870;",
        "length": "3123",
        "sequence": "gaacgcgaatgcctctctctctttcgatgggtatgccaattgtccacattcactcgtgttgcctcctctttgccaacacgcaagacaccagaaacgcgtcaaccaaagagaaaaagacgccgacaacgggcagcactcgcgagagacaaaggttatcgcgttgtgttattatacattcgcatccgggtcaactttagtccgttgaacatgcttcttgaaaacctagttctcttaaaataacgttttagaagttttggtcttcagatgtctgattcgctaaatcatccatcgagttctacggtgcatgcagatgatggattcgagccaccaacatctccggaagacaacaacaaaaaaccgtctttagaacaaattaaacaggaaagagaagcgttgtttacggttagttacctattagctgcaagttttgaaaaagcggaatctgtaaaaagcggaatctgtaaaaaaaacatctaaggaataattctgaaaagaaaaagtttctaaatgttaatcggaatccaatttttatgaaattatttaaaaaaaaactaaaattagtttctaaaaaatttttctaaagtaattggaccatgtgaaggtacacccacttgttccaatatgccatatctaactgtaaaataatttgattctcatgagaatatttttcaggatctattcgcagatcgtcgacgaagcgctcgttctgtgattgaagaagctttccaaaacgaactcatgagtgctgaaccagtccagccaaacgtgccgaatccacattgtgagttggaaatttttatttgataaccaagagaaaaaaagttctacctttttttcaaaaacctttccaaaaatgattccatctgatataggattaagaaaaatattttccgaaatctctgcttttcagcgattcccattcgtttccgtcatcaaccagttgctggacctgctcatgatgttttcggagacgcggtgcattcaatttttcaaaaaataatgtccaggtatacactatttttgcatatttttcttgccaaatttggtcaaaaaccgtagtacaacccaaaaagtttcttcatttcagaggagtgaacgcggattatagtcattggatgtcatattggatcgcgttgggaatcgacaaaaaaacacaaatgaactatcatatgaaaccgttttgcaaagatacttatgcaactgaaggctccttaggtaggttagtcttttctaggcacagaagagtgagaaaattctaaatttctgagcagtctgctttttgttttccttgagtttttacttaaagctcttaaaagaaatctaggcgtgaagttcgagccttgtaccataccacaacagcattccaaatgttacagaagcgaaacaaacatttactgataaaatcaggtcagctgttgaggaaattatctggaagtccgctgaatattgtgatattcttagcgagaagtggacaggaattcatgtgtcggccgaccaactgaaaggtcaaagaaataagcaagaagatcgttttgtggcttatccaaatggacaatacatgaatcgtggacaggttagtgcgaatcggggactcaagatttactgaaatagtgaagagaaaacaaaagaaaactatattttcaaaaaaaatgagaactctaataaacagaatgaaaaacattcaaagctacagtagtatttccagctggagtttccagagccaaaaaaatgcgagtattactgtagttttgaaattggtttctcactttacgtacgattttttgatttttttttcagactcttcatatgaaaaaaaatcatgttttctcctttacaagatttttttgatctcaaaacatttccagagtgacatttcacttcttgcggtgttcgatgggcatggcggacacgagtgctctcaatatgcagctgctcatttctgggaagcatggtccgatgctcaacatcatcattcacaagatatgaaacttgacgaactcctagaaaaggctctagaaacattggacgaaagaatgacagtcagaagtgttcgagaatcttggaaaggtggaaccactgctgtctgctgtgctgttgatttgaacactaatcaaatcgcatttgcctggcttggagattcaccagggtaatcaatttttttttagtttttggaactttacgtcccgaaaaattattcctttatcacctaattcctacagtaacccaagctccgaattaaataaagttaaagcgtggtatacacataaaaataagaaaaaattgttcatgaaatccatttttccagttacatcatgtcaaacttggagttccgcaaattcactactgaacactccccgtctgacccggaggaatgtcgacgagtcgaagaagtcggtggccagatttttgtgatcggtggtgagctccgtgtgaatggagtactcaacctgacgcgagcactaggagacgtacctggaagaccaatgatatccaacaaacctgataccttactgaagacgatcgaacctgcggattatcttgttttgttggcctgtgacgggatttctgacgtcttcaacactagtgatttgtacaatttggttcaggcttttgtcaatgaatatgacgtagaaggtatcaaactgatcgtttttcacatcacaaaattcttgaattttccagattatcacgaacttgcacgctacatttgcaatcaagcagtttcagctggaagtgctgacaatgtgacagtagttataggtttcctccgtccaccagaagacgtttggcgtgtaatgaaaacagactcggatgatgaagagagcgagctcgaggaagaagatgacaatgaatagtttattgcaagttttccaaaacttttccaatttccctgggtattgattagcatccatatcttacggcgattatatcaattgtaacattatttctgtttctccccccacctctcaaattttcaaatgaccctttttcttttcgtctacctgtatcgttttccattcatctccccccctccactgtggtatatcattttgtcattagaaagtattattttgattttcattggcagtagaagacaacaggatacagaagaggttttcacag",
        "features": [
            {
                "feature_name": "source",
                "feature_strand": 1,
                "location_text": "1..3123",
                "feature_locations": [
                    {
                        "feature_range_start": "1",
                        "feature_range_end": "3123"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "organism",
                        "feature_value": "Caenorhabditis brenneri"
                    },
                    {
                        "feature_name": "strain",
                        "feature_value": "CB5161"
                    },
                    {
                        "feature_name": "mol_type",
                        "feature_value": "genomic DNA"
                    },
                    {
                        "feature_name": "db_xref",
                        "feature_value": "taxon:135651"
                    }
                ],
                "feature_sequence": "gaacgcgaatgcctctctctctttcgatgggtatgccaattgtccacattcactcgtgttgcctcctctttgccaacacgcaagacaccagaaacgcgtcaaccaaagagaaaaagacgccgacaacgggcagcactcgcgagagacaaaggttatcgcgttgtgttattatacattcgcatccgggtcaactttagtccgttgaacatgcttcttgaaaacctagttctcttaaaataacgttttagaagttttggtcttcagatgtctgattcgctaaatcatccatcgagttctacggtgcatgcagatgatggattcgagccaccaacatctccggaagacaacaacaaaaaaccgtctttagaacaaattaaacaggaaagagaagcgttgtttacggttagttacctattagctgcaagttttgaaaaagcggaatctgtaaaaagcggaatctgtaaaaaaaacatctaaggaataattctgaaaagaaaaagtttctaaatgttaatcggaatccaatttttatgaaattatttaaaaaaaaactaaaattagtttctaaaaaatttttctaaagtaattggaccatgtgaaggtacacccacttgttccaatatgccatatctaactgtaaaataatttgattctcatgagaatatttttcaggatctattcgcagatcgtcgacgaagcgctcgttctgtgattgaagaagctttccaaaacgaactcatgagtgctgaaccagtccagccaaacgtgccgaatccacattgtgagttggaaatttttatttgataaccaagagaaaaaaagttctacctttttttcaaaaacctttccaaaaatgattccatctgatataggattaagaaaaatattttccgaaatctctgcttttcagcgattcccattcgtttccgtcatcaaccagttgctggacctgctcatgatgttttcggagacgcggtgcattcaatttttcaaaaaataatgtccaggtatacactatttttgcatatttttcttgccaaatttggtcaaaaaccgtagtacaacccaaaaagtttcttcatttcagaggagtgaacgcggattatagtcattggatgtcatattggatcgcgttgggaatcgacaaaaaaacacaaatgaactatcatatgaaaccgttttgcaaagatacttatgcaactgaaggctccttaggtaggttagtcttttctaggcacagaagagtgagaaaattctaaatttctgagcagtctgctttttgttttccttgagtttttacttaaagctcttaaaagaaatctaggcgtgaagttcgagccttgtaccataccacaacagcattccaaatgttacagaagcgaaacaaacatttactgataaaatcaggtcagctgttgaggaaattatctggaagtccgctgaatattgtgatattcttagcgagaagtggacaggaattcatgtgtcggccgaccaactgaaaggtcaaagaaataagcaagaagatcgttttgtggcttatccaaatggacaatacatgaatcgtggacaggttagtgcgaatcggggactcaagatttactgaaatagtgaagagaaaacaaaagaaaactatattttcaaaaaaaatgagaactctaataaacagaatgaaaaacattcaaagctacagtagtatttccagctggagtttccagagccaaaaaaatgcgagtattactgtagttttgaaattggtttctcactttacgtacgattttttgatttttttttcagactcttcatatgaaaaaaaatcatgttttctcctttacaagatttttttgatctcaaaacatttccagagtgacatttcacttcttgcggtgttcgatgggcatggcggacacgagtgctctcaatatgcagctgctcatttctgggaagcatggtccgatgctcaacatcatcattcacaagatatgaaacttgacgaactcctagaaaaggctctagaaacattggacgaaagaatgacagtcagaagtgttcgagaatcttggaaaggtggaaccactgctgtctgctgtgctgttgatttgaacactaatcaaatcgcatttgcctggcttggagattcaccagggtaatcaatttttttttagtttttggaactttacgtcccgaaaaattattcctttatcacctaattcctacagtaacccaagctccgaattaaataaagttaaagcgtggtatacacataaaaataagaaaaaattgttcatgaaatccatttttccagttacatcatgtcaaacttggagttccgcaaattcactactgaacactccccgtctgacccggaggaatgtcgacgagtcgaagaagtcggtggccagatttttgtgatcggtggtgagctccgtgtgaatggagtactcaacctgacgcgagcactaggagacgtacctggaagaccaatgatatccaacaaacctgataccttactgaagacgatcgaacctgcggattatcttgttttgttggcctgtgacgggatttctgacgtcttcaacactagtgatttgtacaatttggttcaggcttttgtcaatgaatatgacgtagaaggtatcaaactgatcgtttttcacatcacaaaattcttgaattttccagattatcacgaacttgcacgctacatttgcaatcaagcagtttcagctggaagtgctgacaatgtgacagtagttataggtttcctccgtccaccagaagacgtttggcgtgtaatgaaaacagactcggatgatgaagagagcgagctcgaggaagaagatgacaatgaatagtttattgcaagttttccaaaacttttccaatttccctgggtattgattagcatccatatcttacggcgattatatcaattgtaacattatttctgtttctccccccacctctcaaattttcaaatgaccctttttcttttcgtctacctgtatcgttttccattcatctccccccctccactgtggtatatcattttgtcattagaaagtattattttgattttcattggcagtagaagacaacaggatacagaagaggttttcacag"
            },
            {
                "feature_name": "gene",
                "feature_strand": 1,
                "location_text": "<265..>2855",
                "feature_locations": [
                    {
                        "feature_range_start": "265",
                        "feature_range_end": "2855"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    }
                ],
                "feature_sequence": "atgtctgattcgctaaatcatccatcgagttctacggtgcatgcagatgatggattcgagccaccaacatctccggaagacaacaacaaaaaaccgtctttagaacaaattaaacaggaaagagaagcgttgtttacggttagttacctattagctgcaagttttgaaaaagcggaatctgtaaaaagcggaatctgtaaaaaaaacatctaaggaataattctgaaaagaaaaagtttctaaatgttaatcggaatccaatttttatgaaattatttaaaaaaaaactaaaattagtttctaaaaaatttttctaaagtaattggaccatgtgaaggtacacccacttgttccaatatgccatatctaactgtaaaataatttgattctcatgagaatatttttcaggatctattcgcagatcgtcgacgaagcgctcgttctgtgattgaagaagctttccaaaacgaactcatgagtgctgaaccagtccagccaaacgtgccgaatccacattgtgagttggaaatttttatttgataaccaagagaaaaaaagttctacctttttttcaaaaacctttccaaaaatgattccatctgatataggattaagaaaaatattttccgaaatctctgcttttcagcgattcccattcgtttccgtcatcaaccagttgctggacctgctcatgatgttttcggagacgcggtgcattcaatttttcaaaaaataatgtccaggtatacactatttttgcatatttttcttgccaaatttggtcaaaaaccgtagtacaacccaaaaagtttcttcatttcagaggagtgaacgcggattatagtcattggatgtcatattggatcgcgttgggaatcgacaaaaaaacacaaatgaactatcatatgaaaccgttttgcaaagatacttatgcaactgaaggctccttaggtaggttagtcttttctaggcacagaagagtgagaaaattctaaatttctgagcagtctgctttttgttttccttgagtttttacttaaagctcttaaaagaaatctaggcgtgaagttcgagccttgtaccataccacaacagcattccaaatgttacagaagcgaaacaaacatttactgataaaatcaggtcagctgttgaggaaattatctggaagtccgctgaatattgtgatattcttagcgagaagtggacaggaattcatgtgtcggccgaccaactgaaaggtcaaagaaataagcaagaagatcgttttgtggcttatccaaatggacaatacatgaatcgtggacaggttagtgcgaatcggggactcaagatttactgaaatagtgaagagaaaacaaaagaaaactatattttcaaaaaaaatgagaactctaataaacagaatgaaaaacattcaaagctacagtagtatttccagctggagtttccagagccaaaaaaatgcgagtattactgtagttttgaaattggtttctcactttacgtacgattttttgatttttttttcagactcttcatatgaaaaaaaatcatgttttctcctttacaagatttttttgatctcaaaacatttccagagtgacatttcacttcttgcggtgttcgatgggcatggcggacacgagtgctctcaatatgcagctgctcatttctgggaagcatggtccgatgctcaacatcatcattcacaagatatgaaacttgacgaactcctagaaaaggctctagaaacattggacgaaagaatgacagtcagaagtgttcgagaatcttggaaaggtggaaccactgctgtctgctgtgctgttgatttgaacactaatcaaatcgcatttgcctggcttggagattcaccagggtaatcaatttttttttagtttttggaactttacgtcccgaaaaattattcctttatcacctaattcctacagtaacccaagctccgaattaaataaagttaaagcgtggtatacacataaaaataagaaaaaattgttcatgaaatccatttttccagttacatcatgtcaaacttggagttccgcaaattcactactgaacactccccgtctgacccggaggaatgtcgacgagtcgaagaagtcggtggccagatttttgtgatcggtggtgagctccgtgtgaatggagtactcaacctgacgcgagcactaggagacgtacctggaagaccaatgatatccaacaaacctgataccttactgaagacgatcgaacctgcggattatcttgttttgttggcctgtgacgggatttctgacgtcttcaacactagtgatttgtacaatttggttcaggcttttgtcaatgaatatgacgtagaaggtatcaaactgatcgtttttcacatcacaaaattcttgaattttccagattatcacgaacttgcacgctacatttgcaatcaagcagtttcagctggaagtgctgacaatgtgacagtagttataggtttcctccgtccaccagaagacgtttggcgtgtaatgaaaacagactcggatgatgaagagagcgagctcgaggaagaagatgacaatgaatag"
            },
            {
                "feature_name": "mRNA",
                "feature_strand": 1,
                "location_text": "join(<265..402,673..781,911..1007,1088..1215,1377..1573,1866..2146,2306..2634,2683..>2855)",
                "feature_locations": [
                    {
                        "feature_range_start": "265",
                        "feature_range_end": "402"
                    },
                    {
                        "feature_range_start": "673",
                        "feature_range_end": "781"
                    },
                    {
                        "feature_range_start": "911",
                        "feature_range_end": "1007"
                    },
                    {
                        "feature_range_start": "1088",
                        "feature_range_end": "1215"
                    },
                    {
                        "feature_range_start": "1377",
                        "feature_range_end": "1573"
                    },
                    {
                        "feature_range_start": "1866",
                        "feature_range_end": "2146"
                    },
                    {
                        "feature_range_start": "2306",
                        "feature_range_end": "2634"
                    },
                    {
                        "feature_range_start": "2683",
                        "feature_range_end": "2855"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    },
                    {
                        "feature_name": "product",
                        "feature_value": "putative FEM-2 protein phosphatase type 2C"
                    }
                ],
                "feature_sequence": "atgtctgattcgctaaatcatccatcgagttctacggtgcatgcagatgatggattcgagccaccaacatctccggaagacaacaacaaaaaaccgtctttagaacaaattaaacaggaaagagaagcgttgtttacggatctattcgcagatcgtcgacgaagcgctcgttctgtgattgaagaagctttccaaaacgaactcatgagtgctgaaccagtccagccaaacgtgccgaatccacattcgattcccattcgtttccgtcatcaaccagttgctggacctgctcatgatgttttcggagacgcggtgcattcaatttttcaaaaaataatgtccagaggagtgaacgcggattatagtcattggatgtcatattggatcgcgttgggaatcgacaaaaaaacacaaatgaactatcatatgaaaccgttttgcaaagatacttatgcaactgaaggctccttagaagcgaaacaaacatttactgataaaatcaggtcagctgttgaggaaattatctggaagtccgctgaatattgtgatattcttagcgagaagtggacaggaattcatgtgtcggccgaccaactgaaaggtcaaagaaataagcaagaagatcgttttgtggcttatccaaatggacaatacatgaatcgtggacagagtgacatttcacttcttgcggtgttcgatgggcatggcggacacgagtgctctcaatatgcagctgctcatttctgggaagcatggtccgatgctcaacatcatcattcacaagatatgaaacttgacgaactcctagaaaaggctctagaaacattggacgaaagaatgacagtcagaagtgttcgagaatcttggaaaggtggaaccactgctgtctgctgtgctgttgatttgaacactaatcaaatcgcatttgcctggcttggagattcaccaggttacatcatgtcaaacttggagttccgcaaattcactactgaacactccccgtctgacccggaggaatgtcgacgagtcgaagaagtcggtggccagatttttgtgatcggtggtgagctccgtgtgaatggagtactcaacctgacgcgagcactaggagacgtacctggaagaccaatgatatccaacaaacctgataccttactgaagacgatcgaacctgcggattatcttgttttgttggcctgtgacgggatttctgacgtcttcaacactagtgatttgtacaatttggttcaggcttttgtcaatgaatatgacgtagaagattatcacgaacttgcacgctacatttgcaatcaagcagtttcagctggaagtgctgacaatgtgacagtagttataggtttcctccgtccaccagaagacgtttggcgtgtaatgaaaacagactcggatgatgaagagagcgagctcgaggaagaagatgacaatgaatag"
            },
            {
                "feature_name": "CDS",
                "feature_strand": 1,
                "location_text": "join(265..402,673..781,911..1007,1088..1215,1377..1573,1866..2146,2306..2634,2683..2855)",
                "feature_locations": [
                    {
                        "feature_range_start": "265",
                        "feature_range_end": "402"
                    },
                    {
                        "feature_range_start": "673",
                        "feature_range_end": "781"
                    },
                    {
                        "feature_range_start": "911",
                        "feature_range_end": "1007"
                    },
                    {
                        "feature_range_start": "1088",
                        "feature_range_end": "1215"
                    },
                    {
                        "feature_range_start": "1377",
                        "feature_range_end": "1573"
                    },
                    {
                        "feature_range_start": "1866",
                        "feature_range_end": "2146"
                    },
                    {
                        "feature_range_start": "2306",
                        "feature_range_end": "2634"
                    },
                    {
                        "feature_range_start": "2683",
                        "feature_range_end": "2855"
                    }
                ],
                "feature_qualifiers": [
                    {
                        "feature_name": "codon_start",
                        "feature_value": "1"
                    },
                    {
                        "feature_name": "gene",
                        "feature_value": "fem-2"
                    },
                    {
                        "feature_name": "product",
                        "feature_value": "putative PP2C protein phosphatase FEM-2"
                    },
                    {
                        "feature_name": "note",
                        "feature_value": "possible sex-determining protein"
                    },
                    {
                        "feature_name": "db_xref",
                        "feature_value": "GOA:Q9U6S2"
                    },
                    {
                        "feature_name": "db_xref",
                        "feature_value": "InterPro:IPR000222"
                    },
                    {
                        "feature_name": "db_xref",
                        "feature_value": "InterPro:IPR001932"
                    },
                    {
                        "feature_name": "db_xref",
                        "feature_value": "InterPro:IPR015655"
                    },
                    {
                        "feature_name": "db_xref",
                        "feature_value": "InterPro:IPR036457"
                    },
                    {
                        "feature_name": "db_xref",
                        "feature_value": "UniProtKB/TrEMBL:Q9U6S2"
                    },
                    {
                        "feature_name": "protein_id",
                        "feature_value": "AAF04557.1"
                    },
                    {
                        "feature_name": "translation",
                        "feature_value": "MSDSLNHPSSSTVHADDGFEPPTSPEDNNKKPSLEQIKQEREALFTDLFADRRRSARSVIEEAFQNELMSAEPVQPNVPNPHSIPIRFRHQPVAGPAHDVFGDAVHSIFQKIMSRGVNADYSHWMSYWIALGIDKKTQMNYHMKPFCKDTYATEGSLEAKQTFTDKIRSAVEEIIWKSAEYCDILSEKWTGIHVSADQLKGQRNKQEDRFVAYPNGQYMNRGQSDISLLAVFDGHGGHECSQYAAAHFWEAWSDAQHHHSQDMKLDELLEKALETLDERMTVRSVRESWKGGTTAVCCAVDLNTNQIAFAWLGDSPGYIMSNLEFRKFTTEHSPSDPEECRRVEEVGGQIFVIGGELRVNGVLNLTRALGDVPGRPMISNKPDTLLKTIEPADYLVLLACDGISDVFNTSDLYNLVQAFVNEYDVEDYHELARYICNQAVSAGSADNVTVVIGFLRPPEDVWRVMKTDSDDEESELEEEDDNE"
                    }
                ],
                "feature_sequence": "atgtctgattcgctaaatcatccatcgagttctacggtgcatgcagatgatggattcgagccaccaacatctccggaagacaacaacaaaaaaccgtctttagaacaaattaaacaggaaagagaagcgttgtttacggatctattcgcagatcgtcgacgaagcgctcgttctgtgattgaagaagctttccaaaacgaactcatgagtgctgaaccagtccagccaaacgtgccgaatccacattcgattcccattcgtttccgtcatcaaccagttgctggacctgctcatgatgttttcggagacgcggtgcattcaatttttcaaaaaataatgtccagaggagtgaacgcggattatagtcattggatgtcatattggatcgcgttgggaatcgacaaaaaaacacaaatgaactatcatatgaaaccgttttgcaaagatacttatgcaactgaaggctccttagaagcgaaacaaacatttactgataaaatcaggtcagctgttgaggaaattatctggaagtccgctgaatattgtgatattcttagcgagaagtggacaggaattcatgtgtcggccgaccaactgaaaggtcaaagaaataagcaagaagatcgttttgtggcttatccaaatggacaatacatgaatcgtggacagagtgacatttcacttcttgcggtgttcgatgggcatggcggacacgagtgctctcaatatgcagctgctcatttctgggaagcatggtccgatgctcaacatcatcattcacaagatatgaaacttgacgaactcctagaaaaggctctagaaacattggacgaaagaatgacagtcagaagtgttcgagaatcttggaaaggtggaaccactgctgtctgctgtgctgttgatttgaacactaatcaaatcgcatttgcctggcttggagattcaccaggttacatcatgtcaaacttggagttccgcaaattcactactgaacactccccgtctgacccggaggaatgtcgacgagtcgaagaagtcggtggccagatttttgtgatcggtggtgagctccgtgtgaatggagtactcaacctgacgcgagcactaggagacgtacctggaagaccaatgatatccaacaaacctgataccttactgaagacgatcgaacctgcggattatcttgttttgttggcctgtgacgggatttctgacgtcttcaacactagtgatttgtacaatttggttcaggcttttgtcaatgaatatgacgtagaagattatcacgaacttgcacgctacatttgcaatcaagcagtttcagctggaagtgctgacaatgtgacagtagttataggtttcctccgtccaccagaagacgtttggcgtgtaatgaaaacagactcggatgatgaagagagcgagctcgaggaagaagatgacaatgaatag"
            }
        ],
        "type": "dna"
    }
]
```