import unittest

import pytest
import os
import astropy.units as u
import numpy
from pinttestdata import datadir
from os import path
from astropy.time import Time

from pint.observatory import Observatory
from pint.observatory.clock_file import ClockFile


class TestClockcorrection(unittest.TestCase):
    # Note, these tests currently depend on external data (TEMPO2 clock
    # files, which could potentially change.  Values here are taken
    # from tempo2 version 2020-06-01 or so.
    def test_parkes(self):
        obs = Observatory.get("Parkes")
        if os.getenv("TEMPO2") is None:
            pytest.skip("TEMPO2 evnironment variable is not set, can't run this test")
        cf = ClockFile.read(
            obs.clock_fullpath, format=obs.clock_fmt, obscode=obs.tempo_code
        )

        t = Time(51211.73, format="pulsar_mjd", scale="utc")
        assert numpy.isclose(cf.evaluate(t), 1.75358956 * u.us)

        t = Time(55418.11285, format="pulsar_mjd", scale="utc")
        assert numpy.isclose(cf.evaluate(t), -0.593622 * u.us)

    def test_wsrt(self):
        # Issue here is the wsrt clock file has text columns, which used to cause np.loadtxt to crash
        cf = ClockFile.read(
            path.join(datadir, "wsrt2gps.clk"), format="tempo2", obscode="i"
        )

        t = Time(57109.5, scale="utc", format="mjd")
        e = cf.evaluate(t)
        assert numpy.isclose(e.to(u.us).value, 7.907)
