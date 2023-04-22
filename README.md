# classic-mac-tools

Collection of scripts to bridge files from classic Mac OS to modern macOS and vice versa.

## File associations

Converted files won't have any file associations as classic Mac OS [doesn't use file extensions](https://en.wikipedia.org/wiki/Resource_fork). I recommend using [FileTyper](https://www.macintoshrepository.org/2050-filetyper) to set the correct codes, [here is a table](https://whitefiles.org/dta/pgs/f01.htm) with codes (or use `TEXT` and `MACA` for text files, `WORD` and `MACA` for MacWrite files).

## Text files

Both `txt/classic2modern.py` and `txt/modern2classic.py` can be used to convert each line endings. Modern to classic additionally also convert smart Unicode punctation to ASCII equivalents and strip any other Unicode characters.