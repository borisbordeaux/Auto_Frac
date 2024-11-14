# AutoFrac
Software to help conception of fractals and study fractal properties.

## How to build
 
Replace the `{path_to_Qt6}` with the path to Qt. Be sure to have Qt6 installed.  
Replace `{NB_CORES}` by the number of cores you want to use for compiling the project.

```bash
git clone https://github.com/borisbordeaux/AutoFrac.git
cd AutoFrac
mkdir build
cd build
export QT_PATH={path_to_Qt6}/Qt/6.6.1/gcc_64
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j {NB_CORES}
```

For an integration within an IDE, be sure to set the `QT_PATH` environment variable for the project.

## Main features

### Automatic subdivision 2D

Define parameters of a fractal topology, and eventually define control points position by editing the scheme.  
Then export the structure in a python file that will be interpreted by a fractal modeler (link coming soon...).

### Fractal from polyhedron sphere packing

Import a polyhedron and display the sphere packing.  
Export the fractal structure associated in a python file that will be interpreted by a fractal modeler (link coming soon...).

### Computations on fractals

#### Compute of Fractal Dimension

Compute fractal dimension using box counting method on an image.

#### Compute of Area and Perimeter

Compute the area and the perimeter of an image or an OBJ file.

#### Compute of Density

Compute the density of a structure on an image et displays for each pixel its density.

#### Compute of Persistent Homology

Compute the persistent homology of an OBJ file and display the persistent cohomology diagram.
