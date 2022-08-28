
template<typename T>
void readFiles(std::vector<T>& Points,std::fstream& PointsFile, int totalPoints)
{
  long long int p , q , o ,sign ;

  long double y, n;

  std::string line;
  bool dec = false;
  std::getline(PointsFile,line);
  sign = 1;
  long double v[] = {0.0d, 0.0d,0.0d};
for (int j = 0; j < totalPoints; ++j)
{
  p = 0;
  q = 0;
  n = 1.0d;
  sign = 1;
  dec = false;

  for(int i = 0; i < 3; ++i)
  v[i] = 0.0d;
  std::getline(PointsFile,line);
  //cout << line << endl;
  o = 0;
for( int i = 0; line[i] != '\0'; ++i )
{
  if (line[i]>='0' && line[i] <= '9')
  {
    if (dec == false)
    {
      p *= 10;
      p += static_cast<int>(line[i]) - 48;
    }
    else if (dec == true)
    {
      q *= 10;
      q += static_cast<int>(line[i]) - 48 ;
      n *= 0.10d;
    }
  }

  if(line[i] == '.')
  {
    dec = true;
  }
  if(line[i] == '-')
  {
    sign = -1;
  }

  if (line[i]== ' ' || line [i+1] == ')')
  {
    y = (p + q*n)*sign;
    v[o] = y;
    ++o;
    p = 0;
    q = 0;
    n = 1.0d;
    sign = 1;
    dec = false;
  }
}
Points.push_back({v[0],v[1],v[2]});
//std::cout << "Point " << j+1 << " : (" << Points[j].x << "," << Points[j].y << "," <<  std::setprecision(10) <<Points[j].z << ")" << std::endl;
}

}




void readFiles(std::vector<std::vector<int>>& var,std::fstream& file, int total)
{
  int x, j, o;
  std::string line;
  std::getline(file, line);
  for (int i = 0; i < total ; ++i)
  {
    std::getline(file,line);
    j = 0;
    x = 0;

    while(line[j]!= '(')
    {
      if(line[j] >= '0' && line[j] <= '9')
      {
        x *= 10;
        x += (int)(line[j]) - 48;
      }
      j++;
    }
    var.push_back({x,0,0,0});

    for(int n = 3 ; n < x; ++n)
    var[i].push_back(0);

    o = 1;
    x = 0;

    while( line[j] != ')')
    {
      if(line[j] >= '0' && line[j] <= '9')
      {
        x *= 10;
        x += (int)(line[j]) - 48;
      }
      if (line[j]== ' ' || line [j+1] == ')')
      {

        var[i][o] = x;
        ++o;
        x = 0;
      }
      ++j;
    }

  }
}
void readFiles(std::vector<int>& var,std::fstream& file, int total)
{
  std::string line;
  int x, j;
  std::getline(file, line);

  for(int i = 0; i < total; ++i)
  {
    std::getline(file,line);
    x = stoi(line);
    var.push_back(x);
  }

}
