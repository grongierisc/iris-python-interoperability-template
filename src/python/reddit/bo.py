from pathlib import Path

from iop import BusinessOperation

from messages import ClassifiedThread


class FileWriterOperation(BusinessOperation):
    """Append matched titles to output files."""

    def on_message(self, request: ClassifiedThread):
        output_dir = Path("/irisdev/app/output")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_path = output_dir / request.destination_file
        line = request.title
        if request.permalink:
            line = f"{line} | https://www.reddit.com{request.permalink}"

        with output_path.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")

        return None
