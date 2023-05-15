# Lab 14: Find and Makefiles

## Task 1: Finding interesting files on your disk

- Find all `gif` files in your home folder
- Find all files on your machine larger than 100MB
- Find the first 10 files containing space in file (not directory) name
- Find all files in your home modified in the last 1 hour

## Task 2: Generating code for CSV parser

To simplify parsing of CSV files, we will generate a Python
class from the first line (headers) of a given CSV file. The
class will have attributes that correspond to individual columns
and the code will automatically populate those when reading a file. 

_In Python, you could generate this at runtime. The benefit of
code generation here is just that some IDEs may give you better
auto-completion. This technique is much more useful for C# etc._

- Copy (or clone) `demo.py` and `parser.template` into some directory
- We want to write a Makefile that generates `parser.py` in two steps.
  First, it downloads `titanic.csv`, then it generates the parser.
  It should look like this:

  ```
  main: # Main goal, should do everything (via dependencies)
  clean: # Should delete titanic.csv and parser.py
  titanic.csv: # Should download https://raw.githubusercontent.com/tpetricek/nswi177/main/14/titanic.csv
  parser.py # Will do the code generation; depends on titanic.csv
  ```

- Create `Makefile` with the above goals
- Implement the `clean` goal (using `rm`) and `titanic.csv` goal (using `wget`)
- Implement the code generation. Look at `parser.template`. 
  This shows what we want to generate. On lines 4-6, it reads 
  three columns into named attributes. We want to generate this
  part of the file automatically, based on columns in the sample
  `titatnic.csv` file. To do this, you may need:
  * Use `>` to copy first few lines from the template to 
    `parser.py`, then use `>>` to add your attribute parsing and
    then use `>>` again to add last few lines from the template.
  * `head -n3` to get the first 3 lines of `parser.template`
  * `tail -n9` to get the last 9 lines of `parser.template`
  * `tr \; \\n` to turn semicolons (in the first row) into newlines
  * `awk '{ print "\t" $0 NR }` to print a tab, input line, line number
  * **NOTE** If you want to put `$0` into `Makefile`, you need
    to escape it using `$$0`.

## Demo: Running F# web server using Podman

The following shows how to use Podman to run F# without 
installing anything locally (a useful thing to do if you 
want to run code someone gives you in a strange langauge!)

The following runs "F# Interactive" interactively in Podman
and also exposes the 80 port (mapped to local 8080) so that
we can run web server in F#:

```sh
podman run --publish 8080:80/tcp --interactive --tty mcr.microsoft.com/dotnet/sdk:7.0 dotnet fsi
```

Once this starts, you can create a simple server in F# using:

```fsharp
#r "nuget:Suave"
open Suave;;

let cfg = { defaultConfig with bindings = [ HttpBinding.createSimple HTTP "0.0.0.0" 80 ] };;

let web = Successful.OK "Hello from F#";;
let _, start = startWebServerAsync cfg web;;
Async.Start start;;
```