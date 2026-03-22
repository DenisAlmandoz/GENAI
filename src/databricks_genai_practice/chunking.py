from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    text: str
    strategy: str


def paragraph_chunks(text: str, min_chars: int = 120) -> list[Chunk]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[Chunk] = []
    buffer = []
    size = 0
    counter = 1
    for paragraph in paragraphs:
        buffer.append(paragraph)
        size += len(paragraph)
        if size >= min_chars:
            chunks.append(Chunk(f"chunk-{counter}", "\n\n".join(buffer), "paragraph"))
            counter += 1
            buffer = []
            size = 0
    if buffer:
        chunks.append(Chunk(f"chunk-{counter}", "\n\n".join(buffer), "paragraph"))
    return chunks


def markdown_heading_chunks(text: str) -> list[Chunk]:
    sections = []
    current_heading = "Document"
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("#"):
            if current_lines:
                sections.append((current_heading, "\n".join(current_lines).strip()))
            current_heading = line.strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_lines:
        sections.append((current_heading, "\n".join(current_lines).strip()))
    return [Chunk(f"chunk-{i}", f"{heading}\n{body}".strip(), "markdown-heading") for i, (heading, body) in enumerate(sections, start=1)]
