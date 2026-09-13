# Details

Date : 2024-04-02 18:28:41

Directory /media/zox/36c0d412-c5a3-4d73-8ece-b4e01cfb90e6/home/ysc/lite_cog/nav/src

Total : 2713 files,  464576 codes, 132885 comments, 97898 blanks, all 695359 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [fast_gicp/.github/workflows/build.yml](/fast_gicp/.github/workflows/build.yml) | YAML | 27 | 1 | 7 | 35 |
| [fast_gicp/README.md](/fast_gicp/README.md) | Markdown | 122 | 0 | 36 | 158 |
| [fast_gicp/docker/focal/Dockerfile](/fast_gicp/docker/focal/Dockerfile) | Docker | 24 | 0 | 10 | 34 |
| [fast_gicp/docker/focal_cuda/Dockerfile](/fast_gicp/docker/focal_cuda/Dockerfile) | Docker | 23 | 0 | 9 | 32 |
| [fast_gicp/docker/kinetic/Dockerfile](/fast_gicp/docker/kinetic/Dockerfile) | Docker | 24 | 1 | 9 | 34 |
| [fast_gicp/docker/melodic/Dockerfile](/fast_gicp/docker/melodic/Dockerfile) | Docker | 18 | 0 | 8 | 26 |
| [fast_gicp/docker/melodic_llvm/Dockerfile](/fast_gicp/docker/melodic_llvm/Dockerfile) | Docker | 19 | 0 | 8 | 27 |
| [fast_gicp/docker/noetic/Dockerfile](/fast_gicp/docker/noetic/Dockerfile) | Docker | 19 | 0 | 8 | 27 |
| [fast_gicp/docker/noetic_llvm/Dockerfile](/fast_gicp/docker/noetic_llvm/Dockerfile) | Docker | 20 | 0 | 9 | 29 |
| [fast_gicp/include/fast_gicp/cuda/brute_force_knn.cuh](/fast_gicp/include/fast_gicp/cuda/brute_force_knn.cuh) | CUDA C++ | 10 | 0 | 7 | 17 |
| [fast_gicp/include/fast_gicp/cuda/compute_derivatives.cuh](/fast_gicp/include/fast_gicp/cuda/compute_derivatives.cuh) | CUDA C++ | 19 | 0 | 5 | 24 |
| [fast_gicp/include/fast_gicp/cuda/compute_mahalanobis.cuh](/fast_gicp/include/fast_gicp/cuda/compute_mahalanobis.cuh) | CUDA C++ | 19 | 0 | 6 | 25 |
| [fast_gicp/include/fast_gicp/cuda/covariance_estimation.cuh](/fast_gicp/include/fast_gicp/cuda/covariance_estimation.cuh) | CUDA C++ | 12 | 0 | 5 | 17 |
| [fast_gicp/include/fast_gicp/cuda/covariance_regularization.cuh](/fast_gicp/include/fast_gicp/cuda/covariance_regularization.cuh) | CUDA C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/include/fast_gicp/cuda/fast_vgicp_cuda.cuh](/fast_gicp/include/fast_gicp/cuda/fast_vgicp_cuda.cuh) | CUDA C++ | 69 | 0 | 28 | 97 |
| [fast_gicp/include/fast_gicp/cuda/find_voxel_correspondences.cuh](/fast_gicp/include/fast_gicp/cuda/find_voxel_correspondences.cuh) | CUDA C++ | 18 | 0 | 6 | 24 |
| [fast_gicp/include/fast_gicp/cuda/gaussian_voxelmap.cuh](/fast_gicp/include/fast_gicp/cuda/gaussian_voxelmap.cuh) | CUDA C++ | 32 | 1 | 11 | 44 |
| [fast_gicp/include/fast_gicp/cuda/ndt_compute_derivatives.cuh](/fast_gicp/include/fast_gicp/cuda/ndt_compute_derivatives.cuh) | CUDA C++ | 27 | 0 | 7 | 34 |
| [fast_gicp/include/fast_gicp/cuda/ndt_cuda.cuh](/fast_gicp/include/fast_gicp/cuda/ndt_cuda.cuh) | CUDA C++ | 54 | 0 | 19 | 73 |
| [fast_gicp/include/fast_gicp/cuda/vector3_hash.cuh](/fast_gicp/include/fast_gicp/cuda/vector3_hash.cuh) | CUDA C++ | 31 | 2 | 10 | 43 |
| [fast_gicp/include/fast_gicp/gicp/experimental/fast_gicp_mp.hpp](/fast_gicp/include/fast_gicp/gicp/experimental/fast_gicp_mp.hpp) | C++ | 61 | 0 | 27 | 88 |
| [fast_gicp/include/fast_gicp/gicp/experimental/fast_gicp_mp_impl.hpp](/fast_gicp/include/fast_gicp/gicp/experimental/fast_gicp_mp_impl.hpp) | C++ | 214 | 6 | 61 | 281 |
| [fast_gicp/include/fast_gicp/gicp/fast_gicp.hpp](/fast_gicp/include/fast_gicp/gicp/fast_gicp.hpp) | C++ | 75 | 3 | 27 | 105 |
| [fast_gicp/include/fast_gicp/gicp/fast_gicp_st.hpp](/fast_gicp/include/fast_gicp/gicp/fast_gicp_st.hpp) | C++ | 51 | 3 | 15 | 69 |
| [fast_gicp/include/fast_gicp/gicp/fast_vgicp.hpp](/fast_gicp/include/fast_gicp/gicp/fast_vgicp.hpp) | C++ | 63 | 3 | 20 | 86 |
| [fast_gicp/include/fast_gicp/gicp/fast_vgicp_cuda.hpp](/fast_gicp/include/fast_gicp/gicp/fast_vgicp_cuda.hpp) | C++ | 65 | 3 | 22 | 90 |
| [fast_gicp/include/fast_gicp/gicp/fast_vgicp_voxel.hpp](/fast_gicp/include/fast_gicp/gicp/fast_vgicp_voxel.hpp) | C++ | 151 | 2 | 33 | 186 |
| [fast_gicp/include/fast_gicp/gicp/gicp_settings.hpp](/fast_gicp/include/fast_gicp/gicp/gicp_settings.hpp) | C++ | 8 | 0 | 5 | 13 |
| [fast_gicp/include/fast_gicp/gicp/impl/fast_gicp_impl.hpp](/fast_gicp/include/fast_gicp/gicp/impl/fast_gicp_impl.hpp) | C++ | 239 | 0 | 64 | 303 |
| [fast_gicp/include/fast_gicp/gicp/impl/fast_gicp_st_impl.hpp](/fast_gicp/include/fast_gicp/gicp/impl/fast_gicp_st_impl.hpp) | C++ | 96 | 0 | 34 | 130 |
| [fast_gicp/include/fast_gicp/gicp/impl/fast_vgicp_cuda_impl.hpp](/fast_gicp/include/fast_gicp/gicp/impl/fast_vgicp_cuda_impl.hpp) | C++ | 145 | 2 | 36 | 183 |
| [fast_gicp/include/fast_gicp/gicp/impl/fast_vgicp_impl.hpp](/fast_gicp/include/fast_gicp/gicp/impl/fast_vgicp_impl.hpp) | C++ | 160 | 1 | 48 | 209 |
| [fast_gicp/include/fast_gicp/gicp/impl/lsq_registration_impl.hpp](/fast_gicp/include/fast_gicp/gicp/impl/lsq_registration_impl.hpp) | C++ | 135 | 0 | 39 | 174 |
| [fast_gicp/include/fast_gicp/gicp/lsq_registration.hpp](/fast_gicp/include/fast_gicp/gicp/lsq_registration.hpp) | C++ | 65 | 0 | 23 | 88 |
| [fast_gicp/include/fast_gicp/ndt/impl/ndt_cuda_impl.hpp](/fast_gicp/include/fast_gicp/ndt/impl/ndt_cuda_impl.hpp) | C++ | 73 | 0 | 21 | 94 |
| [fast_gicp/include/fast_gicp/ndt/ndt_cuda.hpp](/fast_gicp/include/fast_gicp/ndt/ndt_cuda.hpp) | C++ | 58 | 0 | 16 | 74 |
| [fast_gicp/include/fast_gicp/ndt/ndt_settings.hpp](/fast_gicp/include/fast_gicp/ndt/ndt_settings.hpp) | C++ | 6 | 0 | 4 | 10 |
| [fast_gicp/include/fast_gicp/so3/so3.hpp](/fast_gicp/include/fast_gicp/so3/so3.hpp) | C++ | 45 | 25 | 11 | 81 |
| [fast_gicp/package.xml](/fast_gicp/package.xml) | XML | 11 | 0 | 4 | 15 |
| [fast_gicp/scripts/runtest_cuda.sh](/fast_gicp/scripts/runtest_cuda.sh) | Shell Script | 2 | 1 | 1 | 4 |
| [fast_gicp/setup.py](/fast_gicp/setup.py) | Python | 66 | 32 | 20 | 118 |
| [fast_gicp/src/align.cpp](/fast_gicp/src/align.cpp) | C++ | 154 | 25 | 37 | 216 |
| [fast_gicp/src/fast_gicp/cuda/brute_force_knn.cu](/fast_gicp/src/fast_gicp/cuda/brute_force_knn.cu) | CUDA C++ | 81 | 6 | 25 | 112 |
| [fast_gicp/src/fast_gicp/cuda/compute_derivatives.cu](/fast_gicp/src/fast_gicp/cuda/compute_derivatives.cu) | CUDA C++ | 142 | 2 | 43 | 187 |
| [fast_gicp/src/fast_gicp/cuda/compute_mahalanobis.cu](/fast_gicp/src/fast_gicp/cuda/compute_mahalanobis.cu) | CUDA C++ | 59 | 1 | 15 | 75 |
| [fast_gicp/src/fast_gicp/cuda/covariance_estimation.cu](/fast_gicp/src/fast_gicp/cuda/covariance_estimation.cu) | CUDA C++ | 42 | 1 | 11 | 54 |
| [fast_gicp/src/fast_gicp/cuda/covariance_estimation_rbf.cu](/fast_gicp/src/fast_gicp/cuda/covariance_estimation_rbf.cu) | CUDA C++ | 119 | 3 | 32 | 154 |
| [fast_gicp/src/fast_gicp/cuda/covariance_regularization.cu](/fast_gicp/src/fast_gicp/cuda/covariance_regularization.cu) | CUDA C++ | 94 | 6 | 24 | 124 |
| [fast_gicp/src/fast_gicp/cuda/fast_vgicp_cuda.cu](/fast_gicp/src/fast_gicp/cuda/fast_vgicp_cuda.cu) | CUDA C++ | 230 | 1 | 57 | 288 |
| [fast_gicp/src/fast_gicp/cuda/find_voxel_correspondences.cu](/fast_gicp/src/fast_gicp/cuda/find_voxel_correspondences.cu) | CUDA C++ | 86 | 4 | 25 | 115 |
| [fast_gicp/src/fast_gicp/cuda/gaussian_voxelmap.cu](/fast_gicp/src/fast_gicp/cuda/gaussian_voxelmap.cu) | CUDA C++ | 227 | 4 | 62 | 293 |
| [fast_gicp/src/fast_gicp/cuda/ndt_compute_derivatives.cu](/fast_gicp/src/fast_gicp/cuda/ndt_compute_derivatives.cu) | CUDA C++ | 176 | 5 | 54 | 235 |
| [fast_gicp/src/fast_gicp/cuda/ndt_cuda.cu](/fast_gicp/src/fast_gicp/cuda/ndt_cuda.cu) | CUDA C++ | 144 | 0 | 37 | 181 |
| [fast_gicp/src/fast_gicp/gicp/experimental/fast_gicp_mp.cpp](/fast_gicp/src/fast_gicp/gicp/experimental/fast_gicp_mp.cpp) | C++ | 3 | 1 | 2 | 6 |
| [fast_gicp/src/fast_gicp/gicp/fast_gicp.cpp](/fast_gicp/src/fast_gicp/gicp/fast_gicp.cpp) | C++ | 5 | 0 | 2 | 7 |
| [fast_gicp/src/fast_gicp/gicp/fast_gicp_st.cpp](/fast_gicp/src/fast_gicp/gicp/fast_gicp_st.cpp) | C++ | 5 | 0 | 2 | 7 |
| [fast_gicp/src/fast_gicp/gicp/fast_vgicp.cpp](/fast_gicp/src/fast_gicp/gicp/fast_vgicp.cpp) | C++ | 5 | 0 | 2 | 7 |
| [fast_gicp/src/fast_gicp/gicp/fast_vgicp_cuda.cpp](/fast_gicp/src/fast_gicp/gicp/fast_vgicp_cuda.cpp) | C++ | 5 | 0 | 2 | 7 |
| [fast_gicp/src/fast_gicp/gicp/lsq_registration.cpp](/fast_gicp/src/fast_gicp/gicp/lsq_registration.cpp) | C++ | 5 | 0 | 2 | 7 |
| [fast_gicp/src/fast_gicp/ndt/ndt_cuda.cpp](/fast_gicp/src/fast_gicp/ndt/ndt_cuda.cpp) | C++ | 5 | 0 | 2 | 7 |
| [fast_gicp/src/kitti.cpp](/fast_gicp/src/kitti.cpp) | C++ | 107 | 19 | 30 | 156 |
| [fast_gicp/src/kitti.py](/fast_gicp/src/kitti.py) | Python | 36 | 10 | 14 | 60 |
| [fast_gicp/src/python/main.cpp](/fast_gicp/src/python/main.cpp) | C++ | 193 | 0 | 31 | 224 |
| [fast_gicp/src/test/gicp_test.cpp](/fast_gicp/src/test/gicp_test.cpp) | C++ | 167 | 4 | 37 | 208 |
| [fast_gicp/thirdparty/Eigen/.gitlab-ci.yml](/fast_gicp/thirdparty/Eigen/.gitlab-ci.yml) | YAML | 12 | 8 | 4 | 24 |
| [fast_gicp/thirdparty/Eigen/.gitlab/issue_templates/Bug Report.md](/fast_gicp/thirdparty/Eigen/.gitlab/issue_templates/Bug%20Report.md) | Markdown | 23 | 33 | 14 | 70 |
| [fast_gicp/thirdparty/Eigen/.gitlab/issue_templates/Feature Request.md](/fast_gicp/thirdparty/Eigen/.gitlab/issue_templates/Feature%20Request.md) | Markdown | 4 | 0 | 4 | 8 |
| [fast_gicp/thirdparty/Eigen/.gitlab/merge_request_templates/Merge Request Template.md](/fast_gicp/thirdparty/Eigen/.gitlab/merge_request_templates/Merge%20Request%20Template.md) | Markdown | 3 | 20 | 4 | 27 |
| [fast_gicp/thirdparty/Eigen/CTestConfig.cmake](/fast_gicp/thirdparty/Eigen/CTestConfig.cmake) | CMake | 16 | 0 | 2 | 18 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Cholesky/LDLT.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Cholesky/LDLT.h) | C++ | 410 | 188 | 91 | 689 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Cholesky/LLT.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Cholesky/LLT.h) | C++ | 344 | 143 | 72 | 559 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Cholesky/LLT_LAPACKE.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Cholesky/LLT_LAPACKE.h) | C++ | 59 | 31 | 10 | 100 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/CholmodSupport/CholmodSupport.h](/fast_gicp/thirdparty/Eigen/Eigen/src/CholmodSupport/CholmodSupport.h) | C++ | 410 | 177 | 96 | 683 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/ArithmeticSequence.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/ArithmeticSequence.h) | C++ | 262 | 93 | 59 | 414 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Array.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Array.h) | C++ | 227 | 143 | 48 | 418 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/ArrayBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/ArrayBase.h) | C++ | 137 | 59 | 31 | 227 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/ArrayWrapper.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/ArrayWrapper.h) | C++ | 138 | 38 | 34 | 210 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Assign.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Assign.h) | C++ | 66 | 10 | 15 | 91 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/AssignEvaluator.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/AssignEvaluator.h) | C++ | 748 | 118 | 145 | 1,011 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Assign_MKL.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Assign_MKL.h) | C++ | 124 | 33 | 22 | 179 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/BandMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/BandMatrix.h) | C++ | 235 | 60 | 59 | 354 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Block.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Block.h) | C++ | 309 | 82 | 58 | 449 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/BooleanRedux.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/BooleanRedux.h) | C++ | 112 | 31 | 20 | 163 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/CommaInitializer.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/CommaInitializer.h) | C++ | 102 | 47 | 16 | 165 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/ConditionEstimator.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/ConditionEstimator.h) | C++ | 95 | 66 | 15 | 176 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/CoreEvaluators.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/CoreEvaluators.h) | C++ | 1,345 | 111 | 286 | 1,742 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/CoreIterators.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/CoreIterators.h) | C++ | 76 | 32 | 25 | 133 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/CwiseBinaryOp.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/CwiseBinaryOp.h) | C++ | 116 | 48 | 20 | 184 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/CwiseNullaryOp.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/CwiseNullaryOp.h) | C++ | 417 | 512 | 73 | 1,002 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/CwiseTernaryOp.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/CwiseTernaryOp.h) | C++ | 125 | 53 | 20 | 198 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/CwiseUnaryOp.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/CwiseUnaryOp.h) | C++ | 56 | 32 | 16 | 104 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/CwiseUnaryView.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/CwiseUnaryView.h) | C++ | 83 | 27 | 23 | 133 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/DenseBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/DenseBase.h) | C++ | 410 | 194 | 98 | 702 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/DenseCoeffsBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/DenseCoeffsBase.h) | C++ | 368 | 232 | 86 | 686 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/DenseStorage.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/DenseStorage.h) | C++ | 572 | 39 | 42 | 653 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Diagonal.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Diagonal.h) | C++ | 164 | 62 | 33 | 259 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/DiagonalMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/DiagonalMatrix.h) | C++ | 254 | 85 | 53 | 392 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/DiagonalProduct.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/DiagonalProduct.h) | C++ | 12 | 11 | 6 | 29 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Dot.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Dot.h) | C++ | 181 | 108 | 30 | 319 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/EigenBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/EigenBase.h) | C++ | 80 | 60 | 21 | 161 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/ForceAlignedAccess.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/ForceAlignedAccess.h) | C++ | 93 | 32 | 26 | 151 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Fuzzy.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Fuzzy.h) | C++ | 90 | 49 | 17 | 156 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/GeneralProduct.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/GeneralProduct.h) | C++ | 323 | 84 | 59 | 466 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/GenericPacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/GenericPacketMath.h) | C++ | 574 | 198 | 141 | 913 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/GlobalFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/GlobalFunctions.h) | C++ | 132 | 47 | 16 | 195 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/IO.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/IO.h) | C++ | 166 | 70 | 23 | 259 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/IndexedView.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/IndexedView.h) | C++ | 134 | 55 | 49 | 238 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Inverse.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Inverse.h) | C++ | 67 | 29 | 22 | 118 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Map.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Map.h) | C++ | 77 | 77 | 18 | 172 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/MapBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/MapBase.h) | C++ | 206 | 60 | 45 | 311 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/MathFunctions.h) | C++ | 1,604 | 161 | 291 | 2,056 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/MathFunctionsImpl.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/MathFunctionsImpl.h) | C++ | 104 | 74 | 23 | 201 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Matrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Matrix.h) | C++ | 240 | 270 | 56 | 566 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/MatrixBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/MatrixBase.h) | C++ | 351 | 103 | 94 | 548 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/NestByValue.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/NestByValue.h) | C++ | 45 | 24 | 17 | 86 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/NoAlias.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/NoAlias.h) | C++ | 46 | 51 | 13 | 110 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/NumTraits.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/NumTraits.h) | C++ | 224 | 67 | 45 | 336 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/PartialReduxEvaluator.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/PartialReduxEvaluator.h) | C++ | 151 | 46 | 36 | 233 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/PermutationMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/PermutationMatrix.h) | C++ | 372 | 149 | 85 | 606 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/PlainObjectBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/PlainObjectBase.h) | C++ | 758 | 259 | 112 | 1,129 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Product.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Product.h) | C++ | 127 | 26 | 39 | 192 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/ProductEvaluators.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/ProductEvaluators.h) | C++ | 863 | 143 | 174 | 1,180 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Random.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Random.h) | C++ | 63 | 139 | 17 | 219 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Redux.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Redux.h) | C++ | 370 | 82 | 64 | 516 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Ref.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Ref.h) | C++ | 222 | 111 | 49 | 382 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Replicate.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Replicate.h) | C++ | 85 | 42 | 16 | 143 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Reshaped.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Reshaped.h) | C++ | 310 | 73 | 72 | 455 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/ReturnByValue.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/ReturnByValue.h) | C++ | 74 | 26 | 20 | 120 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Reverse.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Reverse.h) | C++ | 135 | 54 | 29 | 218 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Select.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Select.h) | C++ | 104 | 40 | 21 | 165 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/SelfAdjointView.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/SelfAdjointView.h) | C++ | 212 | 102 | 52 | 366 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/SelfCwiseBinaryOp.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/SelfCwiseBinaryOp.h) | C++ | 29 | 9 | 10 | 48 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Solve.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Solve.h) | C++ | 125 | 28 | 36 | 189 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/SolveTriangular.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/SolveTriangular.h) | C++ | 168 | 20 | 48 | 236 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/SolverBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/SolverBase.h) | C++ | 94 | 48 | 27 | 169 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/StableNorm.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/StableNorm.h) | C++ | 180 | 42 | 30 | 252 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/StlIterators.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/StlIterators.h) | C++ | 339 | 32 | 93 | 464 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Stride.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Stride.h) | C++ | 53 | 51 | 13 | 117 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Swap.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Swap.h) | C++ | 46 | 10 | 13 | 69 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Transpose.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Transpose.h) | C++ | 286 | 120 | 59 | 465 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Transpositions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Transpositions.h) | C++ | 223 | 97 | 67 | 387 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/TriangularMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/TriangularMatrix.h) | C++ | 670 | 185 | 147 | 1,002 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/VectorBlock.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/VectorBlock.h) | C++ | 43 | 43 | 11 | 97 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/VectorwiseOp.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/VectorwiseOp.h) | C++ | 437 | 255 | 93 | 785 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/Visitor.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/Visitor.h) | C++ | 258 | 85 | 39 | 382 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX/Complex.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX/Complex.h) | C++ | 295 | 13 | 59 | 367 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX/MathFunctions.h) | C++ | 151 | 39 | 39 | 229 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX/PacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX/PacketMath.h) | C++ | 1,280 | 93 | 207 | 1,580 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX/TypeCasting.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX/TypeCasting.h) | C++ | 81 | 10 | 25 | 116 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX512/Complex.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX512/Complex.h) | C++ | 315 | 10 | 58 | 383 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX512/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX512/MathFunctions.h) | C++ | 236 | 55 | 72 | 363 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX512/PacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX512/PacketMath.h) | C++ | 1,964 | 85 | 263 | 2,312 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX512/TypeCasting.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AVX512/TypeCasting.h) | C++ | 63 | 8 | 19 | 90 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/Complex.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/Complex.h) | C++ | 320 | 25 | 67 | 412 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/MathFunctions.h) | C++ | 63 | 11 | 17 | 91 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/MatrixProduct.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/MatrixProduct.h) | C++ | 2,489 | 85 | 364 | 2,938 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/MatrixProductCommon.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/MatrixProductCommon.h) | C++ | 182 | 5 | 35 | 222 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/MatrixProductMMA.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/MatrixProductMMA.h) | C++ | 521 | 15 | 94 | 630 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/PacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/AltiVec/PacketMath.h) | C++ | 2,242 | 78 | 383 | 2,703 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/CUDA/Complex.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/CUDA/Complex.h) | C++ | 202 | 33 | 24 | 259 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/BFloat16.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/BFloat16.h) | C++ | 448 | 197 | 63 | 708 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/ConjHelper.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/ConjHelper.h) | C++ | 84 | 13 | 21 | 118 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/GenericPacketMathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/GenericPacketMathFunctions.h) | C++ | 931 | 566 | 173 | 1,670 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/GenericPacketMathFunctionsFwd.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/GenericPacketMathFunctionsFwd.h) | C++ | 58 | 35 | 24 | 117 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/Half.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/Half.h) | C++ | 700 | 139 | 104 | 943 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/Settings.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/Settings.h) | C++ | 15 | 25 | 10 | 50 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/TypeCasting.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/Default/TypeCasting.h) | C++ | 88 | 9 | 24 | 121 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/GPU/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/GPU/MathFunctions.h) | C++ | 72 | 11 | 21 | 104 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/GPU/PacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/GPU/PacketMath.h) | C++ | 1,461 | 28 | 197 | 1,686 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/GPU/TypeCasting.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/GPU/TypeCasting.h) | C++ | 54 | 10 | 17 | 81 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/HIP/hcc/math_constants.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/HIP/hcc/math_constants.h) | C++ | 12 | 6 | 6 | 24 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/MSA/Complex.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/MSA/Complex.h) | C++ | 488 | 28 | 130 | 646 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/MSA/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/MSA/MathFunctions.h) | C++ | 239 | 86 | 63 | 388 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/MSA/PacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/MSA/PacketMath.h) | C++ | 941 | 48 | 245 | 1,234 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/NEON/Complex.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/NEON/Complex.h) | C++ | 422 | 57 | 85 | 564 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/NEON/GeneralBlockPanelKernel.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/NEON/GeneralBlockPanelKernel.h) | C++ | 140 | 13 | 31 | 184 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/NEON/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/NEON/MathFunctions.h) | C++ | 49 | 8 | 19 | 76 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/NEON/PacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/NEON/PacketMath.h) | C++ | 4,063 | 120 | 405 | 4,588 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/NEON/TypeCasting.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/NEON/TypeCasting.h) | C++ | 1,222 | 80 | 118 | 1,420 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SSE/Complex.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SSE/Complex.h) | C++ | 269 | 21 | 54 | 344 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SSE/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SSE/MathFunctions.h) | C++ | 120 | 38 | 42 | 200 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SSE/PacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SSE/PacketMath.h) | C++ | 1,204 | 131 | 171 | 1,506 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SSE/TypeCasting.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SSE/TypeCasting.h) | C++ | 106 | 11 | 26 | 143 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SVE/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SVE/MathFunctions.h) | C++ | 27 | 9 | 9 | 45 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SVE/PacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SVE/PacketMath.h) | C++ | 603 | 35 | 115 | 753 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SVE/TypeCasting.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SVE/TypeCasting.h) | C++ | 31 | 8 | 11 | 50 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SYCL/InteropHeaders.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SYCL/InteropHeaders.h) | C++ | 181 | 28 | 24 | 233 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SYCL/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SYCL/MathFunctions.h) | C++ | 219 | 30 | 53 | 302 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SYCL/PacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SYCL/PacketMath.h) | C++ | 541 | 34 | 96 | 671 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SYCL/SyclMemoryModel.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SYCL/SyclMemoryModel.h) | C++ | 380 | 227 | 88 | 695 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SYCL/TypeCasting.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/SYCL/TypeCasting.h) | C++ | 52 | 19 | 15 | 86 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/ZVector/Complex.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/ZVector/Complex.h) | C++ | 329 | 21 | 67 | 417 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/ZVector/MathFunctions.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/ZVector/MathFunctions.h) | C++ | 159 | 26 | 49 | 234 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/ZVector/PacketMath.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/arch/ZVector/PacketMath.h) | C++ | 851 | 52 | 158 | 1,061 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/AssignmentFunctors.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/AssignmentFunctors.h) | C++ | 103 | 49 | 26 | 178 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/BinaryFunctors.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/BinaryFunctors.h) | C++ | 388 | 92 | 62 | 542 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/NullaryFunctors.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/NullaryFunctors.h) | C++ | 140 | 22 | 28 | 190 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/StlFunctors.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/StlFunctors.h) | C++ | 88 | 14 | 35 | 137 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/TernaryFunctors.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/TernaryFunctors.h) | C++ | 7 | 9 | 10 | 26 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/UnaryFunctors.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/functors/UnaryFunctors.h) | C++ | 778 | 277 | 77 | 1,132 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralBlockPanelKernel.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralBlockPanelKernel.h) | C++ | 1,971 | 367 | 308 | 2,646 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixMatrix.h) | C++ | 373 | 54 | 91 | 518 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixMatrixTriangular.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixMatrixTriangular.h) | C++ | 221 | 38 | 59 | 318 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixMatrixTriangular_BLAS.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixMatrixTriangular_BLAS.h) | C++ | 90 | 40 | 16 | 146 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixMatrix_BLAS.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixMatrix_BLAS.h) | C++ | 76 | 38 | 11 | 125 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixVector.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixVector.h) | C++ | 423 | 40 | 56 | 519 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixVector_BLAS.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/GeneralMatrixVector_BLAS.h) | C++ | 85 | 38 | 14 | 137 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/Parallelizer.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/Parallelizer.h) | C++ | 108 | 40 | 33 | 181 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointMatrixMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointMatrixMatrix.h) | C++ | 423 | 51 | 71 | 545 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointMatrixMatrix_BLAS.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointMatrixMatrix_BLAS.h) | C++ | 246 | 33 | 17 | 296 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointMatrixVector.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointMatrixVector.h) | C++ | 196 | 19 | 48 | 263 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointMatrixVector_BLAS.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointMatrixVector_BLAS.h) | C++ | 70 | 35 | 14 | 119 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointProduct.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointProduct.h) | C++ | 93 | 14 | 27 | 134 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointRank2Update.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/SelfadjointRank2Update.h) | C++ | 64 | 13 | 18 | 95 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularMatrixMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularMatrixMatrix.h) | C++ | 342 | 69 | 62 | 473 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularMatrixMatrix_BLAS.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularMatrixMatrix_BLAS.h) | C++ | 269 | 34 | 15 | 318 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularMatrixVector.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularMatrixVector.h) | C++ | 280 | 14 | 57 | 351 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularMatrixVector_BLAS.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularMatrixVector_BLAS.h) | C++ | 203 | 37 | 16 | 256 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularSolverMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularSolverMatrix.h) | C++ | 250 | 40 | 48 | 338 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularSolverMatrix_BLAS.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularSolverMatrix_BLAS.h) | C++ | 124 | 33 | 11 | 168 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularSolverVector.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/products/TriangularSolverVector.h) | C++ | 114 | 16 | 19 | 149 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/BlasUtil.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/BlasUtil.h) | C++ | 467 | 34 | 83 | 584 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/ConfigureVectorization.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/ConfigureVectorization.h) | C++ | 335 | 112 | 66 | 513 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/Constants.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/Constants.h) | C++ | 214 | 291 | 59 | 564 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/DisableStupidWarnings.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/DisableStupidWarnings.h) | C++ | 65 | 33 | 9 | 107 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/ForwardDeclarations.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/ForwardDeclarations.h) | C++ | 242 | 37 | 44 | 323 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/IndexedViewHelper.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/IndexedViewHelper.h) | C++ | 91 | 60 | 36 | 187 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/IntegralConstant.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/IntegralConstant.h) | C++ | 103 | 136 | 34 | 273 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/MKL_support.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/MKL_support.h) | C++ | 82 | 35 | 21 | 138 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/Macros.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/Macros.h) | C++ | 900 | 363 | 198 | 1,461 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/Memory.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/Memory.h) | C++ | 802 | 224 | 138 | 1,164 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/Meta.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/Meta.h) | C++ | 585 | 104 | 119 | 808 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/NonMPL2.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/NonMPL2.h) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/ReenableStupidWarnings.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/ReenableStupidWarnings.h) | C++ | 18 | 8 | 6 | 32 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/ReshapedHelper.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/ReshapedHelper.h) | C++ | 30 | 8 | 14 | 52 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/StaticAssert.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/StaticAssert.h) | C++ | 150 | 35 | 37 | 222 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/SymbolicIndex.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/SymbolicIndex.h) | C++ | 190 | 62 | 42 | 294 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/XprHelper.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Core/util/XprHelper.h) | C++ | 585 | 165 | 119 | 869 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/ComplexEigenSolver.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/ComplexEigenSolver.h) | C++ | 156 | 152 | 39 | 347 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/ComplexSchur.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/ComplexSchur.h) | C++ | 233 | 181 | 49 | 463 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/ComplexSchur_LAPACKE.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/ComplexSchur_LAPACKE.h) | C++ | 52 | 32 | 8 | 92 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/EigenSolver.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/EigenSolver.h) | C++ | 345 | 221 | 57 | 623 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/GeneralizedEigenSolver.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/GeneralizedEigenSolver.h) | C++ | 202 | 180 | 37 | 419 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/GeneralizedSelfAdjointEigenSolver.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/GeneralizedSelfAdjointEigenSolver.h) | C++ | 70 | 130 | 27 | 227 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/HessenbergDecomposition.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/HessenbergDecomposition.h) | C++ | 138 | 202 | 35 | 375 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/MatrixBaseEigenvalues.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/MatrixBaseEigenvalues.h) | C++ | 61 | 83 | 15 | 159 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/RealQZ.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/RealQZ.h) | C++ | 435 | 162 | 61 | 658 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/RealSchur.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/RealSchur.h) | C++ | 335 | 165 | 59 | 559 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/RealSchur_LAPACKE.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/RealSchur_LAPACKE.h) | C++ | 38 | 32 | 8 | 78 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/SelfAdjointEigenSolver.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/SelfAdjointEigenSolver.h) | C++ | 471 | 333 | 96 | 900 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/SelfAdjointEigenSolver_LAPACKE.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/SelfAdjointEigenSolver_LAPACKE.h) | C++ | 47 | 32 | 9 | 88 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/Tridiagonalization.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Eigenvalues/Tridiagonalization.h) | C++ | 242 | 271 | 49 | 562 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/AlignedBox.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/AlignedBox.h) | C++ | 242 | 181 | 64 | 487 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/AngleAxis.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/AngleAxis.h) | C++ | 126 | 84 | 38 | 248 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/EulerAngles.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/EulerAngles.h) | C++ | 65 | 38 | 12 | 115 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Homogeneous.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Homogeneous.h) | C++ | 359 | 82 | 61 | 502 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Hyperplane.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Hyperplane.h) | C++ | 144 | 105 | 34 | 283 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/OrthoMethods.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/OrthoMethods.h) | C++ | 152 | 59 | 25 | 236 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/ParametrizedLine.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/ParametrizedLine.h) | C++ | 125 | 73 | 35 | 233 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Quaternion.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Quaternion.h) | C++ | 475 | 272 | 124 | 871 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Rotation2D.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Rotation2D.h) | C++ | 94 | 69 | 37 | 200 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/RotationBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/RotationBase.h) | C++ | 115 | 61 | 31 | 207 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Scaling.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Scaling.h) | C++ | 93 | 66 | 30 | 189 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Transform.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Transform.h) | C++ | 950 | 448 | 166 | 1,564 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Translation.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Translation.h) | C++ | 113 | 60 | 30 | 203 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Umeyama.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/Umeyama.h) | C++ | 67 | 69 | 31 | 167 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/arch/Geometry_SIMD.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Geometry/arch/Geometry_SIMD.h) | C++ | 124 | 20 | 25 | 169 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Householder/BlockHouseholder.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Householder/BlockHouseholder.h) | C++ | 47 | 47 | 17 | 111 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Householder/Householder.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Householder/Householder.h) | C++ | 94 | 70 | 13 | 177 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Householder/HouseholderSequence.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Householder/HouseholderSequence.h) | C++ | 330 | 163 | 53 | 546 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/BasicPreconditioners.h](/fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/BasicPreconditioners.h) | C++ | 141 | 54 | 32 | 227 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/BiCGSTAB.h](/fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/BiCGSTAB.h) | C++ | 115 | 64 | 34 | 213 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/ConjugateGradient.h](/fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/ConjugateGradient.h) | C++ | 121 | 76 | 33 | 230 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/IncompleteCholesky.h](/fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/IncompleteCholesky.h) | C++ | 250 | 101 | 44 | 395 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/IncompleteLUT.h](/fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/IncompleteLUT.h) | C++ | 293 | 105 | 56 | 454 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/IterativeSolverBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/IterativeSolverBase.h) | C++ | 293 | 87 | 65 | 445 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/LeastSquareConjugateGradient.h](/fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/LeastSquareConjugateGradient.h) | C++ | 103 | 66 | 30 | 199 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/SolveWithGuess.h](/fast_gicp/thirdparty/Eigen/Eigen/src/IterativeLinearSolvers/SolveWithGuess.h) | C++ | 71 | 23 | 24 | 118 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/Jacobi/Jacobi.h](/fast_gicp/thirdparty/Eigen/Eigen/src/Jacobi/Jacobi.h) | C++ | 344 | 89 | 51 | 484 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/KLUSupport/KLUSupport.h](/fast_gicp/thirdparty/Eigen/Eigen/src/KLUSupport/KLUSupport.h) | C++ | 237 | 60 | 62 | 359 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/LU/Determinant.h](/fast_gicp/thirdparty/Eigen/Eigen/src/LU/Determinant.h) | C++ | 91 | 12 | 15 | 118 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/LU/FullPivLU.h](/fast_gicp/thirdparty/Eigen/Eigen/src/LU/FullPivLU.h) | C++ | 448 | 320 | 110 | 878 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/LU/InverseImpl.h](/fast_gicp/thirdparty/Eigen/Eigen/src/LU/InverseImpl.h) | C++ | 311 | 88 | 40 | 439 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/LU/PartialPivLU.h](/fast_gicp/thirdparty/Eigen/Eigen/src/LU/PartialPivLU.h) | C++ | 336 | 207 | 82 | 625 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/LU/PartialPivLU_LAPACKE.h](/fast_gicp/thirdparty/Eigen/Eigen/src/LU/PartialPivLU_LAPACKE.h) | C++ | 42 | 32 | 10 | 84 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/LU/arch/InverseSize4.h](/fast_gicp/thirdparty/Eigen/Eigen/src/LU/arch/InverseSize4.h) | C++ | 231 | 65 | 56 | 352 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/MetisSupport/MetisSupport.h](/fast_gicp/thirdparty/Eigen/Eigen/src/MetisSupport/MetisSupport.h) | C++ | 94 | 31 | 13 | 138 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/OrderingMethods/Amd.h](/fast_gicp/thirdparty/Eigen/Eigen/src/OrderingMethods/Amd.h) | C++ | 365 | 40 | 31 | 436 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/OrderingMethods/Eigen_Colamd.h](/fast_gicp/thirdparty/Eigen/Eigen/src/OrderingMethods/Eigen_Colamd.h) | C++ | 1,087 | 481 | 296 | 1,864 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/OrderingMethods/Ordering.h](/fast_gicp/thirdparty/Eigen/Eigen/src/OrderingMethods/Ordering.h) | C++ | 77 | 54 | 23 | 154 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/PaStiXSupport/PaStiXSupport.h](/fast_gicp/thirdparty/Eigen/Eigen/src/PaStiXSupport/PaStiXSupport.h) | C++ | 440 | 151 | 88 | 679 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/PardisoSupport/PardisoSupport.h](/fast_gicp/thirdparty/Eigen/Eigen/src/PardisoSupport/PardisoSupport.h) | C++ | 354 | 121 | 71 | 546 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/QR/ColPivHouseholderQR.h](/fast_gicp/thirdparty/Eigen/Eigen/src/QR/ColPivHouseholderQR.h) | C++ | 357 | 232 | 86 | 675 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/QR/ColPivHouseholderQR_LAPACKE.h](/fast_gicp/thirdparty/Eigen/Eigen/src/QR/ColPivHouseholderQR_LAPACKE.h) | C++ | 56 | 33 | 9 | 98 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/QR/CompleteOrthogonalDecomposition.h](/fast_gicp/thirdparty/Eigen/Eigen/src/QR/CompleteOrthogonalDecomposition.h) | C++ | 302 | 261 | 73 | 636 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/QR/FullPivHouseholderQR.h](/fast_gicp/thirdparty/Eigen/Eigen/src/QR/FullPivHouseholderQR.h) | C++ | 407 | 216 | 91 | 714 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/QR/HouseholderQR.h](/fast_gicp/thirdparty/Eigen/Eigen/src/QR/HouseholderQR.h) | C++ | 227 | 143 | 65 | 435 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/QR/HouseholderQR_LAPACKE.h](/fast_gicp/thirdparty/Eigen/Eigen/src/QR/HouseholderQR_LAPACKE.h) | C++ | 26 | 33 | 10 | 69 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SPQRSupport/SuiteSparseQRSupport.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SPQRSupport/SuiteSparseQRSupport.h) | C++ | 239 | 69 | 28 | 336 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SVD/BDCSVD.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SVD/BDCSVD.h) | C++ | 998 | 222 | 147 | 1,367 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SVD/JacobiSVD.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SVD/JacobiSVD.h) | C++ | 582 | 146 | 85 | 813 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SVD/JacobiSVD_LAPACKE.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SVD/JacobiSVD_LAPACKE.h) | C++ | 51 | 32 | 9 | 92 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SVD/SVDBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SVD/SVDBase.h) | C++ | 207 | 126 | 44 | 377 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SVD/UpperBidiagonalization.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SVD/UpperBidiagonalization.h) | C++ | 269 | 84 | 62 | 415 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCholesky/SimplicialCholesky.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCholesky/SimplicialCholesky.h) | C++ | 466 | 145 | 87 | 698 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCholesky/SimplicialCholesky_impl.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCholesky/SimplicialCholesky_impl.h) | C++ | 127 | 24 | 24 | 175 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/AmbiVector.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/AmbiVector.h) | C++ | 300 | 40 | 39 | 379 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/CompressedStorage.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/CompressedStorage.h) | C++ | 209 | 27 | 39 | 275 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/ConservativeSparseSparseProduct.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/ConservativeSparseSparseProduct.h) | C++ | 275 | 31 | 47 | 353 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/MappedSparseMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/MappedSparseMatrix.h) | C++ | 34 | 19 | 15 | 68 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseAssign.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseAssign.h) | C++ | 204 | 21 | 46 | 271 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseBlock.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseBlock.h) | C++ | 427 | 42 | 103 | 572 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseColEtree.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseColEtree.h) | C++ | 123 | 64 | 20 | 207 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseCompressedBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseCompressedBase.h) | C++ | 242 | 68 | 61 | 371 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseCwiseBinaryOp.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseCwiseBinaryOp.h) | C++ | 571 | 43 | 109 | 723 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseCwiseUnaryOp.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseCwiseUnaryOp.h) | C++ | 111 | 8 | 32 | 151 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseDenseProduct.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseDenseProduct.h) | C++ | 264 | 28 | 51 | 343 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseDiagonalProduct.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseDiagonalProduct.h) | C++ | 90 | 19 | 30 | 139 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseDot.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseDot.h) | C++ | 76 | 8 | 15 | 99 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseFuzzy.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseFuzzy.h) | C++ | 15 | 8 | 7 | 30 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseMap.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseMap.h) | C++ | 194 | 67 | 45 | 306 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseMatrix.h) | C++ | 1,029 | 329 | 162 | 1,520 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseMatrixBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseMatrixBase.h) | C++ | 241 | 81 | 77 | 399 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparsePermutation.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparsePermutation.h) | C++ | 128 | 20 | 31 | 179 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseProduct.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseProduct.h) | C++ | 126 | 31 | 25 | 182 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseRedux.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseRedux.h) | C++ | 34 | 8 | 8 | 50 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseRef.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseRef.h) | C++ | 300 | 35 | 63 | 398 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseSelfAdjointView.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseSelfAdjointView.h) | C++ | 482 | 77 | 101 | 660 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseSolverBase.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseSolverBase.h) | C++ | 75 | 32 | 18 | 125 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseSparseProductWithPruning.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseSparseProductWithPruning.h) | C++ | 141 | 31 | 27 | 199 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseTranspose.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseTranspose.h) | C++ | 65 | 8 | 20 | 93 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseTriangularView.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseTriangularView.h) | C++ | 134 | 23 | 33 | 190 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseUtil.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseUtil.h) | C++ | 128 | 21 | 38 | 187 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseVector.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseVector.h) | C++ | 332 | 68 | 79 | 479 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseView.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/SparseView.h) | C++ | 157 | 56 | 42 | 255 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/TriangularSolver.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseCore/TriangularSolver.h) | C++ | 254 | 28 | 34 | 316 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU.h) | C++ | 569 | 251 | 104 | 924 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLUImpl.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLUImpl.h) | C++ | 47 | 12 | 8 | 67 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_Memory.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_Memory.h) | C++ | 132 | 68 | 27 | 227 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_Structs.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_Structs.h) | C++ | 34 | 69 | 8 | 111 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_SupernodalMatrix.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_SupernodalMatrix.h) | C++ | 249 | 78 | 49 | 376 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_Utils.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_Utils.h) | C++ | 49 | 20 | 12 | 81 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_column_bmod.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_column_bmod.h) | C++ | 89 | 70 | 23 | 182 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_column_dfs.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_column_dfs.h) | C++ | 88 | 67 | 25 | 180 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_copy_to_ucol.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_copy_to_ucol.h) | C++ | 53 | 43 | 12 | 108 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_gemm_kernel.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_gemm_kernel.h) | C++ | 216 | 29 | 36 | 281 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_heap_relax_snode.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_heap_relax_snode.h) | C++ | 72 | 44 | 11 | 127 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_kernel_bmod.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_kernel_bmod.h) | C++ | 86 | 30 | 15 | 131 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_panel_bmod.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_panel_bmod.h) | C++ | 132 | 62 | 30 | 224 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_panel_dfs.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_panel_dfs.h) | C++ | 137 | 86 | 36 | 259 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_pivotL.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_pivotL.h) | C++ | 63 | 62 | 13 | 138 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_pruneL.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_pruneL.h) | C++ | 66 | 58 | 13 | 137 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_relax_snode.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseLU/SparseLU_relax_snode.h) | C++ | 34 | 40 | 10 | 84 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SparseQR/SparseQR.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SparseQR/SparseQR.h) | C++ | 479 | 195 | 85 | 759 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/StlSupport/StdDeque.h](/fast_gicp/thirdparty/Eigen/Eigen/src/StlSupport/StdDeque.h) | C++ | 88 | 17 | 12 | 117 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/StlSupport/StdList.h](/fast_gicp/thirdparty/Eigen/Eigen/src/StlSupport/StdList.h) | C++ | 79 | 15 | 13 | 107 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/StlSupport/StdVector.h](/fast_gicp/thirdparty/Eigen/Eigen/src/StlSupport/StdVector.h) | C++ | 99 | 21 | 12 | 132 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/StlSupport/details.h](/fast_gicp/thirdparty/Eigen/Eigen/src/StlSupport/details.h) | C++ | 57 | 13 | 15 | 85 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/SuperLUSupport/SuperLUSupport.h](/fast_gicp/thirdparty/Eigen/Eigen/src/SuperLUSupport/SuperLUSupport.h) | C++ | 750 | 117 | 159 | 1,026 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/UmfPackSupport/UmfPackSupport.h](/fast_gicp/thirdparty/Eigen/Eigen/src/UmfPackSupport/UmfPackSupport.h) | C++ | 439 | 94 | 110 | 643 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/misc/Image.h](/fast_gicp/thirdparty/Eigen/Eigen/src/misc/Image.h) | C++ | 57 | 12 | 14 | 83 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/misc/Kernel.h](/fast_gicp/thirdparty/Eigen/Eigen/src/misc/Kernel.h) | C++ | 52 | 14 | 14 | 80 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/misc/RealSvd2x2.h](/fast_gicp/thirdparty/Eigen/Eigen/src/misc/RealSvd2x2.h) | C++ | 36 | 11 | 9 | 56 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/misc/blas.h](/fast_gicp/thirdparty/Eigen/Eigen/src/misc/blas.h) | C++ | 370 | 2 | 69 | 441 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/misc/lapack.h](/fast_gicp/thirdparty/Eigen/Eigen/src/misc/lapack.h) | C++ | 128 | 0 | 25 | 153 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/misc/lapacke.h](/fast_gicp/thirdparty/Eigen/Eigen/src/misc/lapacke.h) | C++ | 15,567 | 64 | 662 | 16,293 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/misc/lapacke_mangling.h](/fast_gicp/thirdparty/Eigen/Eigen/src/misc/lapacke_mangling.h) | C++ | 14 | 0 | 4 | 18 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/plugins/ArrayCwiseBinaryOps.h](/fast_gicp/thirdparty/Eigen/Eigen/src/plugins/ArrayCwiseBinaryOps.h) | C++ | 147 | 181 | 31 | 359 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/plugins/ArrayCwiseUnaryOps.h](/fast_gicp/thirdparty/Eigen/Eigen/src/plugins/ArrayCwiseUnaryOps.h) | C++ | 293 | 315 | 50 | 658 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/plugins/BlockMethods.h](/fast_gicp/thirdparty/Eigen/Eigen/src/plugins/BlockMethods.h) | C++ | 697 | 637 | 109 | 1,443 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/plugins/CommonCwiseBinaryOps.h](/fast_gicp/thirdparty/Eigen/Eigen/src/plugins/CommonCwiseBinaryOps.h) | C++ | 41 | 63 | 12 | 116 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/plugins/CommonCwiseUnaryOps.h](/fast_gicp/thirdparty/Eigen/Eigen/src/plugins/CommonCwiseUnaryOps.h) | C++ | 100 | 98 | 23 | 221 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/plugins/IndexedViewMethods.h](/fast_gicp/thirdparty/Eigen/Eigen/src/plugins/IndexedViewMethods.h) | C++ | 167 | 53 | 43 | 263 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/plugins/MatrixCwiseBinaryOps.h](/fast_gicp/thirdparty/Eigen/Eigen/src/plugins/MatrixCwiseBinaryOps.h) | C++ | 61 | 79 | 13 | 153 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/plugins/MatrixCwiseUnaryOps.h](/fast_gicp/thirdparty/Eigen/Eigen/src/plugins/MatrixCwiseUnaryOps.h) | C++ | 30 | 54 | 12 | 96 |
| [fast_gicp/thirdparty/Eigen/Eigen/src/plugins/ReshapedMethods.h](/fast_gicp/thirdparty/Eigen/Eigen/src/plugins/ReshapedMethods.h) | C++ | 79 | 51 | 20 | 150 |
| [fast_gicp/thirdparty/Eigen/README.md](/fast_gicp/thirdparty/Eigen/README.md) | Markdown | 3 | 0 | 3 | 6 |
| [fast_gicp/thirdparty/Eigen/bench/BenchSparseUtil.h](/fast_gicp/thirdparty/Eigen/bench/BenchSparseUtil.h) | C++ | 129 | 2 | 19 | 150 |
| [fast_gicp/thirdparty/Eigen/bench/BenchTimer.h](/fast_gicp/thirdparty/Eigen/bench/BenchTimer.h) | C++ | 150 | 25 | 25 | 200 |
| [fast_gicp/thirdparty/Eigen/bench/BenchUtil.h](/fast_gicp/thirdparty/Eigen/bench/BenchUtil.h) | C++ | 80 | 0 | 13 | 93 |
| [fast_gicp/thirdparty/Eigen/bench/analyze-blocking-sizes.cpp](/fast_gicp/thirdparty/Eigen/bench/analyze-blocking-sizes.cpp) | C++ | 786 | 14 | 77 | 877 |
| [fast_gicp/thirdparty/Eigen/bench/basicbenchmark.cpp](/fast_gicp/thirdparty/Eigen/bench/basicbenchmark.cpp) | C++ | 23 | 3 | 10 | 36 |
| [fast_gicp/thirdparty/Eigen/bench/basicbenchmark.h](/fast_gicp/thirdparty/Eigen/bench/basicbenchmark.h) | C++ | 53 | 0 | 11 | 64 |
| [fast_gicp/thirdparty/Eigen/bench/benchBlasGemm.cpp](/fast_gicp/thirdparty/Eigen/bench/benchBlasGemm.cpp) | C++ | 175 | 13 | 32 | 220 |
| [fast_gicp/thirdparty/Eigen/bench/benchCholesky.cpp](/fast_gicp/thirdparty/Eigen/bench/benchCholesky.cpp) | C++ | 106 | 12 | 24 | 142 |
| [fast_gicp/thirdparty/Eigen/bench/benchEigenSolver.cpp](/fast_gicp/thirdparty/Eigen/bench/benchEigenSolver.cpp) | C++ | 162 | 21 | 30 | 213 |
| [fast_gicp/thirdparty/Eigen/bench/benchFFT.cpp](/fast_gicp/thirdparty/Eigen/bench/benchFFT.cpp) | C++ | 86 | 8 | 22 | 116 |
| [fast_gicp/thirdparty/Eigen/bench/benchGeometry.cpp](/fast_gicp/thirdparty/Eigen/bench/benchGeometry.cpp) | C++ | 116 | 0 | 19 | 135 |
| [fast_gicp/thirdparty/Eigen/bench/benchVecAdd.cpp](/fast_gicp/thirdparty/Eigen/bench/benchVecAdd.cpp) | C++ | 92 | 28 | 16 | 136 |
| [fast_gicp/thirdparty/Eigen/bench/bench_gemm.cpp](/fast_gicp/thirdparty/Eigen/bench/bench_gemm.cpp) | C++ | 308 | 13 | 55 | 376 |
| [fast_gicp/thirdparty/Eigen/bench/bench_move_semantics.cpp](/fast_gicp/thirdparty/Eigen/bench/bench_move_semantics.cpp) | C++ | 37 | 8 | 13 | 58 |
| [fast_gicp/thirdparty/Eigen/bench/bench_multi_compilers.sh](/fast_gicp/thirdparty/Eigen/bench/bench_multi_compilers.sh) | Shell Script | 18 | 5 | 6 | 29 |
| [fast_gicp/thirdparty/Eigen/bench/bench_norm.cpp](/fast_gicp/thirdparty/Eigen/bench/bench_norm.cpp) | C++ | 303 | 18 | 40 | 361 |
| [fast_gicp/thirdparty/Eigen/bench/bench_reverse.cpp](/fast_gicp/thirdparty/Eigen/bench/bench_reverse.cpp) | C++ | 59 | 13 | 13 | 85 |
| [fast_gicp/thirdparty/Eigen/bench/bench_sum.cpp](/fast_gicp/thirdparty/Eigen/bench/bench_sum.cpp) | C++ | 17 | 0 | 2 | 19 |
| [fast_gicp/thirdparty/Eigen/bench/benchmark-blocking-sizes.cpp](/fast_gicp/thirdparty/Eigen/bench/benchmark-blocking-sizes.cpp) | C++ | 522 | 61 | 95 | 678 |
| [fast_gicp/thirdparty/Eigen/bench/benchmark.cpp](/fast_gicp/thirdparty/Eigen/bench/benchmark.cpp) | C++ | 31 | 1 | 8 | 40 |
| [fast_gicp/thirdparty/Eigen/bench/benchmarkSlice.cpp](/fast_gicp/thirdparty/Eigen/bench/benchmarkSlice.cpp) | C++ | 30 | 1 | 8 | 39 |
| [fast_gicp/thirdparty/Eigen/bench/benchmarkX.cpp](/fast_gicp/thirdparty/Eigen/bench/benchmarkX.cpp) | C++ | 28 | 1 | 8 | 37 |
| [fast_gicp/thirdparty/Eigen/bench/benchmarkXcwise.cpp](/fast_gicp/thirdparty/Eigen/bench/benchmarkXcwise.cpp) | C++ | 28 | 1 | 7 | 36 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_aat_product.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_aat_product.hh) | C++ | 71 | 27 | 48 | 146 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_ata_product.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_ata_product.hh) | C++ | 71 | 27 | 48 | 146 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_atv_product.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_atv_product.hh) | C++ | 79 | 22 | 34 | 135 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_axpby.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_axpby.hh) | C++ | 75 | 26 | 27 | 128 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_axpy.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_axpy.hh) | C++ | 74 | 27 | 39 | 140 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_cholesky.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_cholesky.hh) | C++ | 65 | 36 | 28 | 129 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_ger.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_ger.hh) | C++ | 81 | 21 | 27 | 129 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_hessenberg.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_hessenberg.hh) | C++ | 126 | 52 | 56 | 234 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_lu_decomp.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_lu_decomp.hh) | C++ | 61 | 35 | 29 | 125 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_lu_solve.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_lu_solve.hh) | C++ | 65 | 29 | 43 | 137 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_matrix_matrix_product.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_matrix_matrix_product.hh) | C++ | 82 | 27 | 42 | 151 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_matrix_matrix_product_bis.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_matrix_matrix_product_bis.hh) | C++ | 77 | 27 | 49 | 153 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_matrix_vector_product.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_matrix_vector_product.hh) | C++ | 81 | 27 | 46 | 154 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_partial_lu.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_partial_lu.hh) | C++ | 60 | 37 | 29 | 126 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_rot.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_rot.hh) | C++ | 63 | 28 | 26 | 117 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_symv.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_symv.hh) | C++ | 81 | 26 | 33 | 140 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_syr2.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_syr2.hh) | C++ | 79 | 27 | 28 | 134 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_trisolve.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_trisolve.hh) | C++ | 80 | 27 | 31 | 138 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_trisolve_matrix.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_trisolve_matrix.hh) | C++ | 84 | 38 | 44 | 166 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/action_trmm.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/action_trmm.hh) | C++ | 84 | 38 | 44 | 166 |
| [fast_gicp/thirdparty/Eigen/bench/btl/actions/basic_actions.hh](/fast_gicp/thirdparty/Eigen/bench/btl/actions/basic_actions.hh) | C++ | 13 | 2 | 7 | 22 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindACML.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindACML.cmake) | CMake | 42 | 0 | 10 | 52 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindATLAS.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindATLAS.cmake) | CMake | 21 | 0 | 11 | 32 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindBLAZE.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindBLAZE.cmake) | CMake | 23 | 0 | 9 | 32 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindBlitz.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindBlitz.cmake) | CMake | 33 | 0 | 8 | 41 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindCBLAS.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindCBLAS.cmake) | CMake | 29 | 0 | 7 | 36 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindGMM.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindGMM.cmake) | CMake | 13 | 0 | 5 | 18 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindMKL.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindMKL.cmake) | CMake | 51 | 0 | 15 | 66 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindMTL4.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindMTL4.cmake) | CMake | 23 | 0 | 9 | 32 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindOPENBLAS.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindOPENBLAS.cmake) | CMake | 12 | 0 | 6 | 18 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindPackageHandleStandardArgs.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindPackageHandleStandardArgs.cmake) | CMake | 54 | 0 | 7 | 61 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindTvmet.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/FindTvmet.cmake) | CMake | 24 | 0 | 9 | 33 |
| [fast_gicp/thirdparty/Eigen/bench/btl/cmake/MacroOptionalAddSubdirectory.cmake](/fast_gicp/thirdparty/Eigen/bench/btl/cmake/MacroOptionalAddSubdirectory.cmake) | CMake | 28 | 0 | 4 | 32 |
| [fast_gicp/thirdparty/Eigen/bench/btl/data/gnuplot_common_settings.hh](/fast_gicp/thirdparty/Eigen/bench/btl/data/gnuplot_common_settings.hh) | C++ | 86 | 0 | 2 | 88 |
| [fast_gicp/thirdparty/Eigen/bench/btl/data/mean.cxx](/fast_gicp/thirdparty/Eigen/bench/btl/data/mean.cxx) | C++ | 110 | 20 | 53 | 183 |
| [fast_gicp/thirdparty/Eigen/bench/btl/data/mk_gnuplot_script.sh](/fast_gicp/thirdparty/Eigen/bench/btl/data/mk_gnuplot_script.sh) | Shell Script | 49 | 3 | 17 | 69 |
| [fast_gicp/thirdparty/Eigen/bench/btl/data/mk_mean_script.sh](/fast_gicp/thirdparty/Eigen/bench/btl/data/mk_mean_script.sh) | Shell Script | 29 | 5 | 19 | 53 |
| [fast_gicp/thirdparty/Eigen/bench/btl/data/mk_new_gnuplot.sh](/fast_gicp/thirdparty/Eigen/bench/btl/data/mk_new_gnuplot.sh) | Shell Script | 34 | 5 | 16 | 55 |
| [fast_gicp/thirdparty/Eigen/bench/btl/data/regularize.cxx](/fast_gicp/thirdparty/Eigen/bench/btl/data/regularize.cxx) | C++ | 70 | 24 | 38 | 132 |
| [fast_gicp/thirdparty/Eigen/bench/btl/data/smooth.cxx](/fast_gicp/thirdparty/Eigen/bench/btl/data/smooth.cxx) | C++ | 98 | 28 | 73 | 199 |
| [fast_gicp/thirdparty/Eigen/bench/btl/data/smooth_all.sh](/fast_gicp/thirdparty/Eigen/bench/btl/data/smooth_all.sh) | Shell Script | 56 | 2 | 11 | 69 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/bench.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/bench.hh) | C++ | 111 | 35 | 23 | 169 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/bench_parameter.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/bench_parameter.hh) | C++ | 17 | 33 | 4 | 54 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/btl.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/btl.hh) | C++ | 188 | 27 | 28 | 243 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/init/init_function.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/init/init_function.hh) | C++ | 27 | 19 | 9 | 55 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/init/init_matrix.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/init/init_matrix.hh) | C++ | 30 | 27 | 8 | 65 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/init/init_vector.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/init/init_vector.hh) | C++ | 10 | 23 | 5 | 38 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/static/bench_static.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/static/bench_static.hh) | C++ | 29 | 24 | 28 | 81 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/static/intel_bench_fixed_size.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/static/intel_bench_fixed_size.hh) | C++ | 27 | 21 | 19 | 67 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/static/static_size_generator.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/static/static_size_generator.hh) | C++ | 26 | 21 | 11 | 58 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/STL_perf_analyzer.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/STL_perf_analyzer.hh) | C++ | 40 | 21 | 22 | 83 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/STL_timer.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/STL_timer.hh) | C++ | 45 | 31 | 3 | 79 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/mixed_perf_analyzer.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/mixed_perf_analyzer.hh) | C++ | 36 | 20 | 18 | 74 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/portable_perf_analyzer.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/portable_perf_analyzer.hh) | C++ | 64 | 25 | 15 | 104 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/portable_perf_analyzer_old.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/portable_perf_analyzer_old.hh) | C++ | 66 | 40 | 29 | 135 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/portable_timer.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/portable_timer.hh) | C++ | 106 | 27 | 55 | 188 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/x86_perf_analyzer.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/x86_perf_analyzer.hh) | C++ | 55 | 25 | 29 | 109 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/x86_timer.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/timers/x86_timer.hh) | C++ | 137 | 27 | 83 | 247 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/utils/size_lin_log.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/utils/size_lin_log.hh) | C++ | 26 | 22 | 23 | 71 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/utils/size_log.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/utils/size_log.hh) | C++ | 19 | 23 | 13 | 55 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/utils/utilities.h](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/utils/utilities.h) | C++ | 55 | 13 | 23 | 91 |
| [fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/utils/xy_file.hh](/fast_gicp/thirdparty/Eigen/bench/btl/generic_bench/utils/xy_file.hh) | C++ | 39 | 23 | 14 | 76 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/BLAS/blas.h](/fast_gicp/thirdparty/Eigen/bench/btl/libs/BLAS/blas.h) | C++ | 592 | 2 | 82 | 676 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/BLAS/blas_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/BLAS/blas_interface.hh) | C++ | 39 | 26 | 19 | 84 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/BLAS/blas_interface_impl.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/BLAS/blas_interface_impl.hh) | C++ | 116 | 0 | 32 | 148 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/BLAS/c_interface_base.h](/fast_gicp/thirdparty/Eigen/bench/btl/libs/BLAS/c_interface_base.h) | C++ | 57 | 0 | 17 | 74 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/BLAS/main.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/BLAS/main.cpp) | C++ | 36 | 21 | 17 | 74 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/STL/STL_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/STL/STL_interface.hh) | C++ | 187 | 19 | 39 | 245 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/STL/main.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/STL/main.cpp) | C++ | 18 | 19 | 6 | 43 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/blaze/blaze_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/blaze/blaze_interface.hh) | C++ | 81 | 30 | 31 | 142 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/blaze/main.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/blaze/main.cpp) | C++ | 16 | 17 | 8 | 41 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/blitz/blitz_LU_solve_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/blitz/blitz_LU_solve_interface.hh) | C++ | 114 | 39 | 40 | 193 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/blitz/blitz_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/blitz/blitz_interface.hh) | C++ | 93 | 30 | 25 | 148 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/blitz/btl_blitz.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/blitz/btl_blitz.cpp) | C++ | 22 | 20 | 10 | 52 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/blitz/btl_tiny_blitz.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/blitz/btl_tiny_blitz.cpp) | C++ | 14 | 19 | 6 | 39 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/blitz/tiny_blitz_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/blitz/tiny_blitz_interface.hh) | C++ | 64 | 19 | 24 | 107 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/btl_tiny_eigen2.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/btl_tiny_eigen2.cpp) | C++ | 23 | 17 | 7 | 47 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/eigen2_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/eigen2_interface.hh) | C++ | 109 | 22 | 38 | 169 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/main_adv.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/main_adv.cpp) | C++ | 19 | 19 | 7 | 45 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/main_linear.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/main_linear.cpp) | C++ | 11 | 17 | 7 | 35 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/main_matmat.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/main_matmat.cpp) | C++ | 11 | 19 | 6 | 36 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/main_vecmat.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen2/main_vecmat.cpp) | C++ | 11 | 20 | 6 | 37 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/btl_tiny_eigen3.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/btl_tiny_eigen3.cpp) | C++ | 23 | 17 | 7 | 47 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/eigen3_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/eigen3_interface.hh) | C++ | 164 | 30 | 49 | 243 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/main_adv.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/main_adv.cpp) | C++ | 19 | 19 | 7 | 45 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/main_linear.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/main_linear.cpp) | C++ | 12 | 17 | 7 | 36 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/main_matmat.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/main_matmat.cpp) | C++ | 13 | 17 | 6 | 36 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/main_vecmat.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/eigen3/main_vecmat.cpp) | C++ | 14 | 17 | 6 | 37 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/gmm/gmm_LU_solve_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/gmm/gmm_LU_solve_interface.hh) | C++ | 114 | 39 | 40 | 193 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/gmm/gmm_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/gmm/gmm_interface.hh) | C++ | 95 | 17 | 33 | 145 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/gmm/main.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/gmm/main.cpp) | C++ | 20 | 20 | 12 | 52 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/mtl4/main.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/mtl4/main.cpp) | C++ | 16 | 22 | 9 | 47 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/mtl4/mtl4_LU_solve_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/mtl4/mtl4_LU_solve_interface.hh) | C++ | 114 | 39 | 40 | 193 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/mtl4/mtl4_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/mtl4/mtl4_interface.hh) | C++ | 81 | 33 | 31 | 145 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/tensors/main_linear.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/tensors/main_linear.cpp) | C++ | 11 | 8 | 5 | 24 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/tensors/main_matmat.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/tensors/main_matmat.cpp) | C++ | 10 | 8 | 4 | 22 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/tensors/main_vecmat.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/tensors/main_vecmat.cpp) | C++ | 10 | 8 | 4 | 22 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/tensors/tensor_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/tensors/tensor_interface.hh) | C++ | 74 | 8 | 24 | 106 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/tvmet/main.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/tvmet/main.cpp) | C++ | 16 | 19 | 6 | 41 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/tvmet/tvmet_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/tvmet/tvmet_interface.hh) | C++ | 60 | 19 | 26 | 105 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/ublas/main.cpp](/fast_gicp/thirdparty/Eigen/bench/btl/libs/ublas/main.cpp) | C++ | 15 | 21 | 9 | 45 |
| [fast_gicp/thirdparty/Eigen/bench/btl/libs/ublas/ublas_interface.hh](/fast_gicp/thirdparty/Eigen/bench/btl/libs/ublas/ublas_interface.hh) | C++ | 89 | 22 | 31 | 142 |
| [fast_gicp/thirdparty/Eigen/bench/check_cache_queries.cpp](/fast_gicp/thirdparty/Eigen/bench/check_cache_queries.cpp) | C++ | 85 | 3 | 14 | 102 |
| [fast_gicp/thirdparty/Eigen/bench/dense_solvers.cpp](/fast_gicp/thirdparty/Eigen/bench/dense_solvers.cpp) | C++ | 153 | 13 | 21 | 187 |
| [fast_gicp/thirdparty/Eigen/bench/eig33.cpp](/fast_gicp/thirdparty/Eigen/bench/eig33.cpp) | C++ | 86 | 85 | 25 | 196 |
| [fast_gicp/thirdparty/Eigen/bench/geometry.cpp](/fast_gicp/thirdparty/Eigen/bench/geometry.cpp) | C++ | 107 | 0 | 20 | 127 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/gemm.cpp](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/gemm.cpp) | C++ | 10 | 0 | 3 | 13 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/gemm_common.h](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/gemm_common.h) | C++ | 53 | 1 | 14 | 68 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/gemv.cpp](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/gemv.cpp) | C++ | 10 | 0 | 3 | 13 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/gemv_common.h](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/gemv_common.h) | C++ | 55 | 1 | 14 | 70 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/gemvt.cpp](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/gemvt.cpp) | C++ | 10 | 0 | 3 | 13 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/lazy_gemm.cpp](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/lazy_gemm.cpp) | C++ | 81 | 4 | 17 | 102 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/llt.cpp](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/llt.cpp) | C++ | 13 | 0 | 3 | 16 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/make_plot.sh](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/make_plot.sh) | Shell Script | 78 | 16 | 19 | 113 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/chart_footer.html](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/chart_footer.html) | HTML | 35 | 0 | 7 | 42 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/chart_header.html](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/chart_header.html) | HTML | 44 | 0 | 2 | 46 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/footer.html](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/footer.html) | HTML | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/header.html](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/header.html) | HTML | 37 | 0 | 6 | 43 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/s1.js](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/s1.js) | JavaScript | 1 | 1 | 0 | 2 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/s2.js](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/resources/s2.js) | JavaScript | 1 | 0 | 0 | 1 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/run.sh](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/run.sh) | Shell Script | 134 | 17 | 33 | 184 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/runall.sh](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/runall.sh) | Shell Script | 45 | 11 | 17 | 73 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/trmv_lo.cpp](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/trmv_lo.cpp) | C++ | 10 | 0 | 3 | 13 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/trmv_lot.cpp](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/trmv_lot.cpp) | C++ | 10 | 0 | 3 | 13 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/trmv_up.cpp](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/trmv_up.cpp) | C++ | 10 | 0 | 3 | 13 |
| [fast_gicp/thirdparty/Eigen/bench/perf_monitoring/trmv_upt.cpp](/fast_gicp/thirdparty/Eigen/bench/perf_monitoring/trmv_upt.cpp) | C++ | 10 | 0 | 3 | 13 |
| [fast_gicp/thirdparty/Eigen/bench/product_threshold.cpp](/fast_gicp/thirdparty/Eigen/bench/product_threshold.cpp) | C++ | 115 | 0 | 29 | 144 |
| [fast_gicp/thirdparty/Eigen/bench/quat_slerp.cpp](/fast_gicp/thirdparty/Eigen/bench/quat_slerp.cpp) | C++ | 189 | 14 | 45 | 248 |
| [fast_gicp/thirdparty/Eigen/bench/quatmul.cpp](/fast_gicp/thirdparty/Eigen/bench/quatmul.cpp) | C++ | 35 | 0 | 13 | 48 |
| [fast_gicp/thirdparty/Eigen/bench/sparse_cholesky.cpp](/fast_gicp/thirdparty/Eigen/bench/sparse_cholesky.cpp) | C++ | 142 | 29 | 46 | 217 |
| [fast_gicp/thirdparty/Eigen/bench/sparse_dense_product.cpp](/fast_gicp/thirdparty/Eigen/bench/sparse_dense_product.cpp) | C++ | 126 | 25 | 37 | 188 |
| [fast_gicp/thirdparty/Eigen/bench/sparse_lu.cpp](/fast_gicp/thirdparty/Eigen/bench/sparse_lu.cpp) | C++ | 96 | 9 | 28 | 133 |
| [fast_gicp/thirdparty/Eigen/bench/sparse_product.cpp](/fast_gicp/thirdparty/Eigen/bench/sparse_product.cpp) | C++ | 153 | 124 | 47 | 324 |
| [fast_gicp/thirdparty/Eigen/bench/sparse_randomsetter.cpp](/fast_gicp/thirdparty/Eigen/bench/sparse_randomsetter.cpp) | C++ | 76 | 28 | 23 | 127 |
| [fast_gicp/thirdparty/Eigen/bench/sparse_setter.cpp](/fast_gicp/thirdparty/Eigen/bench/sparse_setter.cpp) | C++ | 357 | 73 | 56 | 486 |
| [fast_gicp/thirdparty/Eigen/bench/sparse_transpose.cpp](/fast_gicp/thirdparty/Eigen/bench/sparse_transpose.cpp) | C++ | 75 | 8 | 22 | 105 |
| [fast_gicp/thirdparty/Eigen/bench/sparse_trisolver.cpp](/fast_gicp/thirdparty/Eigen/bench/sparse_trisolver.cpp) | C++ | 157 | 27 | 37 | 221 |
| [fast_gicp/thirdparty/Eigen/bench/spbench/sp_solver.cpp](/fast_gicp/thirdparty/Eigen/bench/spbench/sp_solver.cpp) | C++ | 78 | 36 | 12 | 126 |
| [fast_gicp/thirdparty/Eigen/bench/spbench/spbench.dtd](/fast_gicp/thirdparty/Eigen/bench/spbench/spbench.dtd) | XML | 30 | 0 | 1 | 31 |
| [fast_gicp/thirdparty/Eigen/bench/spbench/spbenchsolver.cpp](/fast_gicp/thirdparty/Eigen/bench/spbench/spbenchsolver.cpp) | C++ | 69 | 5 | 14 | 88 |
| [fast_gicp/thirdparty/Eigen/bench/spbench/spbenchsolver.h](/fast_gicp/thirdparty/Eigen/bench/spbench/spbenchsolver.h) | C++ | 447 | 60 | 67 | 574 |
| [fast_gicp/thirdparty/Eigen/bench/spbench/spbenchstyle.h](/fast_gicp/thirdparty/Eigen/bench/spbench/spbenchstyle.h) | C++ | 82 | 8 | 6 | 96 |
| [fast_gicp/thirdparty/Eigen/bench/spbench/test_sparseLU.cpp](/fast_gicp/thirdparty/Eigen/bench/spbench/test_sparseLU.cpp) | C++ | 67 | 18 | 9 | 94 |
| [fast_gicp/thirdparty/Eigen/bench/spmv.cpp](/fast_gicp/thirdparty/Eigen/bench/spmv.cpp) | C++ | 155 | 35 | 44 | 234 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/benchmark.h](/fast_gicp/thirdparty/Eigen/bench/tensors/benchmark.h) | C++ | 33 | 15 | 2 | 50 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/benchmark_main.cc](/fast_gicp/thirdparty/Eigen/bench/tensors/benchmark_main.cc) | C++ | 209 | 19 | 10 | 238 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/contraction_benchmarks_cpu.cc](/fast_gicp/thirdparty/Eigen/bench/tensors/contraction_benchmarks_cpu.cc) | C++ | 25 | 4 | 11 | 40 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/eigen_sycl_bench.sh](/fast_gicp/thirdparty/Eigen/bench/tensors/eigen_sycl_bench.sh) | Shell Script | 29 | 0 | 2 | 31 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/eigen_sycl_bench_contract.sh](/fast_gicp/thirdparty/Eigen/bench/tensors/eigen_sycl_bench_contract.sh) | Shell Script | 6 | 0 | 2 | 8 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/tensor_benchmarks.h](/fast_gicp/thirdparty/Eigen/bench/tensors/tensor_benchmarks.h) | C++ | 500 | 44 | 54 | 598 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/tensor_benchmarks_cpu.cc](/fast_gicp/thirdparty/Eigen/bench/tensors/tensor_benchmarks_cpu.cc) | C++ | 129 | 3 | 37 | 169 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/tensor_benchmarks_fp16_gpu.cu](/fast_gicp/thirdparty/Eigen/bench/tensors/tensor_benchmarks_fp16_gpu.cu) | CUDA C++ | 54 | 12 | 12 | 78 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/tensor_benchmarks_gpu.cu](/fast_gicp/thirdparty/Eigen/bench/tensors/tensor_benchmarks_gpu.cu) | CUDA C++ | 61 | 3 | 12 | 76 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/tensor_benchmarks_sycl.cc](/fast_gicp/thirdparty/Eigen/bench/tensors/tensor_benchmarks_sycl.cc) | C++ | 123 | 2 | 16 | 141 |
| [fast_gicp/thirdparty/Eigen/bench/tensors/tensor_contract_sycl_bench.cc](/fast_gicp/thirdparty/Eigen/bench/tensors/tensor_contract_sycl_bench.cc) | C++ | 255 | 34 | 37 | 326 |
| [fast_gicp/thirdparty/Eigen/bench/vdw_new.cpp](/fast_gicp/thirdparty/Eigen/bench/vdw_new.cpp) | C++ | 35 | 12 | 10 | 57 |
| [fast_gicp/thirdparty/Eigen/blas/BandTriangularSolver.h](/fast_gicp/thirdparty/Eigen/blas/BandTriangularSolver.h) | C++ | 69 | 11 | 18 | 98 |
| [fast_gicp/thirdparty/Eigen/blas/GeneralRank1Update.h](/fast_gicp/thirdparty/Eigen/blas/GeneralRank1Update.h) | C++ | 27 | 9 | 9 | 45 |
| [fast_gicp/thirdparty/Eigen/blas/PackedSelfadjointProduct.h](/fast_gicp/thirdparty/Eigen/blas/PackedSelfadjointProduct.h) | C++ | 33 | 12 | 9 | 54 |
| [fast_gicp/thirdparty/Eigen/blas/PackedTriangularMatrixVector.h](/fast_gicp/thirdparty/Eigen/blas/PackedTriangularMatrixVector.h) | C++ | 62 | 8 | 10 | 80 |
| [fast_gicp/thirdparty/Eigen/blas/PackedTriangularSolverVector.h](/fast_gicp/thirdparty/Eigen/blas/PackedTriangularSolverVector.h) | C++ | 68 | 10 | 11 | 89 |
| [fast_gicp/thirdparty/Eigen/blas/Rank2Update.h](/fast_gicp/thirdparty/Eigen/blas/Rank2Update.h) | C++ | 36 | 15 | 7 | 58 |
| [fast_gicp/thirdparty/Eigen/blas/common.h](/fast_gicp/thirdparty/Eigen/blas/common.h) | C++ | 127 | 10 | 39 | 176 |
| [fast_gicp/thirdparty/Eigen/blas/complex_double.cpp](/fast_gicp/thirdparty/Eigen/blas/complex_double.cpp) | C++ | 10 | 8 | 3 | 21 |
| [fast_gicp/thirdparty/Eigen/blas/complex_single.cpp](/fast_gicp/thirdparty/Eigen/blas/complex_single.cpp) | C++ | 10 | 8 | 3 | 21 |
| [fast_gicp/thirdparty/Eigen/blas/double.cpp](/fast_gicp/thirdparty/Eigen/blas/double.cpp) | C++ | 19 | 9 | 5 | 33 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/chbmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/chbmv.c) | C | 283 | 153 | 52 | 488 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/chpmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/chpmv.c) | C | 272 | 121 | 46 | 439 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/complexdots.c](/fast_gicp/thirdparty/Eigen/blas/f2c/complexdots.c) | C | 45 | 24 | 16 | 85 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/ctbmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/ctbmv.c) | C | 421 | 170 | 57 | 648 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/d_cnjg.c](/fast_gicp/thirdparty/Eigen/blas/f2c/d_cnjg.c) | C | 5 | 0 | 2 | 7 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/datatypes.h](/fast_gicp/thirdparty/Eigen/blas/f2c/datatypes.h) | C++ | 17 | 3 | 5 | 25 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/drotm.c](/fast_gicp/thirdparty/Eigen/blas/f2c/drotm.c) | C | 127 | 62 | 27 | 216 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/drotmg.c](/fast_gicp/thirdparty/Eigen/blas/f2c/drotmg.c) | C | 187 | 76 | 31 | 294 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/dsbmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/dsbmv.c) | C | 168 | 148 | 51 | 367 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/dspmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/dspmv.c) | C | 156 | 116 | 45 | 317 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/dtbmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/dtbmv.c) | C | 212 | 161 | 56 | 429 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/lsame.c](/fast_gicp/thirdparty/Eigen/blas/f2c/lsame.c) | C | 39 | 46 | 33 | 118 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/r_cnjg.c](/fast_gicp/thirdparty/Eigen/blas/f2c/r_cnjg.c) | C | 5 | 0 | 2 | 7 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/srotm.c](/fast_gicp/thirdparty/Eigen/blas/f2c/srotm.c) | C | 127 | 62 | 28 | 217 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/srotmg.c](/fast_gicp/thirdparty/Eigen/blas/f2c/srotmg.c) | C | 187 | 76 | 33 | 296 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/ssbmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/ssbmv.c) | C | 168 | 150 | 51 | 369 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/sspmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/sspmv.c) | C | 156 | 116 | 45 | 317 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/stbmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/stbmv.c) | C | 212 | 161 | 56 | 429 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/zhbmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/zhbmv.c) | C | 284 | 153 | 52 | 489 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/zhpmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/zhpmv.c) | C | 272 | 121 | 46 | 439 |
| [fast_gicp/thirdparty/Eigen/blas/f2c/ztbmv.c](/fast_gicp/thirdparty/Eigen/blas/f2c/ztbmv.c) | C | 421 | 170 | 57 | 648 |
| [fast_gicp/thirdparty/Eigen/blas/level1_cplx_impl.h](/fast_gicp/thirdparty/Eigen/blas/level1_cplx_impl.h) | C++ | 106 | 17 | 33 | 156 |
| [fast_gicp/thirdparty/Eigen/blas/level1_impl.h](/fast_gicp/thirdparty/Eigen/blas/level1_impl.h) | C++ | 109 | 13 | 23 | 145 |
| [fast_gicp/thirdparty/Eigen/blas/level1_real_impl.h](/fast_gicp/thirdparty/Eigen/blas/level1_real_impl.h) | C++ | 61 | 37 | 25 | 123 |
| [fast_gicp/thirdparty/Eigen/blas/level2_cplx_impl.h](/fast_gicp/thirdparty/Eigen/blas/level2_cplx_impl.h) | C++ | 204 | 91 | 66 | 361 |
| [fast_gicp/thirdparty/Eigen/blas/level2_impl.h](/fast_gicp/thirdparty/Eigen/blas/level2_impl.h) | C++ | 360 | 114 | 80 | 554 |
| [fast_gicp/thirdparty/Eigen/blas/level2_real_impl.h](/fast_gicp/thirdparty/Eigen/blas/level2_real_impl.h) | C++ | 175 | 72 | 60 | 307 |
| [fast_gicp/thirdparty/Eigen/blas/level3_impl.h](/fast_gicp/thirdparty/Eigen/blas/level3_impl.h) | C++ | 525 | 103 | 75 | 703 |
| [fast_gicp/thirdparty/Eigen/blas/single.cpp](/fast_gicp/thirdparty/Eigen/blas/single.cpp) | C++ | 11 | 8 | 4 | 23 |
| [fast_gicp/thirdparty/Eigen/blas/testing/runblastest.sh](/fast_gicp/thirdparty/Eigen/blas/testing/runblastest.sh) | Shell Script | 40 | 1 | 5 | 46 |
| [fast_gicp/thirdparty/Eigen/blas/xerbla.cpp](/fast_gicp/thirdparty/Eigen/blas/xerbla.cpp) | C++ | 18 | 0 | 6 | 24 |
| [fast_gicp/thirdparty/Eigen/ci/CTest2JUnit.xsl](/fast_gicp/thirdparty/Eigen/ci/CTest2JUnit.xsl) | XSL | 116 | 0 | 5 | 121 |
| [fast_gicp/thirdparty/Eigen/ci/README.md](/fast_gicp/thirdparty/Eigen/ci/README.md) | Markdown | 48 | 0 | 9 | 57 |
| [fast_gicp/thirdparty/Eigen/ci/build.gitlab-ci.yml](/fast_gicp/thirdparty/Eigen/ci/build.gitlab-ci.yml) | YAML | 187 | 12 | 18 | 217 |
| [fast_gicp/thirdparty/Eigen/ci/smoketests.gitlab-ci.yml](/fast_gicp/thirdparty/Eigen/ci/smoketests.gitlab-ci.yml) | YAML | 98 | 0 | 10 | 108 |
| [fast_gicp/thirdparty/Eigen/ci/test.gitlab-ci.yml](/fast_gicp/thirdparty/Eigen/ci/test.gitlab-ci.yml) | YAML | 329 | 11 | 49 | 389 |
| [fast_gicp/thirdparty/Eigen/cmake/ComputeCppCompilerChecks.cmake](/fast_gicp/thirdparty/Eigen/cmake/ComputeCppCompilerChecks.cmake) | CMake | 48 | 0 | 3 | 51 |
| [fast_gicp/thirdparty/Eigen/cmake/ComputeCppIRMap.cmake](/fast_gicp/thirdparty/Eigen/cmake/ComputeCppIRMap.cmake) | CMake | 17 | 0 | 2 | 19 |
| [fast_gicp/thirdparty/Eigen/cmake/EigenConfigureTesting.cmake](/fast_gicp/thirdparty/Eigen/cmake/EigenConfigureTesting.cmake) | CMake | 44 | 0 | 15 | 59 |
| [fast_gicp/thirdparty/Eigen/cmake/EigenDetermineOSVersion.cmake](/fast_gicp/thirdparty/Eigen/cmake/EigenDetermineOSVersion.cmake) | CMake | 42 | 0 | 5 | 47 |
| [fast_gicp/thirdparty/Eigen/cmake/EigenDetermineVSServicePack.cmake](/fast_gicp/thirdparty/Eigen/cmake/EigenDetermineVSServicePack.cmake) | CMake | 37 | 0 | 5 | 42 |
| [fast_gicp/thirdparty/Eigen/cmake/EigenSmokeTestList.cmake](/fast_gicp/thirdparty/Eigen/cmake/EigenSmokeTestList.cmake) | CMake | 131 | 0 | 0 | 131 |
| [fast_gicp/thirdparty/Eigen/cmake/EigenTesting.cmake](/fast_gicp/thirdparty/Eigen/cmake/EigenTesting.cmake) | CMake | 686 | 0 | 97 | 783 |
| [fast_gicp/thirdparty/Eigen/cmake/EigenUninstall.cmake](/fast_gicp/thirdparty/Eigen/cmake/EigenUninstall.cmake) | CMake | 31 | 0 | 10 | 41 |
| [fast_gicp/thirdparty/Eigen/cmake/FindAdolc.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindAdolc.cmake) | CMake | 15 | 0 | 6 | 21 |
| [fast_gicp/thirdparty/Eigen/cmake/FindBLAS.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindBLAS.cmake) | CMake | 1,257 | 0 | 150 | 1,407 |
| [fast_gicp/thirdparty/Eigen/cmake/FindBLASEXT.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindBLASEXT.cmake) | CMake | 351 | 0 | 30 | 381 |
| [fast_gicp/thirdparty/Eigen/cmake/FindCHOLMOD.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindCHOLMOD.cmake) | CMake | 65 | 0 | 25 | 90 |
| [fast_gicp/thirdparty/Eigen/cmake/FindComputeCpp.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindComputeCpp.cmake) | CMake | 404 | 0 | 51 | 455 |
| [fast_gicp/thirdparty/Eigen/cmake/FindEigen2.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindEigen2.cmake) | CMake | 63 | 0 | 18 | 81 |
| [fast_gicp/thirdparty/Eigen/cmake/FindEigen3.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindEigen3.cmake) | CMake | 89 | 0 | 19 | 108 |
| [fast_gicp/thirdparty/Eigen/cmake/FindFFTW.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindFFTW.cmake) | CMake | 96 | 0 | 24 | 120 |
| [fast_gicp/thirdparty/Eigen/cmake/FindGLEW.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindGLEW.cmake) | CMake | 85 | 0 | 21 | 106 |
| [fast_gicp/thirdparty/Eigen/cmake/FindGMP.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindGMP.cmake) | CMake | 17 | 0 | 5 | 22 |
| [fast_gicp/thirdparty/Eigen/cmake/FindGSL.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindGSL.cmake) | CMake | 144 | 0 | 27 | 171 |
| [fast_gicp/thirdparty/Eigen/cmake/FindGoogleHash.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindGoogleHash.cmake) | CMake | 18 | 0 | 6 | 24 |
| [fast_gicp/thirdparty/Eigen/cmake/FindHWLOC.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindHWLOC.cmake) | CMake | 296 | 0 | 36 | 332 |
| [fast_gicp/thirdparty/Eigen/cmake/FindKLU.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindKLU.cmake) | CMake | 37 | 0 | 12 | 49 |
| [fast_gicp/thirdparty/Eigen/cmake/FindLAPACK.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindLAPACK.cmake) | CMake | 245 | 0 | 29 | 274 |
| [fast_gicp/thirdparty/Eigen/cmake/FindMPFR.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindMPFR.cmake) | CMake | 64 | 0 | 20 | 84 |
| [fast_gicp/thirdparty/Eigen/cmake/FindMetis.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindMetis.cmake) | CMake | 243 | 0 | 23 | 266 |
| [fast_gicp/thirdparty/Eigen/cmake/FindPTSCOTCH.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindPTSCOTCH.cmake) | CMake | 390 | 0 | 34 | 424 |
| [fast_gicp/thirdparty/Eigen/cmake/FindPastix.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindPastix.cmake) | CMake | 655 | 0 | 50 | 705 |
| [fast_gicp/thirdparty/Eigen/cmake/FindSPQR.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindSPQR.cmake) | CMake | 31 | 0 | 10 | 41 |
| [fast_gicp/thirdparty/Eigen/cmake/FindScotch.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindScotch.cmake) | CMake | 339 | 0 | 31 | 370 |
| [fast_gicp/thirdparty/Eigen/cmake/FindStandardMathLibrary.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindStandardMathLibrary.cmake) | CMake | 53 | 0 | 18 | 71 |
| [fast_gicp/thirdparty/Eigen/cmake/FindSuperLU.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindSuperLU.cmake) | CMake | 80 | 0 | 18 | 98 |
| [fast_gicp/thirdparty/Eigen/cmake/FindTriSYCL.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindTriSYCL.cmake) | CMake | 130 | 0 | 23 | 153 |
| [fast_gicp/thirdparty/Eigen/cmake/FindUMFPACK.cmake](/fast_gicp/thirdparty/Eigen/cmake/FindUMFPACK.cmake) | CMake | 41 | 0 | 13 | 54 |
| [fast_gicp/thirdparty/Eigen/cmake/RegexUtils.cmake](/fast_gicp/thirdparty/Eigen/cmake/RegexUtils.cmake) | CMake | 18 | 0 | 1 | 19 |
| [fast_gicp/thirdparty/Eigen/cmake/UseEigen3.cmake](/fast_gicp/thirdparty/Eigen/cmake/UseEigen3.cmake) | CMake | 5 | 0 | 2 | 7 |
| [fast_gicp/thirdparty/Eigen/debug/gdb/__init__.py](/fast_gicp/thirdparty/Eigen/debug/gdb/__init__.py) | Python | 0 | 1 | 1 | 2 |
| [fast_gicp/thirdparty/Eigen/debug/gdb/printers.py](/fast_gicp/thirdparty/Eigen/debug/gdb/printers.py) | Python | 202 | 34 | 79 | 315 |
| [fast_gicp/thirdparty/Eigen/demos/mandelbrot/mandelbrot.cpp](/fast_gicp/thirdparty/Eigen/demos/mandelbrot/mandelbrot.cpp) | C++ | 173 | 17 | 24 | 214 |
| [fast_gicp/thirdparty/Eigen/demos/mandelbrot/mandelbrot.h](/fast_gicp/thirdparty/Eigen/demos/mandelbrot/mandelbrot.h) | C++ | 53 | 8 | 11 | 72 |
| [fast_gicp/thirdparty/Eigen/demos/mix_eigen_and_c/binary_library.cpp](/fast_gicp/thirdparty/Eigen/demos/mix_eigen_and_c/binary_library.cpp) | C++ | 123 | 16 | 47 | 186 |
| [fast_gicp/thirdparty/Eigen/demos/mix_eigen_and_c/binary_library.h](/fast_gicp/thirdparty/Eigen/demos/mix_eigen_and_c/binary_library.h) | C++ | 47 | 18 | 7 | 72 |
| [fast_gicp/thirdparty/Eigen/demos/mix_eigen_and_c/example.c](/fast_gicp/thirdparty/Eigen/demos/mix_eigen_and_c/example.c) | C | 45 | 9 | 12 | 66 |
| [fast_gicp/thirdparty/Eigen/demos/opengl/camera.cpp](/fast_gicp/thirdparty/Eigen/demos/opengl/camera.cpp) | C++ | 203 | 11 | 51 | 265 |
| [fast_gicp/thirdparty/Eigen/demos/opengl/camera.h](/fast_gicp/thirdparty/Eigen/demos/opengl/camera.h) | C++ | 75 | 11 | 33 | 119 |
| [fast_gicp/thirdparty/Eigen/demos/opengl/gpuhelper.cpp](/fast_gicp/thirdparty/Eigen/demos/opengl/gpuhelper.cpp) | C++ | 98 | 11 | 18 | 127 |
| [fast_gicp/thirdparty/Eigen/demos/opengl/gpuhelper.h](/fast_gicp/thirdparty/Eigen/demos/opengl/gpuhelper.h) | C++ | 125 | 40 | 43 | 208 |
| [fast_gicp/thirdparty/Eigen/demos/opengl/icosphere.cpp](/fast_gicp/thirdparty/Eigen/demos/opengl/icosphere.cpp) | C++ | 94 | 13 | 14 | 121 |
| [fast_gicp/thirdparty/Eigen/demos/opengl/icosphere.h](/fast_gicp/thirdparty/Eigen/demos/opengl/icosphere.h) | C++ | 18 | 8 | 5 | 31 |
| [fast_gicp/thirdparty/Eigen/demos/opengl/quaternion_demo.cpp](/fast_gicp/thirdparty/Eigen/demos/opengl/quaternion_demo.cpp) | C++ | 538 | 42 | 77 | 657 |
| [fast_gicp/thirdparty/Eigen/demos/opengl/quaternion_demo.h](/fast_gicp/thirdparty/Eigen/demos/opengl/quaternion_demo.h) | C++ | 79 | 10 | 26 | 115 |
| [fast_gicp/thirdparty/Eigen/demos/opengl/trackball.cpp](/fast_gicp/thirdparty/Eigen/demos/opengl/trackball.cpp) | C++ | 43 | 8 | 9 | 60 |
| [fast_gicp/thirdparty/Eigen/demos/opengl/trackball.h](/fast_gicp/thirdparty/Eigen/demos/opengl/trackball.h) | C++ | 20 | 8 | 15 | 43 |
| [fast_gicp/thirdparty/Eigen/doc/eigen_navtree_hacks.js](/fast_gicp/thirdparty/Eigen/doc/eigen_navtree_hacks.js) | JavaScript | 203 | 15 | 30 | 248 |
| [fast_gicp/thirdparty/Eigen/doc/eigendoxy.css](/fast_gicp/thirdparty/Eigen/doc/eigendoxy.css) | CSS | 165 | 18 | 53 | 236 |
| [fast_gicp/thirdparty/Eigen/doc/eigendoxy_tabs.css](/fast_gicp/thirdparty/Eigen/doc/eigendoxy_tabs.css) | CSS | 52 | 0 | 8 | 60 |
| [fast_gicp/thirdparty/Eigen/doc/examples/CustomizingEigen_Inheritance.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/CustomizingEigen_Inheritance.cpp) | C++ | 24 | 2 | 5 | 31 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Cwise_erf.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Cwise_erf.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Cwise_erfc.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Cwise_erfc.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Cwise_lgamma.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Cwise_lgamma.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/examples/DenseBase_middleCols_int.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/DenseBase_middleCols_int.cpp) | C++ | 13 | 0 | 3 | 16 |
| [fast_gicp/thirdparty/Eigen/doc/examples/DenseBase_middleRows_int.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/DenseBase_middleRows_int.cpp) | C++ | 13 | 0 | 3 | 16 |
| [fast_gicp/thirdparty/Eigen/doc/examples/DenseBase_template_int_middleCols.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/DenseBase_template_int_middleCols.cpp) | C++ | 13 | 0 | 3 | 16 |
| [fast_gicp/thirdparty/Eigen/doc/examples/DenseBase_template_int_middleRows.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/DenseBase_template_int_middleRows.cpp) | C++ | 13 | 0 | 3 | 16 |
| [fast_gicp/thirdparty/Eigen/doc/examples/QuickStart_example.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/QuickStart_example.cpp) | C++ | 12 | 0 | 3 | 15 |
| [fast_gicp/thirdparty/Eigen/doc/examples/QuickStart_example2_dynamic.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/QuickStart_example2_dynamic.cpp) | C++ | 13 | 0 | 3 | 16 |
| [fast_gicp/thirdparty/Eigen/doc/examples/QuickStart_example2_fixed.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/QuickStart_example2_fixed.cpp) | C++ | 12 | 0 | 4 | 16 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TemplateKeyword_flexible.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TemplateKeyword_flexible.cpp) | C++ | 18 | 1 | 4 | 23 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TemplateKeyword_simple.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TemplateKeyword_simple.cpp) | C++ | 17 | 0 | 4 | 21 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TutorialInplaceLU.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TutorialInplaceLU.cpp) | C++ | 50 | 1 | 11 | 62 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgComputeTwice.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgComputeTwice.cpp) | C++ | 21 | 0 | 3 | 24 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgExComputeSolveError.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgExComputeSolveError.cpp) | C++ | 12 | 0 | 3 | 15 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgExSolveColPivHouseholderQR.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgExSolveColPivHouseholderQR.cpp) | C++ | 15 | 0 | 3 | 18 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgExSolveLDLT.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgExSolveLDLT.cpp) | C++ | 14 | 0 | 3 | 17 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgInverseDeterminant.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgInverseDeterminant.cpp) | C++ | 14 | 0 | 3 | 17 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgRankRevealing.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgRankRevealing.cpp) | C++ | 18 | 0 | 3 | 21 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgSVDSolve.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgSVDSolve.cpp) | C++ | 13 | 0 | 3 | 16 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgSelfAdjointEigenSolver.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgSelfAdjointEigenSolver.cpp) | C++ | 16 | 0 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgSetThreshold.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/TutorialLinAlgSetThreshold.cpp) | C++ | 14 | 0 | 3 | 17 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_accessors.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_accessors.cpp) | C++ | 14 | 4 | 7 | 25 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_addition.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_addition.cpp) | C++ | 17 | 2 | 5 | 24 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_cwise_other.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_cwise_other.cpp) | C++ | 17 | 0 | 3 | 20 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_interop.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_interop.cpp) | C++ | 18 | 0 | 5 | 23 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_interop_matrix.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_interop_matrix.cpp) | C++ | 22 | 0 | 5 | 27 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_mult.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ArrayClass_mult.cpp) | C++ | 14 | 0 | 3 | 17 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_BlockOperations_block_assignment.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_BlockOperations_block_assignment.cpp) | C++ | 16 | 0 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_BlockOperations_colrow.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_BlockOperations_colrow.cpp) | C++ | 15 | 0 | 3 | 18 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_BlockOperations_corner.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_BlockOperations_corner.cpp) | C++ | 15 | 0 | 3 | 18 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_BlockOperations_print_block.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_BlockOperations_print_block.cpp) | C++ | 18 | 0 | 3 | 21 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_BlockOperations_vector.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_BlockOperations_vector.cpp) | C++ | 12 | 0 | 3 | 15 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_PartialLU_solve.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_PartialLU_solve.cpp) | C++ | 16 | 0 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_broadcast_1nn.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_broadcast_1nn.cpp) | C++ | 17 | 1 | 7 | 25 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_broadcast_simple.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_broadcast_simple.cpp) | C++ | 15 | 1 | 6 | 22 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_broadcast_simple_rowwise.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_broadcast_simple_rowwise.cpp) | C++ | 14 | 1 | 6 | 21 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_colwise.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_colwise.cpp) | C++ | 11 | 0 | 3 | 14 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_maxnorm.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_maxnorm.cpp) | C++ | 16 | 0 | 5 | 21 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_reductions_bool.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_reductions_bool.cpp) | C++ | 17 | 0 | 5 | 22 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_reductions_norm.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_reductions_norm.cpp) | C++ | 22 | 0 | 7 | 29 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_reductions_operatornorm.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_reductions_operatornorm.cpp) | C++ | 14 | 0 | 5 | 19 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_rowwise.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_rowwise.cpp) | C++ | 11 | 0 | 3 | 14 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_visitors.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_ReductionsVisitorsBroadcasting_visitors.cpp) | C++ | 18 | 2 | 7 | 27 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_simple_example_dynamic_size.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_simple_example_dynamic_size.cpp) | C++ | 17 | 2 | 4 | 23 |
| [fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_simple_example_fixed_size.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/Tutorial_simple_example_fixed_size.cpp) | C++ | 12 | 0 | 4 | 16 |
| [fast_gicp/thirdparty/Eigen/doc/examples/class_Block.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/class_Block.cpp) | C++ | 24 | 0 | 4 | 28 |
| [fast_gicp/thirdparty/Eigen/doc/examples/class_CwiseBinaryOp.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/class_CwiseBinaryOp.cpp) | C++ | 15 | 1 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/doc/examples/class_CwiseUnaryOp.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/class_CwiseUnaryOp.cpp) | C++ | 16 | 1 | 3 | 20 |
| [fast_gicp/thirdparty/Eigen/doc/examples/class_CwiseUnaryOp_ptrfun.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/class_CwiseUnaryOp_ptrfun.cpp) | C++ | 17 | 1 | 3 | 21 |
| [fast_gicp/thirdparty/Eigen/doc/examples/class_FixedBlock.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/class_FixedBlock.cpp) | C++ | 24 | 0 | 4 | 28 |
| [fast_gicp/thirdparty/Eigen/doc/examples/class_FixedReshaped.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/class_FixedReshaped.cpp) | C++ | 20 | 0 | 3 | 23 |
| [fast_gicp/thirdparty/Eigen/doc/examples/class_FixedVectorBlock.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/class_FixedVectorBlock.cpp) | C++ | 24 | 0 | 4 | 28 |
| [fast_gicp/thirdparty/Eigen/doc/examples/class_Reshaped.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/class_Reshaped.cpp) | C++ | 21 | 0 | 3 | 24 |
| [fast_gicp/thirdparty/Eigen/doc/examples/class_VectorBlock.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/class_VectorBlock.cpp) | C++ | 24 | 0 | 4 | 28 |
| [fast_gicp/thirdparty/Eigen/doc/examples/function_taking_eigenbase.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/function_taking_eigenbase.cpp) | C++ | 15 | 1 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/doc/examples/function_taking_ref.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/function_taking_ref.cpp) | C++ | 17 | 0 | 3 | 20 |
| [fast_gicp/thirdparty/Eigen/doc/examples/make_circulant.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/make_circulant.cpp) | C++ | 6 | 4 | 2 | 12 |
| [fast_gicp/thirdparty/Eigen/doc/examples/make_circulant2.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/make_circulant2.cpp) | C++ | 38 | 8 | 7 | 53 |
| [fast_gicp/thirdparty/Eigen/doc/examples/matrixfree_cg.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/matrixfree_cg.cpp) | C++ | 96 | 11 | 23 | 130 |
| [fast_gicp/thirdparty/Eigen/doc/examples/nullary_indexing.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/nullary_indexing.cpp) | C++ | 53 | 4 | 10 | 67 |
| [fast_gicp/thirdparty/Eigen/doc/examples/tut_arithmetic_add_sub.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/tut_arithmetic_add_sub.cpp) | C++ | 20 | 0 | 3 | 23 |
| [fast_gicp/thirdparty/Eigen/doc/examples/tut_arithmetic_dot_cross.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/tut_arithmetic_dot_cross.cpp) | C++ | 13 | 0 | 3 | 16 |
| [fast_gicp/thirdparty/Eigen/doc/examples/tut_arithmetic_matrix_mul.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/tut_arithmetic_matrix_mul.cpp) | C++ | 18 | 0 | 2 | 20 |
| [fast_gicp/thirdparty/Eigen/doc/examples/tut_arithmetic_redux_basic.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/tut_arithmetic_redux_basic.cpp) | C++ | 15 | 0 | 2 | 17 |
| [fast_gicp/thirdparty/Eigen/doc/examples/tut_arithmetic_scalar_mul_div.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/tut_arithmetic_scalar_mul_div.cpp) | C++ | 15 | 0 | 3 | 18 |
| [fast_gicp/thirdparty/Eigen/doc/examples/tut_matrix_coefficient_accessors.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/tut_matrix_coefficient_accessors.cpp) | C++ | 16 | 0 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/doc/examples/tut_matrix_resize.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/tut_matrix_resize.cpp) | C++ | 16 | 0 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/doc/examples/tut_matrix_resize_fixed_size.cpp](/fast_gicp/thirdparty/Eigen/doc/examples/tut_matrix_resize_fixed_size.cpp) | C++ | 10 | 0 | 3 | 13 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/AngleAxis_mimic_euler.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/AngleAxis_mimic_euler.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Array_initializer_list_23_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Array_initializer_list_23_cxx11.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Array_initializer_list_vector_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Array_initializer_list_vector_cxx11.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Array_variadic_ctor_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Array_variadic_ctor_cxx11.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/BiCGSTAB_simple.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/BiCGSTAB_simple.cpp) | C++ | 9 | 2 | 1 | 12 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/BiCGSTAB_step_by_step.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/BiCGSTAB_step_by_step.cpp) | C++ | 12 | 2 | 1 | 15 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/ColPivHouseholderQR_solve.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/ColPivHouseholderQR_solve.cpp) | C++ | 8 | 0 | 1 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/ComplexEigenSolver_compute.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/ComplexEigenSolver_compute.cpp) | C++ | 13 | 0 | 4 | 17 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/ComplexEigenSolver_eigenvalues.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/ComplexEigenSolver_eigenvalues.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/ComplexEigenSolver_eigenvectors.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/ComplexEigenSolver_eigenvectors.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/ComplexSchur_compute.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/ComplexSchur_compute.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/ComplexSchur_matrixT.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/ComplexSchur_matrixT.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/ComplexSchur_matrixU.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/ComplexSchur_matrixU.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_abs.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_abs.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_abs2.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_abs2.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_acos.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_acos.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_arg.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_arg.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_array_power_array.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_array_power_array.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_asin.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_asin.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_atan.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_atan.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_boolean_and.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_boolean_and.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_boolean_not.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_boolean_not.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_boolean_or.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_boolean_or.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_boolean_xor.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_boolean_xor.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_ceil.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_ceil.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_cos.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_cos.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_cosh.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_cosh.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_cube.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_cube.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_equal_equal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_equal_equal.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_exp.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_exp.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_floor.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_floor.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_greater.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_greater.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_greater_equal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_greater_equal.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_inverse.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_inverse.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_isFinite.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_isFinite.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_isInf.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_isInf.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_isNaN.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_isNaN.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_less.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_less.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_less_equal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_less_equal.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_log.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_log.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_log10.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_log10.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_max.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_max.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_min.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_min.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_minus.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_minus.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_minus_equal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_minus_equal.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_not_equal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_not_equal.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_plus.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_plus.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_plus_equal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_plus_equal.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_pow.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_pow.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_product.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_product.cpp) | C++ | 3 | 0 | 2 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_quotient.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_quotient.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_rint.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_rint.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_round.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_round.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_scalar_power_array.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_scalar_power_array.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_sign.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_sign.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_sin.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_sin.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_sinh.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_sinh.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_slash_equal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_slash_equal.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_sqrt.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_sqrt.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_square.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_square.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_tan.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_tan.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_tanh.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_tanh.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_times_equal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Cwise_times_equal.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/DenseBase_LinSpaced.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/DenseBase_LinSpaced.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/DenseBase_LinSpacedInt.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/DenseBase_LinSpacedInt.cpp) | C++ | 8 | 0 | 1 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/DenseBase_LinSpaced_seq_deprecated.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/DenseBase_LinSpaced_seq_deprecated.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/DenseBase_setLinSpaced.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/DenseBase_setLinSpaced.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/DirectionWise_hnormalized.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/DirectionWise_hnormalized.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/DirectionWise_replicate.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/DirectionWise_replicate.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/DirectionWise_replicate_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/DirectionWise_replicate_int.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/EigenSolver_EigenSolver_MatrixType.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/EigenSolver_EigenSolver_MatrixType.cpp) | C++ | 13 | 0 | 4 | 17 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/EigenSolver_compute.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/EigenSolver_compute.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/EigenSolver_eigenvalues.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/EigenSolver_eigenvalues.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/EigenSolver_eigenvectors.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/EigenSolver_eigenvectors.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/EigenSolver_pseudoEigenvectors.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/EigenSolver_pseudoEigenvectors.cpp) | C++ | 8 | 0 | 2 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/FullPivHouseholderQR_solve.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/FullPivHouseholderQR_solve.cpp) | C++ | 8 | 0 | 1 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/FullPivLU_image.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/FullPivLU_image.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/FullPivLU_kernel.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/FullPivLU_kernel.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/FullPivLU_solve.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/FullPivLU_solve.cpp) | C++ | 11 | 0 | 1 | 12 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/GeneralizedEigenSolver.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/GeneralizedEigenSolver.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/HessenbergDecomposition_compute.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/HessenbergDecomposition_compute.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/HessenbergDecomposition_matrixH.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/HessenbergDecomposition_matrixH.cpp) | C++ | 8 | 0 | 1 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/HessenbergDecomposition_packedMatrix.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/HessenbergDecomposition_packedMatrix.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/HouseholderQR_householderQ.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/HouseholderQR_householderQ.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/HouseholderQR_solve.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/HouseholderQR_solve.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/HouseholderSequence_HouseholderSequence.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/HouseholderSequence_HouseholderSequence.cpp) | C++ | 27 | 0 | 5 | 32 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/IOFormat.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/IOFormat.cpp) | C++ | 12 | 0 | 3 | 15 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/JacobiSVD_basic.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/JacobiSVD_basic.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Jacobi_makeGivens.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Jacobi_makeGivens.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Jacobi_makeJacobi.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Jacobi_makeJacobi.cpp) | C++ | 8 | 0 | 1 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/LLT_example.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/LLT_example.cpp) | C++ | 9 | 1 | 3 | 13 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/LLT_solve.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/LLT_solve.cpp) | C++ | 6 | 2 | 1 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/LeastSquaresNormalEquations.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/LeastSquaresNormalEquations.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/LeastSquaresQR.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/LeastSquaresQR.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Map_general_stride.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Map_general_stride.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Map_inner_stride.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Map_inner_stride.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Map_outer_stride.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Map_outer_stride.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Map_placement_new.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Map_placement_new.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Map_simple.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Map_simple.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_adjoint.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_adjoint.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_all.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_all.cpp) | C++ | 6 | 1 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_applyOnTheLeft.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_applyOnTheLeft.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_applyOnTheRight.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_applyOnTheRight.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_array.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_array.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_array_const.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_array_const.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_asDiagonal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_asDiagonal.cpp) | C++ | 1 | 0 | 1 | 2 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_block_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_block_int_int.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_block_int_int_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_block_int_int_int_int.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_bottomLeftCorner_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_bottomLeftCorner_int_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_bottomRightCorner_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_bottomRightCorner_int_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_bottomRows_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_bottomRows_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cast.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cast.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_col.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_col.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_colwise.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_colwise.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_colwise_iterator_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_colwise_iterator_cxx11.cpp) | C++ | 12 | 0 | 1 | 13 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_computeInverseAndDetWithCheck.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_computeInverseAndDetWithCheck.cpp) | C++ | 13 | 0 | 1 | 14 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_computeInverseWithCheck.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_computeInverseWithCheck.cpp) | C++ | 11 | 0 | 1 | 12 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseAbs.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseAbs.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseAbs2.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseAbs2.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseArg.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseArg.cpp) | C++ | 3 | 0 | 0 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseEqual.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseEqual.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseInverse.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseInverse.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseMax.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseMax.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseMin.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseMin.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseNotEqual.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseNotEqual.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseProduct.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseProduct.cpp) | C++ | 3 | 0 | 2 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseQuotient.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseQuotient.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseSign.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseSign.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseSqrt.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_cwiseSqrt.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_diagonal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_diagonal.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_diagonal_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_diagonal_int.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_diagonal_template_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_diagonal_template_int.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_eigenvalues.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_eigenvalues.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_end_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_end_int.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_eval.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_eval.cpp) | C++ | 12 | 0 | 1 | 13 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_fixedBlock_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_fixedBlock_int_int.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_hnormalized.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_hnormalized.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_homogeneous.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_homogeneous.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_identity.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_identity.cpp) | C++ | 1 | 0 | 1 | 2 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_identity_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_identity_int_int.cpp) | C++ | 1 | 0 | 1 | 2 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_inverse.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_inverse.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isDiagonal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isDiagonal.cpp) | C++ | 5 | 0 | 2 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isIdentity.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isIdentity.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isOnes.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isOnes.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isOrthogonal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isOrthogonal.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isUnitary.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isUnitary.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isZero.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_isZero.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_leftCols_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_leftCols_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_noalias.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_noalias.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_ones.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_ones.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_ones_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_ones_int.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_ones_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_ones_int_int.cpp) | C++ | 1 | 0 | 1 | 2 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_operatorNorm.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_operatorNorm.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_prod.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_prod.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_random.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_random.cpp) | C++ | 1 | 0 | 1 | 2 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_random_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_random_int.cpp) | C++ | 1 | 0 | 1 | 2 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_random_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_random_int_int.cpp) | C++ | 1 | 0 | 1 | 2 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_replicate.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_replicate.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_replicate_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_replicate_int_int.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_reshaped_auto.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_reshaped_auto.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_reshaped_fixed.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_reshaped_fixed.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_reshaped_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_reshaped_int_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_reshaped_to_vector.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_reshaped_to_vector.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_reverse.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_reverse.cpp) | C++ | 8 | 0 | 1 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_rightCols_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_rightCols_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_row.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_row.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_rowwise.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_rowwise.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_segment_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_segment_int_int.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_select.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_select.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_selfadjointView.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_selfadjointView.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_set.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_set.cpp) | C++ | 13 | 0 | 1 | 14 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_setIdentity.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_setIdentity.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_setOnes.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_setOnes.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_setRandom.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_setRandom.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_setZero.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_setZero.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_start_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_start_int.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_bottomRows.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_bottomRows.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_end.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_end.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_block_int_int_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_block_int_int_int_int.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_bottomLeftCorner.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_bottomLeftCorner.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_bottomLeftCorner_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_bottomLeftCorner_int_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_bottomRightCorner.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_bottomRightCorner.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_bottomRightCorner_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_bottomRightCorner_int_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_topLeftCorner.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_topLeftCorner.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_topLeftCorner_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_topLeftCorner_int_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_topRightCorner.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_topRightCorner.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_topRightCorner_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_int_topRightCorner_int_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_leftCols.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_leftCols.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_rightCols.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_rightCols.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_segment.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_segment.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_start.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_start.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_topRows.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_template_int_topRows.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_topLeftCorner_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_topLeftCorner_int_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_topRightCorner_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_topRightCorner_int_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_topRows_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_topRows_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_transpose.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_transpose.cpp) | C++ | 8 | 0 | 1 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_triangularView.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_triangularView.cpp) | C++ | 8 | 1 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_zero.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_zero.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_zero_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_zero_int.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_zero_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/MatrixBase_zero_int_int.cpp) | C++ | 1 | 0 | 1 | 2 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_Map_stride.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_Map_stride.cpp) | C++ | 6 | 0 | 2 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_initializer_list_23_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_initializer_list_23_cxx11.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_initializer_list_vector_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_initializer_list_vector_cxx11.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_resize_NoChange_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_resize_NoChange_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_resize_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_resize_int.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_resize_int_NoChange.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_resize_int_NoChange.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_resize_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_resize_int_int.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setConstant_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setConstant_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setConstant_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setConstant_int_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setIdentity_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setIdentity_int_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setOnes_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setOnes_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setOnes_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setOnes_int_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setRandom_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setRandom_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setRandom_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setRandom_int_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setZero_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setZero_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setZero_int_int.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_setZero_int_int.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_variadic_ctor_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Matrix_variadic_ctor_cxx11.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/PartialPivLU_solve.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/PartialPivLU_solve.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_count.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_count.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_maxCoeff.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_maxCoeff.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_minCoeff.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_minCoeff.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_norm.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_norm.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_prod.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_prod.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_squaredNorm.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_squaredNorm.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_sum.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/PartialRedux_sum.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/RealQZ_compute.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/RealQZ_compute.cpp) | C++ | 13 | 2 | 3 | 18 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/RealSchur_RealSchur_MatrixType.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/RealSchur_RealSchur_MatrixType.cpp) | C++ | 8 | 0 | 3 | 11 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/RealSchur_compute.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/RealSchur_compute.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_SelfAdjointEigenSolver.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_SelfAdjointEigenSolver.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_SelfAdjointEigenSolver_MatrixType.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_SelfAdjointEigenSolver_MatrixType.cpp) | C++ | 14 | 0 | 4 | 18 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_SelfAdjointEigenSolver_MatrixType2.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_SelfAdjointEigenSolver_MatrixType2.cpp) | C++ | 14 | 0 | 3 | 17 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_compute_MatrixType.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_compute_MatrixType.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_compute_MatrixType2.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_compute_MatrixType2.cpp) | C++ | 8 | 0 | 2 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_eigenvalues.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_eigenvalues.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_eigenvectors.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_eigenvectors.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_operatorInverseSqrt.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_operatorInverseSqrt.cpp) | C++ | 8 | 0 | 2 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_operatorSqrt.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointEigenSolver_operatorSqrt.cpp) | C++ | 7 | 0 | 2 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointView_eigenvalues.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointView_eigenvalues.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointView_operatorNorm.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SelfAdjointView_operatorNorm.cpp) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Slicing_arrayexpr.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Slicing_arrayexpr.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Slicing_custom_padding_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Slicing_custom_padding_cxx11.cpp) | C++ | 11 | 0 | 2 | 13 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Slicing_rawarray_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Slicing_rawarray_cxx11.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Slicing_stdvector_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Slicing_stdvector_cxx11.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/SparseMatrix_coeffs.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/SparseMatrix_coeffs.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_block.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_block.cpp) | C++ | 5 | 1 | 2 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_block_correct.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_block_correct.cpp) | C++ | 5 | 1 | 2 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_cwise.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_cwise.cpp) | C++ | 13 | 1 | 7 | 21 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_mult1.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_mult1.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_mult2.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_mult2.cpp) | C++ | 6 | 2 | 3 | 11 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_mult3.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_mult3.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_mult4.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_mult4.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_mult5.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/TopicAliasing_mult5.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/TopicStorageOrders_example.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/TopicStorageOrders_example.cpp) | C++ | 15 | 0 | 4 | 19 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Triangular_solve.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Triangular_solve.cpp) | C++ | 11 | 0 | 1 | 12 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_Tridiagonalization_MatrixType.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_Tridiagonalization_MatrixType.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_compute.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_compute.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_decomposeInPlace.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_decomposeInPlace.cpp) | C++ | 9 | 0 | 2 | 11 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_diagonal.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_diagonal.cpp) | C++ | 11 | 0 | 3 | 14 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_householderCoefficients.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_householderCoefficients.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_packedMatrix.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tridiagonalization_packedMatrix.cpp) | C++ | 8 | 0 | 1 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_Block.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_Block.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_CommaTemporary.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_CommaTemporary.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_Join.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_Join.cpp) | C++ | 9 | 0 | 3 | 12 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_LinSpaced.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_LinSpaced.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_ThreeWays.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_ThreeWays.cpp) | C++ | 17 | 0 | 4 | 21 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_Zero.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_AdvancedInitialization_Zero.cpp) | C++ | 9 | 0 | 5 | 14 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_Map_rowmajor.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_Map_rowmajor.cpp) | C++ | 6 | 0 | 2 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_Map_using.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_Map_using.cpp) | C++ | 19 | 0 | 3 | 22 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_ReshapeMat2Mat.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_ReshapeMat2Mat.cpp) | C++ | 5 | 0 | 2 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_ReshapeMat2Vec.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_ReshapeMat2Vec.cpp) | C++ | 9 | 0 | 3 | 12 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_SlicingCol.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_SlicingCol.cpp) | C++ | 10 | 0 | 2 | 12 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_SlicingVec.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_SlicingVec.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_commainit_01.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_commainit_01.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_commainit_01b.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_commainit_01b.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_commainit_02.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_commainit_02.cpp) | C++ | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_range_for_loop_1d_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_range_for_loop_1d_cxx11.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_range_for_loop_2d_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_range_for_loop_2d_cxx11.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_reshaped_vs_resize_1.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_reshaped_vs_resize_1.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_reshaped_vs_resize_2.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_reshaped_vs_resize_2.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_matrix_inverse.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_matrix_inverse.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_multiple_rhs.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_multiple_rhs.cpp) | C++ | 10 | 0 | 1 | 11 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_reuse_decomposition.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_reuse_decomposition.cpp) | C++ | 13 | 0 | 1 | 14 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_singular.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_singular.cpp) | C++ | 9 | 0 | 1 | 10 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_triangular.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_triangular.cpp) | C++ | 8 | 0 | 1 | 9 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_triangular_inplace.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_solve_triangular_inplace.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_std_sort.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_std_sort.cpp) | C++ | 4 | 0 | 1 | 5 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_std_sort_rows_cxx11.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Tutorial_std_sort_rows_cxx11.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/VectorwiseOp_homogeneous.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/VectorwiseOp_homogeneous.cpp) | C++ | 6 | 0 | 1 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/Vectorwise_reverse.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/Vectorwise_reverse.cpp) | C++ | 8 | 1 | 2 | 11 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/class_FullPivLU.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/class_FullPivLU.cpp) | C++ | 16 | 0 | 1 | 17 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/tut_arithmetic_redux_minmax.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/tut_arithmetic_redux_minmax.cpp) | C++ | 11 | 0 | 2 | 13 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/tut_arithmetic_transpose_aliasing.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/tut_arithmetic_transpose_aliasing.cpp) | C++ | 4 | 0 | 2 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/tut_arithmetic_transpose_conjugate.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/tut_arithmetic_transpose_conjugate.cpp) | C++ | 5 | 0 | 8 | 13 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/tut_arithmetic_transpose_inplace.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/tut_arithmetic_transpose_inplace.cpp) | C++ | 4 | 0 | 3 | 7 |
| [fast_gicp/thirdparty/Eigen/doc/snippets/tut_matrix_assignment_resizing.cpp](/fast_gicp/thirdparty/Eigen/doc/snippets/tut_matrix_assignment_resizing.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/doc/special_examples/Tutorial_sparse_example.cpp](/fast_gicp/thirdparty/Eigen/doc/special_examples/Tutorial_sparse_example.cpp) | C++ | 25 | 3 | 11 | 39 |
| [fast_gicp/thirdparty/Eigen/doc/special_examples/Tutorial_sparse_example_details.cpp](/fast_gicp/thirdparty/Eigen/doc/special_examples/Tutorial_sparse_example_details.cpp) | C++ | 39 | 0 | 6 | 45 |
| [fast_gicp/thirdparty/Eigen/doc/special_examples/random_cpp11.cpp](/fast_gicp/thirdparty/Eigen/doc/special_examples/random_cpp11.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/doc/tutorial.cpp](/fast_gicp/thirdparty/Eigen/doc/tutorial.cpp) | C++ | 38 | 11 | 14 | 63 |
| [fast_gicp/thirdparty/Eigen/failtest/bdcsvd_int.cpp](/fast_gicp/thirdparty/Eigen/failtest/bdcsvd_int.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/block_nonconst_ctor_on_const_xpr_0.cpp](/fast_gicp/thirdparty/Eigen/failtest/block_nonconst_ctor_on_const_xpr_0.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/block_nonconst_ctor_on_const_xpr_1.cpp](/fast_gicp/thirdparty/Eigen/failtest/block_nonconst_ctor_on_const_xpr_1.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/block_nonconst_ctor_on_const_xpr_2.cpp](/fast_gicp/thirdparty/Eigen/failtest/block_nonconst_ctor_on_const_xpr_2.cpp) | C++ | 11 | 1 | 5 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/block_on_const_type_actually_const_0.cpp](/fast_gicp/thirdparty/Eigen/failtest/block_on_const_type_actually_const_0.cpp) | C++ | 12 | 0 | 5 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/block_on_const_type_actually_const_1.cpp](/fast_gicp/thirdparty/Eigen/failtest/block_on_const_type_actually_const_1.cpp) | C++ | 12 | 0 | 5 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/colpivqr_int.cpp](/fast_gicp/thirdparty/Eigen/failtest/colpivqr_int.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/const_qualified_block_method_retval_0.cpp](/fast_gicp/thirdparty/Eigen/failtest/const_qualified_block_method_retval_0.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/const_qualified_block_method_retval_1.cpp](/fast_gicp/thirdparty/Eigen/failtest/const_qualified_block_method_retval_1.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/const_qualified_diagonal_method_retval.cpp](/fast_gicp/thirdparty/Eigen/failtest/const_qualified_diagonal_method_retval.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/const_qualified_transpose_method_retval.cpp](/fast_gicp/thirdparty/Eigen/failtest/const_qualified_transpose_method_retval.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/cwiseunaryview_nonconst_ctor_on_const_xpr.cpp](/fast_gicp/thirdparty/Eigen/failtest/cwiseunaryview_nonconst_ctor_on_const_xpr.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/cwiseunaryview_on_const_type_actually_const.cpp](/fast_gicp/thirdparty/Eigen/failtest/cwiseunaryview_on_const_type_actually_const.cpp) | C++ | 12 | 0 | 5 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/diagonal_nonconst_ctor_on_const_xpr.cpp](/fast_gicp/thirdparty/Eigen/failtest/diagonal_nonconst_ctor_on_const_xpr.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/diagonal_on_const_type_actually_const.cpp](/fast_gicp/thirdparty/Eigen/failtest/diagonal_on_const_type_actually_const.cpp) | C++ | 12 | 0 | 5 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/eigensolver_cplx.cpp](/fast_gicp/thirdparty/Eigen/failtest/eigensolver_cplx.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/eigensolver_int.cpp](/fast_gicp/thirdparty/Eigen/failtest/eigensolver_int.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/failtest_sanity_check.cpp](/fast_gicp/thirdparty/Eigen/failtest/failtest_sanity_check.cpp) | C++ | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/Eigen/failtest/fullpivlu_int.cpp](/fast_gicp/thirdparty/Eigen/failtest/fullpivlu_int.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/fullpivqr_int.cpp](/fast_gicp/thirdparty/Eigen/failtest/fullpivqr_int.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/initializer_list_1.cpp](/fast_gicp/thirdparty/Eigen/failtest/initializer_list_1.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/initializer_list_2.cpp](/fast_gicp/thirdparty/Eigen/failtest/initializer_list_2.cpp) | C++ | 13 | 0 | 4 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/jacobisvd_int.cpp](/fast_gicp/thirdparty/Eigen/failtest/jacobisvd_int.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/ldlt_int.cpp](/fast_gicp/thirdparty/Eigen/failtest/ldlt_int.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/llt_int.cpp](/fast_gicp/thirdparty/Eigen/failtest/llt_int.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/map_nonconst_ctor_on_const_ptr_0.cpp](/fast_gicp/thirdparty/Eigen/failtest/map_nonconst_ctor_on_const_ptr_0.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/map_nonconst_ctor_on_const_ptr_1.cpp](/fast_gicp/thirdparty/Eigen/failtest/map_nonconst_ctor_on_const_ptr_1.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/map_nonconst_ctor_on_const_ptr_2.cpp](/fast_gicp/thirdparty/Eigen/failtest/map_nonconst_ctor_on_const_ptr_2.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/map_nonconst_ctor_on_const_ptr_3.cpp](/fast_gicp/thirdparty/Eigen/failtest/map_nonconst_ctor_on_const_ptr_3.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/map_nonconst_ctor_on_const_ptr_4.cpp](/fast_gicp/thirdparty/Eigen/failtest/map_nonconst_ctor_on_const_ptr_4.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/map_on_const_type_actually_const_0.cpp](/fast_gicp/thirdparty/Eigen/failtest/map_on_const_type_actually_const_0.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/map_on_const_type_actually_const_1.cpp](/fast_gicp/thirdparty/Eigen/failtest/map_on_const_type_actually_const_1.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/partialpivlu_int.cpp](/fast_gicp/thirdparty/Eigen/failtest/partialpivlu_int.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/qr_int.cpp](/fast_gicp/thirdparty/Eigen/failtest/qr_int.cpp) | C++ | 11 | 0 | 4 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/ref_1.cpp](/fast_gicp/thirdparty/Eigen/failtest/ref_1.cpp) | C++ | 14 | 0 | 5 | 19 |
| [fast_gicp/thirdparty/Eigen/failtest/ref_2.cpp](/fast_gicp/thirdparty/Eigen/failtest/ref_2.cpp) | C++ | 12 | 0 | 4 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/ref_3.cpp](/fast_gicp/thirdparty/Eigen/failtest/ref_3.cpp) | C++ | 12 | 0 | 4 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/ref_4.cpp](/fast_gicp/thirdparty/Eigen/failtest/ref_4.cpp) | C++ | 12 | 0 | 4 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/ref_5.cpp](/fast_gicp/thirdparty/Eigen/failtest/ref_5.cpp) | C++ | 13 | 0 | 4 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/selfadjointview_nonconst_ctor_on_const_xpr.cpp](/fast_gicp/thirdparty/Eigen/failtest/selfadjointview_nonconst_ctor_on_const_xpr.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/selfadjointview_on_const_type_actually_const.cpp](/fast_gicp/thirdparty/Eigen/failtest/selfadjointview_on_const_type_actually_const.cpp) | C++ | 12 | 0 | 5 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/sparse_ref_1.cpp](/fast_gicp/thirdparty/Eigen/failtest/sparse_ref_1.cpp) | C++ | 14 | 0 | 5 | 19 |
| [fast_gicp/thirdparty/Eigen/failtest/sparse_ref_2.cpp](/fast_gicp/thirdparty/Eigen/failtest/sparse_ref_2.cpp) | C++ | 12 | 0 | 4 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/sparse_ref_3.cpp](/fast_gicp/thirdparty/Eigen/failtest/sparse_ref_3.cpp) | C++ | 12 | 0 | 4 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/sparse_ref_4.cpp](/fast_gicp/thirdparty/Eigen/failtest/sparse_ref_4.cpp) | C++ | 12 | 0 | 4 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/sparse_ref_5.cpp](/fast_gicp/thirdparty/Eigen/failtest/sparse_ref_5.cpp) | C++ | 13 | 0 | 4 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/sparse_storage_mismatch.cpp](/fast_gicp/thirdparty/Eigen/failtest/sparse_storage_mismatch.cpp) | C++ | 14 | 0 | 3 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/swap_1.cpp](/fast_gicp/thirdparty/Eigen/failtest/swap_1.cpp) | C++ | 12 | 0 | 3 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/swap_2.cpp](/fast_gicp/thirdparty/Eigen/failtest/swap_2.cpp) | C++ | 12 | 0 | 3 | 15 |
| [fast_gicp/thirdparty/Eigen/failtest/ternary_1.cpp](/fast_gicp/thirdparty/Eigen/failtest/ternary_1.cpp) | C++ | 11 | 0 | 3 | 14 |
| [fast_gicp/thirdparty/Eigen/failtest/ternary_2.cpp](/fast_gicp/thirdparty/Eigen/failtest/ternary_2.cpp) | C++ | 11 | 0 | 3 | 14 |
| [fast_gicp/thirdparty/Eigen/failtest/transpose_nonconst_ctor_on_const_xpr.cpp](/fast_gicp/thirdparty/Eigen/failtest/transpose_nonconst_ctor_on_const_xpr.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/transpose_on_const_type_actually_const.cpp](/fast_gicp/thirdparty/Eigen/failtest/transpose_on_const_type_actually_const.cpp) | C++ | 12 | 0 | 5 | 17 |
| [fast_gicp/thirdparty/Eigen/failtest/triangularview_nonconst_ctor_on_const_xpr.cpp](/fast_gicp/thirdparty/Eigen/failtest/triangularview_nonconst_ctor_on_const_xpr.cpp) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/Eigen/failtest/triangularview_on_const_type_actually_const.cpp](/fast_gicp/thirdparty/Eigen/failtest/triangularview_on_const_type_actually_const.cpp) | C++ | 12 | 0 | 5 | 17 |
| [fast_gicp/thirdparty/Eigen/lapack/cholesky.cpp](/fast_gicp/thirdparty/Eigen/lapack/cholesky.cpp) | C++ | 51 | 12 | 10 | 73 |
| [fast_gicp/thirdparty/Eigen/lapack/complex_double.cpp](/fast_gicp/thirdparty/Eigen/lapack/complex_double.cpp) | C++ | 8 | 8 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/lapack/complex_single.cpp](/fast_gicp/thirdparty/Eigen/lapack/complex_single.cpp) | C++ | 8 | 8 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/lapack/double.cpp](/fast_gicp/thirdparty/Eigen/lapack/double.cpp) | C++ | 8 | 8 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/lapack/eigenvalues.cpp](/fast_gicp/thirdparty/Eigen/lapack/eigenvalues.cpp) | C++ | 40 | 11 | 12 | 63 |
| [fast_gicp/thirdparty/Eigen/lapack/lapack_common.h](/fast_gicp/thirdparty/Eigen/lapack/lapack_common.h) | C++ | 14 | 8 | 8 | 30 |
| [fast_gicp/thirdparty/Eigen/lapack/lu.cpp](/fast_gicp/thirdparty/Eigen/lapack/lu.cpp) | C++ | 66 | 12 | 12 | 90 |
| [fast_gicp/thirdparty/Eigen/lapack/single.cpp](/fast_gicp/thirdparty/Eigen/lapack/single.cpp) | C++ | 8 | 8 | 3 | 19 |
| [fast_gicp/thirdparty/Eigen/lapack/svd.cpp](/fast_gicp/thirdparty/Eigen/lapack/svd.cpp) | C++ | 105 | 12 | 22 | 139 |
| [fast_gicp/thirdparty/Eigen/scripts/eigen_gen_credits.cpp](/fast_gicp/thirdparty/Eigen/scripts/eigen_gen_credits.cpp) | C++ | 168 | 28 | 37 | 233 |
| [fast_gicp/thirdparty/Eigen/scripts/eigen_gen_split_test_help.cmake](/fast_gicp/thirdparty/Eigen/scripts/eigen_gen_split_test_help.cmake) | CMake | 11 | 0 | 0 | 11 |
| [fast_gicp/thirdparty/Eigen/scripts/eigen_monitor_perf.sh](/fast_gicp/thirdparty/Eigen/scripts/eigen_monitor_perf.sh) | Shell Script | 12 | 6 | 8 | 26 |
| [fast_gicp/thirdparty/Eigen/scripts/relicense.py](/fast_gicp/thirdparty/Eigen/scripts/relicense.py) | Python | 46 | 16 | 8 | 70 |
| [fast_gicp/thirdparty/Eigen/test/AnnoyingScalar.h](/fast_gicp/thirdparty/Eigen/test/AnnoyingScalar.h) | C++ | 130 | 11 | 29 | 170 |
| [fast_gicp/thirdparty/Eigen/test/MovableScalar.h](/fast_gicp/thirdparty/Eigen/test/MovableScalar.h) | C++ | 20 | 8 | 8 | 36 |
| [fast_gicp/thirdparty/Eigen/test/OffByOneScalar.h](/fast_gicp/thirdparty/Eigen/test/OffByOneScalar.h) | C++ | 21 | 3 | 5 | 29 |
| [fast_gicp/thirdparty/Eigen/test/SafeScalar.h](/fast_gicp/thirdparty/Eigen/test/SafeScalar.h) | C++ | 25 | 1 | 5 | 31 |
| [fast_gicp/thirdparty/Eigen/test/adjoint.cpp](/fast_gicp/thirdparty/Eigen/test/adjoint.cpp) | C++ | 150 | 30 | 40 | 220 |
| [fast_gicp/thirdparty/Eigen/test/array_cwise.cpp](/fast_gicp/thirdparty/Eigen/test/array_cwise.cpp) | C++ | 544 | 42 | 88 | 674 |
| [fast_gicp/thirdparty/Eigen/test/array_for_matrix.cpp](/fast_gicp/thirdparty/Eigen/test/array_for_matrix.cpp) | C++ | 236 | 24 | 48 | 308 |
| [fast_gicp/thirdparty/Eigen/test/array_of_string.cpp](/fast_gicp/thirdparty/Eigen/test/array_of_string.cpp) | C++ | 20 | 8 | 5 | 33 |
| [fast_gicp/thirdparty/Eigen/test/array_replicate.cpp](/fast_gicp/thirdparty/Eigen/test/array_replicate.cpp) | C++ | 54 | 11 | 17 | 82 |
| [fast_gicp/thirdparty/Eigen/test/array_reverse.cpp](/fast_gicp/thirdparty/Eigen/test/array_reverse.cpp) | C++ | 147 | 27 | 31 | 205 |
| [fast_gicp/thirdparty/Eigen/test/bandmatrix.cpp](/fast_gicp/thirdparty/Eigen/test/bandmatrix.cpp) | C++ | 51 | 10 | 11 | 72 |
| [fast_gicp/thirdparty/Eigen/test/basicstuff.cpp](/fast_gicp/thirdparty/Eigen/test/basicstuff.cpp) | C++ | 296 | 23 | 38 | 357 |
| [fast_gicp/thirdparty/Eigen/test/bdcsvd.cpp](/fast_gicp/thirdparty/Eigen/test/bdcsvd.cpp) | C++ | 78 | 20 | 21 | 119 |
| [fast_gicp/thirdparty/Eigen/test/bfloat16_float.cpp](/fast_gicp/thirdparty/Eigen/test/bfloat16_float.cpp) | C++ | 360 | 43 | 65 | 468 |
| [fast_gicp/thirdparty/Eigen/test/bicgstab.cpp](/fast_gicp/thirdparty/Eigen/test/bicgstab.cpp) | C++ | 18 | 11 | 6 | 35 |
| [fast_gicp/thirdparty/Eigen/test/blasutil.cpp](/fast_gicp/thirdparty/Eigen/test/blasutil.cpp) | C++ | 157 | 21 | 33 | 211 |
| [fast_gicp/thirdparty/Eigen/test/block.cpp](/fast_gicp/thirdparty/Eigen/test/block.cpp) | C++ | 244 | 26 | 47 | 317 |
| [fast_gicp/thirdparty/Eigen/test/boostmultiprec.cpp](/fast_gicp/thirdparty/Eigen/test/boostmultiprec.cpp) | C++ | 148 | 13 | 48 | 209 |
| [fast_gicp/thirdparty/Eigen/test/bug1213.cpp](/fast_gicp/thirdparty/Eigen/test/bug1213.cpp) | C++ | 8 | 1 | 5 | 14 |
| [fast_gicp/thirdparty/Eigen/test/bug1213.h](/fast_gicp/thirdparty/Eigen/test/bug1213.h) | C++ | 4 | 0 | 5 | 9 |
| [fast_gicp/thirdparty/Eigen/test/bug1213_main.cpp](/fast_gicp/thirdparty/Eigen/test/bug1213_main.cpp) | C++ | 11 | 1 | 7 | 19 |
| [fast_gicp/thirdparty/Eigen/test/cholesky.cpp](/fast_gicp/thirdparty/Eigen/test/cholesky.cpp) | C++ | 404 | 49 | 80 | 533 |
| [fast_gicp/thirdparty/Eigen/test/cholmod_support.cpp](/fast_gicp/thirdparty/Eigen/test/cholmod_support.cpp) | C++ | 49 | 11 | 10 | 70 |
| [fast_gicp/thirdparty/Eigen/test/commainitializer.cpp](/fast_gicp/thirdparty/Eigen/test/commainitializer.cpp) | C++ | 88 | 10 | 21 | 119 |
| [fast_gicp/thirdparty/Eigen/test/conjugate_gradient.cpp](/fast_gicp/thirdparty/Eigen/test/conjugate_gradient.cpp) | C++ | 22 | 8 | 5 | 35 |
| [fast_gicp/thirdparty/Eigen/test/conservative_resize.cpp](/fast_gicp/thirdparty/Eigen/test/conservative_resize.cpp) | C++ | 122 | 15 | 27 | 164 |
| [fast_gicp/thirdparty/Eigen/test/constructor.cpp](/fast_gicp/thirdparty/Eigen/test/constructor.cpp) | C++ | 78 | 9 | 12 | 99 |
| [fast_gicp/thirdparty/Eigen/test/corners.cpp](/fast_gicp/thirdparty/Eigen/test/corners.cpp) | C++ | 89 | 8 | 21 | 118 |
| [fast_gicp/thirdparty/Eigen/test/ctorleak.cpp](/fast_gicp/thirdparty/Eigen/test/ctorleak.cpp) | C++ | 70 | 1 | 11 | 82 |
| [fast_gicp/thirdparty/Eigen/test/denseLM.cpp](/fast_gicp/thirdparty/Eigen/test/denseLM.cpp) | C++ | 142 | 20 | 29 | 191 |
| [fast_gicp/thirdparty/Eigen/test/dense_storage.cpp](/fast_gicp/thirdparty/Eigen/test/dense_storage.cpp) | C++ | 145 | 17 | 29 | 191 |
| [fast_gicp/thirdparty/Eigen/test/determinant.cpp](/fast_gicp/thirdparty/Eigen/test/determinant.cpp) | C++ | 48 | 13 | 6 | 67 |
| [fast_gicp/thirdparty/Eigen/test/diagonal.cpp](/fast_gicp/thirdparty/Eigen/test/diagonal.cpp) | C++ | 75 | 10 | 21 | 106 |
| [fast_gicp/thirdparty/Eigen/test/diagonal_matrix_variadic_ctor.cpp](/fast_gicp/thirdparty/Eigen/test/diagonal_matrix_variadic_ctor.cpp) | C++ | 153 | 12 | 21 | 186 |
| [fast_gicp/thirdparty/Eigen/test/diagonalmatrices.cpp](/fast_gicp/thirdparty/Eigen/test/diagonalmatrices.cpp) | C++ | 134 | 10 | 30 | 174 |
| [fast_gicp/thirdparty/Eigen/test/dontalign.cpp](/fast_gicp/thirdparty/Eigen/test/dontalign.cpp) | C++ | 45 | 9 | 9 | 63 |
| [fast_gicp/thirdparty/Eigen/test/dynalloc.cpp](/fast_gicp/thirdparty/Eigen/test/dynalloc.cpp) | C++ | 137 | 18 | 23 | 178 |
| [fast_gicp/thirdparty/Eigen/test/eigen2support.cpp](/fast_gicp/thirdparty/Eigen/test/eigen2support.cpp) | C++ | 45 | 9 | 12 | 66 |
| [fast_gicp/thirdparty/Eigen/test/eigensolver_complex.cpp](/fast_gicp/thirdparty/Eigen/test/eigensolver_complex.cpp) | C++ | 124 | 25 | 28 | 177 |
| [fast_gicp/thirdparty/Eigen/test/eigensolver_generalized_real.cpp](/fast_gicp/thirdparty/Eigen/test/eigensolver_generalized_real.cpp) | C++ | 69 | 21 | 14 | 104 |
| [fast_gicp/thirdparty/Eigen/test/eigensolver_generic.cpp](/fast_gicp/thirdparty/Eigen/test/eigensolver_generic.cpp) | C++ | 193 | 27 | 28 | 248 |
| [fast_gicp/thirdparty/Eigen/test/eigensolver_selfadjoint.cpp](/fast_gicp/thirdparty/Eigen/test/eigensolver_selfadjoint.cpp) | C++ | 210 | 27 | 45 | 282 |
| [fast_gicp/thirdparty/Eigen/test/evaluator_common.h](/fast_gicp/thirdparty/Eigen/test/evaluator_common.h) | C++ | 0 | 0 | 1 | 1 |
| [fast_gicp/thirdparty/Eigen/test/evaluators.cpp](/fast_gicp/thirdparty/Eigen/test/evaluators.cpp) | C++ | 401 | 37 | 88 | 526 |
| [fast_gicp/thirdparty/Eigen/test/exceptions.cpp](/fast_gicp/thirdparty/Eigen/test/exceptions.cpp) | C++ | 31 | 11 | 8 | 50 |
| [fast_gicp/thirdparty/Eigen/test/fastmath.cpp](/fast_gicp/thirdparty/Eigen/test/fastmath.cpp) | C++ | 84 | 8 | 8 | 100 |
| [fast_gicp/thirdparty/Eigen/test/first_aligned.cpp](/fast_gicp/thirdparty/Eigen/test/first_aligned.cpp) | C++ | 35 | 8 | 9 | 52 |
| [fast_gicp/thirdparty/Eigen/test/geo_alignedbox.cpp](/fast_gicp/thirdparty/Eigen/test/geo_alignedbox.cpp) | C++ | 372 | 50 | 110 | 532 |
| [fast_gicp/thirdparty/Eigen/test/geo_eulerangles.cpp](/fast_gicp/thirdparty/Eigen/test/geo_eulerangles.cpp) | C++ | 81 | 13 | 19 | 113 |
| [fast_gicp/thirdparty/Eigen/test/geo_homogeneous.cpp](/fast_gicp/thirdparty/Eigen/test/geo_homogeneous.cpp) | C++ | 84 | 13 | 29 | 126 |
| [fast_gicp/thirdparty/Eigen/test/geo_hyperplane.cpp](/fast_gicp/thirdparty/Eigen/test/geo_hyperplane.cpp) | C++ | 149 | 17 | 32 | 198 |
| [fast_gicp/thirdparty/Eigen/test/geo_orthomethods.cpp](/fast_gicp/thirdparty/Eigen/test/geo_orthomethods.cpp) | C++ | 94 | 17 | 23 | 134 |
| [fast_gicp/thirdparty/Eigen/test/geo_parametrizedline.cpp](/fast_gicp/thirdparty/Eigen/test/geo_parametrizedline.cpp) | C++ | 95 | 15 | 21 | 131 |
| [fast_gicp/thirdparty/Eigen/test/geo_quaternion.cpp](/fast_gicp/thirdparty/Eigen/test/geo_quaternion.cpp) | C++ | 243 | 38 | 60 | 341 |
| [fast_gicp/thirdparty/Eigen/test/geo_transformations.cpp](/fast_gicp/thirdparty/Eigen/test/geo_transformations.cpp) | C++ | 551 | 60 | 126 | 737 |
| [fast_gicp/thirdparty/Eigen/test/gpu_basic.cu](/fast_gicp/thirdparty/Eigen/test/gpu_basic.cu) | CUDA C++ | 355 | 58 | 50 | 463 |
| [fast_gicp/thirdparty/Eigen/test/gpu_common.h](/fast_gicp/thirdparty/Eigen/test/gpu_common.h) | C++ | 139 | 5 | 33 | 177 |
| [fast_gicp/thirdparty/Eigen/test/half_float.cpp](/fast_gicp/thirdparty/Eigen/test/half_float.cpp) | C++ | 263 | 34 | 53 | 350 |
| [fast_gicp/thirdparty/Eigen/test/hessenberg.cpp](/fast_gicp/thirdparty/Eigen/test/hessenberg.cpp) | C++ | 40 | 14 | 9 | 63 |
| [fast_gicp/thirdparty/Eigen/test/householder.cpp](/fast_gicp/thirdparty/Eigen/test/householder.cpp) | C++ | 116 | 14 | 19 | 149 |
| [fast_gicp/thirdparty/Eigen/test/incomplete_cholesky.cpp](/fast_gicp/thirdparty/Eigen/test/incomplete_cholesky.cpp) | C++ | 49 | 11 | 10 | 70 |
| [fast_gicp/thirdparty/Eigen/test/indexed_view.cpp](/fast_gicp/thirdparty/Eigen/test/indexed_view.cpp) | C++ | 359 | 33 | 82 | 474 |
| [fast_gicp/thirdparty/Eigen/test/initializer_list_construction.cpp](/fast_gicp/thirdparty/Eigen/test/initializer_list_construction.cpp) | C++ | 342 | 8 | 36 | 386 |
| [fast_gicp/thirdparty/Eigen/test/inplace_decomposition.cpp](/fast_gicp/thirdparty/Eigen/test/inplace_decomposition.cpp) | C++ | 76 | 13 | 22 | 111 |
| [fast_gicp/thirdparty/Eigen/test/integer_types.cpp](/fast_gicp/thirdparty/Eigen/test/integer_types.cpp) | C++ | 122 | 14 | 38 | 174 |
| [fast_gicp/thirdparty/Eigen/test/inverse.cpp](/fast_gicp/thirdparty/Eigen/test/inverse.cpp) | C++ | 106 | 19 | 26 | 151 |
| [fast_gicp/thirdparty/Eigen/test/io.cpp](/fast_gicp/thirdparty/Eigen/test/io.cpp) | C++ | 55 | 8 | 9 | 72 |
| [fast_gicp/thirdparty/Eigen/test/is_same_dense.cpp](/fast_gicp/thirdparty/Eigen/test/is_same_dense.cpp) | C++ | 24 | 8 | 10 | 42 |
| [fast_gicp/thirdparty/Eigen/test/jacobi.cpp](/fast_gicp/thirdparty/Eigen/test/jacobi.cpp) | C++ | 57 | 10 | 14 | 81 |
| [fast_gicp/thirdparty/Eigen/test/jacobisvd.cpp](/fast_gicp/thirdparty/Eigen/test/jacobisvd.cpp) | C++ | 99 | 20 | 26 | 145 |
| [fast_gicp/thirdparty/Eigen/test/klu_support.cpp](/fast_gicp/thirdparty/Eigen/test/klu_support.cpp) | C++ | 15 | 10 | 8 | 33 |
| [fast_gicp/thirdparty/Eigen/test/linearstructure.cpp](/fast_gicp/thirdparty/Eigen/test/linearstructure.cpp) | C++ | 106 | 19 | 23 | 148 |
| [fast_gicp/thirdparty/Eigen/test/lscg.cpp](/fast_gicp/thirdparty/Eigen/test/lscg.cpp) | C++ | 22 | 8 | 8 | 38 |
| [fast_gicp/thirdparty/Eigen/test/lu.cpp](/fast_gicp/thirdparty/Eigen/test/lu.cpp) | C++ | 182 | 28 | 43 | 253 |
| [fast_gicp/thirdparty/Eigen/test/main.h](/fast_gicp/thirdparty/Eigen/test/main.h) | C++ | 636 | 150 | 117 | 903 |
| [fast_gicp/thirdparty/Eigen/test/mapped_matrix.cpp](/fast_gicp/thirdparty/Eigen/test/mapped_matrix.cpp) | C++ | 162 | 14 | 32 | 208 |
| [fast_gicp/thirdparty/Eigen/test/mapstaticmethods.cpp](/fast_gicp/thirdparty/Eigen/test/mapstaticmethods.cpp) | C++ | 135 | 10 | 33 | 178 |
| [fast_gicp/thirdparty/Eigen/test/mapstride.cpp](/fast_gicp/thirdparty/Eigen/test/mapstride.cpp) | C++ | 208 | 15 | 38 | 261 |
| [fast_gicp/thirdparty/Eigen/test/meta.cpp](/fast_gicp/thirdparty/Eigen/test/meta.cpp) | C++ | 114 | 21 | 24 | 159 |
| [fast_gicp/thirdparty/Eigen/test/metis_support.cpp](/fast_gicp/thirdparty/Eigen/test/metis_support.cpp) | C++ | 13 | 8 | 5 | 26 |
| [fast_gicp/thirdparty/Eigen/test/miscmatrices.cpp](/fast_gicp/thirdparty/Eigen/test/miscmatrices.cpp) | C++ | 31 | 11 | 5 | 47 |
| [fast_gicp/thirdparty/Eigen/test/mixingtypes.cpp](/fast_gicp/thirdparty/Eigen/test/mixingtypes.cpp) | C++ | 226 | 42 | 62 | 330 |
| [fast_gicp/thirdparty/Eigen/test/mpl2only.cpp](/fast_gicp/thirdparty/Eigen/test/mpl2only.cpp) | C++ | 14 | 8 | 3 | 25 |
| [fast_gicp/thirdparty/Eigen/test/nestbyvalue.cpp](/fast_gicp/thirdparty/Eigen/test/nestbyvalue.cpp) | C++ | 24 | 8 | 6 | 38 |
| [fast_gicp/thirdparty/Eigen/test/nesting_ops.cpp](/fast_gicp/thirdparty/Eigen/test/nesting_ops.cpp) | C++ | 78 | 12 | 18 | 108 |
| [fast_gicp/thirdparty/Eigen/test/nomalloc.cpp](/fast_gicp/thirdparty/Eigen/test/nomalloc.cpp) | C++ | 156 | 31 | 42 | 229 |
| [fast_gicp/thirdparty/Eigen/test/nullary.cpp](/fast_gicp/thirdparty/Eigen/test/nullary.cpp) | C++ | 259 | 28 | 55 | 342 |
| [fast_gicp/thirdparty/Eigen/test/num_dimensions.cpp](/fast_gicp/thirdparty/Eigen/test/num_dimensions.cpp) | C++ | 67 | 8 | 16 | 91 |
| [fast_gicp/thirdparty/Eigen/test/numext.cpp](/fast_gicp/thirdparty/Eigen/test/numext.cpp) | C++ | 223 | 21 | 32 | 276 |
| [fast_gicp/thirdparty/Eigen/test/packetmath.cpp](/fast_gicp/thirdparty/Eigen/test/packetmath.cpp) | C++ | 1,070 | 75 | 158 | 1,303 |
| [fast_gicp/thirdparty/Eigen/test/packetmath_test_shared.h](/fast_gicp/thirdparty/Eigen/test/packetmath_test_shared.h) | C++ | 215 | 18 | 43 | 276 |
| [fast_gicp/thirdparty/Eigen/test/pardiso_support.cpp](/fast_gicp/thirdparty/Eigen/test/pardiso_support.cpp) | C++ | 22 | 3 | 5 | 30 |
| [fast_gicp/thirdparty/Eigen/test/pastix_support.cpp](/fast_gicp/thirdparty/Eigen/test/pastix_support.cpp) | C++ | 35 | 12 | 8 | 55 |
| [fast_gicp/thirdparty/Eigen/test/permutationmatrices.cpp](/fast_gicp/thirdparty/Eigen/test/permutationmatrices.cpp) | C++ | 139 | 11 | 32 | 182 |
| [fast_gicp/thirdparty/Eigen/test/prec_inverse_4x4.cpp](/fast_gicp/thirdparty/Eigen/test/prec_inverse_4x4.cpp) | C++ | 65 | 10 | 8 | 83 |
| [fast_gicp/thirdparty/Eigen/test/product.h](/fast_gicp/thirdparty/Eigen/test/product.h) | C++ | 187 | 38 | 35 | 260 |
| [fast_gicp/thirdparty/Eigen/test/product_extra.cpp](/fast_gicp/thirdparty/Eigen/test/product_extra.cpp) | C++ | 306 | 37 | 48 | 391 |
| [fast_gicp/thirdparty/Eigen/test/product_large.cpp](/fast_gicp/thirdparty/Eigen/test/product_large.cpp) | C++ | 97 | 18 | 17 | 132 |
| [fast_gicp/thirdparty/Eigen/test/product_mmtr.cpp](/fast_gicp/thirdparty/Eigen/test/product_mmtr.cpp) | C++ | 79 | 11 | 17 | 107 |
| [fast_gicp/thirdparty/Eigen/test/product_notemporary.cpp](/fast_gicp/thirdparty/Eigen/test/product_notemporary.cpp) | C++ | 149 | 24 | 37 | 210 |
| [fast_gicp/thirdparty/Eigen/test/product_selfadjoint.cpp](/fast_gicp/thirdparty/Eigen/test/product_selfadjoint.cpp) | C++ | 61 | 9 | 17 | 87 |
| [fast_gicp/thirdparty/Eigen/test/product_small.cpp](/fast_gicp/thirdparty/Eigen/test/product_small.cpp) | C++ | 270 | 18 | 36 | 324 |
| [fast_gicp/thirdparty/Eigen/test/product_symm.cpp](/fast_gicp/thirdparty/Eigen/test/product_symm.cpp) | C++ | 87 | 11 | 28 | 126 |
| [fast_gicp/thirdparty/Eigen/test/product_syrk.cpp](/fast_gicp/thirdparty/Eigen/test/product_syrk.cpp) | C++ | 108 | 10 | 29 | 147 |
| [fast_gicp/thirdparty/Eigen/test/product_trmm.cpp](/fast_gicp/thirdparty/Eigen/test/product_trmm.cpp) | C++ | 102 | 11 | 25 | 138 |
| [fast_gicp/thirdparty/Eigen/test/product_trmv.cpp](/fast_gicp/thirdparty/Eigen/test/product_trmv.cpp) | C++ | 60 | 14 | 17 | 91 |
| [fast_gicp/thirdparty/Eigen/test/product_trsolve.cpp](/fast_gicp/thirdparty/Eigen/test/product_trsolve.cpp) | C++ | 93 | 13 | 22 | 128 |
| [fast_gicp/thirdparty/Eigen/test/qr.cpp](/fast_gicp/thirdparty/Eigen/test/qr.cpp) | C++ | 91 | 14 | 26 | 131 |
| [fast_gicp/thirdparty/Eigen/test/qr_colpivoting.cpp](/fast_gicp/thirdparty/Eigen/test/qr_colpivoting.cpp) | C++ | 293 | 25 | 51 | 369 |
| [fast_gicp/thirdparty/Eigen/test/qr_fullpivoting.cpp](/fast_gicp/thirdparty/Eigen/test/qr_fullpivoting.cpp) | C++ | 120 | 14 | 26 | 160 |
| [fast_gicp/thirdparty/Eigen/test/qtvector.cpp](/fast_gicp/thirdparty/Eigen/test/qtvector.cpp) | C++ | 119 | 21 | 17 | 157 |
| [fast_gicp/thirdparty/Eigen/test/rand.cpp](/fast_gicp/thirdparty/Eigen/test/rand.cpp) | C++ | 96 | 8 | 15 | 119 |
| [fast_gicp/thirdparty/Eigen/test/random_without_cast_overflow.h](/fast_gicp/thirdparty/Eigen/test/random_without_cast_overflow.h) | C++ | 112 | 25 | 16 | 153 |
| [fast_gicp/thirdparty/Eigen/test/real_qz.cpp](/fast_gicp/thirdparty/Eigen/test/real_qz.cpp) | C++ | 66 | 17 | 12 | 95 |
| [fast_gicp/thirdparty/Eigen/test/redux.cpp](/fast_gicp/thirdparty/Eigen/test/redux.cpp) | C++ | 143 | 19 | 22 | 184 |
| [fast_gicp/thirdparty/Eigen/test/ref.cpp](/fast_gicp/thirdparty/Eigen/test/ref.cpp) | C++ | 281 | 22 | 58 | 361 |
| [fast_gicp/thirdparty/Eigen/test/reshape.cpp](/fast_gicp/thirdparty/Eigen/test/reshape.cpp) | C++ | 167 | 19 | 31 | 217 |
| [fast_gicp/thirdparty/Eigen/test/resize.cpp](/fast_gicp/thirdparty/Eigen/test/resize.cpp) | C++ | 27 | 8 | 7 | 42 |
| [fast_gicp/thirdparty/Eigen/test/rvalue_types.cpp](/fast_gicp/thirdparty/Eigen/test/rvalue_types.cpp) | C++ | 106 | 22 | 30 | 158 |
| [fast_gicp/thirdparty/Eigen/test/schur_complex.cpp](/fast_gicp/thirdparty/Eigen/test/schur_complex.cpp) | C++ | 65 | 15 | 12 | 92 |
| [fast_gicp/thirdparty/Eigen/test/schur_real.cpp](/fast_gicp/thirdparty/Eigen/test/schur_real.cpp) | C++ | 79 | 18 | 14 | 111 |
| [fast_gicp/thirdparty/Eigen/test/selfadjoint.cpp](/fast_gicp/thirdparty/Eigen/test/selfadjoint.cpp) | C++ | 48 | 11 | 17 | 76 |
| [fast_gicp/thirdparty/Eigen/test/simplicial_cholesky.cpp](/fast_gicp/thirdparty/Eigen/test/simplicial_cholesky.cpp) | C++ | 36 | 8 | 7 | 51 |
| [fast_gicp/thirdparty/Eigen/test/sizeof.cpp](/fast_gicp/thirdparty/Eigen/test/sizeof.cpp) | C++ | 35 | 8 | 5 | 48 |
| [fast_gicp/thirdparty/Eigen/test/sizeoverflow.cpp](/fast_gicp/thirdparty/Eigen/test/sizeoverflow.cpp) | C++ | 40 | 12 | 13 | 65 |
| [fast_gicp/thirdparty/Eigen/test/smallvectors.cpp](/fast_gicp/thirdparty/Eigen/test/smallvectors.cpp) | C++ | 53 | 8 | 7 | 68 |
| [fast_gicp/thirdparty/Eigen/test/solverbase.h](/fast_gicp/thirdparty/Eigen/test/solverbase.h) | C++ | 34 | 4 | 3 | 41 |
| [fast_gicp/thirdparty/Eigen/test/sparse.h](/fast_gicp/thirdparty/Eigen/test/sparse.h) | C++ | 163 | 20 | 22 | 205 |
| [fast_gicp/thirdparty/Eigen/test/sparseLM.cpp](/fast_gicp/thirdparty/Eigen/test/sparseLM.cpp) | C++ | 141 | 19 | 17 | 177 |
| [fast_gicp/thirdparty/Eigen/test/sparse_basic.cpp](/fast_gicp/thirdparty/Eigen/test/sparse_basic.cpp) | C++ | 619 | 47 | 95 | 761 |
| [fast_gicp/thirdparty/Eigen/test/sparse_block.cpp](/fast_gicp/thirdparty/Eigen/test/sparse_block.cpp) | C++ | 264 | 15 | 44 | 323 |
| [fast_gicp/thirdparty/Eigen/test/sparse_permutations.cpp](/fast_gicp/thirdparty/Eigen/test/sparse_permutations.cpp) | C++ | 171 | 11 | 55 | 237 |
| [fast_gicp/thirdparty/Eigen/test/sparse_product.cpp](/fast_gicp/thirdparty/Eigen/test/sparse_product.cpp) | C++ | 365 | 37 | 76 | 478 |
| [fast_gicp/thirdparty/Eigen/test/sparse_ref.cpp](/fast_gicp/thirdparty/Eigen/test/sparse_ref.cpp) | C++ | 100 | 14 | 26 | 140 |
| [fast_gicp/thirdparty/Eigen/test/sparse_solver.h](/fast_gicp/thirdparty/Eigen/test/sparse_solver.h) | C++ | 561 | 43 | 96 | 700 |
| [fast_gicp/thirdparty/Eigen/test/sparse_solvers.cpp](/fast_gicp/thirdparty/Eigen/test/sparse_solvers.cpp) | C++ | 90 | 19 | 17 | 126 |
| [fast_gicp/thirdparty/Eigen/test/sparse_vector.cpp](/fast_gicp/thirdparty/Eigen/test/sparse_vector.cpp) | C++ | 116 | 16 | 32 | 164 |
| [fast_gicp/thirdparty/Eigen/test/sparselu.cpp](/fast_gicp/thirdparty/Eigen/test/sparselu.cpp) | C++ | 26 | 11 | 9 | 46 |
| [fast_gicp/thirdparty/Eigen/test/sparseqr.cpp](/fast_gicp/thirdparty/Eigen/test/sparseqr.cpp) | C++ | 103 | 27 | 20 | 150 |
| [fast_gicp/thirdparty/Eigen/test/special_numbers.cpp](/fast_gicp/thirdparty/Eigen/test/special_numbers.cpp) | C++ | 41 | 8 | 10 | 59 |
| [fast_gicp/thirdparty/Eigen/test/split_test_helper.h](/fast_gicp/thirdparty/Eigen/test/split_test_helper.h) | C++ | 4,995 | 0 | 1,000 | 5,995 |
| [fast_gicp/thirdparty/Eigen/test/spqr_support.cpp](/fast_gicp/thirdparty/Eigen/test/spqr_support.cpp) | C++ | 50 | 8 | 7 | 65 |
| [fast_gicp/thirdparty/Eigen/test/stable_norm.cpp](/fast_gicp/thirdparty/Eigen/test/stable_norm.cpp) | C++ | 185 | 26 | 35 | 246 |
| [fast_gicp/thirdparty/Eigen/test/stddeque.cpp](/fast_gicp/thirdparty/Eigen/test/stddeque.cpp) | C++ | 101 | 14 | 16 | 131 |
| [fast_gicp/thirdparty/Eigen/test/stddeque_overload.cpp](/fast_gicp/thirdparty/Eigen/test/stddeque_overload.cpp) | C++ | 118 | 20 | 21 | 159 |
| [fast_gicp/thirdparty/Eigen/test/stdlist.cpp](/fast_gicp/thirdparty/Eigen/test/stdlist.cpp) | C++ | 101 | 14 | 16 | 131 |
| [fast_gicp/thirdparty/Eigen/test/stdlist_overload.cpp](/fast_gicp/thirdparty/Eigen/test/stdlist_overload.cpp) | C++ | 150 | 20 | 23 | 193 |
| [fast_gicp/thirdparty/Eigen/test/stdvector.cpp](/fast_gicp/thirdparty/Eigen/test/stdvector.cpp) | C++ | 119 | 23 | 17 | 159 |
| [fast_gicp/thirdparty/Eigen/test/stdvector_overload.cpp](/fast_gicp/thirdparty/Eigen/test/stdvector_overload.cpp) | C++ | 121 | 20 | 21 | 162 |
| [fast_gicp/thirdparty/Eigen/test/stl_iterators.cpp](/fast_gicp/thirdparty/Eigen/test/stl_iterators.cpp) | C++ | 427 | 52 | 84 | 563 |
| [fast_gicp/thirdparty/Eigen/test/superlu_support.cpp](/fast_gicp/thirdparty/Eigen/test/superlu_support.cpp) | C++ | 12 | 8 | 4 | 24 |
| [fast_gicp/thirdparty/Eigen/test/svd_common.h](/fast_gicp/thirdparty/Eigen/test/svd_common.h) | C++ | 393 | 44 | 76 | 513 |
| [fast_gicp/thirdparty/Eigen/test/svd_fill.h](/fast_gicp/thirdparty/Eigen/test/svd_fill.h) | C++ | 94 | 13 | 12 | 119 |
| [fast_gicp/thirdparty/Eigen/test/swap.cpp](/fast_gicp/thirdparty/Eigen/test/swap.cpp) | C++ | 66 | 15 | 14 | 95 |
| [fast_gicp/thirdparty/Eigen/test/symbolic_index.cpp](/fast_gicp/thirdparty/Eigen/test/symbolic_index.cpp) | C++ | 58 | 10 | 17 | 85 |
| [fast_gicp/thirdparty/Eigen/test/triangular.cpp](/fast_gicp/thirdparty/Eigen/test/triangular.cpp) | C++ | 216 | 27 | 50 | 293 |
| [fast_gicp/thirdparty/Eigen/test/type_alias.cpp](/fast_gicp/thirdparty/Eigen/test/type_alias.cpp) | C++ | 31 | 9 | 9 | 49 |
| [fast_gicp/thirdparty/Eigen/test/umeyama.cpp](/fast_gicp/thirdparty/Eigen/test/umeyama.cpp) | C++ | 115 | 26 | 43 | 184 |
| [fast_gicp/thirdparty/Eigen/test/umfpack_support.cpp](/fast_gicp/thirdparty/Eigen/test/umfpack_support.cpp) | C++ | 19 | 8 | 8 | 35 |
| [fast_gicp/thirdparty/Eigen/test/unalignedassert.cpp](/fast_gicp/thirdparty/Eigen/test/unalignedassert.cpp) | C++ | 145 | 15 | 21 | 181 |
| [fast_gicp/thirdparty/Eigen/test/unalignedcount.cpp](/fast_gicp/thirdparty/Eigen/test/unalignedcount.cpp) | C++ | 45 | 9 | 7 | 61 |
| [fast_gicp/thirdparty/Eigen/test/upperbidiagonalization.cpp](/fast_gicp/thirdparty/Eigen/test/upperbidiagonalization.cpp) | C++ | 30 | 8 | 6 | 44 |
| [fast_gicp/thirdparty/Eigen/test/vectorization_logic.cpp](/fast_gicp/thirdparty/Eigen/test/vectorization_logic.cpp) | C++ | 334 | 14 | 82 | 430 |
| [fast_gicp/thirdparty/Eigen/test/vectorwiseop.cpp](/fast_gicp/thirdparty/Eigen/test/vectorwiseop.cpp) | C++ | 214 | 26 | 59 | 299 |
| [fast_gicp/thirdparty/Eigen/test/visitor.cpp](/fast_gicp/thirdparty/Eigen/test/visitor.cpp) | C++ | 163 | 12 | 19 | 194 |
| [fast_gicp/thirdparty/Eigen/test/zerosized.cpp](/fast_gicp/thirdparty/Eigen/test/zerosized.cpp) | C++ | 87 | 9 | 16 | 112 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/README.md](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/README.md) | Markdown | 1,352 | 0 | 464 | 1,816 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/Tensor.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/Tensor.h) | C++ | 420 | 81 | 54 | 555 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorArgMax.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorArgMax.h) | C++ | 250 | 31 | 49 | 330 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorAssign.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorAssign.h) | C++ | 176 | 33 | 39 | 248 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorBase.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorBase.h) | C++ | 980 | 49 | 148 | 1,177 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorBlock.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorBlock.h) | C++ | 1,018 | 303 | 239 | 1,560 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorBroadcasting.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorBroadcasting.h) | C++ | 831 | 132 | 131 | 1,094 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorChipping.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorChipping.h) | C++ | 405 | 42 | 72 | 519 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorConcatenation.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorConcatenation.h) | C++ | 306 | 29 | 43 | 378 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContraction.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContraction.h) | C++ | 748 | 136 | 140 | 1,024 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionBlocking.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionBlocking.h) | C++ | 38 | 22 | 14 | 74 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionCuda.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionCuda.h) | C++ | 4 | 0 | 3 | 7 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionGpu.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionGpu.h) | C++ | 1,143 | 131 | 140 | 1,414 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionMapper.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionMapper.h) | C++ | 453 | 32 | 91 | 576 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionSycl.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionSycl.h) | C++ | 1,087 | 447 | 117 | 1,651 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionThreadPool.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorContractionThreadPool.h) | C++ | 1,086 | 385 | 209 | 1,680 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorConversion.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorConversion.h) | C++ | 357 | 28 | 72 | 457 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorConvolution.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorConvolution.h) | C++ | 937 | 43 | 153 | 1,133 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorConvolutionSycl.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorConvolutionSycl.h) | C++ | 444 | 38 | 63 | 545 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorCostModel.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorCostModel.h) | C++ | 146 | 46 | 23 | 215 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorCustomOp.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorCustomOp.h) | C++ | 253 | 32 | 63 | 348 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDevice.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDevice.h) | C++ | 81 | 33 | 24 | 138 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceCuda.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceCuda.h) | C++ | 4 | 0 | 3 | 7 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceDefault.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceDefault.h) | C++ | 81 | 24 | 11 | 116 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceGpu.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceGpu.h) | C++ | 325 | 46 | 58 | 429 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceSycl.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceSycl.h) | C++ | 884 | 124 | 96 | 1,104 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceThreadPool.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceThreadPool.h) | C++ | 278 | 81 | 56 | 415 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDimensionList.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDimensionList.h) | C++ | 194 | 17 | 26 | 237 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDimensions.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorDimensions.h) | C++ | 390 | 38 | 63 | 491 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorEvalTo.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorEvalTo.h) | C++ | 164 | 25 | 48 | 237 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorEvaluator.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorEvaluator.h) | C++ | 758 | 68 | 158 | 984 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorExecutor.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorExecutor.h) | C++ | 517 | 84 | 103 | 704 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorExpr.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorExpr.h) | C++ | 285 | 37 | 67 | 389 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorFFT.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorFFT.h) | C++ | 534 | 62 | 74 | 670 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorFixedSize.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorFixedSize.h) | C++ | 301 | 35 | 44 | 380 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorForcedEval.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorForcedEval.h) | C++ | 174 | 23 | 41 | 238 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorForwardDeclarations.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorForwardDeclarations.h) | C++ | 132 | 24 | 36 | 192 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorFunctors.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorFunctors.h) | C++ | 426 | 17 | 46 | 489 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorGenerator.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorGenerator.h) | C++ | 225 | 31 | 47 | 303 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorGlobalFunctions.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorGlobalFunctions.h) | C++ | 15 | 13 | 6 | 34 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorGpuHipCudaDefines.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorGpuHipCudaDefines.h) | C++ | 69 | 21 | 12 | 102 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorGpuHipCudaUndefines.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorGpuHipCudaUndefines.h) | C++ | 30 | 9 | 7 | 46 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorIO.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorIO.h) | C++ | 51 | 14 | 15 | 80 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorImagePatch.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorImagePatch.h) | C++ | 454 | 74 | 76 | 604 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorIndexList.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorIndexList.h) | C++ | 574 | 31 | 134 | 739 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorInflation.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorInflation.h) | C++ | 193 | 25 | 30 | 248 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorInitializer.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorInitializer.h) | C++ | 52 | 14 | 17 | 83 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorIntDiv.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorIntDiv.h) | C++ | 194 | 36 | 34 | 264 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorLayoutSwap.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorLayoutSwap.h) | C++ | 143 | 37 | 37 | 217 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorMacros.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorMacros.h) | C++ | 53 | 34 | 12 | 99 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorMap.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorMap.h) | C++ | 266 | 33 | 29 | 328 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorMeta.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorMeta.h) | C++ | 241 | 13 | 58 | 312 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorMorphing.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorMorphing.h) | C++ | 881 | 77 | 145 | 1,103 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorPadding.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorPadding.h) | C++ | 517 | 89 | 103 | 709 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorPatch.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorPatch.h) | C++ | 229 | 21 | 42 | 292 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorRandom.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorRandom.h) | C++ | 221 | 63 | 39 | 323 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorReduction.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorReduction.h) | C++ | 818 | 75 | 106 | 999 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorReductionCuda.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorReductionCuda.h) | C++ | 4 | 0 | 3 | 7 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorReductionGpu.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorReductionGpu.h) | C++ | 791 | 70 | 106 | 967 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorReductionSycl.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorReductionSycl.h) | C++ | 448 | 76 | 59 | 583 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorRef.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorRef.h) | C++ | 365 | 25 | 65 | 455 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorReverse.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorReverse.h) | C++ | 349 | 47 | 70 | 466 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorScan.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorScan.h) | C++ | 419 | 52 | 58 | 529 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorScanSycl.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorScanSycl.h) | C++ | 421 | 57 | 36 | 514 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorShuffling.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorShuffling.h) | C++ | 365 | 33 | 74 | 472 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorStorage.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorStorage.h) | C++ | 112 | 24 | 26 | 162 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorStriding.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorStriding.h) | C++ | 283 | 23 | 41 | 347 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorTrace.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorTrace.h) | C++ | 230 | 29 | 45 | 304 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorTraits.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorTraits.h) | C++ | 181 | 49 | 35 | 265 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorUInt128.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorUInt128.h) | C++ | 186 | 25 | 39 | 250 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorVolumePatch.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/Tensor/TensorVolumePatch.h) | C++ | 484 | 60 | 86 | 630 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/TensorSymmetry/DynamicSymmetry.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/TensorSymmetry/DynamicSymmetry.h) | C++ | 232 | 24 | 38 | 294 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/TensorSymmetry/StaticSymmetry.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/TensorSymmetry/StaticSymmetry.h) | C++ | 180 | 19 | 38 | 237 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/TensorSymmetry/Symmetry.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/TensorSymmetry/Symmetry.h) | C++ | 184 | 115 | 40 | 339 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/TensorSymmetry/util/TemplateGroupTheory.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/TensorSymmetry/util/TemplateGroupTheory.h) | C++ | 371 | 250 | 49 | 670 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/Barrier.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/Barrier.h) | C++ | 39 | 18 | 11 | 68 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/EventCount.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/EventCount.h) | C++ | 161 | 71 | 18 | 250 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/NonBlockingThreadPool.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/NonBlockingThreadPool.h) | C++ | 351 | 93 | 43 | 487 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/RunQueue.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/RunQueue.h) | C++ | 150 | 68 | 19 | 237 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/ThreadCancel.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/ThreadCancel.h) | C++ | 10 | 9 | 5 | 24 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/ThreadEnvironment.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/ThreadEnvironment.h) | C++ | 21 | 11 | 9 | 41 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/ThreadLocal.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/ThreadLocal.h) | C++ | 153 | 102 | 47 | 302 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/ThreadPoolInterface.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/ThreadPoolInterface.h) | C++ | 17 | 21 | 11 | 49 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/ThreadYield.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/ThreadPool/ThreadYield.h) | C++ | 8 | 9 | 4 | 21 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/util/CXX11Meta.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/util/CXX11Meta.h) | C++ | 380 | 54 | 104 | 538 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/util/CXX11Workarounds.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/util/CXX11Workarounds.h) | C++ | 33 | 42 | 14 | 89 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/util/EmulateArray.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/util/EmulateArray.h) | C++ | 205 | 23 | 34 | 262 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/util/MaxSizeVector.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/CXX11/src/util/MaxSizeVector.h) | C++ | 104 | 29 | 26 | 159 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/AutoDiff/AutoDiffJacobian.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/AutoDiff/AutoDiffJacobian.h) | C++ | 78 | 11 | 20 | 109 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/AutoDiff/AutoDiffScalar.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/AutoDiff/AutoDiffScalar.h) | C++ | 512 | 106 | 113 | 731 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/AutoDiff/AutoDiffVector.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/AutoDiff/AutoDiffVector.h) | C++ | 144 | 43 | 34 | 221 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/BVH/BVAlgorithms.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/BVH/BVAlgorithms.h) | C++ | 208 | 40 | 46 | 294 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/BVH/KdBVH.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/BVH/KdBVH.h) | C++ | 151 | 38 | 35 | 224 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Eigenvalues/ArpackSelfAdjointEigenSolver.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Eigenvalues/ArpackSelfAdjointEigenSolver.h) | C++ | 411 | 273 | 107 | 791 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/EulerAngles/EulerAngles.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/EulerAngles/EulerAngles.h) | C++ | 145 | 174 | 37 | 356 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/EulerAngles/EulerSystem.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/EulerAngles/EulerSystem.h) | C++ | 168 | 92 | 46 | 306 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/FFT/ei_fftw_impl.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/FFT/ei_fftw_impl.h) | C++ | 209 | 22 | 31 | 262 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/FFT/ei_kissfft_impl.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/FFT/ei_kissfft_impl.h) | C++ | 373 | 27 | 50 | 450 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/ConstrainedConjGrad.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/ConstrainedConjGrad.h) | C++ | 115 | 44 | 29 | 188 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/DGMRES.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/DGMRES.h) | C++ | 320 | 138 | 54 | 512 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/GMRES.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/GMRES.h) | C++ | 158 | 120 | 58 | 336 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/IDRS.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/IDRS.h) | C++ | 230 | 140 | 67 | 437 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/IncompleteLU.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/IncompleteLU.h) | C++ | 68 | 8 | 15 | 91 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/IterationController.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/IterationController.h) | C++ | 70 | 61 | 24 | 155 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/MINRES.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/MINRES.h) | C++ | 142 | 91 | 35 | 268 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/Scaling.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/IterativeSolvers/Scaling.h) | C++ | 117 | 62 | 15 | 194 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/KroneckerProduct/KroneckerTensorProduct.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/KroneckerProduct/KroneckerTensorProduct.h) | C++ | 166 | 101 | 39 | 306 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/LevenbergMarquardt/LMcovar.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/LevenbergMarquardt/LMcovar.h) | C++ | 54 | 18 | 13 | 85 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/LevenbergMarquardt/LMonestep.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/LevenbergMarquardt/LMonestep.h) | C++ | 135 | 40 | 28 | 203 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/LevenbergMarquardt/LMpar.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/LevenbergMarquardt/LMpar.h) | C++ | 96 | 37 | 28 | 161 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/LevenbergMarquardt/LMqrsolv.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/LevenbergMarquardt/LMqrsolv.h) | C++ | 105 | 56 | 28 | 189 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/LevenbergMarquardt/LevenbergMarquardt.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/LevenbergMarquardt/LevenbergMarquardt.h) | C++ | 250 | 83 | 64 | 397 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/MatrixExponential.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/MatrixExponential.h) | C++ | 309 | 88 | 45 | 442 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/MatrixFunction.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/MatrixFunction.h) | C++ | 357 | 146 | 67 | 570 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/MatrixLogarithm.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/MatrixLogarithm.h) | C++ | 283 | 52 | 39 | 374 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/MatrixPower.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/MatrixPower.h) | C++ | 427 | 193 | 86 | 706 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/MatrixSquareRoot.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/MatrixSquareRoot.h) | C++ | 223 | 100 | 46 | 369 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/StemFunction.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MatrixFunctions/StemFunction.h) | C++ | 89 | 13 | 16 | 118 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MoreVectorization/MathFunctions.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/MoreVectorization/MathFunctions.h) | C++ | 54 | 18 | 24 | 96 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/HybridNonLinearSolver.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/HybridNonLinearSolver.h) | C++ | 410 | 89 | 103 | 602 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/LevenbergMarquardt.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/LevenbergMarquardt.h) | C++ | 455 | 96 | 107 | 658 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/chkder.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/chkder.h) | C++ | 55 | 2 | 10 | 67 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/covar.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/covar.h) | C++ | 52 | 8 | 11 | 71 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/dogleg.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/dogleg.h) | C++ | 71 | 19 | 18 | 108 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/fdjac1.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/fdjac1.h) | C++ | 66 | 4 | 10 | 80 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/lmpar.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/lmpar.h) | C++ | 201 | 50 | 48 | 299 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/qrsolv.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/qrsolv.h) | C++ | 50 | 23 | 19 | 92 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/r1mpyq.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/r1mpyq.h) | C++ | 21 | 3 | 7 | 31 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/r1updt.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/r1updt.h) | C++ | 63 | 20 | 17 | 100 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/rwupdt.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NonLinearOptimization/rwupdt.h) | C++ | 32 | 6 | 12 | 50 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NumericalDiff/NumericalDiff.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/NumericalDiff/NumericalDiff.h) | C++ | 82 | 32 | 17 | 131 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Polynomials/Companion.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Polynomials/Companion.h) | C++ | 180 | 56 | 45 | 281 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Polynomials/PolynomialSolver.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Polynomials/PolynomialSolver.h) | C++ | 255 | 129 | 45 | 429 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Polynomials/PolynomialUtils.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Polynomials/PolynomialUtils.h) | C++ | 73 | 53 | 18 | 144 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineInplaceLU.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineInplaceLU.h) | C++ | 210 | 69 | 74 | 353 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineMatrix.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineMatrix.h) | C++ | 635 | 80 | 148 | 863 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineMatrixBase.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineMatrixBase.h) | C++ | 108 | 63 | 42 | 213 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineProduct.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineProduct.h) | C++ | 207 | 31 | 58 | 296 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineStorage.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineStorage.h) | C++ | 199 | 17 | 44 | 260 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineUtil.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Skyline/SkylineUtil.h) | C++ | 63 | 8 | 19 | 90 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/BlockOfDynamicSparseMatrix.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/BlockOfDynamicSparseMatrix.h) | C++ | 79 | 20 | 24 | 123 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/BlockSparseMatrix.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/BlockSparseMatrix.h) | C++ | 729 | 248 | 103 | 1,080 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/DynamicSparseMatrix.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/DynamicSparseMatrix.h) | C++ | 269 | 76 | 60 | 405 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/MarketIO.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/MarketIO.h) | C++ | 232 | 12 | 39 | 283 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/MatrixMarketIterator.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/MatrixMarketIterator.h) | C++ | 165 | 53 | 30 | 248 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/RandomSetter.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SparseExtra/RandomSetter.h) | C++ | 208 | 111 | 31 | 350 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsArrayAPI.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsArrayAPI.h) | C++ | 101 | 168 | 18 | 287 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsBFloat16.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsBFloat16.h) | C++ | 57 | 6 | 6 | 69 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsFunctors.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsFunctors.h) | C++ | 235 | 103 | 20 | 358 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsHalf.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsHalf.h) | C++ | 55 | 6 | 6 | 67 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsImpl.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsImpl.h) | C++ | 1,086 | 771 | 103 | 1,960 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsPacketMath.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/BesselFunctionsPacketMath.h) | C++ | 67 | 32 | 20 | 119 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/HipVectorCompatibility.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/HipVectorCompatibility.h) | C++ | 54 | 0 | 14 | 68 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsArrayAPI.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsArrayAPI.h) | C++ | 65 | 88 | 15 | 168 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsBFloat16.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsBFloat16.h) | C++ | 47 | 6 | 6 | 59 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsFunctors.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsFunctors.h) | C++ | 225 | 84 | 22 | 331 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsHalf.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsHalf.h) | C++ | 47 | 6 | 6 | 59 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsImpl.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsImpl.h) | C++ | 1,218 | 601 | 227 | 2,046 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsPacketMath.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsPacketMath.h) | C++ | 38 | 23 | 19 | 80 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/AVX/BesselFunctions.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/AVX/BesselFunctions.h) | C++ | 31 | 0 | 16 | 47 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/AVX/SpecialFunctions.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/AVX/SpecialFunctions.h) | C++ | 11 | 0 | 6 | 17 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/AVX512/BesselFunctions.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/AVX512/BesselFunctions.h) | C++ | 31 | 0 | 16 | 47 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/AVX512/SpecialFunctions.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/AVX512/SpecialFunctions.h) | C++ | 11 | 0 | 6 | 17 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/GPU/SpecialFunctions.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/GPU/SpecialFunctions.h) | C++ | 302 | 11 | 57 | 370 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/NEON/BesselFunctions.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/NEON/BesselFunctions.h) | C++ | 46 | 0 | 9 | 55 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/NEON/SpecialFunctions.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/SpecialFunctions/arch/NEON/SpecialFunctions.h) | C++ | 26 | 0 | 9 | 35 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Splines/Spline.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Splines/Spline.h) | C++ | 279 | 152 | 77 | 508 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Splines/SplineFitting.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Splines/SplineFitting.h) | C++ | 247 | 123 | 62 | 432 |
| [fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Splines/SplineFwd.h](/fast_gicp/thirdparty/Eigen/unsupported/Eigen/src/Splines/SplineFwd.h) | C++ | 39 | 31 | 24 | 94 |
| [fast_gicp/thirdparty/Eigen/unsupported/bench/bench_svd.cpp](/fast_gicp/thirdparty/Eigen/unsupported/bench/bench_svd.cpp) | C++ | 80 | 16 | 28 | 124 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/BVH_Example.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/BVH_Example.cpp) | C++ | 38 | 2 | 11 | 51 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/EulerAngles.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/EulerAngles.cpp) | C++ | 26 | 9 | 12 | 47 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/FFT.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/FFT.cpp) | C++ | 97 | 4 | 18 | 119 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixExponential.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixExponential.cpp) | C++ | 13 | 0 | 4 | 17 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixFunction.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixFunction.cpp) | C++ | 18 | 0 | 6 | 24 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixLogarithm.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixLogarithm.cpp) | C++ | 13 | 0 | 3 | 16 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixPower.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixPower.cpp) | C++ | 14 | 0 | 3 | 17 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixPower_optimal.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixPower_optimal.cpp) | C++ | 14 | 0 | 4 | 18 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixSine.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixSine.cpp) | C++ | 13 | 2 | 6 | 21 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixSinh.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixSinh.cpp) | C++ | 13 | 2 | 6 | 21 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixSquareRoot.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/MatrixSquareRoot.cpp) | C++ | 13 | 0 | 4 | 17 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/PolynomialSolver1.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/PolynomialSolver1.cpp) | C++ | 45 | 0 | 9 | 54 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/PolynomialUtils1.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/PolynomialUtils1.cpp) | C++ | 18 | 0 | 3 | 21 |
| [fast_gicp/thirdparty/Eigen/unsupported/doc/examples/SYCL/CwiseMul.cpp](/fast_gicp/thirdparty/Eigen/unsupported/doc/examples/SYCL/CwiseMul.cpp) | C++ | 46 | 7 | 11 | 64 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/BVH.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/BVH.cpp) | C++ | 165 | 8 | 50 | 223 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/EulerAngles.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/EulerAngles.cpp) | C++ | 197 | 48 | 52 | 297 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/FFT.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/FFT.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/FFTW.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/FFTW.cpp) | C++ | 168 | 49 | 46 | 263 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/NonLinearOptimization.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/NonLinearOptimization.cpp) | C++ | 1,301 | 314 | 235 | 1,850 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/NumericalDiff.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/NumericalDiff.cpp) | C++ | 82 | 11 | 22 | 115 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/alignedvector3.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/alignedvector3.cpp) | C++ | 63 | 8 | 17 | 88 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/autodiff.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/autodiff.cpp) | C++ | 281 | 40 | 67 | 388 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/autodiff_scalar.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/autodiff_scalar.cpp) | C++ | 67 | 14 | 21 | 102 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/bessel_functions.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/bessel_functions.cpp) | C++ | 295 | 21 | 55 | 371 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_eventcount.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_eventcount.cpp) | C++ | 111 | 15 | 17 | 143 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_maxsizevector.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_maxsizevector.cpp) | C++ | 65 | 1 | 12 | 78 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_meta.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_meta.cpp) | C++ | 297 | 13 | 48 | 358 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_non_blocking_thread_pool.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_non_blocking_thread_pool.cpp) | C++ | 139 | 27 | 15 | 181 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_runqueue.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_runqueue.cpp) | C++ | 200 | 28 | 8 | 236 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_argmax.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_argmax.cpp) | C++ | 220 | 17 | 58 | 295 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_argmax_gpu.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_argmax_gpu.cu) | CUDA C++ | 180 | 16 | 58 | 254 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_argmax_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_argmax_sycl.cpp) | C++ | 194 | 21 | 44 | 259 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_assign.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_assign.cpp) | C++ | 305 | 11 | 49 | 365 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_block_access.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_block_access.cpp) | C++ | 484 | 39 | 54 | 577 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_block_eval.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_block_eval.cpp) | C++ | 613 | 72 | 174 | 859 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_block_io.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_block_io.cpp) | C++ | 313 | 45 | 88 | 446 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_broadcast_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_broadcast_sycl.cpp) | C++ | 106 | 14 | 25 | 145 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_broadcasting.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_broadcasting.cpp) | C++ | 276 | 9 | 47 | 332 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_builtins_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_builtins_sycl.cpp) | C++ | 310 | 19 | 26 | 355 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_cast_float16_gpu.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_cast_float16_gpu.cu) | CUDA C++ | 52 | 8 | 20 | 80 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_casts.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_casts.cpp) | C++ | 147 | 10 | 30 | 187 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_chipping.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_chipping.cpp) | C++ | 377 | 8 | 41 | 426 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_chipping_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_chipping_sycl.cpp) | C++ | 500 | 20 | 104 | 624 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_comparisons.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_comparisons.cpp) | C++ | 62 | 8 | 15 | 85 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_complex_cwise_ops_gpu.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_complex_cwise_ops_gpu.cu) | CUDA C++ | 78 | 8 | 17 | 103 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_complex_gpu.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_complex_gpu.cu) | CUDA C++ | 124 | 11 | 52 | 187 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_concatenation.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_concatenation.cpp) | C++ | 98 | 23 | 23 | 144 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_concatenation_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_concatenation_sycl.cpp) | C++ | 132 | 21 | 28 | 181 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_const.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_const.cpp) | C++ | 41 | 8 | 14 | 63 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_contract_gpu.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_contract_gpu.cu) | CUDA C++ | 158 | 16 | 45 | 219 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_contract_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_contract_sycl.cpp) | C++ | 871 | 41 | 115 | 1,027 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_contraction.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_contraction.cpp) | C++ | 474 | 28 | 100 | 602 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_convolution.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_convolution.cpp) | C++ | 115 | 14 | 22 | 151 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_convolution_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_convolution_sycl.cpp) | C++ | 358 | 18 | 94 | 470 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_custom_index.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_custom_index.cpp) | C++ | 71 | 8 | 22 | 101 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_custom_op.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_custom_op.cpp) | C++ | 85 | 8 | 19 | 112 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_custom_op_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_custom_op_sycl.cpp) | C++ | 132 | 12 | 27 | 171 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_device.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_device.cu) | CUDA C++ | 354 | 16 | 71 | 441 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_device_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_device_sycl.cpp) | C++ | 76 | 20 | 19 | 115 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_dimension.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_dimension.cpp) | C++ | 64 | 8 | 17 | 89 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_empty.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_empty.cpp) | C++ | 25 | 8 | 8 | 41 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_executor.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_executor.cpp) | C++ | 522 | 55 | 155 | 732 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_expr.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_expr.cpp) | C++ | 372 | 39 | 54 | 465 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_fft.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_fft.cpp) | C++ | 230 | 8 | 67 | 305 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_fixed_size.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_fixed_size.cpp) | C++ | 195 | 24 | 43 | 262 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_forced_eval.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_forced_eval.cpp) | C++ | 56 | 8 | 16 | 80 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_forced_eval_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_forced_eval_sycl.cpp) | C++ | 53 | 14 | 11 | 78 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_generator.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_generator.cpp) | C++ | 66 | 8 | 18 | 92 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_generator_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_generator_sycl.cpp) | C++ | 109 | 12 | 27 | 148 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_gpu.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_gpu.cu) | CUDA C++ | 1,291 | 22 | 331 | 1,644 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_ifft.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_ifft.cpp) | C++ | 115 | 9 | 31 | 155 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_image_op_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_image_op_sycl.cpp) | C++ | 69 | 13 | 22 | 104 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_image_patch.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_image_patch.cpp) | C++ | 658 | 87 | 65 | 810 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_image_patch_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_image_patch_sycl.cpp) | C++ | 892 | 84 | 117 | 1,093 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_index_list.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_index_list.cpp) | C++ | 320 | 8 | 58 | 386 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_inflation.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_inflation.cpp) | C++ | 61 | 8 | 13 | 82 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_inflation_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_inflation_sycl.cpp) | C++ | 95 | 17 | 25 | 137 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_intdiv.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_intdiv.cpp) | C++ | 113 | 12 | 23 | 148 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_io.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_io.cpp) | C++ | 98 | 8 | 31 | 137 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_layout_swap.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_layout_swap.cpp) | C++ | 41 | 8 | 13 | 62 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_layout_swap_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_layout_swap_sycl.cpp) | C++ | 81 | 20 | 26 | 127 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_lvalue.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_lvalue.cpp) | C++ | 25 | 8 | 10 | 43 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_map.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_map.cpp) | C++ | 254 | 12 | 62 | 328 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_math.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_math.cpp) | C++ | 27 | 8 | 12 | 47 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_math_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_math_sycl.cpp) | C++ | 71 | 13 | 22 | 106 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_mixed_indices.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_mixed_indices.cpp) | C++ | 35 | 8 | 11 | 54 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_morphing.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_morphing.cpp) | C++ | 475 | 18 | 73 | 566 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_morphing_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_morphing_sycl.cpp) | C++ | 309 | 14 | 64 | 387 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_move.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_move.cpp) | C++ | 51 | 10 | 16 | 77 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_notification.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_notification.cpp) | C++ | 39 | 13 | 13 | 65 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_of_complex.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_of_complex.cpp) | C++ | 75 | 9 | 20 | 104 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_of_const_values.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_of_const_values.cpp) | C++ | 77 | 8 | 21 | 106 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_of_float16_gpu.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_of_float16_gpu.cu) | CUDA C++ | 392 | 8 | 89 | 489 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_of_strings.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_of_strings.cpp) | C++ | 117 | 9 | 27 | 153 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_padding.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_padding.cpp) | C++ | 71 | 8 | 15 | 94 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_padding_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_padding_sycl.cpp) | C++ | 116 | 13 | 29 | 158 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_patch.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_patch.cpp) | C++ | 145 | 9 | 19 | 173 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_patch_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_patch_sycl.cpp) | C++ | 206 | 13 | 31 | 250 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_random.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_random.cpp) | C++ | 56 | 16 | 15 | 87 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_random_gpu.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_random_gpu.cu) | CUDA C++ | 50 | 12 | 25 | 87 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_random_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_random_sycl.cpp) | C++ | 67 | 16 | 18 | 101 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_reduction.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_reduction.cpp) | C++ | 449 | 15 | 69 | 533 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_reduction_gpu.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_reduction_gpu.cu) | CUDA C++ | 98 | 21 | 36 | 155 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_reduction_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_reduction_sycl.cpp) | C++ | 798 | 49 | 168 | 1,015 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_ref.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_ref.cpp) | C++ | 197 | 8 | 44 | 249 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_reverse.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_reverse.cpp) | C++ | 150 | 9 | 32 | 191 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_reverse_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_reverse_sycl.cpp) | C++ | 213 | 13 | 28 | 254 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_roundings.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_roundings.cpp) | C++ | 41 | 8 | 14 | 63 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_scan.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_scan.cpp) | C++ | 89 | 8 | 14 | 111 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_scan_gpu.cu](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_scan_gpu.cu) | CUDA C++ | 52 | 8 | 19 | 79 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_scan_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_scan_sycl.cpp) | C++ | 117 | 12 | 13 | 142 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_shuffling.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_shuffling.cpp) | C++ | 233 | 9 | 42 | 284 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_shuffling_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_shuffling_sycl.cpp) | C++ | 88 | 13 | 17 | 118 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_simple.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_simple.cpp) | C++ | 274 | 8 | 46 | 328 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_striding.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_striding.cpp) | C++ | 93 | 8 | 19 | 120 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_striding_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_striding_sycl.cpp) | C++ | 143 | 20 | 41 | 204 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_sugar.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_sugar.cpp) | C++ | 60 | 3 | 19 | 82 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_sycl.cpp) | C++ | 283 | 24 | 55 | 362 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_symmetry.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_symmetry.cpp) | C++ | 731 | 32 | 56 | 819 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_thread_local.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_thread_local.cpp) | C++ | 103 | 14 | 33 | 150 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_thread_pool.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_thread_pool.cpp) | C++ | 526 | 52 | 144 | 722 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_trace.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_trace.cpp) | C++ | 147 | 8 | 18 | 173 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_uint128.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_uint128.cpp) | C++ | 133 | 10 | 18 | 161 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_volume_patch.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_volume_patch.cpp) | C++ | 97 | 0 | 16 | 113 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_volume_patch_sycl.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/cxx11_tensor_volume_patch_sycl.cpp) | C++ | 163 | 21 | 39 | 223 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/dgmres.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/dgmres.cpp) | C++ | 15 | 12 | 5 | 32 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/forward_adolc.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/forward_adolc.cpp) | C++ | 106 | 13 | 23 | 142 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/gmres.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/gmres.cpp) | C++ | 15 | 12 | 5 | 32 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/idrs.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/idrs.cpp) | C++ | 14 | 9 | 5 | 28 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/kronecker_product.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/kronecker_product.cpp) | C++ | 194 | 20 | 39 | 253 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/levenberg_marquardt.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/levenberg_marquardt.cpp) | C++ | 1,040 | 268 | 170 | 1,478 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/matrix_exponential.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/matrix_exponential.cpp) | C++ | 110 | 11 | 21 | 142 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/matrix_function.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/matrix_function.cpp) | C++ | 175 | 21 | 32 | 228 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/matrix_functions.h](/fast_gicp/thirdparty/Eigen/unsupported/test/matrix_functions.h) | C++ | 49 | 10 | 9 | 68 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/matrix_power.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/matrix_power.cpp) | C++ | 159 | 12 | 34 | 205 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/matrix_square_root.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/matrix_square_root.cpp) | C++ | 20 | 8 | 4 | 32 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/minres.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/minres.cpp) | C++ | 20 | 15 | 10 | 45 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/mpreal/mpreal.h](/fast_gicp/thirdparty/Eigen/unsupported/test/mpreal/mpreal.h) | C++ | 2,357 | 291 | 537 | 3,185 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/mpreal_support.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/mpreal_support.cpp) | C++ | 49 | 6 | 11 | 66 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/openglsupport.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/openglsupport.cpp) | C++ | 501 | 39 | 61 | 601 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/polynomialsolver.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/polynomialsolver.cpp) | C++ | 167 | 22 | 44 | 233 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/polynomialutils.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/polynomialutils.cpp) | C++ | 88 | 8 | 18 | 114 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/sparse_extra.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/sparse_extra.cpp) | C++ | 135 | 42 | 33 | 210 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/special_functions.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/special_functions.cpp) | C++ | 361 | 82 | 55 | 498 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/special_packetmath.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/special_packetmath.cpp) | C++ | 110 | 19 | 21 | 150 |
| [fast_gicp/thirdparty/Eigen/unsupported/test/splines.cpp](/fast_gicp/thirdparty/Eigen/unsupported/test/splines.cpp) | C++ | 224 | 15 | 43 | 282 |
| [fast_gicp/thirdparty/Sophus/.travis.yml](/fast_gicp/thirdparty/Sophus/.travis.yml) | YAML | 73 | 0 | 11 | 84 |
| [fast_gicp/thirdparty/Sophus/README.rst](/fast_gicp/thirdparty/Sophus/README.rst) | reStructuredText | 20 | 6 | 12 | 38 |
| [fast_gicp/thirdparty/Sophus/appveyor.yml](/fast_gicp/thirdparty/Sophus/appveyor.yml) | YAML | 19 | 0 | 8 | 27 |
| [fast_gicp/thirdparty/Sophus/cmake_modules/FindEigen3.cmake](/fast_gicp/thirdparty/Sophus/cmake_modules/FindEigen3.cmake) | CMake | 66 | 0 | 17 | 83 |
| [fast_gicp/thirdparty/Sophus/doxyrest-config.lua](/fast_gicp/thirdparty/Sophus/doxyrest-config.lua) | Lua | 20 | 0 | 0 | 20 |
| [fast_gicp/thirdparty/Sophus/examples/HelloSO3.cpp](/fast_gicp/thirdparty/Sophus/examples/HelloSO3.cpp) | C++ | 27 | 6 | 5 | 38 |
| [fast_gicp/thirdparty/Sophus/make_docs.sh](/fast_gicp/thirdparty/Sophus/make_docs.sh) | Shell Script | 3 | 0 | 0 | 3 |
| [fast_gicp/thirdparty/Sophus/package.xml](/fast_gicp/thirdparty/Sophus/package.xml) | XML | 19 | 0 | 4 | 23 |
| [fast_gicp/thirdparty/Sophus/py/cpp_gencode/Se2_Dx_exp_x.cpp](/fast_gicp/thirdparty/Sophus/py/cpp_gencode/Se2_Dx_exp_x.cpp) | C++ | 22 | 0 | 1 | 23 |
| [fast_gicp/thirdparty/Sophus/py/cpp_gencode/Se2_Dx_this_mul_exp_x_at_0.cpp](/fast_gicp/thirdparty/Sophus/py/cpp_gencode/Se2_Dx_this_mul_exp_x_at_0.cpp) | C++ | 13 | 0 | 1 | 14 |
| [fast_gicp/thirdparty/Sophus/py/cpp_gencode/Se3_Dx_exp_x.cpp](/fast_gicp/thirdparty/Sophus/py/cpp_gencode/Se3_Dx_exp_x.cpp) | C++ | 138 | 0 | 1 | 139 |
| [fast_gicp/thirdparty/Sophus/py/cpp_gencode/Se3_Dx_this_mul_exp_x_at_0.cpp](/fast_gicp/thirdparty/Sophus/py/cpp_gencode/Se3_Dx_this_mul_exp_x_at_0.cpp) | C++ | 64 | 0 | 1 | 65 |
| [fast_gicp/thirdparty/Sophus/py/cpp_gencode/So2_Dx_exp_x.cpp](/fast_gicp/thirdparty/Sophus/py/cpp_gencode/So2_Dx_exp_x.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Sophus/py/cpp_gencode/So2_Dx_this_mul_exp_x_at_0.cpp](/fast_gicp/thirdparty/Sophus/py/cpp_gencode/So2_Dx_this_mul_exp_x_at_0.cpp) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/Sophus/py/cpp_gencode/So3_Dx_exp_x.cpp](/fast_gicp/thirdparty/Sophus/py/cpp_gencode/So3_Dx_exp_x.cpp) | C++ | 29 | 0 | 1 | 30 |
| [fast_gicp/thirdparty/Sophus/py/cpp_gencode/So3_Dx_this_mul_exp_x_at_0.cpp](/fast_gicp/thirdparty/Sophus/py/cpp_gencode/So3_Dx_this_mul_exp_x_at_0.cpp) | C++ | 19 | 0 | 1 | 20 |
| [fast_gicp/thirdparty/Sophus/py/run_tests.sh](/fast_gicp/thirdparty/Sophus/py/run_tests.sh) | Shell Script | 9 | 1 | 4 | 14 |
| [fast_gicp/thirdparty/Sophus/py/sophus/__init__.py](/fast_gicp/thirdparty/Sophus/py/sophus/__init__.py) | Python | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/Sophus/py/sophus/complex.py](/fast_gicp/thirdparty/Sophus/py/sophus/complex.py) | Python | 78 | 9 | 26 | 113 |
| [fast_gicp/thirdparty/Sophus/py/sophus/cse_codegen.py](/fast_gicp/thirdparty/Sophus/py/sophus/cse_codegen.py) | Python | 14 | 0 | 4 | 18 |
| [fast_gicp/thirdparty/Sophus/py/sophus/dual_quaternion.py](/fast_gicp/thirdparty/Sophus/py/sophus/dual_quaternion.py) | Python | 65 | 8 | 20 | 93 |
| [fast_gicp/thirdparty/Sophus/py/sophus/matrix.py](/fast_gicp/thirdparty/Sophus/py/sophus/matrix.py) | Python | 38 | 0 | 23 | 61 |
| [fast_gicp/thirdparty/Sophus/py/sophus/quaternion.py](/fast_gicp/thirdparty/Sophus/py/sophus/quaternion.py) | Python | 97 | 12 | 27 | 136 |
| [fast_gicp/thirdparty/Sophus/py/sophus/se2.py](/fast_gicp/thirdparty/Sophus/py/sophus/se2.py) | Python | 181 | 10 | 34 | 225 |
| [fast_gicp/thirdparty/Sophus/py/sophus/se3.py](/fast_gicp/thirdparty/Sophus/py/sophus/se3.py) | Python | 207 | 15 | 39 | 261 |
| [fast_gicp/thirdparty/Sophus/py/sophus/so2.py](/fast_gicp/thirdparty/Sophus/py/sophus/so2.py) | Python | 147 | 9 | 31 | 187 |
| [fast_gicp/thirdparty/Sophus/py/sophus/so3.py](/fast_gicp/thirdparty/Sophus/py/sophus/so3.py) | Python | 198 | 22 | 34 | 254 |
| [fast_gicp/thirdparty/Sophus/py/sophus/so3_codegen.py](/fast_gicp/thirdparty/Sophus/py/sophus/so3_codegen.py) | Python | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/Sophus/rst-dir/conf.py](/fast_gicp/thirdparty/Sophus/rst-dir/conf.py) | Python | 14 | 24 | 17 | 55 |
| [fast_gicp/thirdparty/Sophus/rst-dir/page_index.rst](/fast_gicp/thirdparty/Sophus/rst-dir/page_index.rst) | reStructuredText | 6 | 1 | 2 | 9 |
| [fast_gicp/thirdparty/Sophus/rst-dir/pysophus.rst](/fast_gicp/thirdparty/Sophus/rst-dir/pysophus.rst) | reStructuredText | 9 | 7 | 7 | 23 |
| [fast_gicp/thirdparty/Sophus/run_format.sh](/fast_gicp/thirdparty/Sophus/run_format.sh) | Shell Script | 1 | 0 | 1 | 2 |
| [fast_gicp/thirdparty/Sophus/scripts/install_docs_deps.sh](/fast_gicp/thirdparty/Sophus/scripts/install_docs_deps.sh) | Shell Script | 16 | 1 | 4 | 21 |
| [fast_gicp/thirdparty/Sophus/scripts/install_linux_deps.sh](/fast_gicp/thirdparty/Sophus/scripts/install_linux_deps.sh) | Shell Script | 21 | 1 | 4 | 26 |
| [fast_gicp/thirdparty/Sophus/scripts/install_osx_deps.sh](/fast_gicp/thirdparty/Sophus/scripts/install_osx_deps.sh) | Shell Script | 19 | 1 | 1 | 21 |
| [fast_gicp/thirdparty/Sophus/scripts/run_cpp_tests.sh](/fast_gicp/thirdparty/Sophus/scripts/run_cpp_tests.sh) | Shell Script | 8 | 1 | 3 | 12 |
| [fast_gicp/thirdparty/Sophus/sophus/average.hpp](/fast_gicp/thirdparty/Sophus/sophus/average.hpp) | C++ | 179 | 23 | 30 | 232 |
| [fast_gicp/thirdparty/Sophus/sophus/common.hpp](/fast_gicp/thirdparty/Sophus/sophus/common.hpp) | C++ | 119 | 16 | 38 | 173 |
| [fast_gicp/thirdparty/Sophus/sophus/example_ensure_handler.cpp](/fast_gicp/thirdparty/Sophus/sophus/example_ensure_handler.cpp) | C++ | 12 | 0 | 3 | 15 |
| [fast_gicp/thirdparty/Sophus/sophus/formatstring.hpp](/fast_gicp/thirdparty/Sophus/sophus/formatstring.hpp) | C++ | 55 | 4 | 14 | 73 |
| [fast_gicp/thirdparty/Sophus/sophus/geometry.hpp](/fast_gicp/thirdparty/Sophus/sophus/geometry.hpp) | C++ | 105 | 55 | 20 | 180 |
| [fast_gicp/thirdparty/Sophus/sophus/interpolate.hpp](/fast_gicp/thirdparty/Sophus/sophus/interpolate.hpp) | C++ | 16 | 15 | 8 | 39 |
| [fast_gicp/thirdparty/Sophus/sophus/interpolate_details.hpp](/fast_gicp/thirdparty/Sophus/sophus/interpolate_details.hpp) | C++ | 83 | 0 | 22 | 105 |
| [fast_gicp/thirdparty/Sophus/sophus/num_diff.hpp](/fast_gicp/thirdparty/Sophus/sophus/num_diff.hpp) | C++ | 68 | 12 | 14 | 94 |
| [fast_gicp/thirdparty/Sophus/sophus/rotation_matrix.hpp](/fast_gicp/thirdparty/Sophus/sophus/rotation_matrix.hpp) | C++ | 53 | 12 | 20 | 85 |
| [fast_gicp/thirdparty/Sophus/sophus/rxso2.hpp](/fast_gicp/thirdparty/Sophus/sophus/rxso2.hpp) | C++ | 314 | 265 | 82 | 661 |
| [fast_gicp/thirdparty/Sophus/sophus/rxso3.hpp](/fast_gicp/thirdparty/Sophus/sophus/rxso3.hpp) | C++ | 380 | 266 | 85 | 731 |
| [fast_gicp/thirdparty/Sophus/sophus/se2.hpp](/fast_gicp/thirdparty/Sophus/sophus/se2.hpp) | C++ | 477 | 264 | 100 | 841 |
| [fast_gicp/thirdparty/Sophus/sophus/se3.hpp](/fast_gicp/thirdparty/Sophus/sophus/se3.hpp) | C++ | 673 | 301 | 108 | 1,082 |
| [fast_gicp/thirdparty/Sophus/sophus/sim2.hpp](/fast_gicp/thirdparty/Sophus/sophus/sim2.hpp) | C++ | 371 | 270 | 87 | 728 |
| [fast_gicp/thirdparty/Sophus/sophus/sim3.hpp](/fast_gicp/thirdparty/Sophus/sophus/sim3.hpp) | C++ | 375 | 283 | 88 | 746 |
| [fast_gicp/thirdparty/Sophus/sophus/sim_details.hpp](/fast_gicp/thirdparty/Sophus/sophus/sim_details.hpp) | C++ | 96 | 0 | 8 | 104 |
| [fast_gicp/thirdparty/Sophus/sophus/so2.hpp](/fast_gicp/thirdparty/Sophus/sophus/so2.hpp) | C++ | 318 | 230 | 79 | 627 |
| [fast_gicp/thirdparty/Sophus/sophus/so3.hpp](/fast_gicp/thirdparty/Sophus/sophus/so3.hpp) | C++ | 478 | 282 | 96 | 856 |
| [fast_gicp/thirdparty/Sophus/sophus/test_macros.hpp](/fast_gicp/thirdparty/Sophus/sophus/test_macros.hpp) | C++ | 103 | 12 | 15 | 130 |
| [fast_gicp/thirdparty/Sophus/sophus/types.hpp](/fast_gicp/thirdparty/Sophus/sophus/types.hpp) | C++ | 179 | 19 | 44 | 242 |
| [fast_gicp/thirdparty/Sophus/sophus/velocities.hpp](/fast_gicp/thirdparty/Sophus/sophus/velocities.hpp) | C++ | 41 | 24 | 10 | 75 |
| [fast_gicp/thirdparty/Sophus/test/ceres/local_parameterization_se3.hpp](/fast_gicp/thirdparty/Sophus/test/ceres/local_parameterization_se3.hpp) | C++ | 31 | 8 | 9 | 48 |
| [fast_gicp/thirdparty/Sophus/test/ceres/test_ceres_se3.cpp](/fast_gicp/thirdparty/Sophus/test/ceres/test_ceres_se3.cpp) | C++ | 137 | 26 | 30 | 193 |
| [fast_gicp/thirdparty/Sophus/test/core/test_common.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_common.cpp) | C++ | 50 | 0 | 12 | 62 |
| [fast_gicp/thirdparty/Sophus/test/core/test_geometry.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_geometry.cpp) | C++ | 103 | 6 | 22 | 131 |
| [fast_gicp/thirdparty/Sophus/test/core/test_rxso2.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_rxso2.cpp) | C++ | 206 | 4 | 32 | 242 |
| [fast_gicp/thirdparty/Sophus/test/core/test_rxso3.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_rxso3.cpp) | C++ | 227 | 4 | 32 | 263 |
| [fast_gicp/thirdparty/Sophus/test/core/test_se2.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_se2.cpp) | C++ | 205 | 2 | 34 | 241 |
| [fast_gicp/thirdparty/Sophus/test/core/test_se3.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_se3.cpp) | C++ | 210 | 2 | 33 | 245 |
| [fast_gicp/thirdparty/Sophus/test/core/test_sim2.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_sim2.cpp) | C++ | 175 | 2 | 27 | 204 |
| [fast_gicp/thirdparty/Sophus/test/core/test_sim3.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_sim3.cpp) | C++ | 218 | 2 | 27 | 247 |
| [fast_gicp/thirdparty/Sophus/test/core/test_so2.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_so2.cpp) | C++ | 141 | 3 | 29 | 173 |
| [fast_gicp/thirdparty/Sophus/test/core/test_so3.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_so3.cpp) | C++ | 216 | 14 | 40 | 270 |
| [fast_gicp/thirdparty/Sophus/test/core/test_velocities.cpp](/fast_gicp/thirdparty/Sophus/test/core/test_velocities.cpp) | C++ | 96 | 10 | 25 | 131 |
| [fast_gicp/thirdparty/Sophus/test/core/tests.hpp](/fast_gicp/thirdparty/Sophus/test/core/tests.hpp) | C++ | 480 | 20 | 63 | 563 |
| [fast_gicp/thirdparty/nvbio/README.md](/fast_gicp/thirdparty/nvbio/README.md) | Markdown | 23 | 0 | 15 | 38 |
| [fast_gicp/thirdparty/nvbio/cmake-local/gcc.cmake](/fast_gicp/thirdparty/nvbio/cmake-local/gcc.cmake) | CMake | 21 | 0 | 5 | 26 |
| [fast_gicp/thirdparty/nvbio/cmake-local/nvbio.cmake](/fast_gicp/thirdparty/nvbio/cmake-local/nvbio.cmake) | CMake | 74 | 0 | 11 | 85 |
| [fast_gicp/thirdparty/nvbio/contrib/bamtools/BGZF.cpp](/fast_gicp/thirdparty/nvbio/contrib/bamtools/BGZF.cpp) | C++ | 313 | 43 | 85 | 441 |
| [fast_gicp/thirdparty/nvbio/contrib/bamtools/BGZF.h](/fast_gicp/thirdparty/nvbio/contrib/bamtools/BGZF.h) | C++ | 128 | 43 | 28 | 199 |
| [fast_gicp/thirdparty/nvbio/contrib/bamtools/BamAux.h](/fast_gicp/thirdparty/nvbio/contrib/bamtools/BamAux.h) | C++ | 346 | 70 | 70 | 486 |
| [fast_gicp/thirdparty/nvbio/contrib/bamtools/BamReader.cpp](/fast_gicp/thirdparty/nvbio/contrib/bamtools/BamReader.cpp) | C++ | 575 | 243 | 224 | 1,042 |
| [fast_gicp/thirdparty/nvbio/contrib/bamtools/BamReader.h](/fast_gicp/thirdparty/nvbio/contrib/bamtools/BamReader.h) | C++ | 26 | 39 | 19 | 84 |
| [fast_gicp/thirdparty/nvbio/contrib/bamtools/BamWriter.cpp](/fast_gicp/thirdparty/nvbio/contrib/bamtools/BamWriter.cpp) | C++ | 173 | 64 | 54 | 291 |
| [fast_gicp/thirdparty/nvbio/contrib/bamtools/BamWriter.h](/fast_gicp/thirdparty/nvbio/contrib/bamtools/BamWriter.h) | C++ | 19 | 20 | 11 | 50 |
| [fast_gicp/thirdparty/nvbio/contrib/crc/crc.cpp](/fast_gicp/thirdparty/nvbio/contrib/crc/crc.cpp) | C++ | 56 | 65 | 20 | 141 |
| [fast_gicp/thirdparty/nvbio/contrib/crc/crc.h](/fast_gicp/thirdparty/nvbio/contrib/crc/crc.h) | C++ | 72 | 39 | 26 | 137 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_discontinuity.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_discontinuity.cuh) | CUDA C++ | 186 | 351 | 65 | 602 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_exchange.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_exchange.cuh) | CUDA C++ | 517 | 364 | 125 | 1,006 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_histo_256.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_histo_256.cuh) | CUDA C++ | 160 | 216 | 71 | 447 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_histogram.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_histogram.cuh) | CUDA C++ | 99 | 271 | 55 | 425 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_load.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_load.cuh) | CUDA C++ | 450 | 497 | 147 | 1,094 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_radix_rank.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_radix_rank.cuh) | CUDA C++ | 231 | 169 | 91 | 491 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_radix_sort.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_radix_sort.cuh) | CUDA C++ | 275 | 496 | 91 | 862 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_raking_layout.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_raking_layout.cuh) | CUDA C++ | 46 | 72 | 27 | 145 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_reduce.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_reduce.cuh) | CUDA C++ | 124 | 426 | 61 | 611 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_scan.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_scan.cuh) | CUDA C++ | 495 | 1,648 | 180 | 2,323 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_shift.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_shift.cuh) | CUDA C++ | 175 | 107 | 64 | 346 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/block_store.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/block_store.cuh) | CUDA C++ | 345 | 438 | 118 | 901 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_histogram_atomic.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_histogram_atomic.cuh) | CUDA C++ | 31 | 40 | 15 | 86 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_histogram_sort.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_histogram_sort.cuh) | CUDA C++ | 100 | 58 | 40 | 198 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_reduce_raking.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_reduce_raking.cuh) | CUDA C++ | 125 | 69 | 44 | 238 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_reduce_raking_commutative_only.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_reduce_raking_commutative_only.cuh) | CUDA C++ | 96 | 58 | 36 | 190 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_reduce_warp_reductions.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_reduce_warp_reductions.cuh) | CUDA C++ | 125 | 54 | 39 | 218 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_scan_raking.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_scan_raking.cuh) | CUDA C++ | 491 | 151 | 139 | 781 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_scan_warp_scans.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/block/specializations/block_scan_warp_scans.cuh) | CUDA C++ | 228 | 70 | 66 | 364 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/cub.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/cub.cuh) | CUDA C++ | 43 | 40 | 13 | 96 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_histo_tiles.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_histo_tiles.cuh) | CUDA C++ | 126 | 135 | 62 | 323 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_partition_tiles.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_partition_tiles.cuh) | CUDA C++ | 217 | 97 | 68 | 382 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_radix_sort_downsweep_tiles.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_radix_sort_downsweep_tiles.cuh) | CUDA C++ | 445 | 154 | 115 | 714 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_radix_sort_upsweep_tiles.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_radix_sort_upsweep_tiles.cuh) | CUDA C++ | 237 | 133 | 95 | 465 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_reduce_by_key_tiles.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_reduce_by_key_tiles.cuh) | CUDA C++ | 229 | 102 | 69 | 400 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_reduce_tiles.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_reduce_tiles.cuh) | CUDA C++ | 193 | 111 | 72 | 376 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_scan_tiles.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/block_scan_tiles.cuh) | CUDA C++ | 292 | 134 | 84 | 510 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/scan_tiles_types.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/scan_tiles_types.cuh) | CUDA C++ | 185 | 79 | 55 | 319 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/specializations/block_histo_tiles_gatomic.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/specializations/block_histo_tiles_gatomic.cuh) | CUDA C++ | 92 | 61 | 32 | 185 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/specializations/block_histo_tiles_satomic.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/specializations/block_histo_tiles_satomic.cuh) | CUDA C++ | 131 | 68 | 39 | 238 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block/specializations/block_histo_tiles_sort.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block/specializations/block_histo_tiles_sort.cuh) | CUDA C++ | 190 | 105 | 70 | 365 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_histo.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_histo.cuh) | CUDA C++ | 124 | 135 | 61 | 320 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_radix_sort_downsweep.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_radix_sort_downsweep.cuh) | CUDA C++ | 462 | 156 | 119 | 737 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_radix_sort_upsweep.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_radix_sort_upsweep.cuh) | CUDA C++ | 224 | 129 | 91 | 444 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_reduce.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_reduce.cuh) | CUDA C++ | 226 | 123 | 82 | 431 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_reduce_by_key.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_reduce_by_key.cuh) | CUDA C++ | 607 | 230 | 174 | 1,011 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_scan.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_scan.cuh) | CUDA C++ | 311 | 138 | 88 | 537 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_select.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/block_region_select.cuh) | CUDA C++ | 468 | 152 | 116 | 736 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/device_scan_types.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/device_scan_types.cuh) | CUDA C++ | 312 | 146 | 104 | 562 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/specializations/block_region_histo_gatomic.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/specializations/block_region_histo_gatomic.cuh) | CUDA C++ | 92 | 61 | 32 | 185 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/specializations/block_region_histo_satomic.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/specializations/block_region_histo_satomic.cuh) | CUDA C++ | 134 | 68 | 44 | 246 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/specializations/block_region_histo_sort.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/block_region/specializations/block_region_histo_sort.cuh) | CUDA C++ | 190 | 105 | 70 | 365 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/device_histo_256.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/device_histo_256.cuh) | CUDA C++ | 492 | 176 | 125 | 793 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/device_histogram.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/device_histogram.cuh) | CUDA C++ | 216 | 396 | 42 | 654 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/device_partition.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/device_partition.cuh) | CUDA C++ | 78 | 179 | 19 | 276 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/device_radix_sort.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/device_radix_sort.cuh) | CUDA C++ | 116 | 278 | 27 | 421 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/device_reduce.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/device_reduce.cuh) | CUDA C++ | 247 | 510 | 48 | 805 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/device_reduce_by_key.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/device_reduce_by_key.cuh) | CUDA C++ | 387 | 114 | 97 | 598 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/device_reorder.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/device_reorder.cuh) | CUDA C++ | 333 | 127 | 91 | 551 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/device_scan.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/device_scan.cuh) | CUDA C++ | 121 | 269 | 30 | 420 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/device_select.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/device_select.cuh) | CUDA C++ | 110 | 241 | 22 | 373 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_histogram_dispatch.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_histogram_dispatch.cuh) | CUDA C++ | 329 | 124 | 93 | 546 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_radix_sort_dispatch.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_radix_sort_dispatch.cuh) | CUDA C++ | 603 | 165 | 157 | 925 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_reduce_by_key_dispatch.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_reduce_by_key_dispatch.cuh) | CUDA C++ | 385 | 114 | 90 | 589 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_reduce_dispatch.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_reduce_dispatch.cuh) | CUDA C++ | 472 | 148 | 112 | 732 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_scan_dispatch.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_scan_dispatch.cuh) | CUDA C++ | 359 | 113 | 88 | 560 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_select_dispatch.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/dispatch/device_select_dispatch.cuh) | CUDA C++ | 359 | 114 | 86 | 559 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/persistent_block/persistent_block_histo_256.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/persistent_block/persistent_block_histo_256.cuh) | CUDA C++ | 440 | 231 | 140 | 811 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/persistent_block/persistent_block_reduce.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/persistent_block/persistent_block_reduce.cuh) | CUDA C++ | 125 | 79 | 44 | 248 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/persistent_block/persistent_block_scan.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/persistent_block/persistent_block_scan.cuh) | CUDA C++ | 304 | 123 | 87 | 514 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_histo_region.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_histo_region.cuh) | CUDA C++ | 124 | 135 | 61 | 320 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_radix_sort_downsweep_region.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_radix_sort_downsweep_region.cuh) | CUDA C++ | 462 | 156 | 119 | 737 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_radix_sort_upsweep_region.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_radix_sort_upsweep_region.cuh) | CUDA C++ | 224 | 129 | 91 | 444 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_reduce_by_key_region.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_reduce_by_key_region.cuh) | CUDA C++ | 607 | 230 | 174 | 1,011 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_reduce_region.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_reduce_region.cuh) | CUDA C++ | 226 | 123 | 82 | 431 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_scan_region.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_scan_region.cuh) | CUDA C++ | 311 | 138 | 88 | 537 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_select_region.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/block_select_region.cuh) | CUDA C++ | 468 | 152 | 116 | 736 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/device_scan_types.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/device_scan_types.cuh) | CUDA C++ | 312 | 146 | 104 | 562 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/specializations/block_histo_region_gatomic.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/specializations/block_histo_region_gatomic.cuh) | CUDA C++ | 92 | 61 | 32 | 185 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/specializations/block_histo_region_satomic.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/specializations/block_histo_region_satomic.cuh) | CUDA C++ | 134 | 68 | 44 | 246 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/device/region/specializations/block_histo_region_sort.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/device/region/specializations/block_histo_region_sort.cuh) | CUDA C++ | 190 | 105 | 70 | 365 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/grid/grid_barrier.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/grid/grid_barrier.cuh) | CUDA C++ | 95 | 75 | 42 | 212 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/grid/grid_even_share.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/grid/grid_even_share.cuh) | CUDA C++ | 83 | 75 | 28 | 186 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/grid/grid_mapping.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/grid/grid_mapping.cuh) | CUDA C++ | 12 | 67 | 17 | 96 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/grid/grid_multi_buffer.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/grid/grid_multi_buffer.cuh) | CUDA C++ | 45 | 82 | 26 | 153 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/grid/grid_queue.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/grid/grid_queue.cuh) | CUDA C++ | 95 | 80 | 42 | 217 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/host/spinlock.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/host/spinlock.cuh) | CUDA C++ | 45 | 54 | 25 | 124 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/iterator/arg_index_input_iterator.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/iterator/arg_index_input_iterator.cuh) | CUDA C++ | 119 | 99 | 38 | 256 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/iterator/cache_modified_input_iterator.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/iterator/cache_modified_input_iterator.cuh) | CUDA C++ | 111 | 92 | 38 | 241 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/iterator/cache_modified_output_iterator.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/iterator/cache_modified_output_iterator.cuh) | CUDA C++ | 118 | 97 | 39 | 254 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/iterator/constant_input_iterator.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/iterator/constant_input_iterator.cuh) | CUDA C++ | 116 | 84 | 36 | 236 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/iterator/counting_input_iterator.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/iterator/counting_input_iterator.cuh) | CUDA C++ | 111 | 83 | 35 | 229 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/iterator/tex_obj_input_iterator.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/iterator/tex_obj_input_iterator.cuh) | CUDA C++ | 160 | 104 | 45 | 309 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/iterator/tex_ref_input_iterator.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/iterator/tex_ref_input_iterator.cuh) | CUDA C++ | 186 | 122 | 63 | 371 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/iterator/transform_input_iterator.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/iterator/transform_input_iterator.cuh) | CUDA C++ | 115 | 103 | 35 | 253 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/thread/thread_load.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/thread/thread_load.cuh) | CUDA C++ | 241 | 123 | 73 | 437 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/thread/thread_operators.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/thread/thread_operators.cuh) | CUDA C++ | 94 | 78 | 35 | 207 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/thread/thread_reduce.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/thread/thread_reduce.cuh) | CUDA C++ | 76 | 70 | 24 | 170 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/thread/thread_scan.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/thread/thread_scan.cuh) | CUDA C++ | 156 | 86 | 42 | 284 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/thread/thread_store.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/thread/thread_store.cuh) | CUDA C++ | 219 | 125 | 69 | 413 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/util_allocator.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/util_allocator.cuh) | CUDA C++ | 365 | 180 | 120 | 665 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/util_arch.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/util_arch.cuh) | CUDA C++ | 100 | 53 | 34 | 187 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/util_debug.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/util_debug.cuh) | CUDA C++ | 37 | 55 | 24 | 116 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/util_device.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/util_device.cuh) | CUDA C++ | 186 | 112 | 75 | 373 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/util_iterator.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/util_iterator.cuh) | CUDA C++ | 441 | 153 | 125 | 719 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/util_macro.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/util_macro.cuh) | CUDA C++ | 24 | 63 | 21 | 108 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/util_namespace.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/util_namespace.cuh) | CUDA C++ | 3 | 34 | 5 | 42 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/util_ptx.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/util_ptx.cuh) | CUDA C++ | 279 | 224 | 93 | 596 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/util_type.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/util_type.cuh) | CUDA C++ | 607 | 222 | 199 | 1,028 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/util_vector.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/util_vector.cuh) | CUDA C++ | 141 | 64 | 32 | 237 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/warp/specializations/warp_reduce_shfl.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/warp/specializations/warp_reduce_shfl.cuh) | CUDA C++ | 194 | 79 | 55 | 328 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/warp/specializations/warp_reduce_smem.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/warp/specializations/warp_reduce_smem.cuh) | CUDA C++ | 145 | 88 | 59 | 292 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/warp/specializations/warp_scan_shfl.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/warp/specializations/warp_scan_shfl.cuh) | CUDA C++ | 205 | 90 | 61 | 356 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/warp/specializations/warp_scan_smem.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/warp/specializations/warp_scan_smem.cuh) | CUDA C++ | 172 | 89 | 67 | 328 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/warp/warp_reduce.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/warp/warp_reduce.cuh) | CUDA C++ | 159 | 464 | 63 | 686 |
| [fast_gicp/thirdparty/nvbio/contrib/cub/warp/warp_scan.cuh](/fast_gicp/thirdparty/nvbio/contrib/cub/warp/warp_scan.cuh) | CUDA C++ | 271 | 952 | 90 | 1,313 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/.travis.yml](/fast_gicp/thirdparty/nvbio/contrib/htslib/.travis.yml) | YAML | 5 | 1 | 3 | 9 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/Makefile](/fast_gicp/thirdparty/nvbio/contrib/htslib/Makefile) | Makefile | 206 | 30 | 68 | 304 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/README.md](/fast_gicp/thirdparty/nvbio/contrib/htslib/README.md) | Markdown | 14 | 0 | 4 | 18 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/bgzf.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/bgzf.c) | C | 934 | 64 | 89 | 1,087 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/bgzip.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/bgzip.c) | C | 243 | 23 | 18 | 284 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/config.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/config.h) | C++ | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram.h) | C++ | 20 | 39 | 8 | 67 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_codecs.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_codecs.c) | C | 1,279 | 208 | 278 | 1,765 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_codecs.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_codecs.h) | C++ | 88 | 44 | 24 | 156 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_decode.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_decode.c) | C | 1,629 | 226 | 284 | 2,139 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_decode.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_decode.h) | C++ | 16 | 81 | 16 | 113 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_encode.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_encode.c) | C | 1,841 | 475 | 315 | 2,631 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_encode.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_encode.h) | C++ | 14 | 79 | 13 | 106 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_index.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_index.c) | C | 314 | 111 | 79 | 504 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_index.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_index.h) | C++ | 16 | 71 | 12 | 99 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_io.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_io.c) | C | 2,539 | 539 | 575 | 3,653 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_io.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_io.h) | C++ | 102 | 352 | 79 | 533 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_samtools.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_samtools.c) | C | 94 | 33 | 18 | 145 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_samtools.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_samtools.h) | C++ | 54 | 30 | 14 | 98 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_stats.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_stats.c) | C | 237 | 73 | 48 | 358 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_stats.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_stats.h) | C++ | 15 | 38 | 7 | 60 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_structs.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/cram_structs.h) | C++ | 518 | 139 | 96 | 753 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/files.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/files.c) | C | 35 | 33 | 9 | 77 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/mFILE.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/mFILE.c) | C | 371 | 168 | 96 | 635 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/mFILE.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/mFILE.h) | C++ | 51 | 29 | 9 | 89 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/md5.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/md5.c) | C | 194 | 62 | 40 | 296 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/md5.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/md5.h) | C++ | 21 | 25 | 9 | 55 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/misc.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/misc.h) | C++ | 28 | 71 | 12 | 111 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/open_trace_file.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/open_trace_file.c) | C | 222 | 123 | 42 | 387 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/open_trace_file.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/open_trace_file.h) | C++ | 13 | 92 | 11 | 116 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/os.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/os.h) | C++ | 125 | 146 | 36 | 307 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/pooled_alloc.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/pooled_alloc.c) | C | 104 | 34 | 33 | 171 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/pooled_alloc.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/pooled_alloc.h) | C++ | 17 | 33 | 7 | 57 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/sam_header.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/sam_header.c) | C | 799 | 218 | 206 | 1,223 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/sam_header.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/sam_header.h) | C++ | 106 | 295 | 52 | 453 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/string_alloc.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/string_alloc.c) | C | 64 | 45 | 45 | 154 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/string_alloc.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/string_alloc.h) | C++ | 24 | 35 | 11 | 70 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/thread_pool.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/thread_pool.c) | C | 436 | 141 | 137 | 714 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/thread_pool.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/thread_pool.h) | C++ | 58 | 112 | 28 | 198 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/vlen.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/vlen.c) | C | 236 | 135 | 62 | 433 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/vlen.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/vlen.h) | C++ | 11 | 32 | 6 | 49 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/zfio.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/zfio.c) | C | 98 | 61 | 27 | 186 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/cram/zfio.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/cram/zfio.h) | C++ | 17 | 32 | 6 | 55 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/faidx.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/faidx.c) | C | 384 | 8 | 30 | 422 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/hfile.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/hfile.c) | C | 357 | 88 | 82 | 527 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/hfile_internal.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/hfile_internal.h) | C++ | 16 | 47 | 13 | 76 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/hfile_net.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/hfile_net.c) | C | 54 | 27 | 19 | 100 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/hts.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/hts.c) | C | 1,189 | 49 | 98 | 1,336 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib.mk](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib.mk) | Makefile | 85 | 30 | 13 | 128 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/bgzf.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/bgzf.h) | C++ | 71 | 202 | 41 | 314 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/faidx.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/faidx.h) | C++ | 17 | 82 | 14 | 113 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/hfile.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/hfile.h) | C++ | 80 | 98 | 27 | 205 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/hts.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/hts.h) | C++ | 167 | 95 | 44 | 306 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/hts_defs.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/hts_defs.h) | C++ | 19 | 23 | 6 | 48 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/kfunc.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/kfunc.h) | C++ | 9 | 33 | 8 | 50 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/khash.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/khash.h) | C++ | 281 | 282 | 55 | 618 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/khash_str2int.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/khash_str2int.h) | C++ | 62 | 25 | 12 | 99 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/klist.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/klist.h) | C++ | 89 | 24 | 9 | 122 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/knetfile.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/knetfile.h) | C++ | 45 | 14 | 17 | 76 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/kseq.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/kseq.h) | C++ | 197 | 33 | 24 | 254 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/ksort.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/ksort.h) | C++ | 216 | 57 | 13 | 286 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/kstdint.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/kstdint.h) | C++ | 40 | 17 | 8 | 65 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/kstring.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/kstring.h) | C++ | 201 | 44 | 26 | 271 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/sam.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/sam.h) | C++ | 155 | 197 | 50 | 402 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/synced_bcf_reader.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/synced_bcf_reader.h) | C++ | 86 | 143 | 27 | 256 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/tbx.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/tbx.h) | C++ | 38 | 1 | 14 | 53 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/vcf.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/vcf.h) | C++ | 386 | 340 | 103 | 829 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/vcf_sweep.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/vcf_sweep.h) | C++ | 11 | 0 | 5 | 16 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/vcfutils.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib/vcfutils.h) | C++ | 26 | 54 | 13 | 93 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/htslib_vars.mk](/fast_gicp/thirdparty/nvbio/contrib/htslib/htslib_vars.mk) | Makefile | 11 | 7 | 3 | 21 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/kfunc.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/kfunc.c) | C | 191 | 43 | 21 | 255 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/knetfile.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/knetfile.c) | C | 505 | 86 | 32 | 623 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/kstring.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/kstring.c) | C | 202 | 12 | 16 | 230 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/sam.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/sam.c) | C | 1,565 | 113 | 120 | 1,798 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/synced_bcf_reader.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/synced_bcf_reader.c) | C | 997 | 76 | 113 | 1,186 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/tabix.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/tabix.c) | C | 341 | 7 | 27 | 375 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/tbx.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/tbx.c) | C | 271 | 2 | 18 | 291 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/vcf.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/vcf.c) | C | 2,672 | 114 | 237 | 3,023 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/vcf_sweep.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/vcf_sweep.c) | C | 132 | 1 | 26 | 159 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/vcfutils.c](/fast_gicp/thirdparty/nvbio/contrib/htslib/vcfutils.c) | C | 597 | 9 | 37 | 643 |
| [fast_gicp/thirdparty/nvbio/contrib/htslib/version.h](/fast_gicp/thirdparty/nvbio/contrib/htslib/version.h) | C++ | 1 | 0 | 1 | 2 |
| [fast_gicp/thirdparty/nvbio/contrib/libdivsufsort-lite/divsufsort.c](/fast_gicp/thirdparty/nvbio/contrib/libdivsufsort-lite/divsufsort.c) | C | 1,479 | 123 | 181 | 1,783 |
| [fast_gicp/thirdparty/nvbio/contrib/libdivsufsort-lite/divsufsort.h](/fast_gicp/thirdparty/nvbio/contrib/libdivsufsort-lite/divsufsort.h) | C++ | 13 | 41 | 10 | 64 |
| [fast_gicp/thirdparty/nvbio/contrib/libdivsufsort-lite/suftest.c](/fast_gicp/thirdparty/nvbio/contrib/libdivsufsort-lite/suftest.c) | C | 138 | 38 | 22 | 198 |
| [fast_gicp/thirdparty/nvbio/contrib/libdivsufsortxx/divsufsortxx.h](/fast_gicp/thirdparty/nvbio/contrib/libdivsufsortxx/divsufsortxx.h) | C++ | 1,255 | 116 | 176 | 1,547 |
| [fast_gicp/thirdparty/nvbio/contrib/lz4/Makefile](/fast_gicp/thirdparty/nvbio/contrib/lz4/Makefile) | Makefile | 65 | 37 | 16 | 118 |
| [fast_gicp/thirdparty/nvbio/contrib/lz4/lz4.c](/fast_gicp/thirdparty/nvbio/contrib/lz4/lz4.c) | C | 968 | 204 | 196 | 1,368 |
| [fast_gicp/thirdparty/nvbio/contrib/lz4/lz4.h](/fast_gicp/thirdparty/nvbio/contrib/lz4/lz4.h) | C++ | 50 | 222 | 44 | 316 |
| [fast_gicp/thirdparty/nvbio/contrib/lz4/lz4frame.c](/fast_gicp/thirdparty/nvbio/contrib/lz4/lz4frame.c) | C | 929 | 205 | 197 | 1,331 |
| [fast_gicp/thirdparty/nvbio/contrib/lz4/lz4frame.h](/fast_gicp/thirdparty/nvbio/contrib/lz4/lz4frame.h) | C++ | 55 | 156 | 42 | 253 |
| [fast_gicp/thirdparty/nvbio/contrib/lz4/lz4frame_static.h](/fast_gicp/thirdparty/nvbio/contrib/lz4/lz4frame_static.h) | C++ | 19 | 43 | 11 | 73 |
| [fast_gicp/thirdparty/nvbio/contrib/lz4/lz4hc.c](/fast_gicp/thirdparty/nvbio/contrib/lz4/lz4hc.c) | C | 522 | 110 | 120 | 752 |
| [fast_gicp/thirdparty/nvbio/contrib/lz4/lz4hc.h](/fast_gicp/thirdparty/nvbio/contrib/lz4/lz4hc.h) | C++ | 33 | 113 | 29 | 175 |
| [fast_gicp/thirdparty/nvbio/contrib/lz4/xxhash.c](/fast_gicp/thirdparty/nvbio/contrib/lz4/xxhash.c) | C | 707 | 94 | 135 | 936 |
| [fast_gicp/thirdparty/nvbio/contrib/lz4/xxhash.h](/fast_gicp/thirdparty/nvbio/contrib/lz4/xxhash.h) | C++ | 23 | 108 | 26 | 157 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/README.md](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/README.md) | Markdown | 5 | 0 | 4 | 9 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctaloadbalance.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctaloadbalance.cuh) | CUDA C++ | 56 | 55 | 26 | 137 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctamerge.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctamerge.cuh) | CUDA C++ | 194 | 83 | 57 | 334 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctascan.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctascan.cuh) | CUDA C++ | 195 | 61 | 53 | 309 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctasearch.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctasearch.cuh) | CUDA C++ | 119 | 52 | 37 | 208 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctasegreduce.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctasegreduce.cuh) | CUDA C++ | 121 | 80 | 38 | 239 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctasegscan.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctasegscan.cuh) | CUDA C++ | 61 | 52 | 25 | 138 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctasegsort.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctasegsort.cuh) | CUDA C++ | 262 | 104 | 78 | 444 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctasortedsearch.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/ctasortedsearch.cuh) | CUDA C++ | 105 | 81 | 23 | 209 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/devicetypes.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/devicetypes.cuh) | CUDA C++ | 286 | 37 | 41 | 364 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/deviceutil.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/deviceutil.cuh) | CUDA C++ | 77 | 51 | 25 | 153 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/intrinsics.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/intrinsics.cuh) | CUDA C++ | 291 | 60 | 57 | 408 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/launchbox.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/launchbox.cuh) | CUDA C++ | 51 | 35 | 12 | 98 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/loadstore.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/loadstore.cuh) | CUDA C++ | 486 | 86 | 102 | 674 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/serialsets.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/serialsets.cuh) | CUDA C++ | 148 | 52 | 36 | 236 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/sortnetwork.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/device/sortnetwork.cuh) | CUDA C++ | 89 | 63 | 17 | 169 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/bulkinsert.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/bulkinsert.cuh) | CUDA C++ | 93 | 51 | 30 | 174 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/bulkremove.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/bulkremove.cuh) | CUDA C++ | 77 | 49 | 25 | 151 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/csrtools.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/csrtools.cuh) | CUDA C++ | 278 | 83 | 82 | 443 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/cubradixsort.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/cubradixsort.cuh) | CUDA C++ | 32 | 0 | 15 | 47 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/intervalmove.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/intervalmove.cuh) | CUDA C++ | 176 | 72 | 52 | 300 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/join.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/join.cuh) | CUDA C++ | 200 | 55 | 49 | 304 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/loadbalance.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/loadbalance.cuh) | CUDA C++ | 37 | 36 | 16 | 89 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/localitysort.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/localitysort.cuh) | CUDA C++ | 71 | 32 | 23 | 126 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/merge.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/merge.cuh) | CUDA C++ | 90 | 38 | 25 | 153 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/mergesort.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/mergesort.cuh) | CUDA C++ | 181 | 42 | 46 | 269 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/reduce.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/reduce.cuh) | CUDA C++ | 77 | 42 | 26 | 145 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/reducebykey.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/reducebykey.cuh) | CUDA C++ | 177 | 66 | 47 | 290 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/scan.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/scan.cuh) | CUDA C++ | 145 | 47 | 43 | 235 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/search.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/search.cuh) | CUDA C++ | 89 | 42 | 30 | 161 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/segmentedsort.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/segmentedsort.cuh) | CUDA C++ | 549 | 79 | 144 | 772 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/segreduce.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/segreduce.cuh) | CUDA C++ | 141 | 59 | 41 | 241 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/segreducecsr.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/segreducecsr.cuh) | CUDA C++ | 344 | 87 | 82 | 513 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/sets.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/sets.cuh) | CUDA C++ | 247 | 71 | 60 | 378 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/sortedsearch.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/sortedsearch.cuh) | CUDA C++ | 214 | 74 | 55 | 343 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/spmvcsr.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/kernels/spmvcsr.cuh) | CUDA C++ | 377 | 91 | 97 | 565 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/mgpudevice.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/mgpudevice.cuh) | CUDA C++ | 115 | 130 | 46 | 291 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/mgpuenums.h](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/mgpuenums.h) | C++ | 29 | 32 | 10 | 71 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/mgpuhost.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/mgpuhost.cuh) | CUDA C++ | 267 | 425 | 124 | 816 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/mmio.h](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/mmio.h) | C++ | 72 | 26 | 36 | 134 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/moderngpu.cuh](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/moderngpu.cuh) | CUDA C++ | 17 | 32 | 4 | 53 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/sparsematrix.h](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/sparsematrix.h) | C++ | 66 | 36 | 23 | 125 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/util/format.h](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/util/format.h) | C++ | 86 | 36 | 27 | 149 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/util/mgpualloc.h](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/util/mgpualloc.h) | C++ | 64 | 9 | 26 | 99 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/util/mgpucontext.h](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/util/mgpucontext.h) | C++ | 381 | 42 | 91 | 514 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/util/static.h](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/util/static.h) | C++ | 116 | 40 | 28 | 184 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/util/util.h](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/include/util/util.h) | C++ | 71 | 37 | 17 | 125 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/src/mgpucontext.cu](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/src/mgpucontext.cu) | CUDA C++ | 201 | 311 | 42 | 554 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/src/mgpuutil.cpp](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/src/mgpuutil.cpp) | C++ | 115 | 37 | 19 | 171 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/src/mmio.cpp](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/src/mmio.cpp) | C++ | 364 | 47 | 101 | 512 |
| [fast_gicp/thirdparty/nvbio/contrib/moderngpu/src/sparsematrix.cpp](/fast_gicp/thirdparty/nvbio/contrib/moderngpu/src/sparsematrix.cpp) | C++ | 227 | 42 | 59 | 328 |
| [fast_gicp/thirdparty/nvbio/contrib/priority-deque/README.md](/fast_gicp/thirdparty/nvbio/contrib/priority-deque/README.md) | Markdown | 7 | 0 | 5 | 12 |
| [fast_gicp/thirdparty/nvbio/contrib/priority-deque/interval_heap.hpp](/fast_gicp/thirdparty/nvbio/contrib/priority-deque/interval_heap.hpp) | C++ | 373 | 172 | 35 | 580 |
| [fast_gicp/thirdparty/nvbio/contrib/priority-deque/main.cpp](/fast_gicp/thirdparty/nvbio/contrib/priority-deque/main.cpp) | C++ | 170 | 19 | 19 | 208 |
| [fast_gicp/thirdparty/nvbio/contrib/priority-deque/priority_deque.hpp](/fast_gicp/thirdparty/nvbio/contrib/priority-deque/priority_deque.hpp) | C++ | 285 | 214 | 27 | 526 |
| [fast_gicp/thirdparty/nvbio/contrib/priority-deque/priority_deque_verify.hpp](/fast_gicp/thirdparty/nvbio/contrib/priority-deque/priority_deque_verify.hpp) | C++ | 12 | 3 | 6 | 21 |
| [fast_gicp/thirdparty/nvbio/contrib/sais.h](/fast_gicp/thirdparty/nvbio/contrib/sais.h) | C++ | 506 | 67 | 32 | 605 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/Makefile](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/Makefile) | Makefile | 210 | 22 | 57 | 289 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/adler32.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/adler32.c) | C | 137 | 22 | 21 | 180 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/compress.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/compress.c) | C | 47 | 23 | 11 | 81 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/configure.log](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/configure.log) | Log | 153 | 0 | 16 | 169 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/crc32.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/crc32.c) | C | 285 | 85 | 56 | 426 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/crc32.h](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/crc32.h) | C++ | 437 | 3 | 2 | 442 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/deflate.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/deflate.c) | C | 1,315 | 445 | 206 | 1,966 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/deflate.h](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/deflate.h) | C++ | 155 | 127 | 65 | 347 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/gzclose.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/gzclose.c) | C | 14 | 7 | 5 | 26 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/gzguts.h](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/gzguts.h) | C++ | 142 | 30 | 22 | 194 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/gzlib.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/gzlib.c) | C | 465 | 82 | 74 | 621 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/gzread.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/gzread.c) | C | 405 | 116 | 69 | 590 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/gzwrite.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/gzwrite.c) | C | 401 | 89 | 76 | 566 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/infback.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/infback.c) | C | 492 | 101 | 48 | 641 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inffast.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inffast.c) | C | 261 | 69 | 11 | 341 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inffast.h](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inffast.h) | C++ | 1 | 8 | 3 | 12 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inffixed.h](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inffixed.h) | C++ | 84 | 7 | 4 | 95 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inflate.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inflate.c) | C | 1,146 | 274 | 77 | 1,497 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inflate.h](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inflate.h) | C++ | 73 | 44 | 6 | 123 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inftrees.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inftrees.c) | C | 176 | 105 | 26 | 307 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inftrees.h](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/inftrees.h) | C++ | 16 | 40 | 7 | 63 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/treebuild.xml](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/treebuild.xml) | XML | 95 | 17 | 5 | 117 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/trees.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/trees.c) | C | 761 | 310 | 154 | 1,225 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/trees.h](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/trees.h) | C++ | 120 | 1 | 8 | 129 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/uncompr.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/uncompr.c) | C | 31 | 19 | 10 | 60 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/zlib.h](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/zlib.h) | C++ | 268 | 1,356 | 121 | 1,745 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/zutil.c](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/zutil.c) | C | 245 | 31 | 49 | 325 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/zutil.h](/fast_gicp/thirdparty/nvbio/contrib/zlib-1.2.7/zutil.h) | C++ | 182 | 28 | 43 | 253 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib/zconf.h](/fast_gicp/thirdparty/nvbio/contrib/zlib/zconf.h) | C++ | 328 | 63 | 38 | 429 |
| [fast_gicp/thirdparty/nvbio/contrib/zlib/zlib.h](/fast_gicp/thirdparty/nvbio/contrib/zlib/zlib.h) | C++ | 228 | 1,270 | 116 | 1,614 |
| [fast_gicp/thirdparty/nvbio/doxy/DoxygenLayout.xml](/fast_gicp/thirdparty/nvbio/doxy/DoxygenLayout.xml) | XML | 176 | 7 | 6 | 189 |
| [fast_gicp/thirdparty/nvbio/doxy/extra_stylesheet.css](/fast_gicp/thirdparty/nvbio/doxy/extra_stylesheet.css) | CSS | 325 | 26 | 91 | 442 |
| [fast_gicp/thirdparty/nvbio/doxy/header.html](/fast_gicp/thirdparty/nvbio/doxy/header.html) | HTML | 48 | 16 | 6 | 70 |
| [fast_gicp/thirdparty/nvbio/examples/fmmap/fmmap.cu](/fast_gicp/thirdparty/nvbio/examples/fmmap/fmmap.cu) | CUDA C++ | 352 | 92 | 98 | 542 |
| [fast_gicp/thirdparty/nvbio/examples/fmmap/util.h](/fast_gicp/thirdparty/nvbio/examples/fmmap/util.h) | C++ | 43 | 35 | 15 | 93 |
| [fast_gicp/thirdparty/nvbio/examples/hello_world/hello_world.cu](/fast_gicp/thirdparty/nvbio/examples/hello_world/hello_world.cu) | CUDA C++ | 19 | 35 | 12 | 66 |
| [fast_gicp/thirdparty/nvbio/examples/hello_world2/hello_world2.cu](/fast_gicp/thirdparty/nvbio/examples/hello_world2/hello_world2.cu) | CUDA C++ | 49 | 37 | 20 | 106 |
| [fast_gicp/thirdparty/nvbio/examples/mem/mem.cu](/fast_gicp/thirdparty/nvbio/examples/mem/mem.cu) | CUDA C++ | 138 | 42 | 45 | 225 |
| [fast_gicp/thirdparty/nvbio/examples/proteinsw/proteinsw.cu](/fast_gicp/thirdparty/nvbio/examples/proteinsw/proteinsw.cu) | CUDA C++ | 155 | 47 | 32 | 234 |
| [fast_gicp/thirdparty/nvbio/examples/proteinsw/proteinsw_qp.cu](/fast_gicp/thirdparty/nvbio/examples/proteinsw/proteinsw_qp.cu) | CUDA C++ | 156 | 41 | 31 | 228 |
| [fast_gicp/thirdparty/nvbio/examples/qmap/alignment.h](/fast_gicp/thirdparty/nvbio/examples/qmap/alignment.h) | C++ | 51 | 42 | 19 | 112 |
| [fast_gicp/thirdparty/nvbio/examples/qmap/qmap.cu](/fast_gicp/thirdparty/nvbio/examples/qmap/qmap.cu) | CUDA C++ | 355 | 73 | 88 | 516 |
| [fast_gicp/thirdparty/nvbio/examples/qmap/util.h](/fast_gicp/thirdparty/nvbio/examples/qmap/util.h) | C++ | 43 | 35 | 15 | 93 |
| [fast_gicp/thirdparty/nvbio/examples/seeding/seeding.cu](/fast_gicp/thirdparty/nvbio/examples/seeding/seeding.cu) | CUDA C++ | 75 | 48 | 25 | 148 |
| [fast_gicp/thirdparty/nvbio/examples/waveletfm/waveletfm.cu](/fast_gicp/thirdparty/nvbio/examples/waveletfm/waveletfm.cu) | CUDA C++ | 56 | 54 | 28 | 138 |
| [fast_gicp/thirdparty/nvbio/nvBWT/filelist.cpp](/fast_gicp/thirdparty/nvbio/nvBWT/filelist.cpp) | C++ | 72 | 31 | 14 | 117 |
| [fast_gicp/thirdparty/nvbio/nvBWT/filelist.h](/fast_gicp/thirdparty/nvbio/nvBWT/filelist.h) | C++ | 1 | 28 | 4 | 33 |
| [fast_gicp/thirdparty/nvbio/nvBWT/nvBWT.cu](/fast_gicp/thirdparty/nvbio/nvBWT/nvBWT.cu) | CUDA C++ | 628 | 72 | 114 | 814 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner.h) | C++ | 283 | 51 | 55 | 389 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_all.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_all.h) | C++ | 455 | 114 | 126 | 695 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_all_ed.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_all_ed.cu) | CUDA C++ | 31 | 26 | 5 | 62 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_all_sw.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_all_sw.cu) | CUDA C++ | 31 | 26 | 5 | 62 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx.h) | C++ | 533 | 148 | 160 | 841 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx_ed.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx_ed.cu) | CUDA C++ | 31 | 26 | 5 | 62 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx_paired.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx_paired.h) | C++ | 784 | 195 | 214 | 1,193 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx_paired_ed.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx_paired_ed.cu) | CUDA C++ | 33 | 26 | 5 | 64 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx_paired_sw.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx_paired_sw.cu) | CUDA C++ | 33 | 26 | 5 | 64 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx_sw.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_approx_sw.cu) | CUDA C++ | 31 | 26 | 5 | 62 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_exact.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_best_exact.h) | C++ | 446 | 125 | 121 | 692 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_init.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_init.cu) | CUDA C++ | 347 | 72 | 85 | 504 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_inst.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_inst.h) | C++ | 77 | 26 | 10 | 113 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_sort.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/aligner_sort.cu) | CUDA C++ | 57 | 37 | 15 | 109 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/alignment_utils.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/alignment_utils.h) | C++ | 218 | 94 | 44 | 356 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/checksums.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/checksums.cu) | CUDA C++ | 34 | 34 | 13 | 81 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/checksums.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/checksums.h) | C++ | 36 | 34 | 13 | 83 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/compute_thread.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/compute_thread.cu) | CUDA C++ | 558 | 59 | 122 | 739 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/compute_thread.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/compute_thread.h) | C++ | 74 | 42 | 21 | 137 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/defs.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/defs.h) | C++ | 103 | 73 | 37 | 213 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/fmindex_def.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/fmindex_def.h) | C++ | 18 | 26 | 6 | 50 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/func.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/func.h) | C++ | 36 | 29 | 12 | 77 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/input_thread.cpp](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/input_thread.cpp) | C++ | 251 | 48 | 41 | 340 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/input_thread.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/input_thread.h) | C++ | 68 | 48 | 29 | 145 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/locate.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/locate.h) | C++ | 51 | 87 | 18 | 156 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/locate_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/locate_inl.h) | C++ | 250 | 98 | 44 | 392 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapping.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapping.cu) | CUDA C++ | 114 | 58 | 20 | 192 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapping.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapping.h) | C++ | 88 | 76 | 17 | 181 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapping_impl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapping_impl.h) | C++ | 87 | 77 | 18 | 182 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapping_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapping_inl.h) | C++ | 600 | 148 | 101 | 849 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapq.cpp](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapq.cpp) | C++ | 7 | 26 | 4 | 37 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapq.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/mapq.h) | C++ | 227 | 72 | 37 | 336 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/params.cpp](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/params.cpp) | C++ | 297 | 20 | 47 | 364 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/params.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/params.h) | C++ | 105 | 44 | 22 | 171 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/persist.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/persist.cu) | CUDA C++ | 275 | 49 | 65 | 389 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/persist.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/persist.h) | C++ | 47 | 36 | 11 | 94 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/pipeline_states.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/pipeline_states.h) | C++ | 192 | 73 | 37 | 302 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/reads_def.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/reads_def.h) | C++ | 18 | 26 | 6 | 50 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/reduce.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/reduce.cu) | CUDA C++ | 38 | 41 | 9 | 88 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/reduce.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/reduce.h) | C++ | 68 | 82 | 23 | 173 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/reduce_impl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/reduce_impl.h) | C++ | 26 | 41 | 13 | 80 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/reduce_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/reduce_inl.h) | C++ | 338 | 120 | 84 | 542 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score.cu) | CUDA C++ | 69 | 132 | 12 | 213 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score.h) | C++ | 49 | 154 | 19 | 222 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_all.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_all.cu) | CUDA C++ | 29 | 60 | 6 | 95 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_all_impl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_all_impl.h) | C++ | 20 | 49 | 11 | 80 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_all_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_all_inl.h) | C++ | 157 | 83 | 38 | 278 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_best.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_best.cu) | CUDA C++ | 25 | 48 | 6 | 79 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_best_impl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_best_impl.h) | C++ | 18 | 43 | 11 | 72 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_best_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_best_inl.h) | C++ | 126 | 75 | 38 | 239 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_gapped.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_gapped.cu) | CUDA C++ | 43 | 57 | 7 | 107 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_opposite_impl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_opposite_impl.h) | C++ | 17 | 46 | 11 | 74 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_opposite_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_opposite_inl.h) | C++ | 148 | 81 | 52 | 281 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_paired.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_paired.cu) | CUDA C++ | 55 | 76 | 12 | 143 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_paired_impl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_paired_impl.h) | C++ | 18 | 43 | 11 | 72 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_paired_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_paired_inl.h) | C++ | 149 | 82 | 46 | 277 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_ungapped.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/score_ungapped.cu) | CUDA C++ | 43 | 57 | 7 | 107 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/scoring.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/scoring.h) | C++ | 213 | 145 | 85 | 443 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/scoring_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/scoring_inl.h) | C++ | 153 | 31 | 18 | 202 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/scoring_queues.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/scoring_queues.h) | C++ | 255 | 241 | 86 | 582 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/scoring_queues_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/scoring_queues_inl.h) | C++ | 244 | 93 | 33 | 370 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/scoring_queues_test.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/scoring_queues_test.cu) | CUDA C++ | 230 | 83 | 69 | 382 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/seed_hit.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/seed_hit.h) | C++ | 135 | 85 | 32 | 252 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/seed_hit_deque_array.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/seed_hit_deque_array.cu) | CUDA C++ | 32 | 32 | 8 | 72 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/seed_hit_deque_array.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/seed_hit_deque_array.h) | C++ | 170 | 127 | 58 | 355 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/seed_hit_deque_array_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/seed_hit_deque_array_inl.h) | C++ | 69 | 37 | 8 | 114 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/seed_hit_deque_array_test.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/seed_hit_deque_array_test.cu) | CUDA C++ | 60 | 35 | 27 | 122 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/select.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/select.cu) | CUDA C++ | 170 | 78 | 42 | 290 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/select.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/select.h) | C++ | 62 | 92 | 21 | 175 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/select_impl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/select_impl.h) | C++ | 60 | 72 | 17 | 149 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/select_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/select_inl.h) | C++ | 469 | 216 | 126 | 811 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/stats.cpp](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/stats.cpp) | C++ | 1,067 | 118 | 135 | 1,320 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/stats.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/stats.h) | C++ | 116 | 39 | 31 | 186 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/string_utils.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/string_utils.h) | C++ | 35 | 30 | 13 | 78 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/traceback.cu](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/traceback.cu) | CUDA C++ | 182 | 62 | 18 | 262 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/traceback.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/traceback.h) | C++ | 130 | 68 | 23 | 221 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/traceback_impl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/traceback_impl.h) | C++ | 98 | 50 | 18 | 166 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/traceback_inl.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/traceback_inl.h) | C++ | 730 | 171 | 132 | 1,033 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/utils.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/cuda/utils.h) | C++ | 38 | 28 | 12 | 78 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/quality_coeffs.cpp](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/quality_coeffs.cpp) | C++ | 63 | 30 | 6 | 99 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/quality_coeffs.h](/fast_gicp/thirdparty/nvbio/nvBowtie/bowtie2/quality_coeffs.h) | C++ | 20 | 30 | 8 | 58 |
| [fast_gicp/thirdparty/nvbio/nvBowtie/nvBowtie.cpp](/fast_gicp/thirdparty/nvbio/nvBowtie/nvBowtie.cpp) | C++ | 751 | 79 | 120 | 950 |
| [fast_gicp/thirdparty/nvbio/nvExtractReads/nvExtractReads.cu](/fast_gicp/thirdparty/nvbio/nvExtractReads/nvExtractReads.cu) | CUDA C++ | 240 | 49 | 61 | 350 |
| [fast_gicp/thirdparty/nvbio/nvFM-server/nvFM-server.cpp](/fast_gicp/thirdparty/nvbio/nvFM-server/nvFM-server.cpp) | C++ | 23 | 28 | 11 | 62 |
| [fast_gicp/thirdparty/nvbio/nvLighter/bloom_filters.h](/fast_gicp/thirdparty/nvbio/nvLighter/bloom_filters.h) | C++ | 48 | 56 | 17 | 121 |
| [fast_gicp/thirdparty/nvbio/nvLighter/bloom_filters_inl.h](/fast_gicp/thirdparty/nvbio/nvLighter/bloom_filters_inl.h) | C++ | 185 | 52 | 44 | 281 |
| [fast_gicp/thirdparty/nvbio/nvLighter/error_correct.cu](/fast_gicp/thirdparty/nvbio/nvLighter/error_correct.cu) | CUDA C++ | 686 | 117 | 137 | 940 |
| [fast_gicp/thirdparty/nvbio/nvLighter/error_correct.h](/fast_gicp/thirdparty/nvbio/nvLighter/error_correct.h) | C++ | 48 | 45 | 12 | 105 |
| [fast_gicp/thirdparty/nvbio/nvLighter/input_thread.cu](/fast_gicp/thirdparty/nvbio/nvLighter/input_thread.cu) | CUDA C++ | 36 | 31 | 13 | 80 |
| [fast_gicp/thirdparty/nvbio/nvLighter/input_thread.h](/fast_gicp/thirdparty/nvbio/nvLighter/input_thread.h) | C++ | 36 | 57 | 13 | 106 |
| [fast_gicp/thirdparty/nvbio/nvLighter/nvLighter.cu](/fast_gicp/thirdparty/nvbio/nvLighter/nvLighter.cu) | CUDA C++ | 611 | 98 | 120 | 829 |
| [fast_gicp/thirdparty/nvbio/nvLighter/output_thread.cu](/fast_gicp/thirdparty/nvbio/nvLighter/output_thread.cu) | CUDA C++ | 96 | 31 | 13 | 140 |
| [fast_gicp/thirdparty/nvbio/nvLighter/output_thread.h](/fast_gicp/thirdparty/nvbio/nvLighter/output_thread.h) | C++ | 18 | 51 | 13 | 82 |
| [fast_gicp/thirdparty/nvbio/nvLighter/sample_kmers.cu](/fast_gicp/thirdparty/nvbio/nvLighter/sample_kmers.cu) | CUDA C++ | 406 | 133 | 98 | 637 |
| [fast_gicp/thirdparty/nvbio/nvLighter/sample_kmers.h](/fast_gicp/thirdparty/nvbio/nvLighter/sample_kmers.h) | C++ | 72 | 59 | 19 | 150 |
| [fast_gicp/thirdparty/nvbio/nvLighter/utils.h](/fast_gicp/thirdparty/nvbio/nvLighter/utils.h) | C++ | 94 | 32 | 23 | 149 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/assembly.h](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/assembly.h) | C++ | 18 | 35 | 13 | 66 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/assembly_graph.h](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/assembly_graph.h) | C++ | 77 | 35 | 24 | 136 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/assembly_graph_inl.h](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/assembly_graph_inl.h) | C++ | 495 | 83 | 91 | 669 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/assembly_types.h](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/assembly_types.h) | C++ | 73 | 27 | 17 | 117 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/bam_io.cu](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/bam_io.cu) | CUDA C++ | 213 | 40 | 32 | 285 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/bam_io.h](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/bam_io.h) | C++ | 297 | 42 | 39 | 378 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/haplotype_caller.cu](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/haplotype_caller.cu) | CUDA C++ | 61 | 34 | 12 | 107 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/haplotype_caller.h](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/haplotype_caller.h) | C++ | 79 | 40 | 20 | 139 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/kmers.h](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/kmers.h) | C++ | 83 | 29 | 20 | 132 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/kmers_inl.h](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/kmers_inl.h) | C++ | 1,237 | 206 | 188 | 1,631 |
| [fast_gicp/thirdparty/nvbio/nvMicroAssembly/regions.h](/fast_gicp/thirdparty/nvbio/nvMicroAssembly/regions.h) | C++ | 16 | 29 | 6 | 51 |
| [fast_gicp/thirdparty/nvbio/nvSSA/nvSSA.cpp](/fast_gicp/thirdparty/nvbio/nvSSA/nvSSA.cpp) | C++ | 71 | 31 | 21 | 123 |
| [fast_gicp/thirdparty/nvbio/nvSetBWT/input_thread.h](/fast_gicp/thirdparty/nvbio/nvSetBWT/input_thread.h) | C++ | 35 | 40 | 12 | 87 |
| [fast_gicp/thirdparty/nvbio/nvSetBWT/nvSetBWT.cu](/fast_gicp/thirdparty/nvbio/nvSetBWT/nvSetBWT.cu) | CUDA C++ | 290 | 83 | 63 | 436 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/alignment.cpp](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/alignment.cpp) | C++ | 17 | 26 | 7 | 50 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/alignment.h](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/alignment.h) | C++ | 108 | 34 | 21 | 163 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/alignment_bam.cpp](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/alignment_bam.cpp) | C++ | 96 | 32 | 28 | 156 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/alignment_dbg.cpp](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/alignment_dbg.cpp) | C++ | 73 | 39 | 21 | 133 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/filter.h](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/filter.h) | C++ | 55 | 43 | 14 | 112 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/html.h](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/html.h) | C++ | 620 | 59 | 68 | 747 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/nvbio-aln-diff.cpp](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/nvbio-aln-diff.cpp) | C++ | 367 | 29 | 82 | 478 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/pe_analyzer.cpp](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/pe_analyzer.cpp) | C++ | 528 | 80 | 77 | 685 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/pe_analyzer.h](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/pe_analyzer.h) | C++ | 62 | 28 | 20 | 110 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/se_analyzer.cpp](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/se_analyzer.cpp) | C++ | 317 | 53 | 46 | 416 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/se_analyzer.h](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/se_analyzer.h) | C++ | 41 | 28 | 15 | 84 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/stats.h](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/stats.h) | C++ | 110 | 26 | 15 | 151 |
| [fast_gicp/thirdparty/nvbio/nvbio-aln-diff/utils.h](/fast_gicp/thirdparty/nvbio/nvbio-aln-diff/utils.h) | C++ | 175 | 30 | 22 | 227 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/alignment_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/alignment_test.cu) | CUDA C++ | 940 | 107 | 153 | 1,200 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/alignment_test_utils.h](/fast_gicp/thirdparty/nvbio/nvbio-test/alignment_test_utils.h) | C++ | 616 | 73 | 105 | 794 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/alloc_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/alloc_test.cu) | CUDA C++ | 54 | 30 | 21 | 105 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/bloom_filter_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/bloom_filter_test.cu) | CUDA C++ | 108 | 29 | 34 | 171 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/bwt_test.cpp](/fast_gicp/thirdparty/nvbio/nvbio-test/bwt_test.cpp) | C++ | 40 | 28 | 14 | 82 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/cache_test.cpp](/fast_gicp/thirdparty/nvbio/nvbio-test/cache_test.cpp) | C++ | 54 | 32 | 13 | 99 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/condtion_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/condtion_test.cu) | CUDA C++ | 251 | 65 | 79 | 395 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/fasta_test.cpp](/fast_gicp/thirdparty/nvbio/nvbio-test/fasta_test.cpp) | C++ | 45 | 26 | 15 | 86 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/fastq_test.cpp](/fast_gicp/thirdparty/nvbio/nvbio-test/fastq_test.cpp) | C++ | 49 | 26 | 16 | 91 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/fmindex_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/fmindex_test.cu) | CUDA C++ | 796 | 81 | 171 | 1,048 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/nvbio-test.cpp](/fast_gicp/thirdparty/nvbio/nvbio-test/nvbio-test.cpp) | C++ | 216 | 30 | 26 | 272 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/packedstream_test.cpp](/fast_gicp/thirdparty/nvbio/nvbio-test/packedstream_test.cpp) | C++ | 311 | 36 | 75 | 422 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/qgram_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/qgram_test.cu) | CUDA C++ | 534 | 71 | 129 | 734 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/rank_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/rank_test.cu) | CUDA C++ | 165 | 43 | 50 | 258 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/sequence_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/sequence_test.cu) | CUDA C++ | 99 | 33 | 21 | 153 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/string_set_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/string_set_test.cu) | CUDA C++ | 657 | 96 | 196 | 949 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/sum_tree_test.cpp](/fast_gicp/thirdparty/nvbio/nvbio-test/sum_tree_test.cpp) | C++ | 125 | 41 | 35 | 201 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/syncblocks_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/syncblocks_test.cu) | CUDA C++ | 80 | 31 | 27 | 138 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/utils.h](/fast_gicp/thirdparty/nvbio/nvbio-test/utils.h) | C++ | 43 | 26 | 14 | 83 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/wavelet_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/wavelet_test.cu) | CUDA C++ | 85 | 35 | 29 | 149 |
| [fast_gicp/thirdparty/nvbio/nvbio-test/work_queue_test.cu](/fast_gicp/thirdparty/nvbio/nvbio-test/work_queue_test.cu) | CUDA C++ | 609 | 88 | 148 | 845 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/alignment.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/alignment.h) | C++ | 175 | 528 | 23 | 726 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/alignment_base.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/alignment_base.h) | C++ | 190 | 173 | 59 | 422 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/alignment_base_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/alignment_base_inl.h) | C++ | 64 | 29 | 12 | 105 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/alignment_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/alignment_inl.h) | C++ | 339 | 211 | 38 | 588 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/banded_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/banded_inl.h) | C++ | 280 | 186 | 27 | 493 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/batched.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/batched.h) | C++ | 124 | 325 | 39 | 488 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/batched_banded_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/batched_banded_inl.h) | C++ | 264 | 116 | 79 | 459 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/batched_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/batched_inl.h) | C++ | 728 | 209 | 172 | 1,109 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/batched_stream.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/batched_stream.h) | C++ | 181 | 90 | 33 | 304 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/ed/ed_banded_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/ed/ed_banded_inl.h) | C++ | 152 | 142 | 15 | 309 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/ed/ed_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/ed/ed_inl.h) | C++ | 177 | 163 | 36 | 376 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/ed/ed_utils.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/ed/ed_utils.h) | C++ | 17 | 33 | 11 | 61 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/ed/ed_warp_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/ed/ed_warp_inl.h) | C++ | 38 | 27 | 8 | 73 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/gotoh/gotoh_banded_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/gotoh/gotoh_banded_inl.h) | C++ | 579 | 300 | 91 | 970 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/gotoh/gotoh_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/gotoh/gotoh_inl.h) | C++ | 1,176 | 529 | 173 | 1,878 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/gotoh/gotoh_warp_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/gotoh/gotoh_warp_inl.h) | C++ | 184 | 63 | 43 | 290 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/hamming/hamming_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/hamming/hamming_inl.h) | C++ | 860 | 654 | 141 | 1,655 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/myers/myers_banded_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/myers/myers_banded_inl.h) | C++ | 257 | 67 | 50 | 374 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/sink.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/sink.h) | C++ | 72 | 98 | 31 | 201 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/sink_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/sink_inl.h) | C++ | 119 | 62 | 20 | 201 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/sw/sw_banded_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/sw/sw_banded_inl.h) | C++ | 491 | 244 | 79 | 814 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/sw/sw_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/sw/sw_inl.h) | C++ | 912 | 656 | 142 | 1,710 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/sw/sw_warp_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/sw/sw_warp_inl.h) | C++ | 147 | 62 | 35 | 244 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/utils.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/utils.h) | C++ | 144 | 112 | 40 | 296 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/utils_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/utils_inl.h) | C++ | 214 | 70 | 34 | 318 |
| [fast_gicp/thirdparty/nvbio/nvbio/alignment/warp_utils.h](/fast_gicp/thirdparty/nvbio/nvbio/alignment/warp_utils.h) | C++ | 63 | 28 | 14 | 105 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/algorithms.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/algorithms.h) | C++ | 184 | 94 | 45 | 323 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/atomics.cpp](/fast_gicp/thirdparty/nvbio/nvbio/basic/atomics.cpp) | C++ | 145 | 28 | 26 | 199 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/atomics.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/atomics.h) | C++ | 269 | 99 | 100 | 468 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/bloom_filter.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/bloom_filter.h) | C++ | 195 | 192 | 43 | 430 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/bloom_filter_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/bloom_filter_inl.h) | C++ | 130 | 26 | 26 | 182 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/bnt.cpp](/fast_gicp/thirdparty/nvbio/nvbio/basic/bnt.cpp) | C++ | 185 | 51 | 48 | 284 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/bnt.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/bnt.h) | C++ | 56 | 30 | 17 | 103 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cache.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cache.h) | C++ | 36 | 46 | 16 | 98 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cache_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cache_inl.h) | C++ | 119 | 38 | 29 | 186 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cached_iterator.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cached_iterator.h) | C++ | 126 | 133 | 42 | 301 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cached_iterator_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cached_iterator_inl.h) | C++ | 113 | 60 | 20 | 193 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cast_iterator.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cast_iterator.h) | C++ | 11 | 34 | 9 | 54 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/console.cpp](/fast_gicp/thirdparty/nvbio/nvbio/basic/console.cpp) | C++ | 471 | 27 | 35 | 533 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/console.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/console.h) | C++ | 41 | 29 | 12 | 82 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/arch.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/arch.h) | C++ | 43 | 39 | 25 | 107 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/arch_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/arch_inl.h) | C++ | 199 | 43 | 46 | 288 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/atomics.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/atomics.h) | C++ | 48 | 27 | 8 | 83 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/condition.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/condition.h) | C++ | 54 | 66 | 21 | 141 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/host_device_buffer.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/host_device_buffer.h) | C++ | 142 | 31 | 28 | 201 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/ldg.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/ldg.h) | C++ | 229 | 99 | 46 | 374 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/pingpong_queues.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/pingpong_queues.h) | C++ | 60 | 138 | 25 | 223 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/primitives.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/primitives.h) | C++ | 81 | 135 | 23 | 239 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/primitives_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/primitives_inl.h) | C++ | 302 | 119 | 62 | 483 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/scan.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/scan.h) | C++ | 331 | 148 | 45 | 524 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/scan_test.cu](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/scan_test.cu) | CUDA C++ | 92 | 28 | 22 | 142 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/simd_functions.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/simd_functions.h) | C++ | 803 | 187 | 48 | 1,038 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/sort.cu](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/sort.cu) | CUDA C++ | 142 | 62 | 62 | 266 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/sort.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/sort.h) | C++ | 32 | 136 | 18 | 186 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/syncblocks.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/syncblocks.h) | C++ | 25 | 48 | 13 | 86 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/syncblocks_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/syncblocks_inl.h) | C++ | 47 | 52 | 19 | 118 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/tex.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/tex.h) | C++ | 216 | 29 | 28 | 273 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/timer.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/timer.h) | C++ | 49 | 53 | 18 | 120 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue.h) | C++ | 82 | 223 | 34 | 339 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_inl.h) | C++ | 69 | 46 | 27 | 142 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_multipass.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_multipass.h) | C++ | 45 | 51 | 18 | 114 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_multipass_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_multipass_inl.h) | C++ | 189 | 58 | 58 | 305 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_ordered.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_ordered.h) | C++ | 63 | 47 | 17 | 127 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_ordered_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_ordered_inl.h) | C++ | 315 | 121 | 106 | 542 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_persistent.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_persistent.h) | C++ | 51 | 90 | 21 | 162 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_persistent_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/cuda/work_queue_persistent_inl.h) | C++ | 128 | 76 | 52 | 256 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/deinterleaved_iterator.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/deinterleaved_iterator.h) | C++ | 103 | 61 | 25 | 189 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/dna.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/dna.h) | C++ | 136 | 54 | 23 | 213 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/exceptions.cpp](/fast_gicp/thirdparty/nvbio/nvbio/basic/exceptions.cpp) | C++ | 43 | 30 | 11 | 84 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/exceptions.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/exceptions.h) | C++ | 33 | 33 | 18 | 84 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/html.cpp](/fast_gicp/thirdparty/nvbio/nvbio/basic/html.cpp) | C++ | 663 | 124 | 30 | 817 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/html.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/html.h) | C++ | 65 | 85 | 25 | 175 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/index_transform_iterator.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/index_transform_iterator.h) | C++ | 127 | 87 | 31 | 245 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/interval_heap.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/interval_heap.h) | C++ | 289 | 194 | 51 | 534 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/iterator.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/iterator.h) | C++ | 67 | 37 | 19 | 123 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/iterator_reference.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/iterator_reference.h) | C++ | 31 | 55 | 20 | 106 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/merge_sort.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/merge_sort.h) | C++ | 56 | 55 | 14 | 125 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/mmap.cpp](/fast_gicp/thirdparty/nvbio/nvbio/basic/mmap.cpp) | C++ | 181 | 30 | 52 | 263 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/mmap.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/mmap.h) | C++ | 46 | 100 | 23 | 169 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/numbers.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/numbers.h) | C++ | 881 | 297 | 210 | 1,388 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/omp.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/omp.h) | C++ | 11 | 26 | 7 | 44 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/options.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/options.h) | C++ | 127 | 26 | 18 | 171 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/packed_vector.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/packed_vector.h) | C++ | 73 | 76 | 36 | 185 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/packed_vector_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/packed_vector_inl.h) | C++ | 65 | 46 | 16 | 127 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/packedstream.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/packedstream.h) | C++ | 313 | 272 | 107 | 692 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/packedstream_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/packedstream_inl.h) | C++ | 1,002 | 202 | 275 | 1,479 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/packedstream_loader.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/packedstream_loader.h) | C++ | 47 | 103 | 21 | 171 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/packedstream_loader_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/packedstream_loader_inl.h) | C++ | 100 | 38 | 23 | 161 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/pipeline.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/pipeline.h) | C++ | 23 | 63 | 18 | 104 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/pipeline_context.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/pipeline_context.h) | C++ | 13 | 28 | 9 | 50 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/pipeline_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/pipeline_inl.h) | C++ | 192 | 140 | 72 | 404 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/pod.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/pod.h) | C++ | 38 | 26 | 15 | 79 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/popcount.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/popcount.h) | C++ | 41 | 86 | 29 | 156 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/popcount_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/popcount_inl.h) | C++ | 333 | 127 | 47 | 507 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/primitives.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/primitives.h) | C++ | 202 | 206 | 41 | 449 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/primitives_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/primitives_inl.h) | C++ | 969 | 376 | 119 | 1,464 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/priority_deque.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/priority_deque.h) | C++ | 192 | 281 | 37 | 510 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/priority_queue.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/priority_queue.h) | C++ | 35 | 107 | 27 | 169 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/priority_queue_inline.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/priority_queue_inline.h) | C++ | 141 | 61 | 30 | 232 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/profiling.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/profiling.h) | C++ | 27 | 26 | 6 | 59 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/shared_pointer.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/shared_pointer.h) | C++ | 480 | 55 | 124 | 659 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/simd.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/simd.h) | C++ | 66 | 29 | 33 | 128 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/simd_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/simd_inl.h) | C++ | 230 | 26 | 12 | 268 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/static_vector.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/static_vector.h) | C++ | 118 | 43 | 49 | 210 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/static_vector_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/static_vector_inl.h) | C++ | 166 | 26 | 11 | 203 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/strided_iterator.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/strided_iterator.h) | C++ | 143 | 114 | 34 | 291 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/sum_tree.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/sum_tree.h) | C++ | 40 | 121 | 23 | 184 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/sum_tree_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/sum_tree_inl.h) | C++ | 109 | 46 | 27 | 182 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/system.cpp](/fast_gicp/thirdparty/nvbio/nvbio/basic/system.cpp) | C++ | 25 | 29 | 9 | 63 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/system.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/system.h) | C++ | 5 | 26 | 6 | 37 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/threads.cpp](/fast_gicp/thirdparty/nvbio/nvbio/basic/threads.cpp) | C++ | 209 | 51 | 55 | 315 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/threads.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/threads.h) | C++ | 95 | 123 | 36 | 254 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/thrust_view.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/thrust_view.h) | C++ | 40 | 57 | 21 | 118 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/timer.cpp](/fast_gicp/thirdparty/nvbio/nvbio/basic/timer.cpp) | C++ | 92 | 26 | 27 | 145 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/timer.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/timer.h) | C++ | 95 | 64 | 32 | 191 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/transform_iterator.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/transform_iterator.h) | C++ | 237 | 130 | 49 | 416 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/types.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/types.h) | C++ | 199 | 124 | 65 | 388 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/vector.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/vector.h) | C++ | 77 | 54 | 28 | 159 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/vector_array.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/vector_array.h) | C++ | 190 | 184 | 47 | 421 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/vector_loads.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/vector_loads.h) | C++ | 135 | 31 | 25 | 191 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/vector_view.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/vector_view.h) | C++ | 108 | 149 | 52 | 309 |
| [fast_gicp/thirdparty/nvbio/nvbio/basic/version.h](/fast_gicp/thirdparty/nvbio/nvbio/basic/version.h) | C++ | 6 | 26 | 4 | 36 |
| [fast_gicp/thirdparty/nvbio/nvbio/fasta/fasta.h](/fast_gicp/thirdparty/nvbio/nvbio/fasta/fasta.h) | C++ | 40 | 115 | 25 | 180 |
| [fast_gicp/thirdparty/nvbio/nvbio/fasta/fasta_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/fasta/fasta_inl.h) | C++ | 130 | 91 | 31 | 252 |
| [fast_gicp/thirdparty/nvbio/nvbio/fastq/fastq.cpp](/fast_gicp/thirdparty/nvbio/nvbio/fastq/fastq.cpp) | C++ | 49 | 38 | 17 | 104 |
| [fast_gicp/thirdparty/nvbio/nvbio/fastq/fastq.h](/fast_gicp/thirdparty/nvbio/nvbio/fastq/fastq.h) | C++ | 73 | 129 | 38 | 240 |
| [fast_gicp/thirdparty/nvbio/nvbio/fastq/fastq_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/fastq/fastq_inl.h) | C++ | 155 | 52 | 36 | 243 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/backtrack.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/backtrack.h) | C++ | 83 | 63 | 27 | 173 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/bidir.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/bidir.h) | C++ | 29 | 55 | 10 | 94 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/bidir_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/bidir_inl.h) | C++ | 75 | 56 | 16 | 147 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/bwt.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/bwt.h) | C++ | 47 | 41 | 13 | 101 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/filter.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/filter.h) | C++ | 97 | 126 | 33 | 256 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/filter_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/filter_inl.h) | C++ | 254 | 85 | 66 | 405 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/fmindex.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/fmindex.h) | C++ | 190 | 446 | 35 | 671 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/fmindex_device.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/fmindex_device.h) | C++ | 31 | 33 | 9 | 73 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/fmindex_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/fmindex_inl.h) | C++ | 410 | 131 | 69 | 610 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/mem.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/mem.h) | C++ | 199 | 242 | 58 | 499 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/mem_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/mem_inl.h) | C++ | 1,071 | 252 | 229 | 1,552 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/paged_text.cpp](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/paged_text.cpp) | C++ | 188 | 57 | 45 | 290 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/paged_text.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/paged_text.h) | C++ | 121 | 124 | 46 | 291 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/paged_text_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/paged_text_inl.h) | C++ | 818 | 213 | 253 | 1,284 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/rank_dictionary.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/rank_dictionary.h) | C++ | 93 | 160 | 32 | 285 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/rank_dictionary_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/rank_dictionary_inl.h) | C++ | 463 | 131 | 108 | 702 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/ssa.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/ssa.h) | C++ | 145 | 168 | 55 | 368 |
| [fast_gicp/thirdparty/nvbio/nvbio/fmindex/ssa_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/fmindex/ssa_inl.h) | C++ | 307 | 111 | 89 | 507 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/alignments.h](/fast_gicp/thirdparty/nvbio/nvbio/io/alignments.h) | C++ | 322 | 75 | 86 | 483 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/alignments_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/io/alignments_inl.h) | C++ | 90 | 41 | 9 | 140 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/bam_format.h](/fast_gicp/thirdparty/nvbio/nvbio/io/bam_format.h) | C++ | 44 | 40 | 14 | 98 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/bufferedtextfile.h](/fast_gicp/thirdparty/nvbio/nvbio/io/bufferedtextfile.h) | C++ | 102 | 40 | 28 | 170 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/fmindex/fmindex.h](/fast_gicp/thirdparty/nvbio/nvbio/io/fmindex/fmindex.h) | C++ | 206 | 112 | 58 | 376 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/fmindex/fmindex_impl.cu](/fast_gicp/thirdparty/nvbio/nvbio/io/fmindex/fmindex_impl.cu) | CUDA C++ | 649 | 72 | 135 | 856 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_bam.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_bam.cpp) | C++ | 459 | 112 | 130 | 701 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_bam.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_bam.h) | C++ | 63 | 40 | 22 | 125 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_batch.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_batch.cpp) | C++ | 52 | 32 | 13 | 97 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_batch.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_batch.h) | C++ | 69 | 45 | 22 | 136 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_databuffer.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_databuffer.cpp) | C++ | 99 | 27 | 31 | 157 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_databuffer.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_databuffer.h) | C++ | 35 | 45 | 14 | 94 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_debug.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_debug.cpp) | C++ | 150 | 44 | 35 | 229 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_debug.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_debug.h) | C++ | 68 | 42 | 16 | 126 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_file.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_file.cpp) | C++ | 64 | 28 | 16 | 108 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_file.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_file.h) | C++ | 55 | 85 | 25 | 165 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_gzip.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_gzip.cpp) | C++ | 85 | 41 | 31 | 157 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_gzip.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_gzip.h) | C++ | 31 | 28 | 13 | 72 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_priv.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_priv.cpp) | C++ | 73 | 32 | 13 | 118 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_priv.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_priv.h) | C++ | 87 | 41 | 26 | 154 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_sam.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_sam.cpp) | C++ | 399 | 74 | 110 | 583 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_sam.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_sam.h) | C++ | 75 | 53 | 22 | 150 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_stats.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_stats.cpp) | C++ | 6 | 26 | 4 | 36 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_stats.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_stats.h) | C++ | 20 | 29 | 10 | 59 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_types.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_types.h) | C++ | 53 | 69 | 20 | 142 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output/output_utils.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output/output_utils.h) | C++ | 77 | 31 | 17 | 125 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output_stream.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/output_stream.cpp) | C++ | 90 | 37 | 27 | 154 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/output_stream.h](/fast_gicp/thirdparty/nvbio/nvbio/io/output_stream.h) | C++ | 30 | 59 | 21 | 110 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/bam.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/bam.cpp) | C++ | 234 | 71 | 63 | 368 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/bam.h](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/bam.h) | C++ | 22 | 46 | 15 | 83 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads.cpp) | C++ | 451 | 79 | 101 | 631 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads.h](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads.h) | C++ | 301 | 182 | 74 | 557 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads_fastq.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads_fastq.cpp) | C++ | 168 | 54 | 42 | 264 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads_fastq.h](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads_fastq.h) | C++ | 67 | 54 | 25 | 146 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads_priv.h](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads_priv.h) | C++ | 41 | 52 | 18 | 111 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads_txt.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads_txt.cpp) | C++ | 120 | 43 | 25 | 188 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads_txt.h](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/reads_txt.h) | C++ | 65 | 54 | 25 | 144 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/sam.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/sam.cpp) | C++ | 333 | 71 | 67 | 471 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/reads/sam.h](/fast_gicp/thirdparty/nvbio/nvbio/io/reads/sam.h) | C++ | 55 | 48 | 20 | 123 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence.h) | C++ | 366 | 321 | 84 | 771 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_access.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_access.h) | C++ | 210 | 113 | 53 | 376 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_bam.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_bam.cpp) | C++ | 250 | 73 | 66 | 389 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_bam.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_bam.h) | C++ | 22 | 47 | 16 | 85 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_encoder.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_encoder.cpp) | C++ | 398 | 93 | 70 | 561 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_encoder.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_encoder.h) | C++ | 44 | 60 | 18 | 122 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_fasta.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_fasta.cpp) | C++ | 165 | 49 | 39 | 253 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_fasta.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_fasta.h) | C++ | 32 | 55 | 17 | 104 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_fastq.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_fastq.cpp) | C++ | 341 | 103 | 89 | 533 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_fastq.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_fastq.h) | C++ | 98 | 74 | 39 | 211 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_mmap.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_mmap.cpp) | C++ | 73 | 39 | 14 | 126 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_mmap.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_mmap.h) | C++ | 78 | 57 | 18 | 153 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_pac.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_pac.cpp) | C++ | 335 | 87 | 72 | 494 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_pac.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_pac.h) | C++ | 20 | 54 | 9 | 83 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_priv.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_priv.cpp) | C++ | 261 | 75 | 48 | 384 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_priv.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_priv.h) | C++ | 56 | 52 | 20 | 128 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_sam.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_sam.cpp) | C++ | 355 | 73 | 68 | 496 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_sam.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_sam.h) | C++ | 55 | 57 | 22 | 134 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_traits.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_traits.h) | C++ | 13 | 32 | 9 | 54 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_txt.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_txt.cpp) | C++ | 228 | 56 | 54 | 338 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_txt.h](/fast_gicp/thirdparty/nvbio/nvbio/io/sequence/sequence_txt.h) | C++ | 76 | 68 | 33 | 177 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/utils.h](/fast_gicp/thirdparty/nvbio/nvbio/io/utils.h) | C++ | 177 | 112 | 59 | 348 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/vcf.cpp](/fast_gicp/thirdparty/nvbio/nvbio/io/vcf.cpp) | C++ | 158 | 48 | 37 | 243 |
| [fast_gicp/thirdparty/nvbio/nvbio/io/vcf.h](/fast_gicp/thirdparty/nvbio/nvbio/io/vcf.h) | C++ | 42 | 37 | 15 | 94 |
| [fast_gicp/thirdparty/nvbio/nvbio/qgram/filter.h](/fast_gicp/thirdparty/nvbio/nvbio/qgram/filter.h) | C++ | 107 | 185 | 34 | 326 |
| [fast_gicp/thirdparty/nvbio/nvbio/qgram/filter_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/qgram/filter_inl.h) | C++ | 298 | 128 | 67 | 493 |
| [fast_gicp/thirdparty/nvbio/nvbio/qgram/qgram.h](/fast_gicp/thirdparty/nvbio/nvbio/qgram/qgram.h) | C++ | 365 | 485 | 82 | 932 |
| [fast_gicp/thirdparty/nvbio/nvbio/qgram/qgram_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/qgram/qgram_inl.h) | C++ | 280 | 116 | 68 | 464 |
| [fast_gicp/thirdparty/nvbio/nvbio/qgram/qgroup.h](/fast_gicp/thirdparty/nvbio/nvbio/qgram/qgroup.h) | C++ | 158 | 104 | 42 | 304 |
| [fast_gicp/thirdparty/nvbio/nvbio/qgram/qgroup_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/qgram/qgroup_inl.h) | C++ | 152 | 80 | 57 | 289 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/alphabet.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/alphabet.h) | C++ | 185 | 101 | 31 | 317 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/alphabet_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/alphabet_inl.h) | C++ | 152 | 46 | 20 | 218 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/infix.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/infix.h) | C++ | 268 | 228 | 102 | 598 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/prefetcher.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/prefetcher.h) | C++ | 178 | 152 | 44 | 374 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/prefix.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/prefix.h) | C++ | 225 | 188 | 83 | 496 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/seeds.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/seeds.h) | C++ | 40 | 78 | 17 | 135 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/seeds_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/seeds_inl.h) | C++ | 141 | 55 | 37 | 233 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/string.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/string.h) | C++ | 18 | 31 | 9 | 58 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/string_iterator.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/string_iterator.h) | C++ | 88 | 97 | 34 | 219 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/string_iterator_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/string_iterator_inl.h) | C++ | 107 | 60 | 20 | 187 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/string_set.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/string_set.h) | C++ | 612 | 554 | 130 | 1,296 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/string_set_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/string_set_inl.h) | C++ | 1,649 | 214 | 314 | 2,177 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/string_set_transform.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/string_set_transform.h) | C++ | 47 | 59 | 17 | 123 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/string_traits.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/string_traits.h) | C++ | 37 | 35 | 13 | 85 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/suffix.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/suffix.h) | C++ | 269 | 193 | 91 | 553 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/vectorized_string.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/vectorized_string.h) | C++ | 190 | 141 | 47 | 378 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/wavelet_tree.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/wavelet_tree.h) | C++ | 159 | 154 | 48 | 361 |
| [fast_gicp/thirdparty/nvbio/nvbio/strings/wavelet_tree_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/strings/wavelet_tree_inl.h) | C++ | 285 | 125 | 90 | 500 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/blockwise_sufsort.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/blockwise_sufsort.h) | C++ | 356 | 90 | 92 | 538 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/bwte.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/bwte.h) | C++ | 122 | 87 | 37 | 246 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/bwte_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/bwte_inl.h) | C++ | 718 | 128 | 158 | 1,004 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/compression_sort.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/compression_sort.h) | C++ | 560 | 250 | 124 | 934 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/dcs.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/dcs.h) | C++ | 234 | 73 | 53 | 360 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/dcs_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/dcs_inl.h) | C++ | 107 | 62 | 29 | 198 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt.cu](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt.cu) | CUDA C++ | 574 | 159 | 124 | 857 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt.h) | C++ | 5 | 68 | 8 | 81 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt_bgz.cu](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt_bgz.cu) | CUDA C++ | 207 | 91 | 50 | 348 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt_bgz.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt_bgz.h) | C++ | 35 | 53 | 20 | 108 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt_lz4.cu](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt_lz4.cu) | CUDA C++ | 146 | 74 | 38 | 258 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt_lz4.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/file_bwt_lz4.h) | C++ | 32 | 51 | 19 | 102 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/prefix_doubling_sufsort.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/prefix_doubling_sufsort.h) | C++ | 502 | 158 | 108 | 768 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort.h) | C++ | 67 | 222 | 24 | 313 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort_bucketing.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort_bucketing.h) | C++ | 644 | 214 | 200 | 1,058 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort_inl.h) | C++ | 723 | 141 | 187 | 1,051 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort_priv.cu](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort_priv.cu) | CUDA C++ | 422 | 57 | 59 | 538 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort_priv.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort_priv.h) | C++ | 1,471 | 500 | 319 | 2,290 |
| [fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort_utils.h](/fast_gicp/thirdparty/nvbio/nvbio/sufsort/sufsort_utils.h) | C++ | 364 | 135 | 89 | 588 |
| [fast_gicp/thirdparty/nvbio/nvbio/trie/sorted_dictionary.h](/fast_gicp/thirdparty/nvbio/nvbio/trie/sorted_dictionary.h) | C++ | 38 | 60 | 20 | 118 |
| [fast_gicp/thirdparty/nvbio/nvbio/trie/sorted_dictionary_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/trie/sorted_dictionary_inl.h) | C++ | 51 | 38 | 13 | 102 |
| [fast_gicp/thirdparty/nvbio/nvbio/trie/suffix_trie.h](/fast_gicp/thirdparty/nvbio/nvbio/trie/suffix_trie.h) | C++ | 120 | 144 | 51 | 315 |
| [fast_gicp/thirdparty/nvbio/nvbio/trie/suffix_trie_inl.h](/fast_gicp/thirdparty/nvbio/nvbio/trie/suffix_trie_inl.h) | C++ | 207 | 34 | 50 | 291 |
| [fast_gicp/thirdparty/nvbio/nvmem/align.cu](/fast_gicp/thirdparty/nvbio/nvmem/align.cu) | CUDA C++ | 252 | 74 | 59 | 385 |
| [fast_gicp/thirdparty/nvbio/nvmem/align.h](/fast_gicp/thirdparty/nvbio/nvmem/align.h) | C++ | 7 | 32 | 5 | 44 |
| [fast_gicp/thirdparty/nvbio/nvmem/build-chains.cu](/fast_gicp/thirdparty/nvbio/nvmem/build-chains.cu) | CUDA C++ | 180 | 71 | 45 | 296 |
| [fast_gicp/thirdparty/nvbio/nvmem/build-chains.h](/fast_gicp/thirdparty/nvbio/nvmem/build-chains.h) | C++ | 4 | 30 | 5 | 39 |
| [fast_gicp/thirdparty/nvbio/nvmem/filter-chains.cu](/fast_gicp/thirdparty/nvbio/nvmem/filter-chains.cu) | CUDA C++ | 227 | 52 | 56 | 335 |
| [fast_gicp/thirdparty/nvbio/nvmem/filter-chains.h](/fast_gicp/thirdparty/nvbio/nvmem/filter-chains.h) | C++ | 3 | 28 | 4 | 35 |
| [fast_gicp/thirdparty/nvbio/nvmem/mem-search.cu](/fast_gicp/thirdparty/nvbio/nvmem/mem-search.cu) | CUDA C++ | 162 | 55 | 48 | 265 |
| [fast_gicp/thirdparty/nvbio/nvmem/mem-search.h](/fast_gicp/thirdparty/nvbio/nvmem/mem-search.h) | C++ | 9 | 35 | 7 | 51 |
| [fast_gicp/thirdparty/nvbio/nvmem/nvmem.cu](/fast_gicp/thirdparty/nvbio/nvmem/nvmem.cu) | CUDA C++ | 142 | 43 | 32 | 217 |
| [fast_gicp/thirdparty/nvbio/nvmem/options.cpp](/fast_gicp/thirdparty/nvbio/nvmem/options.cpp) | C++ | 64 | 29 | 16 | 109 |
| [fast_gicp/thirdparty/nvbio/nvmem/options.h](/fast_gicp/thirdparty/nvbio/nvmem/options.h) | C++ | 42 | 33 | 11 | 86 |
| [fast_gicp/thirdparty/nvbio/nvmem/pipeline.h](/fast_gicp/thirdparty/nvbio/nvmem/pipeline.h) | C++ | 181 | 71 | 48 | 300 |
| [fast_gicp/thirdparty/nvbio/nvmem/util.cu](/fast_gicp/thirdparty/nvbio/nvmem/util.cu) | CUDA C++ | 36 | 28 | 12 | 76 |
| [fast_gicp/thirdparty/nvbio/nvmem/util.h](/fast_gicp/thirdparty/nvbio/nvmem/util.h) | C++ | 9 | 26 | 6 | 41 |
| [fast_gicp/thirdparty/nvbio/prototypes/bamsort/bam_io.cu](/fast_gicp/thirdparty/nvbio/prototypes/bamsort/bam_io.cu) | CUDA C++ | 590 | 51 | 78 | 719 |
| [fast_gicp/thirdparty/nvbio/prototypes/bamsort/bam_io.h](/fast_gicp/thirdparty/nvbio/prototypes/bamsort/bam_io.h) | C++ | 343 | 33 | 48 | 424 |
| [fast_gicp/thirdparty/nvbio/prototypes/bamsort/bam_sort.cu](/fast_gicp/thirdparty/nvbio/prototypes/bamsort/bam_sort.cu) | CUDA C++ | 527 | 101 | 95 | 723 |
| [fast_gicp/thirdparty/nvbio/prototypes/bamsort/bam_sort.h](/fast_gicp/thirdparty/nvbio/prototypes/bamsort/bam_sort.h) | C++ | 157 | 45 | 33 | 235 |
| [fast_gicp/thirdparty/nvbio/prototypes/bamsort/bamsort_types.h](/fast_gicp/thirdparty/nvbio/prototypes/bamsort/bamsort_types.h) | C++ | 63 | 22 | 17 | 102 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/README.md](/fast_gicp/thirdparty/nvbio/prototypes/psa/README.md) | Markdown | 147 | 0 | 67 | 214 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_alignments.h](/fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_alignments.h) | C++ | 27 | 8 | 10 | 45 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_commons.h](/fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_commons.h) | C++ | 32 | 13 | 13 | 58 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_errors.h](/fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_errors.h) | C++ | 22 | 6 | 8 | 36 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_pairwise.h](/fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_pairwise.h) | C++ | 19 | 6 | 8 | 33 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_pairwise_gpu.h](/fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_pairwise_gpu.h) | C++ | 8 | 6 | 6 | 20 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_profile.h](/fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_profile.h) | C++ | 15 | 6 | 19 | 40 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_regions.h](/fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_regions.h) | C++ | 24 | 6 | 19 | 49 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_sequences.h](/fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_sequences.h) | C++ | 77 | 13 | 33 | 123 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_time.h](/fast_gicp/thirdparty/nvbio/prototypes/psa/include/psa_time.h) | C++ | 10 | 6 | 5 | 21 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/include/simd_functions.h](/fast_gicp/thirdparty/nvbio/prototypes/psa/include/simd_functions.h) | C++ | 1,855 | 296 | 86 | 2,237 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/makefile](/fast_gicp/thirdparty/nvbio/prototypes/psa/makefile) | Makefile | 91 | 31 | 26 | 148 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swfarrar_gpu.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swfarrar_gpu.c) | C | 74 | 10 | 36 | 120 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swfarrar_gpu.cu](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swfarrar_gpu.cu) | CUDA C++ | 129 | 33 | 39 | 201 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swgotoh_registers_16b_gpu.cu](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swgotoh_registers_16b_gpu.cu) | CUDA C++ | 119 | 16 | 33 | 168 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swgotoh_registers_32b_gpu.cu](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swgotoh_registers_32b_gpu.cu) | CUDA C++ | 119 | 16 | 33 | 168 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swgotoh_registers_tilling_2D_gpu.cu](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swgotoh_registers_tilling_2D_gpu.cu) | CUDA C++ | 173 | 17 | 48 | 238 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swwozniak_gpu.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swwozniak_gpu.c) | C | 74 | 10 | 35 | 119 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swwozniak_gpu.cu](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/misc/psa_swwozniak_gpu.cu) | CUDA C++ | 142 | 43 | 47 | 232 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_2b_gpu.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_2b_gpu.c) | C | 102 | 10 | 39 | 151 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_2b_integer_gpu.cu](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_2b_integer_gpu.cu) | CUDA C++ | 128 | 18 | 32 | 178 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_2b_mixed_gpu.cu](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_2b_mixed_gpu.cu) | CUDA C++ | 176 | 19 | 45 | 240 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_2b_mixedsim_gpu.cu](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_2b_mixedsim_gpu.cu) | CUDA C++ | 176 | 19 | 45 | 240 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_2b_video_gpu.cu](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_2b_video_gpu.cu) | CUDA C++ | 170 | 17 | 40 | 227 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_cpu.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_cpu.c) | C | 167 | 13 | 45 | 225 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_ref_2b_gpu.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_ref_2b_gpu.c) | C | 124 | 14 | 47 | 185 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_ref_2b_integer_gpu.cu](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/gotoh/psa_swgotoh_ref_2b_integer_gpu.cu) | CUDA C++ | 134 | 20 | 32 | 186 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_alignments.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_alignments.c) | C | 82 | 9 | 27 | 118 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_errors.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_errors.c) | C | 23 | 6 | 4 | 33 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_profile.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_profile.c) | C | 128 | 9 | 32 | 169 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_regions.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_regions.c) | C | 126 | 6 | 37 | 169 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_sequences.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_sequences.c) | C | 521 | 50 | 107 | 678 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_time.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/src/psa_time.c) | C | 17 | 6 | 8 | 31 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/tools/benchmark.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/tools/benchmark.c) | C | 78 | 13 | 21 | 112 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/tools/checksum.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/tools/checksum.c) | C | 200 | 9 | 53 | 262 |
| [fast_gicp/thirdparty/nvbio/prototypes/psa/tools/genRegions.c](/fast_gicp/thirdparty/nvbio/prototypes/psa/tools/genRegions.c) | C | 99 | 8 | 32 | 139 |
| [fast_gicp/thirdparty/nvbio/sufsort-test/sufsort_test.cu](/fast_gicp/thirdparty/nvbio/sufsort-test/sufsort_test.cu) | CUDA C++ | 680 | 38 | 172 | 890 |
| [fast_gicp/thirdparty/nvbio/sw-benchmark/sw-benchmark.cu](/fast_gicp/thirdparty/nvbio/sw-benchmark/sw-benchmark.cu) | CUDA C++ | 521 | 79 | 117 | 717 |
| [fast_gicp/thirdparty/pybind11/.appveyor.yml](/fast_gicp/thirdparty/pybind11/.appveyor.yml) | YAML | 37 | 0 | 1 | 38 |
| [fast_gicp/thirdparty/pybind11/.cmake-format.yaml](/fast_gicp/thirdparty/pybind11/.cmake-format.yaml) | YAML | 31 | 28 | 15 | 74 |
| [fast_gicp/thirdparty/pybind11/.github/CONTRIBUTING.md](/fast_gicp/thirdparty/pybind11/.github/CONTRIBUTING.md) | Markdown | 279 | 0 | 80 | 359 |
| [fast_gicp/thirdparty/pybind11/.github/ISSUE_TEMPLATE/bug-report.md](/fast_gicp/thirdparty/pybind11/.github/ISSUE_TEMPLATE/bug-report.md) | Markdown | 19 | 0 | 10 | 29 |
| [fast_gicp/thirdparty/pybind11/.github/ISSUE_TEMPLATE/config.yml](/fast_gicp/thirdparty/pybind11/.github/ISSUE_TEMPLATE/config.yml) | YAML | 5 | 0 | 1 | 6 |
| [fast_gicp/thirdparty/pybind11/.github/ISSUE_TEMPLATE/feature-request.md](/fast_gicp/thirdparty/pybind11/.github/ISSUE_TEMPLATE/feature-request.md) | Markdown | 11 | 0 | 6 | 17 |
| [fast_gicp/thirdparty/pybind11/.github/ISSUE_TEMPLATE/question.md](/fast_gicp/thirdparty/pybind11/.github/ISSUE_TEMPLATE/question.md) | Markdown | 17 | 0 | 5 | 22 |
| [fast_gicp/thirdparty/pybind11/.github/dependabot.yml](/fast_gicp/thirdparty/pybind11/.github/dependabot.yml) | YAML | 13 | 3 | 1 | 17 |
| [fast_gicp/thirdparty/pybind11/.github/labeler.yml](/fast_gicp/thirdparty/pybind11/.github/labeler.yml) | YAML | 7 | 0 | 2 | 9 |
| [fast_gicp/thirdparty/pybind11/.github/labeler_merged.yml](/fast_gicp/thirdparty/pybind11/.github/labeler_merged.yml) | YAML | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/pybind11/.github/pull_request_template.md](/fast_gicp/thirdparty/pybind11/.github/pull_request_template.md) | Markdown | 4 | 4 | 8 | 16 |
| [fast_gicp/thirdparty/pybind11/.github/workflows/ci.yml](/fast_gicp/thirdparty/pybind11/.github/workflows/ci.yml) | YAML | 594 | 88 | 165 | 847 |
| [fast_gicp/thirdparty/pybind11/.github/workflows/configure.yml](/fast_gicp/thirdparty/pybind11/.github/workflows/configure.yml) | YAML | 63 | 6 | 16 | 85 |
| [fast_gicp/thirdparty/pybind11/.github/workflows/format.yml](/fast_gicp/thirdparty/pybind11/.github/workflows/format.yml) | YAML | 36 | 3 | 8 | 47 |
| [fast_gicp/thirdparty/pybind11/.github/workflows/labeler.yml](/fast_gicp/thirdparty/pybind11/.github/workflows/labeler.yml) | YAML | 14 | 0 | 3 | 17 |
| [fast_gicp/thirdparty/pybind11/.github/workflows/pip.yml](/fast_gicp/thirdparty/pybind11/.github/workflows/pip.yml) | YAML | 73 | 7 | 24 | 104 |
| [fast_gicp/thirdparty/pybind11/.pre-commit-config.yaml](/fast_gicp/thirdparty/pybind11/.pre-commit-config.yaml) | YAML | 66 | 25 | 10 | 101 |
| [fast_gicp/thirdparty/pybind11/.readthedocs.yml](/fast_gicp/thirdparty/pybind11/.readthedocs.yml) | YAML | 3 | 0 | 1 | 4 |
| [fast_gicp/thirdparty/pybind11/README.rst](/fast_gicp/thirdparty/pybind11/README.rst) | reStructuredText | 138 | 12 | 42 | 192 |
| [fast_gicp/thirdparty/pybind11/docs/_static/theme_overrides.css](/fast_gicp/thirdparty/pybind11/docs/_static/theme_overrides.css) | CSS | 11 | 0 | 1 | 12 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/cast/chrono.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/cast/chrono.rst) | reStructuredText | 62 | 2 | 18 | 82 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/cast/custom.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/cast/custom.rst) | reStructuredText | 68 | 5 | 19 | 92 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/cast/eigen.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/cast/eigen.rst) | reStructuredText | 229 | 13 | 69 | 311 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/cast/functional.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/cast/functional.rst) | reStructuredText | 74 | 9 | 27 | 110 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/cast/index.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/cast/index.rst) | reStructuredText | 31 | 2 | 11 | 44 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/cast/overview.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/cast/overview.rst) | reStructuredText | 136 | 8 | 22 | 166 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/cast/stl.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/cast/stl.rst) | reStructuredText | 166 | 19 | 67 | 252 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/cast/strings.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/cast/strings.rst) | reStructuredText | 195 | 20 | 91 | 306 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/classes.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/classes.rst) | reStructuredText | 856 | 96 | 310 | 1,262 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/embedding.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/embedding.rst) | reStructuredText | 168 | 14 | 80 | 262 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/exceptions.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/exceptions.rst) | reStructuredText | 232 | 14 | 61 | 307 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/functions.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/functions.rst) | reStructuredText | 367 | 48 | 149 | 564 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/misc.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/misc.rst) | reStructuredText | 214 | 27 | 97 | 338 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/pycpp/index.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/pycpp/index.rst) | reStructuredText | 9 | 1 | 4 | 14 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/pycpp/numpy.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/pycpp/numpy.rst) | reStructuredText | 301 | 26 | 112 | 439 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/pycpp/object.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/pycpp/object.rst) | reStructuredText | 143 | 27 | 82 | 252 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/pycpp/utilities.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/pycpp/utilities.rst) | reStructuredText | 91 | 13 | 41 | 145 |
| [fast_gicp/thirdparty/pybind11/docs/advanced/smart_ptrs.rst](/fast_gicp/thirdparty/pybind11/docs/advanced/smart_ptrs.rst) | reStructuredText | 107 | 14 | 53 | 174 |
| [fast_gicp/thirdparty/pybind11/docs/basics.rst](/fast_gicp/thirdparty/pybind11/docs/basics.rst) | reStructuredText | 175 | 33 | 101 | 309 |
| [fast_gicp/thirdparty/pybind11/docs/benchmark.py](/fast_gicp/thirdparty/pybind11/docs/benchmark.py) | Python | 78 | 1 | 14 | 93 |
| [fast_gicp/thirdparty/pybind11/docs/benchmark.rst](/fast_gicp/thirdparty/pybind11/docs/benchmark.rst) | reStructuredText | 53 | 16 | 27 | 96 |
| [fast_gicp/thirdparty/pybind11/docs/changelog.rst](/fast_gicp/thirdparty/pybind11/docs/changelog.rst) | reStructuredText | 1,244 | 15 | 421 | 1,680 |
| [fast_gicp/thirdparty/pybind11/docs/classes.rst](/fast_gicp/thirdparty/pybind11/docs/classes.rst) | reStructuredText | 333 | 49 | 151 | 533 |
| [fast_gicp/thirdparty/pybind11/docs/cmake/index.rst](/fast_gicp/thirdparty/pybind11/docs/cmake/index.rst) | reStructuredText | 5 | 1 | 3 | 9 |
| [fast_gicp/thirdparty/pybind11/docs/compiling.rst](/fast_gicp/thirdparty/pybind11/docs/compiling.rst) | reStructuredText | 403 | 53 | 187 | 643 |
| [fast_gicp/thirdparty/pybind11/docs/conf.py](/fast_gicp/thirdparty/pybind11/docs/conf.py) | Python | 94 | 194 | 95 | 383 |
| [fast_gicp/thirdparty/pybind11/docs/faq.rst](/fast_gicp/thirdparty/pybind11/docs/faq.rst) | reStructuredText | 227 | 20 | 97 | 344 |
| [fast_gicp/thirdparty/pybind11/docs/index.rst](/fast_gicp/thirdparty/pybind11/docs/index.rst) | reStructuredText | 29 | 7 | 13 | 49 |
| [fast_gicp/thirdparty/pybind11/docs/installing.rst](/fast_gicp/thirdparty/pybind11/docs/installing.rst) | reStructuredText | 62 | 10 | 34 | 106 |
| [fast_gicp/thirdparty/pybind11/docs/limitations.rst](/fast_gicp/thirdparty/pybind11/docs/limitations.rst) | reStructuredText | 54 | 0 | 19 | 73 |
| [fast_gicp/thirdparty/pybind11/docs/pybind11_vs_boost_python1.svg](/fast_gicp/thirdparty/pybind11/docs/pybind11_vs_boost_python1.svg) | XML | 427 | 0 | 1 | 428 |
| [fast_gicp/thirdparty/pybind11/docs/pybind11_vs_boost_python2.svg](/fast_gicp/thirdparty/pybind11/docs/pybind11_vs_boost_python2.svg) | XML | 427 | 0 | 1 | 428 |
| [fast_gicp/thirdparty/pybind11/docs/reference.rst](/fast_gicp/thirdparty/pybind11/docs/reference.rst) | reStructuredText | 43 | 35 | 50 | 128 |
| [fast_gicp/thirdparty/pybind11/docs/release.rst](/fast_gicp/thirdparty/pybind11/docs/release.rst) | reStructuredText | 69 | 3 | 21 | 93 |
| [fast_gicp/thirdparty/pybind11/docs/requirements.txt](/fast_gicp/thirdparty/pybind11/docs/requirements.txt) | pip requirements | 7 | 0 | 1 | 8 |
| [fast_gicp/thirdparty/pybind11/docs/upgrade.rst](/fast_gicp/thirdparty/pybind11/docs/upgrade.rst) | reStructuredText | 377 | 19 | 142 | 538 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/attr.h](/fast_gicp/thirdparty/pybind11/include/pybind11/attr.h) | C++ | 306 | 126 | 120 | 552 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/buffer_info.h](/fast_gicp/thirdparty/pybind11/include/pybind11/buffer_info.h) | C++ | 106 | 14 | 27 | 147 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/cast.h](/fast_gicp/thirdparty/pybind11/include/pybind11/cast.h) | C++ | 1,026 | 159 | 199 | 1,384 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/chrono.h](/fast_gicp/thirdparty/pybind11/include/pybind11/chrono.h) | C++ | 131 | 34 | 34 | 199 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/common.h](/fast_gicp/thirdparty/pybind11/include/pybind11/common.h) | C++ | 2 | 0 | 1 | 3 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/complex.h](/fast_gicp/thirdparty/pybind11/include/pybind11/complex.h) | C++ | 43 | 9 | 14 | 66 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/detail/class.h](/fast_gicp/thirdparty/pybind11/include/pybind11/detail/class.h) | C++ | 485 | 117 | 107 | 709 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/detail/common.h](/fast_gicp/thirdparty/pybind11/include/pybind11/detail/common.h) | C++ | 547 | 235 | 116 | 898 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/detail/descr.h](/fast_gicp/thirdparty/pybind11/include/pybind11/detail/descr.h) | C++ | 68 | 10 | 23 | 101 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/detail/init.h](/fast_gicp/thirdparty/pybind11/include/pybind11/detail/init.h) | C++ | 228 | 66 | 43 | 337 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/detail/internals.h](/fast_gicp/thirdparty/pybind11/include/pybind11/detail/internals.h) | C++ | 265 | 64 | 35 | 364 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/detail/type_caster_base.h](/fast_gicp/thirdparty/pybind11/include/pybind11/detail/type_caster_base.h) | C++ | 657 | 172 | 116 | 945 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/detail/typeid.h](/fast_gicp/thirdparty/pybind11/include/pybind11/detail/typeid.h) | C++ | 37 | 10 | 9 | 56 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/eigen.h](/fast_gicp/thirdparty/pybind11/include/pybind11/eigen.h) | C++ | 417 | 106 | 85 | 608 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/embed.h](/fast_gicp/thirdparty/pybind11/include/pybind11/embed.h) | C++ | 89 | 90 | 23 | 202 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/eval.h](/fast_gicp/thirdparty/pybind11/include/pybind11/eval.h) | C++ | 108 | 21 | 24 | 153 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/functional.h](/fast_gicp/thirdparty/pybind11/include/pybind11/functional.h) | C++ | 68 | 20 | 17 | 105 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/gil.h](/fast_gicp/thirdparty/pybind11/include/pybind11/gil.h) | C++ | 120 | 49 | 25 | 194 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/iostream.h](/fast_gicp/thirdparty/pybind11/include/pybind11/iostream.h) | C++ | 107 | 78 | 36 | 221 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/numpy.h](/fast_gicp/thirdparty/pybind11/include/pybind11/numpy.h) | C++ | 1,241 | 207 | 256 | 1,704 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/operators.h](/fast_gicp/thirdparty/pybind11/include/pybind11/operators.h) | C++ | 136 | 18 | 20 | 174 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/options.h](/fast_gicp/thirdparty/pybind11/include/pybind11/options.h) | C++ | 30 | 14 | 22 | 66 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/pybind11.h](/fast_gicp/thirdparty/pybind11/include/pybind11/pybind11.h) | C++ | 1,665 | 349 | 275 | 2,289 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/pytypes.h](/fast_gicp/thirdparty/pybind11/include/pybind11/pytypes.h) | C++ | 1,169 | 313 | 231 | 1,713 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/stl.h](/fast_gicp/thirdparty/pybind11/include/pybind11/stl.h) | C++ | 303 | 26 | 60 | 389 |
| [fast_gicp/thirdparty/pybind11/include/pybind11/stl_bind.h](/fast_gicp/thirdparty/pybind11/include/pybind11/stl_bind.h) | C++ | 502 | 58 | 117 | 677 |
| [fast_gicp/thirdparty/pybind11/pybind11/__init__.py](/fast_gicp/thirdparty/pybind11/pybind11/__init__.py) | Python | 8 | 1 | 4 | 13 |
| [fast_gicp/thirdparty/pybind11/pybind11/__main__.py](/fast_gicp/thirdparty/pybind11/pybind11/__main__.py) | Python | 37 | 4 | 12 | 53 |
| [fast_gicp/thirdparty/pybind11/pybind11/_version.py](/fast_gicp/thirdparty/pybind11/pybind11/_version.py) | Python | 7 | 1 | 5 | 13 |
| [fast_gicp/thirdparty/pybind11/pybind11/_version.pyi](/fast_gicp/thirdparty/pybind11/pybind11/_version.pyi) | Python | 4 | 0 | 3 | 7 |
| [fast_gicp/thirdparty/pybind11/pybind11/commands.py](/fast_gicp/thirdparty/pybind11/pybind11/commands.py) | Python | 13 | 3 | 7 | 23 |
| [fast_gicp/thirdparty/pybind11/pybind11/setup_helpers.py](/fast_gicp/thirdparty/pybind11/pybind11/setup_helpers.py) | Python | 193 | 170 | 82 | 445 |
| [fast_gicp/thirdparty/pybind11/pybind11/setup_helpers.pyi](/fast_gicp/thirdparty/pybind11/pybind11/setup_helpers.pyi) | Python | 50 | 2 | 10 | 62 |
| [fast_gicp/thirdparty/pybind11/setup.cfg](/fast_gicp/thirdparty/pybind11/setup.cfg) | Properties | 71 | 4 | 11 | 86 |
| [fast_gicp/thirdparty/pybind11/setup.py](/fast_gicp/thirdparty/pybind11/setup.py) | Python | 77 | 14 | 25 | 116 |
| [fast_gicp/thirdparty/pybind11/tests/conftest.py](/fast_gicp/thirdparty/pybind11/tests/conftest.py) | Python | 133 | 22 | 54 | 209 |
| [fast_gicp/thirdparty/pybind11/tests/constructor_stats.h](/fast_gicp/thirdparty/pybind11/tests/constructor_stats.h) | C++ | 180 | 77 | 19 | 276 |
| [fast_gicp/thirdparty/pybind11/tests/cross_module_gil_utils.cpp](/fast_gicp/thirdparty/pybind11/tests/cross_module_gil_utils.cpp) | C++ | 48 | 15 | 11 | 74 |
| [fast_gicp/thirdparty/pybind11/tests/env.py](/fast_gicp/thirdparty/pybind11/tests/env.py) | Python | 9 | 1 | 5 | 15 |
| [fast_gicp/thirdparty/pybind11/tests/extra_python_package/pytest.ini](/fast_gicp/thirdparty/pybind11/tests/extra_python_package/pytest.ini) | Ini | 0 | 0 | 1 | 1 |
| [fast_gicp/thirdparty/pybind11/tests/extra_python_package/test_files.py](/fast_gicp/thirdparty/pybind11/tests/extra_python_package/test_files.py) | Python | 213 | 3 | 49 | 265 |
| [fast_gicp/thirdparty/pybind11/tests/extra_setuptools/pytest.ini](/fast_gicp/thirdparty/pybind11/tests/extra_setuptools/pytest.ini) | Ini | 0 | 0 | 1 | 1 |
| [fast_gicp/thirdparty/pybind11/tests/extra_setuptools/test_setuphelper.py](/fast_gicp/thirdparty/pybind11/tests/extra_setuptools/test_setuphelper.py) | Python | 44 | 46 | 12 | 102 |
| [fast_gicp/thirdparty/pybind11/tests/local_bindings.h](/fast_gicp/thirdparty/pybind11/tests/local_bindings.h) | C++ | 44 | 11 | 10 | 65 |
| [fast_gicp/thirdparty/pybind11/tests/object.h](/fast_gicp/thirdparty/pybind11/tests/object.h) | C++ | 92 | 47 | 37 | 176 |
| [fast_gicp/thirdparty/pybind11/tests/pybind11_cross_module_tests.cpp](/fast_gicp/thirdparty/pybind11/tests/pybind11_cross_module_tests.cpp) | C++ | 60 | 43 | 21 | 124 |
| [fast_gicp/thirdparty/pybind11/tests/pybind11_tests.cpp](/fast_gicp/thirdparty/pybind11/tests/pybind11_tests.cpp) | C++ | 55 | 23 | 14 | 92 |
| [fast_gicp/thirdparty/pybind11/tests/pybind11_tests.h](/fast_gicp/thirdparty/pybind11/tests/pybind11_tests.h) | C++ | 62 | 7 | 16 | 85 |
| [fast_gicp/thirdparty/pybind11/tests/pytest.ini](/fast_gicp/thirdparty/pybind11/tests/pytest.ini) | Ini | 19 | 0 | 1 | 20 |
| [fast_gicp/thirdparty/pybind11/tests/requirements.txt](/fast_gicp/thirdparty/pybind11/tests/requirements.txt) | pip requirements | 11 | 0 | 1 | 12 |
| [fast_gicp/thirdparty/pybind11/tests/test_async.cpp](/fast_gicp/thirdparty/pybind11/tests/test_async.cpp) | C++ | 16 | 8 | 3 | 27 |
| [fast_gicp/thirdparty/pybind11/tests/test_async.py](/fast_gicp/thirdparty/pybind11/tests/test_async.py) | Python | 15 | 1 | 10 | 26 |
| [fast_gicp/thirdparty/pybind11/tests/test_buffers.cpp](/fast_gicp/thirdparty/pybind11/tests/test_buffers.cpp) | C++ | 165 | 18 | 32 | 215 |
| [fast_gicp/thirdparty/pybind11/tests/test_buffers.py](/fast_gicp/thirdparty/pybind11/tests/test_buffers.py) | Python | 123 | 5 | 37 | 165 |
| [fast_gicp/thirdparty/pybind11/tests/test_builtin_casters.cpp](/fast_gicp/thirdparty/pybind11/tests/test_builtin_casters.cpp) | C++ | 191 | 42 | 39 | 272 |
| [fast_gicp/thirdparty/pybind11/tests/test_builtin_casters.py](/fast_gicp/thirdparty/pybind11/tests/test_builtin_casters.py) | Python | 374 | 60 | 104 | 538 |
| [fast_gicp/thirdparty/pybind11/tests/test_call_policies.cpp](/fast_gicp/thirdparty/pybind11/tests/test_call_policies.cpp) | C++ | 70 | 15 | 17 | 102 |
| [fast_gicp/thirdparty/pybind11/tests/test_call_policies.py](/fast_gicp/thirdparty/pybind11/tests/test_call_policies.py) | Python | 162 | 31 | 27 | 220 |
| [fast_gicp/thirdparty/pybind11/tests/test_callbacks.cpp](/fast_gicp/thirdparty/pybind11/tests/test_callbacks.cpp) | C++ | 128 | 24 | 24 | 176 |
| [fast_gicp/thirdparty/pybind11/tests/test_callbacks.py](/fast_gicp/thirdparty/pybind11/tests/test_callbacks.py) | Python | 104 | 7 | 38 | 149 |
| [fast_gicp/thirdparty/pybind11/tests/test_chrono.cpp](/fast_gicp/thirdparty/pybind11/tests/test_chrono.cpp) | C++ | 46 | 25 | 14 | 85 |
| [fast_gicp/thirdparty/pybind11/tests/test_chrono.py](/fast_gicp/thirdparty/pybind11/tests/test_chrono.py) | Python | 124 | 24 | 62 | 210 |
| [fast_gicp/thirdparty/pybind11/tests/test_class.cpp](/fast_gicp/thirdparty/pybind11/tests/test_class.cpp) | C++ | 381 | 82 | 74 | 537 |
| [fast_gicp/thirdparty/pybind11/tests/test_class.py](/fast_gicp/thirdparty/pybind11/tests/test_class.py) | Python | 296 | 67 | 104 | 467 |
| [fast_gicp/thirdparty/pybind11/tests/test_cmake_build/embed.cpp](/fast_gicp/thirdparty/pybind11/tests/test_cmake_build/embed.cpp) | C++ | 16 | 0 | 6 | 22 |
| [fast_gicp/thirdparty/pybind11/tests/test_cmake_build/main.cpp](/fast_gicp/thirdparty/pybind11/tests/test_cmake_build/main.cpp) | C++ | 5 | 0 | 2 | 7 |
| [fast_gicp/thirdparty/pybind11/tests/test_cmake_build/test.py](/fast_gicp/thirdparty/pybind11/tests/test_cmake_build/test.py) | Python | 4 | 1 | 2 | 7 |
| [fast_gicp/thirdparty/pybind11/tests/test_constants_and_functions.cpp](/fast_gicp/thirdparty/pybind11/tests/test_constants_and_functions.cpp) | C++ | 112 | 20 | 18 | 150 |
| [fast_gicp/thirdparty/pybind11/tests/test_constants_and_functions.py](/fast_gicp/thirdparty/pybind11/tests/test_constants_and_functions.py) | Python | 38 | 1 | 15 | 54 |
| [fast_gicp/thirdparty/pybind11/tests/test_copy_move.cpp](/fast_gicp/thirdparty/pybind11/tests/test_copy_move.cpp) | C++ | 177 | 23 | 21 | 221 |
| [fast_gicp/thirdparty/pybind11/tests/test_copy_move.py](/fast_gicp/thirdparty/pybind11/tests/test_copy_move.py) | Python | 83 | 17 | 26 | 126 |
| [fast_gicp/thirdparty/pybind11/tests/test_custom_type_casters.cpp](/fast_gicp/thirdparty/pybind11/tests/test_custom_type_casters.cpp) | C++ | 91 | 20 | 18 | 129 |
| [fast_gicp/thirdparty/pybind11/tests/test_custom_type_casters.py](/fast_gicp/thirdparty/pybind11/tests/test_custom_type_casters.py) | Python | 66 | 39 | 12 | 117 |
| [fast_gicp/thirdparty/pybind11/tests/test_docstring_options.cpp](/fast_gicp/thirdparty/pybind11/tests/test_docstring_options.cpp) | C++ | 44 | 9 | 17 | 70 |
| [fast_gicp/thirdparty/pybind11/tests/test_docstring_options.py](/fast_gicp/thirdparty/pybind11/tests/test_docstring_options.py) | Python | 17 | 12 | 14 | 43 |
| [fast_gicp/thirdparty/pybind11/tests/test_eigen.cpp](/fast_gicp/thirdparty/pybind11/tests/test_eigen.cpp) | C++ | 219 | 70 | 41 | 330 |
| [fast_gicp/thirdparty/pybind11/tests/test_eigen.py](/fast_gicp/thirdparty/pybind11/tests/test_eigen.py) | Python | 583 | 65 | 123 | 771 |
| [fast_gicp/thirdparty/pybind11/tests/test_embed/catch.cpp](/fast_gicp/thirdparty/pybind11/tests/test_embed/catch.cpp) | C++ | 12 | 4 | 7 | 23 |
| [fast_gicp/thirdparty/pybind11/tests/test_embed/external_module.cpp](/fast_gicp/thirdparty/pybind11/tests/test_embed/external_module.cpp) | C++ | 15 | 3 | 6 | 24 |
| [fast_gicp/thirdparty/pybind11/tests/test_embed/test_interpreter.cpp](/fast_gicp/thirdparty/pybind11/tests/test_embed/test_interpreter.cpp) | C++ | 200 | 31 | 54 | 285 |
| [fast_gicp/thirdparty/pybind11/tests/test_embed/test_interpreter.py](/fast_gicp/thirdparty/pybind11/tests/test_embed/test_interpreter.py) | Python | 6 | 1 | 4 | 11 |
| [fast_gicp/thirdparty/pybind11/tests/test_enum.cpp](/fast_gicp/thirdparty/pybind11/tests/test_enum.cpp) | C++ | 63 | 14 | 11 | 88 |
| [fast_gicp/thirdparty/pybind11/tests/test_enum.py](/fast_gicp/thirdparty/pybind11/tests/test_enum.py) | Python | 167 | 30 | 40 | 237 |
| [fast_gicp/thirdparty/pybind11/tests/test_eval.cpp](/fast_gicp/thirdparty/pybind11/tests/test_eval.cpp) | C++ | 70 | 12 | 18 | 100 |
| [fast_gicp/thirdparty/pybind11/tests/test_eval.py](/fast_gicp/thirdparty/pybind11/tests/test_eval.py) | Python | 21 | 1 | 14 | 36 |
| [fast_gicp/thirdparty/pybind11/tests/test_eval_call.py](/fast_gicp/thirdparty/pybind11/tests/test_eval_call.py) | Python | 2 | 2 | 2 | 6 |
| [fast_gicp/thirdparty/pybind11/tests/test_exceptions.cpp](/fast_gicp/thirdparty/pybind11/tests/test_exceptions.cpp) | C++ | 170 | 34 | 28 | 232 |
| [fast_gicp/thirdparty/pybind11/tests/test_exceptions.py](/fast_gicp/thirdparty/pybind11/tests/test_exceptions.py) | Python | 138 | 20 | 52 | 210 |
| [fast_gicp/thirdparty/pybind11/tests/test_factory_constructors.cpp](/fast_gicp/thirdparty/pybind11/tests/test_factory_constructors.cpp) | C++ | 259 | 60 | 36 | 355 |
| [fast_gicp/thirdparty/pybind11/tests/test_factory_constructors.py](/fast_gicp/thirdparty/pybind11/tests/test_factory_constructors.py) | Python | 333 | 95 | 91 | 519 |
| [fast_gicp/thirdparty/pybind11/tests/test_gil_scoped.cpp](/fast_gicp/thirdparty/pybind11/tests/test_gil_scoped.cpp) | C++ | 40 | 8 | 7 | 55 |
| [fast_gicp/thirdparty/pybind11/tests/test_gil_scoped.py](/fast_gicp/thirdparty/pybind11/tests/test_gil_scoped.py) | Python | 48 | 26 | 21 | 95 |
| [fast_gicp/thirdparty/pybind11/tests/test_iostream.cpp](/fast_gicp/thirdparty/pybind11/tests/test_iostream.cpp) | C++ | 80 | 12 | 27 | 119 |
| [fast_gicp/thirdparty/pybind11/tests/test_iostream.py](/fast_gicp/thirdparty/pybind11/tests/test_iostream.py) | Python | 179 | 11 | 52 | 242 |
| [fast_gicp/thirdparty/pybind11/tests/test_kwargs_and_defaults.cpp](/fast_gicp/thirdparty/pybind11/tests/test_kwargs_and_defaults.cpp) | C++ | 90 | 35 | 18 | 143 |
| [fast_gicp/thirdparty/pybind11/tests/test_kwargs_and_defaults.py](/fast_gicp/thirdparty/pybind11/tests/test_kwargs_and_defaults.py) | Python | 205 | 28 | 53 | 286 |
| [fast_gicp/thirdparty/pybind11/tests/test_local_bindings.cpp](/fast_gicp/thirdparty/pybind11/tests/test_local_bindings.cpp) | C++ | 54 | 32 | 16 | 102 |
| [fast_gicp/thirdparty/pybind11/tests/test_local_bindings.py](/fast_gicp/thirdparty/pybind11/tests/test_local_bindings.py) | Python | 177 | 25 | 57 | 259 |
| [fast_gicp/thirdparty/pybind11/tests/test_methods_and_attributes.cpp](/fast_gicp/thirdparty/pybind11/tests/test_methods_and_attributes.cpp) | C++ | 299 | 41 | 44 | 384 |
| [fast_gicp/thirdparty/pybind11/tests/test_methods_and_attributes.py](/fast_gicp/thirdparty/pybind11/tests/test_methods_and_attributes.py) | Python | 372 | 34 | 102 | 508 |
| [fast_gicp/thirdparty/pybind11/tests/test_modules.cpp](/fast_gicp/thirdparty/pybind11/tests/test_modules.cpp) | C++ | 74 | 16 | 12 | 102 |
| [fast_gicp/thirdparty/pybind11/tests/test_modules.py](/fast_gicp/thirdparty/pybind11/tests/test_modules.py) | Python | 61 | 9 | 21 | 91 |
| [fast_gicp/thirdparty/pybind11/tests/test_multiple_inheritance.cpp](/fast_gicp/thirdparty/pybind11/tests/test_multiple_inheritance.cpp) | C++ | 147 | 49 | 35 | 231 |
| [fast_gicp/thirdparty/pybind11/tests/test_multiple_inheritance.py](/fast_gicp/thirdparty/pybind11/tests/test_multiple_inheritance.py) | Python | 260 | 19 | 83 | 362 |
| [fast_gicp/thirdparty/pybind11/tests/test_numpy_array.cpp](/fast_gicp/thirdparty/pybind11/tests/test_numpy_array.cpp) | C++ | 340 | 49 | 52 | 441 |
| [fast_gicp/thirdparty/pybind11/tests/test_numpy_array.py](/fast_gicp/thirdparty/pybind11/tests/test_numpy_array.py) | Python | 401 | 44 | 97 | 542 |
| [fast_gicp/thirdparty/pybind11/tests/test_numpy_dtypes.cpp](/fast_gicp/thirdparty/pybind11/tests/test_numpy_dtypes.cpp) | C++ | 427 | 34 | 59 | 520 |
| [fast_gicp/thirdparty/pybind11/tests/test_numpy_dtypes.py](/fast_gicp/thirdparty/pybind11/tests/test_numpy_dtypes.py) | Python | 341 | 10 | 84 | 435 |
| [fast_gicp/thirdparty/pybind11/tests/test_numpy_vectorize.cpp](/fast_gicp/thirdparty/pybind11/tests/test_numpy_vectorize.cpp) | C++ | 58 | 22 | 14 | 94 |
| [fast_gicp/thirdparty/pybind11/tests/test_numpy_vectorize.py](/fast_gicp/thirdparty/pybind11/tests/test_numpy_vectorize.py) | Python | 195 | 49 | 23 | 267 |
| [fast_gicp/thirdparty/pybind11/tests/test_opaque_types.cpp](/fast_gicp/thirdparty/pybind11/tests/test_opaque_types.cpp) | C++ | 47 | 17 | 10 | 74 |
| [fast_gicp/thirdparty/pybind11/tests/test_opaque_types.py](/fast_gicp/thirdparty/pybind11/tests/test_opaque_types.py) | Python | 41 | 5 | 13 | 59 |
| [fast_gicp/thirdparty/pybind11/tests/test_operator_overloading.cpp](/fast_gicp/thirdparty/pybind11/tests/test_operator_overloading.cpp) | C++ | 167 | 31 | 29 | 227 |
| [fast_gicp/thirdparty/pybind11/tests/test_operator_overloading.py](/fast_gicp/thirdparty/pybind11/tests/test_operator_overloading.py) | Python | 116 | 5 | 25 | 146 |
| [fast_gicp/thirdparty/pybind11/tests/test_pickling.cpp](/fast_gicp/thirdparty/pybind11/tests/test_pickling.cpp) | C++ | 102 | 19 | 18 | 139 |
| [fast_gicp/thirdparty/pybind11/tests/test_pickling.py](/fast_gicp/thirdparty/pybind11/tests/test_pickling.py) | Python | 34 | 1 | 13 | 48 |
| [fast_gicp/thirdparty/pybind11/tests/test_pytypes.cpp](/fast_gicp/thirdparty/pybind11/tests/test_pytypes.cpp) | C++ | 353 | 30 | 62 | 445 |
| [fast_gicp/thirdparty/pybind11/tests/test_pytypes.py](/fast_gicp/thirdparty/pybind11/tests/test_pytypes.py) | Python | 434 | 44 | 106 | 584 |
| [fast_gicp/thirdparty/pybind11/tests/test_sequences_and_iterators.cpp](/fast_gicp/thirdparty/pybind11/tests/test_sequences_and_iterators.cpp) | C++ | 284 | 30 | 45 | 359 |
| [fast_gicp/thirdparty/pybind11/tests/test_sequences_and_iterators.py](/fast_gicp/thirdparty/pybind11/tests/test_sequences_and_iterators.py) | Python | 140 | 6 | 50 | 196 |
| [fast_gicp/thirdparty/pybind11/tests/test_smart_ptr.cpp](/fast_gicp/thirdparty/pybind11/tests/test_smart_ptr.cpp) | C++ | 314 | 65 | 55 | 434 |
| [fast_gicp/thirdparty/pybind11/tests/test_smart_ptr.py](/fast_gicp/thirdparty/pybind11/tests/test_smart_ptr.py) | Python | 249 | 13 | 57 | 319 |
| [fast_gicp/thirdparty/pybind11/tests/test_stl.cpp](/fast_gicp/thirdparty/pybind11/tests/test_stl.cpp) | C++ | 241 | 37 | 47 | 325 |
| [fast_gicp/thirdparty/pybind11/tests/test_stl.py](/fast_gicp/thirdparty/pybind11/tests/test_stl.py) | Python | 175 | 29 | 63 | 267 |
| [fast_gicp/thirdparty/pybind11/tests/test_stl_binders.cpp](/fast_gicp/thirdparty/pybind11/tests/test_stl_binders.cpp) | C++ | 91 | 19 | 20 | 130 |
| [fast_gicp/thirdparty/pybind11/tests/test_stl_binders.py](/fast_gicp/thirdparty/pybind11/tests/test_stl_binders.py) | Python | 208 | 16 | 68 | 292 |
| [fast_gicp/thirdparty/pybind11/tests/test_tagbased_polymorphic.cpp](/fast_gicp/thirdparty/pybind11/tests/test_tagbased_polymorphic.cpp) | C++ | 107 | 15 | 21 | 143 |
| [fast_gicp/thirdparty/pybind11/tests/test_tagbased_polymorphic.py](/fast_gicp/thirdparty/pybind11/tests/test_tagbased_polymorphic.py) | Python | 26 | 1 | 3 | 30 |
| [fast_gicp/thirdparty/pybind11/tests/test_union.cpp](/fast_gicp/thirdparty/pybind11/tests/test_union.cpp) | C++ | 11 | 8 | 4 | 23 |
| [fast_gicp/thirdparty/pybind11/tests/test_union.py](/fast_gicp/thirdparty/pybind11/tests/test_union.py) | Python | 5 | 1 | 4 | 10 |
| [fast_gicp/thirdparty/pybind11/tests/test_virtual_functions.cpp](/fast_gicp/thirdparty/pybind11/tests/test_virtual_functions.cpp) | C++ | 352 | 86 | 61 | 499 |
| [fast_gicp/thirdparty/pybind11/tests/test_virtual_functions.py](/fast_gicp/thirdparty/pybind11/tests/test_virtual_functions.py) | Python | 280 | 53 | 76 | 409 |
| [fast_gicp/thirdparty/pybind11/tools/FindCatch.cmake](/fast_gicp/thirdparty/pybind11/tools/FindCatch.cmake) | CMake | 63 | 0 | 8 | 71 |
| [fast_gicp/thirdparty/pybind11/tools/FindEigen3.cmake](/fast_gicp/thirdparty/pybind11/tools/FindEigen3.cmake) | CMake | 70 | 0 | 17 | 87 |
| [fast_gicp/thirdparty/pybind11/tools/FindPythonLibsNew.cmake](/fast_gicp/thirdparty/pybind11/tools/FindPythonLibsNew.cmake) | CMake | 231 | 0 | 27 | 258 |
| [fast_gicp/thirdparty/pybind11/tools/check-style.sh](/fast_gicp/thirdparty/pybind11/tools/check-style.sh) | Shell Script | 26 | 13 | 6 | 45 |
| [fast_gicp/thirdparty/pybind11/tools/libsize.py](/fast_gicp/thirdparty/pybind11/tools/libsize.py) | Python | 24 | 5 | 10 | 39 |
| [fast_gicp/thirdparty/pybind11/tools/make_changelog.py](/fast_gicp/thirdparty/pybind11/tools/make_changelog.py) | Python | 37 | 9 | 18 | 64 |
| [fast_gicp/thirdparty/pybind11/tools/pybind11Common.cmake](/fast_gicp/thirdparty/pybind11/tools/pybind11Common.cmake) | CMake | 340 | 0 | 58 | 398 |
| [fast_gicp/thirdparty/pybind11/tools/pybind11NewTools.cmake](/fast_gicp/thirdparty/pybind11/tools/pybind11NewTools.cmake) | CMake | 229 | 0 | 39 | 268 |
| [fast_gicp/thirdparty/pybind11/tools/pybind11Tools.cmake](/fast_gicp/thirdparty/pybind11/tools/pybind11Tools.cmake) | CMake | 191 | 0 | 30 | 221 |
| [hdl_global_localization/.travis.yml](/hdl_global_localization/.travis.yml) | YAML | 17 | 0 | 4 | 21 |
| [hdl_global_localization/README.md](/hdl_global_localization/README.md) | Markdown | 30 | 0 | 13 | 43 |
| [hdl_global_localization/config/bbs_config.yaml](/hdl_global_localization/config/bbs_config.yaml) | YAML | 16 | 6 | 4 | 26 |
| [hdl_global_localization/config/fpfh_config.yaml](/hdl_global_localization/config/fpfh_config.yaml) | YAML | 2 | 0 | 0 | 2 |
| [hdl_global_localization/config/general_config.yaml](/hdl_global_localization/config/general_config.yaml) | YAML | 3 | 2 | 2 | 7 |
| [hdl_global_localization/config/ransac_config.yaml](/hdl_global_localization/config/ransac_config.yaml) | YAML | 19 | 2 | 3 | 24 |
| [hdl_global_localization/config/teaser_config.yaml](/hdl_global_localization/config/teaser_config.yaml) | YAML | 8 | 2 | 1 | 11 |
| [hdl_global_localization/config/test.rviz](/hdl_global_localization/config/test.rviz) | YAML | 250 | 0 | 1 | 251 |
| [hdl_global_localization/docker/melodic/Dockerfile](/hdl_global_localization/docker/melodic/Dockerfile) | Docker | 17 | 0 | 7 | 24 |
| [hdl_global_localization/docker/melodic_llvm/Dockerfile](/hdl_global_localization/docker/melodic_llvm/Dockerfile) | Docker | 18 | 0 | 8 | 26 |
| [hdl_global_localization/docker/noetic/Dockerfile](/hdl_global_localization/docker/noetic/Dockerfile) | Docker | 17 | 0 | 7 | 24 |
| [hdl_global_localization/docker/noetic_llvm/Dockerfile](/hdl_global_localization/docker/noetic_llvm/Dockerfile) | Docker | 18 | 0 | 8 | 26 |
| [hdl_global_localization/include/hdl_global_localization/bbs/bbs_localization.hpp](/hdl_global_localization/include/hdl_global_localization/bbs/bbs_localization.hpp) | C++ | 62 | 5 | 25 | 92 |
| [hdl_global_localization/include/hdl_global_localization/bbs/occupancy_gridmap.hpp](/hdl_global_localization/include/hdl_global_localization/bbs/occupancy_gridmap.hpp) | C++ | 94 | 0 | 24 | 118 |
| [hdl_global_localization/include/hdl_global_localization/engines/global_localization_bbs.hpp](/hdl_global_localization/include/hdl_global_localization/engines/global_localization_bbs.hpp) | C++ | 25 | 0 | 14 | 39 |
| [hdl_global_localization/include/hdl_global_localization/engines/global_localization_engine.hpp](/hdl_global_localization/include/hdl_global_localization/engines/global_localization_engine.hpp) | C++ | 15 | 0 | 7 | 22 |
| [hdl_global_localization/include/hdl_global_localization/engines/global_localization_fpfh_ransac.hpp](/hdl_global_localization/include/hdl_global_localization/engines/global_localization_fpfh_ransac.hpp) | C++ | 22 | 0 | 11 | 33 |
| [hdl_global_localization/include/hdl_global_localization/engines/global_localization_fpfh_teaser.hpp](/hdl_global_localization/include/hdl_global_localization/engines/global_localization_fpfh_teaser.hpp) | C++ | 17 | 5 | 8 | 30 |
| [hdl_global_localization/include/hdl_global_localization/global_localization_results.hpp](/hdl_global_localization/include/hdl_global_localization/global_localization_results.hpp) | C++ | 31 | 1 | 12 | 44 |
| [hdl_global_localization/include/hdl_global_localization/ransac/matching_cost_evaluater.hpp](/hdl_global_localization/include/hdl_global_localization/ransac/matching_cost_evaluater.hpp) | C++ | 14 | 0 | 6 | 20 |
| [hdl_global_localization/include/hdl_global_localization/ransac/matching_cost_evaluater_flann.hpp](/hdl_global_localization/include/hdl_global_localization/ransac/matching_cost_evaluater_flann.hpp) | C++ | 41 | 0 | 13 | 54 |
| [hdl_global_localization/include/hdl_global_localization/ransac/matching_cost_evaluater_voxels.hpp](/hdl_global_localization/include/hdl_global_localization/ransac/matching_cost_evaluater_voxels.hpp) | C++ | 31 | 0 | 12 | 43 |
| [hdl_global_localization/include/hdl_global_localization/ransac/ransac_pose_estimation.hpp](/hdl_global_localization/include/hdl_global_localization/ransac/ransac_pose_estimation.hpp) | C++ | 33 | 41 | 14 | 88 |
| [hdl_global_localization/include/hdl_global_localization/ransac/voxelset.hpp](/hdl_global_localization/include/hdl_global_localization/ransac/voxelset.hpp) | C++ | 25 | 0 | 11 | 36 |
| [hdl_global_localization/launch/hdl_global_localization.launch](/hdl_global_localization/launch/hdl_global_localization.launch) | XML | 9 | 1 | 3 | 13 |
| [hdl_global_localization/package.xml](/hdl_global_localization/package.xml) | XML | 17 | 0 | 5 | 22 |
| [hdl_global_localization/src/bbs_test.cpp](/hdl_global_localization/src/bbs_test.cpp) | C++ | 85 | 0 | 20 | 105 |
| [hdl_global_localization/src/hdl_global_localization/bbs/bbs_localization.cpp](/hdl_global_localization/src/hdl_global_localization/bbs/bbs_localization.cpp) | C++ | 127 | 1 | 41 | 169 |
| [hdl_global_localization/src/hdl_global_localization/engines/global_localization_bbs.cpp](/hdl_global_localization/src/hdl_global_localization/engines/global_localization_bbs.cpp) | C++ | 89 | 0 | 21 | 110 |
| [hdl_global_localization/src/hdl_global_localization/engines/global_localization_fpfh_ransac.cpp](/hdl_global_localization/src/hdl_global_localization/engines/global_localization_fpfh_ransac.cpp) | C++ | 40 | 0 | 15 | 55 |
| [hdl_global_localization/src/hdl_global_localization/engines/global_localization_fpfh_teaser.cpp](/hdl_global_localization/src/hdl_global_localization/engines/global_localization_fpfh_teaser.cpp) | C++ | 64 | 0 | 19 | 83 |
| [hdl_global_localization/src/hdl_global_localization/ransac/ransac_pose_estimation.cpp](/hdl_global_localization/src/hdl_global_localization/ransac/ransac_pose_estimation.cpp) | C++ | 110 | 45 | 27 | 182 |
| [hdl_global_localization/src/hdl_global_localization/ransac/voxelset.cpp](/hdl_global_localization/src/hdl_global_localization/ransac/voxelset.cpp) | C++ | 58 | 0 | 15 | 73 |
| [hdl_global_localization/src/hdl_global_localization_node.cpp](/hdl_global_localization/src/hdl_global_localization_node.cpp) | C++ | 115 | 0 | 32 | 147 |
| [hdl_global_localization/src/hdl_global_localization_test.cpp](/hdl_global_localization/src/hdl_global_localization_test.cpp) | C++ | 76 | 1 | 25 | 102 |
| [hdl_global_localization/srv/QueryGlobalLocalization.srv](/hdl_global_localization/srv/QueryGlobalLocalization.srv) | ROS Interface | 8 | 0 | 1 | 9 |
| [hdl_global_localization/srv/SetGlobalLocalizationEngine.srv](/hdl_global_localization/srv/SetGlobalLocalizationEngine.srv) | ROS Interface | 2 | 0 | 0 | 2 |
| [hdl_global_localization/srv/SetGlobalMap.srv](/hdl_global_localization/srv/SetGlobalMap.srv) | ROS Interface | 2 | 0 | 0 | 2 |
| [hdl_localization/.travis.yml](/hdl_localization/.travis.yml) | YAML | 22 | 0 | 1 | 23 |
| [hdl_localization/README.md](/hdl_localization/README.md) | Markdown | 75 | 0 | 31 | 106 |
| [hdl_localization/apps/globalmap_server_nodelet.cpp](/hdl_localization/apps/globalmap_server_nodelet.cpp) | C++ | 83 | 5 | 28 | 116 |
| [hdl_localization/apps/hdl_localization_nodelet.cpp](/hdl_localization/apps/hdl_localization_nodelet.cpp) | C++ | 413 | 48 | 95 | 556 |
| [hdl_localization/docker/melodic/Dockerfile](/hdl_localization/docker/melodic/Dockerfile) | Docker | 22 | 0 | 8 | 30 |
| [hdl_localization/docker/melodic_llvm/Dockerfile](/hdl_localization/docker/melodic_llvm/Dockerfile) | Docker | 23 | 0 | 9 | 32 |
| [hdl_localization/docker/noetic/Dockerfile](/hdl_localization/docker/noetic/Dockerfile) | Docker | 22 | 0 | 8 | 30 |
| [hdl_localization/docker/noetic_llvm/Dockerfile](/hdl_localization/docker/noetic_llvm/Dockerfile) | Docker | 23 | 0 | 9 | 32 |
| [hdl_localization/include/hdl_localization/delta_estimater.hpp](/hdl_localization/include/hdl_localization/delta_estimater.hpp) | C++ | 44 | 0 | 15 | 59 |
| [hdl_localization/include/hdl_localization/odom_system.hpp](/hdl_localization/include/hdl_localization/odom_system.hpp) | C++ | 33 | 8 | 12 | 53 |
| [hdl_localization/include/hdl_localization/pose_estimator.hpp](/hdl_localization/include/hdl_localization/pose_estimator.hpp) | C++ | 52 | 29 | 22 | 103 |
| [hdl_localization/include/hdl_localization/pose_system.hpp](/hdl_localization/include/hdl_localization/pose_system.hpp) | C++ | 65 | 14 | 26 | 105 |
| [hdl_localization/include/kkl/alg/unscented_kalman_filter.hpp](/hdl_localization/include/kkl/alg/unscented_kalman_filter.hpp) | C++ | 187 | 54 | 47 | 288 |
| [hdl_localization/launch/hdl_localization.launch](/hdl_localization/launch/hdl_localization.launch) | XML | 47 | 16 | 8 | 71 |
| [hdl_localization/launch/local_rslidar_imu.launch](/hdl_localization/launch/local_rslidar_imu.launch) | XML | 50 | 16 | 8 | 74 |
| [hdl_localization/msg/ScanMatchingStatus.msg](/hdl_localization/msg/ScanMatchingStatus.msg) | ROS Interface | 7 | 0 | 2 | 9 |
| [hdl_localization/nodelet_plugins.xml](/hdl_localization/nodelet_plugins.xml) | XML | 6 | 0 | 2 | 8 |
| [hdl_localization/package.xml](/hdl_localization/package.xml) | XML | 42 | 0 | 6 | 48 |
| [hdl_localization/rviz/hdl_localization.rviz](/hdl_localization/rviz/hdl_localization.rviz) | YAML | 361 | 0 | 1 | 362 |
| [hdl_localization/scripts/plot_status.py](/hdl_localization/scripts/plot_status.py) | Python | 51 | 2 | 19 | 72 |
| [hdl_localization/src/hdl_localization/pose_estimator.cpp](/hdl_localization/src/hdl_localization/pose_estimator.cpp) | C++ | 185 | 29 | 58 | 272 |
| [navigation/config/costmap_common_params_deep.yaml](/navigation/config/costmap_common_params_deep.yaml) | YAML | 41 | 4 | 6 | 51 |
| [navigation/config/costmap_common_params_lite.yaml](/navigation/config/costmap_common_params_lite.yaml) | YAML | 58 | 0 | 6 | 64 |
| [navigation/config/costmap_common_params_mini.yaml](/navigation/config/costmap_common_params_mini.yaml) | YAML | 70 | 0 | 5 | 75 |
| [navigation/config/global_costmap_params.yaml](/navigation/config/global_costmap_params.yaml) | YAML | 15 | 0 | 3 | 18 |
| [navigation/config/global_planner_params.yaml](/navigation/config/global_planner_params.yaml) | YAML | 17 | 1 | 4 | 22 |
| [navigation/config/local_costmap_params.yaml](/navigation/config/local_costmap_params.yaml) | YAML | 14 | 0 | 2 | 16 |
| [navigation/config/teb_local_planner_params_deep.yaml](/navigation/config/teb_local_planner_params_deep.yaml) | YAML | 77 | 7 | 9 | 93 |
| [navigation/config/teb_local_planner_params_lite.yaml](/navigation/config/teb_local_planner_params_lite.yaml) | YAML | 77 | 7 | 10 | 94 |
| [navigation/config/teb_local_planner_params_mini.yaml](/navigation/config/teb_local_planner_params_mini.yaml) | YAML | 77 | 7 | 10 | 94 |
| [navigation/launch/pc.launch](/navigation/launch/pc.launch) | XML | 13 | 3 | 2 | 18 |
| [navigation/launch/robot.launch](/navigation/launch/robot.launch) | XML | 27 | 9 | 7 | 43 |
| [navigation/map/hdl_graph_map.yaml](/navigation/map/hdl_graph_map.yaml) | YAML | 6 | 0 | 2 | 8 |
| [navigation/package.xml](/navigation/package.xml) | XML | 19 | 3 | 2 | 24 |
| [navigation/rviz/nav.rviz](/navigation/rviz/nav.rviz) | YAML | 292 | 0 | 1 | 293 |
| [navigation/tools/pcd2ply.py](/navigation/tools/pcd2ply.py) | Python | 7 | 0 | 2 | 9 |
| [ndt_omp/.github/workflows/build.yml](/ndt_omp/.github/workflows/build.yml) | YAML | 26 | 1 | 7 | 34 |
| [ndt_omp/README.md](/ndt_omp/README.md) | Markdown | 43 | 0 | 14 | 57 |
| [ndt_omp/apps/align.cpp](/ndt_omp/apps/align.cpp) | C++ | 90 | 4 | 25 | 119 |
| [ndt_omp/docker/foxy/Dockerfile](/ndt_omp/docker/foxy/Dockerfile) | Docker | 16 | 3 | 7 | 26 |
| [ndt_omp/docker/foxy_llvm/Dockerfile](/ndt_omp/docker/foxy_llvm/Dockerfile) | Docker | 17 | 3 | 8 | 28 |
| [ndt_omp/docker/galactic/Dockerfile](/ndt_omp/docker/galactic/Dockerfile) | Docker | 16 | 3 | 7 | 26 |
| [ndt_omp/docker/galactic_llvm/Dockerfile](/ndt_omp/docker/galactic_llvm/Dockerfile) | Docker | 17 | 3 | 8 | 28 |
| [ndt_omp/docker/melodic/Dockerfile](/ndt_omp/docker/melodic/Dockerfile) | Docker | 20 | 0 | 7 | 27 |
| [ndt_omp/docker/melodic_llvm/Dockerfile](/ndt_omp/docker/melodic_llvm/Dockerfile) | Docker | 21 | 0 | 8 | 29 |
| [ndt_omp/docker/noetic/Dockerfile](/ndt_omp/docker/noetic/Dockerfile) | Docker | 20 | 0 | 7 | 27 |
| [ndt_omp/docker/noetic_llvm/Dockerfile](/ndt_omp/docker/noetic_llvm/Dockerfile) | Docker | 21 | 0 | 8 | 29 |
| [ndt_omp/include/pclomp/gicp_omp.h](/ndt_omp/include/pclomp/gicp_omp.h) | C++ | 182 | 146 | 53 | 381 |
| [ndt_omp/include/pclomp/gicp_omp_impl.hpp](/ndt_omp/include/pclomp/gicp_omp_impl.hpp) | C++ | 375 | 98 | 63 | 536 |
| [ndt_omp/include/pclomp/ndt_omp.h](/ndt_omp/include/pclomp/ndt_omp.h) | C++ | 220 | 221 | 66 | 507 |
| [ndt_omp/include/pclomp/ndt_omp_impl.hpp](/ndt_omp/include/pclomp/ndt_omp_impl.hpp) | C++ | 645 | 182 | 159 | 986 |
| [ndt_omp/include/pclomp/voxel_grid_covariance_omp.h](/ndt_omp/include/pclomp/voxel_grid_covariance_omp.h) | C++ | 296 | 191 | 71 | 558 |
| [ndt_omp/include/pclomp/voxel_grid_covariance_omp_impl.hpp](/ndt_omp/include/pclomp/voxel_grid_covariance_omp_impl.hpp) | C++ | 317 | 100 | 71 | 488 |
| [ndt_omp/package.xml](/ndt_omp/package.xml) | XML | 18 | 0 | 7 | 25 |
| [ndt_omp/src/pclomp/gicp_omp.cpp](/ndt_omp/src/pclomp/gicp_omp.cpp) | C++ | 4 | 0 | 3 | 7 |
| [ndt_omp/src/pclomp/ndt_omp.cpp](/ndt_omp/src/pclomp/ndt_omp.cpp) | C++ | 4 | 0 | 2 | 6 |
| [ndt_omp/src/pclomp/voxel_grid_covariance_omp.cpp](/ndt_omp/src/pclomp/voxel_grid_covariance_omp.cpp) | C++ | 4 | 0 | 2 | 6 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)