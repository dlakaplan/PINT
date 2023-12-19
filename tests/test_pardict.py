import glob
import pytest
from pint.models import get_model
from pinttestdata import datadir


@pytest.mark.parametrize("parname", list(glob.glob(str(datadir) + "/*.par")))
@pytest.mark.parametrize("components", [True, False])
def test_derived_params(parname, components):
    try:
        m = get_model(parname)
        readin = True
    except:
        readin = False
    if readin:
        out = m.as_dict(components=components)
        assert isinstance(out, dict)
