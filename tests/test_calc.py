from project_name.calculate import run


def test_calc_run():
    assert run("subtract", 1, 3) != -2
