#include "includes.h"
struct vect {
  long double x, y, z;
};

class Mesh
{
public:
  std::vector<vect> Points,SNormal,CG;
  std::vector<std::vector<int>> Faces;
  std::vector<int> Owners,Neighbours;
  int nPoints, nCells, nFaces, nInternalFaces, nBoundaryFaces;
  std::vector<long double> SurfaceArea;

public:
  Mesh()
  {
    # include "ReadFiles.H"
    # include "Calculate.h"
  }
//void calcSurfaceARea(vector<vector<int>>, vector<vector<double>>,vector<vector<double>> &,vector<double>&);

}mesh;

int main()
{
  //std::cout << "Point 1 (x) : " << mesh.Points[1].x << std::endl;

  return 0;
}
