# File-Walker
A program that recursively walks through a directory tree and counts number of word occurences
The words are sorted alphabetically, and for each word the
occurrences are grouped by file name which are also sorted. Within a single
file, the occurrences are sorted, first by line, then by column.
Words are always converted to lower case. Because of this, Day and day are treated as the same
word. This does not apply to filenames: In filenames, we keep the distinction between upper and lower case, because the operating system may make this
distinction.
