# Regular expression tasks

Download the following HTML page using `curl`: https://www.mff.cuni.cz/en/students/bachelor-of-computer-science-2019/degree-plans-general-computer-science and then solve the following puzzles:

* Count the number of different `NPRG` subject codes on the page
* Count the number of all different subject codes on the page
* Count the number of subjects based on the group such as `NAIL` or `NPRG` (for all groups)
* Print a text-based table with course code and title for all courses


## You will need

- `grep -Eo "XYZ"` to find matches of regular expression `"XYZ"` and print the matches
- `wc -l` to count the number of lines in the input
- `uniq` to get just unique lines from the input
- `uniq -c` to get the unique lines alongside with number of occurrences
- `sed -rn "s/XYZ/ABC/p"` to match a regular expression using SED and print the replacement 
