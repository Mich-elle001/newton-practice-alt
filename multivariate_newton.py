class Multivariate_Newton:
    import numpy as np
    from scipy.differentiate import hessian, derivative
    def optimize(self, x0, f, tol=1e-7, max_iter=100):
        """Robust Newton's method optimizer with error trapping and defensive programming"""

        x = np.array(x0, dtype=float)


        for i in range(max_iter):
            grad_result = derivative(f, x)
            g = grad_result.df

            
            hess_result = hessian(f, x)
            h = hess_result.ddf

            try:
                v = np.linalg.solve(H, g)
            except np.linalg.LinAlgError:
                print("Matrix Singularity")
                return x

            x_new = x - v
            
            if abs(x - x_new) < tol:
                return x_new
            x = x_new
        return x

        
optimize = Multivariate_Newton().optimize