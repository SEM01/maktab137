from t import main
import pytest
import shlex


test_case = [
    ("--file='server.log' scan '--ip'", "8.8.8.8"),
    ("--file='server.log' scan '--url'", "https://example.com/"),
    ("--file='server.log' scan '--errors'", "404 512"),
    ("--file='server.log' scan '--ip' '--count'", "15"),
    ("--file='server.log' scan '--url' '--count'", "8"),
    ("--file='server.log' scan '--errors' '--count'", "11"),
    ("--file='server.log' stats", "192.168.10.45"),
    ("--file='server.log' clean '--api'", "172.16.0.55"),
    ("--file='server.log' monitor '--error'", "185.123.45.67"),
]


@pytest.mark.parametrize("command, expected_output", test_case)
def test_argparse(capsys, command, expected_output):
    main(shlex.split(command))
    captured = capsys.readouterr()
    output = captured.out + captured.err
    assert expected_output in output


test_case_sys_exit = [
    (
        "--file=serdver.log",
        "LOG file not found",
    ),
    (
        "--file=server.log scan",
        "one of the arguments --ip --url --errors is required",
    ),
    (
        "--file='server.log' sscan '--ip'",
        "invalid choice: 'sscan'",
    ),
    (
        "--file='server.log' scan '--ipp'",
        "scan: error",
    ),
]


@pytest.mark.parametrize("command, expected_output", test_case_sys_exit)
def test_argparse_sys_exit(capsys, command, expected_output):
    with pytest.raises(SystemExit):
        main(shlex.split(command))
    captured = capsys.readouterr()
    output = captured.err
    assert expected_output in output
