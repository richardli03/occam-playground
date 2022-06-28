#!/bin/bash
BUILDLOCATION="Software_Projects/rtabmap_krishpine/build"

cd
cd ${BUILDLOCATION}
make_func(){
    make -j8
}

echo "testing echo"
cmake ..

{ 
    make_func &&
    echo "make -j8 occuring "

} || {
    echo "error"
    exit
}

sudo make install
./bin/rtabmap-databaseViewer