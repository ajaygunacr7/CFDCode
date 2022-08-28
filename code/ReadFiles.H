std::fstream PointsFile, OwnersFile, NeighboursFile, BoundaryFile, FacesFile;
std::string line;
PointsFile.open("Mesh/points");
FacesFile.open("Mesh/faces");
OwnersFile.open("Mesh/owner");
NeighboursFile.open("Mesh/neighbour");
BoundaryFile.open("Mesh/boundary");

PointsFile >> this->nPoints;
OwnersFile >> this->nFaces;
FacesFile >> this->nFaces;
NeighboursFile >> this->nInternalFaces;
this->nBoundaryFaces = this->nFaces - this->nInternalFaces;

std::cout << "Total Points : " << this->nPoints << std::endl;
std::cout << "Total Faces : " << this->nFaces << std::endl;
std::cout << "Total Internal Faces : " << this->nInternalFaces << std::endl;
std::cout << "Total Boundary Faces : " << this->nBoundaryFaces << std::endl;

std::getline(PointsFile,line);
std::getline(FacesFile,line);
std::getline(OwnersFile,line);
std::getline(NeighboursFile,line);

readFiles(this->Points,PointsFile,this->nPoints);
readFiles(this->Faces,FacesFile,this->nFaces);
readFiles(this->Owners,OwnersFile,this->nFaces);
readFiles(this->Neighbours,NeighboursFile,this->nInternalFaces);
