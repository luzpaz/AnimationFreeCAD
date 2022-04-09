# Presentation

This FreeCAD module allows users to animate any object easily through visual scripting Nodes using [PyFlow](https://github.com/wonderworks-software/PyFlow).

Documentation can be found at `AnimationFreeCAD/docs/guide`

This module use a modified version of PyFlow

# The project

We offer you a new way to create small animations on FreeCAD through visual scripting.

![Image de PyFlow](./docs/img/exampleNode.png)<br/>

![Video de presentation](./docs/img/videoPresentation.gif)

# Installation

## Install

Install the following packages into the local Module directory : <br/>
Exemple For Linux : `/usr/share/freecad/Mod/` <br>
Exemple for Windows : `C:/Program Files/FreeCD 0.19/Mod/` <br/>
using the following command:<br/>

#With git command
(You may have to run your CLI in Administrator mode if you are on Windows)
```bash
git clone https://github.com/QuentinTournier40/AnimationFreeCAD.git
```

#With download zip
Unzip the project in the `Mod` folder
Make sure that the unzipped folder has not generated a sub-folder that contains the contents of the unzipped folder

Example: <br/>
AnimationFreeCAD/AnimationFreeCAD/{Files} :x: <br/>
AnimationFreeCAD/{Files} :white_check_mark: <br/>

## Requirements

For this workench you must have:<br/>
Install the following requirements into the local Module directory `{Your FreeCAD installation folder}/FreeCAD/Mod`

1. **Qt.Py-master**
2. **nine**
3. **blinker-master**
4. **docutils**

You will find in the folder requirements the files of its libraries `{Your FreeCAD installation folder}/FreeCAD/Mod/AnimationFreeCAD/requirements`.<br/>
Simply copy them in the mod folder of FreeCAD `{Your FreeCAD installation folder}/FreeCAD/Mod`.

## ⚠️⚠️ After doing this you will need to run FreeCAD in **administrator mode** for the first time in order to properly load dependencies. ⚠️⚠️

-----------------------------------------------------------------------------------------------------

# Thanks

Thanks to:
[@microelly2](https://github.com/microelly2)<br/>
[@microelly2/NodeEditor](https://github.com/microelly2/NodeEditor)<br/>
[PyFlow](https://github.com/wonderworks-software/PyFlow)<br/>

# Author

We are 4 students from the University of Pau and the Basque Country.<br/>
We are working on a project to graduate from computer science.

[@QuentinTournier40](https://github.com/QuentinTournier40)<br/>
[@SHaiZen](https://github.com/SHaiZen25)<br/>
[@AimFried](https://github.com/AimFried)<br/>
[@nvacher](https://github.com/nvacher)<br/>
