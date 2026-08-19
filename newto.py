    def optimize(self, x0: int, fun, tol = 1e-7, max_iter = 100) -> int:
        x = x0
        
        for i in range(max_iter):
            h = 1e-7
            dfx = (fun(x+h) - fun(x))/h
            fx = fun(x)

            if abs(dfs) < 1e-12:
                return ValueError
            x_new = x - fx / dfx
            if abs(x - x_new) < tol:
                return x_new
            x = x_new
        return x
            