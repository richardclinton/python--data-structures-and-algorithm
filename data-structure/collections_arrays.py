# The `array` module defines a data type array that is similar to the list data type
# except fot the constraint that their contents must be of a single type of the
# underlying representation, as is determined by the machine architecture or underlying
# C implementation.
# The type of `array` is determined at creation time and it is indicated by one of the
# following type codes.
# 1. Code => 'b' C type => signedchar Python type => int Minimum bytes => 1
# 2. Code => 'B' C type => unsignedchar Python type => int Minimum bytes => 1
# 3. Code => 'u' C type => Py_UNICODE Python type => Unicodecharacter Minimum bytes => 2
# 4. Code => 'h' C type => sigleshort Python type => int Minimum bytes => 2
# 5. Code => 'H' C type => unsignedshort Python type => int Minimum bytes => 2
# 6. Code => 'i' C type => signedint Python type => int Minimum bytes => 2
# 7. Code => 'I' C type => unsignedint Python type => int Minimum bytes => 2
# 8. Code => 'l' C type => signedlong Python type => int Minimum bytes => 4
# 9. Code => 'L' C type => unsignedlong Python type => int Minimum bytes => 8
# 10. Code => 'q' C type => signedlonglong Python type => int Minimum bytes => 8
# 11. Code => 'Q' C type => unsignedlonglong Python type => int Minimum bytes => 8
# 12. Code => 'f' C type => float Python type => float Minimum bytes => 4
# 13. Code => 'd' C type => double Python type => double Minimum bytes => 8
