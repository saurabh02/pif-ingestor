from pif_ingestor.ui import get_cli
from pif_ingestor import main
from pypif import pif
from os.path import exists


def test_recursive_dft():
    """Test that recursive application of the DFT ingester works"""
    argv = "tests/dft dft -m tests/dft/metadata.json -r".split()
    args = get_cli().parse_args(args=argv)
    main(args)

    # Make sure both files are processed
    assert exists("tests/dft/B.hR12/pif.json"), "Expected to find output pif for B.hR12"
    assert exists("tests/dft/B.hR105/pif.json"), "Expected to find output pif for B.hR105" 

    # Check basic parsing
    with open("tests/dft/B.hR12/pif.json", "r") as f:
        bhr12 = pif.load(f)[0]
    assert bhr12.chemical_formula == "B12"
    assert len(bhr12.contacts) == 2

    emails = set(["johnsmith@generic.org", "janedoe@generic.org"])
    assert set(x.email for x in bhr12.contacts) == emails
