import io

import src.main


def test_enter_name_and_say_hello(capsys, monkeypatch):
    user_input = "Joe"
    monkeypatch.setattr("sys.stdin", io.StringIO(user_input))

    expected = """Whats your name :
Hello, Joe!\n"""

    src.main.main()

    captured = capsys.readouterr()

    assert captured.out == expected
