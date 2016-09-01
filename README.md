# raptor

##Installation

Pull this repository into `/your/raptor/directory`.

If run permissions are not enabled by default, you may need to add them in yourself.

You can do this with:

`chmod +x raptor`

Finally add raptor to your PATH with

`export PATH=/your/raptor/directory:$PATH`

## Usage

Do a full test by invoking `raptor runtest`

Options include 

`-help`: Get a printout of all available options

`-dfs`: Disable FileSystem tests. They will be ignored in the report and final score
