
import pandas as pd
import shutil
from ps2ff.cmd import get_command_output


def test_rjb_WC94():
    cmd = "bin/run_ps2ff -w rjb tests/config/test_WC94.ini"
    rc, so, se = get_command_output(cmd)
    r1 = pd.read_csv(
        "tests/data/test_Rjb_WC94_mechA_ar1p7_seis0_20_Ratios.csv",
        header=6)
    v1 = pd.read_csv(
        "tests/data/test_Rjb_WC94_mechA_ar1p7_seis0_20_Var.csv",
        header=6)
    r2 = pd.read_csv(
        "TestData/Rjb_WC94_mechA_ar1p7_seis0_20_Ratios.csv",
        header=6)
    v2 = pd.read_csv(
        "TestData/Rjb_WC94_mechA_ar1p7_seis0_20_Var.csv",
        header=6)

    pd.util.testing.assert_frame_equal(r1, r2)
    pd.util.testing.assert_frame_equal(v1, v2)

    # Clean up
    shutil.rmtree('TestData')


def test_rjb_S14():
    cmd = "bin/run_ps2ff -w rjb tests/config/test_S14.ini"
    rc, so, se = get_command_output(cmd)
    r1 = pd.read_csv(
        "tests/data/test_Rjb_S14_mechA_ar1p7_seis0_20_Ratios.csv",
        header=6)
    v1 = pd.read_csv(
        "tests/data/test_Rjb_S14_mechA_ar1p7_seis0_20_Var.csv",
        header=6)
    r2 = pd.read_csv(
        "TestData/Rjb_S14_mechA_ar1p7_seis0_20_Ratios.csv",
        header=6)
    v2 = pd.read_csv(
        "TestData/Rjb_S14_mechA_ar1p7_seis0_20_Var.csv",
        header=6)

    pd.util.testing.assert_frame_equal(r1, r2)
    pd.util.testing.assert_frame_equal(v1, v2)

    # Clean up
    shutil.rmtree('TestData')


def test_rrup_S14():
    cmd = "bin/run_ps2ff -w rrup tests/config/test_2_S14.ini"
    rc, so, se = get_command_output(cmd)
    r1 = pd.read_csv(
        "tests/data/test_Rrup_S14_mechA_ar2p0_seis0_15_Ratios.csv",
        header=6)
    v1 = pd.read_csv(
        "tests/data/test_Rrup_S14_mechA_ar2p0_seis0_15_Var.csv",
        header=6)
    r2 = pd.read_csv(
        "TestData/Rrup_S14_mechA_ar2p0_seis0_15_Ratios.csv",
        header=6)
    v2 = pd.read_csv(
        "TestData/Rrup_S14_mechA_ar2p0_seis0_15_Var.csv",
        header=6)

    pd.util.testing.assert_frame_equal(r1, r2)
    pd.util.testing.assert_frame_equal(v1, v2)

    # Clean up
    shutil.rmtree('TestData')


def test_rrup_WC94():
    cmd = "bin/run_ps2ff -w rrup tests/config/test_2_WC94.ini"
    rc, so, se = get_command_output(cmd)
    r1 = pd.read_csv(
        "tests/data/test_Rrup_WC94_mechA_ar2p0_seis0_15_Ratios.csv",
        header=6)
    v1 = pd.read_csv(
        "tests/data/test_Rrup_WC94_mechA_ar2p0_seis0_15_Var.csv",
        header=6)
    r2 = pd.read_csv(
        "TestData/Rrup_WC94_mechA_ar2p0_seis0_15_Ratios.csv",
        header=6)
    v2 = pd.read_csv(
        "TestData/Rrup_WC94_mechA_ar2p0_seis0_15_Var.csv",
        header=6)

    pd.util.testing.assert_frame_equal(r1, r2)
    pd.util.testing.assert_frame_equal(v1, v2)

    # Clean up
    shutil.rmtree('TestData')
