for (int j = 0; j < nFaces; ++j)
{

  SNormal.push_back({0.0d,0.0d,0.0d});

  CG.push_back({0.0d,0.0d,0.0d});

  CG[j].x += Points[Faces[j][1]].x;
  CG[j].y += Points[Faces[j][1]].y;
  CG[j].z += Points[Faces[j][1]].z;

  for (int i = 2; i < Faces[j][0] - 1; ++i)
  {

    SNormal[j].x += 0.5*((Points[Faces[j][i+1]].y - Points[Faces[j][1]].y) * (Points[Faces[j][i]].z - Points[Faces[j][1]].z));
    SNormal[j].x -= 0.5*((Points[Faces[j][i+1]].z - Points[Faces[j][1]].z) * (Points[Faces[j][i]].z - Points[Faces[j][1]].y));

    SNormal[j].y += 0.5*((Points[Faces[j][i+1]].z - Points[Faces[j][1]].z) * (Points[Faces[j][i]].x - Points[Faces[j][1]].x));
    SNormal[j].y -= 0.5*((Points[Faces[j][i+1]].x - Points[Faces[j][1]].x) * (Points[Faces[j][i]].z - Points[Faces[j][1]].z));

    SNormal[j].z += 0.5*((Points[Faces[j][i+1]].x - Points[Faces[j][1]].x) * (Points[Faces[j][i]].y - Points[Faces[j][1]].y));
    SNormal[j].z -= 0.5*((Points[Faces[j][i+1]].y - Points[Faces[j][1]].y) * (Points[Faces[j][i]].x - Points[Faces[j][1]].x));

    CG[j].x += Points[Faces[j][i]].x;
    CG[j].y += Points[Faces[j][i]].y;
    CG[j].z += Points[Faces[j][i]].z;

  }

  long double sa = pow(SNormal[j].x,2) + pow(SNormal[j].y,2) + pow(SNormal[j].z,2);
  sa = sqrt(sa);
  SurfaceArea.push_back(sa);

   CG[j].x /= Faces[j][0];
   CG[j].y /= Faces[j][0];
   CG[j].z /= Faces[j][0];

  //std::cout << "Face " << j+1 << ", SFArea : (" << SurfaceArea[j] << " )" << std::endl; //SNormal[j].x << " , " << SNormal[j].y << " , " << SNormal[j].z << ")" << std::endl;
}
