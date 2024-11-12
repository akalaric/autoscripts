#include <iostream>
#include <vector>

class veck
{
public:
    void rotVec(std::vector<std::vector<int>> &svec)
    {
        int n = svec.size();
        std::vector<std::vector<int>> res;
        res.assign(n, std::vector<int>(n));
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                res[j][n-i-1] = svec[i][j];
            }
        }
        svec = res;
        printvec(svec);

    }
    void printvec(std::vector<std::vector<int>> svec)
    {
        int n = svec.size();
        for (int i = 0; i < n; i++)
        {
            std::cout << "[";
            for (int j = 0; j < n; j++)
            {
                std::cout << svec[i][j];
                if (j != svec[i].size() - 1)
                {
                    std::cout << ", ";
                }
                else
                {
                    std::cout << "]" << std::endl;
                }
            }
        }
    }
};

int main()
{
    std::vector<std::vector<int>> nvec = {{1, 2, 3, 4},
                                          {5, 6, 7, 8},
                                          {9, 10, 11, 12},
                                          {13, 14, 15, 16}};
    veck sol;
    sol.rotVec(nvec);
}