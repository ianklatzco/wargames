fflush() is used to push the contents of a stream out of the buffer and to the output file.

usually used to clear a buffer and write to a terminal.

however, it's undefined behavior on stdin, and shouldn't be used there.

i'm unclear what "undefined behavior" means, for now.
