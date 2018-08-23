# PDB2JSON

Try it now with this example: [https://pdb2json.samireland.com/1CBN/](https://pdb2json.samireland.com/1CBN/).

## What is This?

Protein structures are stored by the likes of the [RCSB](https://www.rcsb.org/) and other bodies, and come in two flavours - .pdb and .cif. Each structure will have a .pdb and a .cif representation, and they should both describe the same thing. .pdb was the original, .cif is the new and improved file format that will one day replace it.

However, to use them you need to have a parser like [atomium](https://atomium.samireland.com/) or [biopython](https://biopython.org/) installed, which can read these file formats. For the structural biologist on the go, this can be an inconvenience.

JSON is the modern web's *lingua franca*. Data structures in the form of JSON can be read and understood by pretty much any language. So, wouldn't it be wonderful if the RCSB protein structures could be accessed as JSON objects.

Well they can now.

## How do I use it?

All you need is the PDB code of the structure you want. The you just append it to the end of the URL and send a GET request. For example, [https://pdb2json.samireland.com/1CBN/](https://pdb2json.samireland.com/1CBN/) will return the 1CBN structure as a JSON object - all structural information and the most important header annotations.

[https://pdb2json.samireland.com/1CBN.cif/](https://pdb2json.samireland.com/1CBN.cif/) will get the same JSON dictionary, but from the mmCIF file - differences should be minimal.

You can even get the precursor JSON object that was created from the file before being turned into the standard data dictionary, with [https://pdb2json.samireland.com/1CBN.cif?file](https://pdb2json.samireland.com/1CBN.cif?file).

Finally, and most powerfully of all, you can traverse the keys of the resultant dictionary using the URL. [https://pdb2json.samireland.com/1CBN/models/0/residues/0/](https://pdb2json.samireland.com/1CBN/models/0/residues/0/) for example will just return the JSON for the first residue in the first model.

## How does it work?

The Python parser and molecular modeller [atomium](https://atomium.samireland.com/), also made by me, is used to create these JSON objects behind the scenes.