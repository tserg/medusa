from vyper import ast as vy_ast

from medusa.analysis.base import BaseAnalyser


class DeadStoreAnalyser(BaseAnalyser):
    """
    Eliminates dead store statements.

    Example:
    ```
    @external
    def foo() -> uint256:
        x: uint256 = 1
        y: uint256 = 2
        return y
    ```

    `x` is assigned a value but never used.
    """

    _id = "Dead Store"

    def analyse(self, ast: vy_ast.Module, analysis: dict[BaseAnalyser, set[vy_ast.VyperNode]]):

        fn_nodes = ast.get_descendants(vy_ast.FunctionDef)

        for fn_node in fn_nodes:
            local_var_decls = fn_node.get_descendants(vy_ast.AnnAssign)

            for local_var in local_var_decls:
                name_node = local_var.target
                var_name = name_node.id
                used_by = [
                    i
                    for i in fn_node.get_descendants(vy_ast.Name, {"id": var_name})
                    if i != name_node
                ]

                if len(used_by) == 0:
                    temp = analysis.get(self, set())
                    temp.add(local_var)
                    analysis[self] = temp

        return analysis
