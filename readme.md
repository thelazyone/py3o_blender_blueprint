This is a barebones Blender plugin that features some Rust Code in it. Useful as a blueprint for future projects.
This is meant for Windows applications. Linux and (maybe?) Mac appear to have more streamlined processes.

## Instructions
* Set Up a project with the info contained in the current Cargo.toml and the syntax for PyO3
* Make sure to have Python 3.10 installed. Somehow Python 3.11 might be an issue (even though it should work?)
* Pay attention at the naming convention. I haven't fully understood how critical it is, but it's better to navigate on the safer side.
* Once built the .dll, rename it as pyd, and move it into /blender_plugin.
* Zip it together with the hello_plugin.py. Load the zip as an add-on in Blender.

This works on one machine at the time of this commit, but I need to test it on another.