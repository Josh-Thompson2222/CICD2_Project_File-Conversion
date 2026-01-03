import pytest
from pathlib import Path
from app.services.filters import apply_filters

@pytest.mark.asyncio
async def test_apply_filters_edits_file(tmp_path: Path):
    # create input file
    f = tmp_path / "input.txt"
    f.write_text("This is bloody simple", encoding="utf-8")

    # create temp resources
    banned = tmp_path / "banned_words.txt"
    banned.write_text("bloody\n", encoding="utf-8")
    wordlist = tmp_path / "wordlist.txt"
    wordlist.write_text("this\nis\nsimple\n", encoding="utf-8")

    await apply_filters(
        file_path=str(f),
        run_profanity=True,
        run_spellcheck=True,
        wordlist_path=str(wordlist),
        banned_words_path=str(banned),
    )

    out = f.read_text(encoding="utf-8").lower()
    assert "bloody" not in out
    assert "*" in out