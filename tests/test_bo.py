from pathlib import Path

from bo import FileWriterOperation
from messages import ClassifiedThread


def test_file_writer_appends_to_target_file(monkeypatch, tmp_path):
    operation = FileWriterOperation()

    # Redirect hardcoded output path to pytest temporary directory.
    monkeypatch.setattr("bo.Path", lambda _path: tmp_path)

    request = ClassifiedThread(
        title="A cat post",
        destination_file="cat.txt",
        permalink="/r/test/comments/1",
    )

    operation.on_message(request)

    output_file = Path(tmp_path) / "cat.txt"
    assert output_file.exists()
    assert (
        output_file.read_text(encoding="utf-8")
        == "A cat post | https://www.reddit.com/r/test/comments/1\n"
    )

    operation.on_message(
        ClassifiedThread(
            title="Second cat post",
            destination_file="cat.txt",
            permalink="",
        )
    )

    assert output_file.read_text(encoding="utf-8") == (
        "A cat post | https://www.reddit.com/r/test/comments/1\n"
        "Second cat post\n"
    )
